import re
from docutils import nodes
from docutils.parsers.rst import roles
from sphinx import addnodes
from sphinx.environment.adapters import toctree

from . import pygments_override, translator


def setup(app):
    app.set_translator('html', translator.BootstrapTranslator)

    app.connect('html-page-context', set_missing_meta)

    app.add_js_file('js/utils.js')  # Keep in first position
    app.add_js_file('js/layout.js')
    app.add_js_file('js/menu.js')
    app.add_js_file('js/page_toc.js')
    app.add_js_file('js/switchers.js')
    roles.register_local_role('icon', icon_role)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }

def set_missing_meta(app, pagename, templatename, context, doctree):
    if context.get('meta') is None:  # Pages without title (used with `include::`) have no meta
        context['meta'] = {}

class Monkey:
    """ Replace patched method of an object by a new method receiving the old one in argument. """
    def __init__(self, obj):
        self.obj = obj
    def __call__(self, fn):
        name = fn.__name__
        old = getattr(self.obj, name)
        setattr(self.obj, name, lambda self_, *args, **kwargs: fn(old, self_, *args, **kwargs))

@Monkey(toctree.TocTree)
def resolve(old_resolve, tree, docname, *args, **kwargs):

    def _update_toctree_nodes(_node) -> None:
        """ Make necessary changes to Docutils' nodes of the toc.

        Internal structure of toc nodes:
        <ul>
            <li>
                <p><a/></p>
                <ul>
                    ...
                </ul>
            </li>
            <li/>
        <ul/>
        """
        if isinstance(_node, nodes.reference):  # The node is a reference (<a/>)
            _node_docname = _get_docname(_node)
            _clear_reference_if_empty_page(_node, _node_docname)
            _set_docname_as_class(_node, _node_docname)
        elif isinstance(_node, (addnodes.compact_paragraph, nodes.bullet_list, nodes.list_item)):
            for _subnode in _node.children:
                _update_toctree_nodes(_subnode)

    def _get_docname(_node):
        """ Return the docname of the targeted document.

        docname = some_common_root/foo/bar/the_page_being_rendered
        _ref = ../../contributing/documentation
        _path_parts = ['..', '..', 'contributing', 'documentation']
        _res = ['some_common_root', 'contributing', 'documentation']
        _docname = some_common_root/contributing/documentation

        :return: The docname of the document targeted by `_node`, i.e. the relative path from the
                 documentation source directory (the `content/` directory)
        :rtype: str
        """
        _ref = _node['refuri'].replace('.html', '')
        _parent_directory_occurrences = _ref.count('..')
        if not _parent_directory_occurrences and '/' not in docname:
            # The current document is at the root of the documentation source directory
            # (e.g. docname == 'index'|'applications'|...). i.e., the ref is already the docname.
            _docname = _ref
        else:
            _path_parts = _ref.split('/')
            _res = docname.split('/')[:-(_parent_directory_occurrences+1)] \
                   + _path_parts[_parent_directory_occurrences:]
            _docname = '/'.join(_res)
        return _docname

    def _clear_reference_if_empty_page(_reference_node, _node_docname):
        """ Clear reference of 'empty' toctree pages.

        Inspect parent node's siblings to determine whether the node references a toc and, if so,
        clear its reference URL. (<a href="#"/>)
        If the page has the `show-content` metadata, don't clear the reference.
        """
        if _node_docname and any(
            isinstance(_subnode, nodes.bullet_list)
            for _subnode in _reference_node.parent.parent.children
        ):  # The node references a toc
            if 'show-content' not in tree.env.metadata[_node_docname]:
                _reference_node['refuri'] = '#'  # The page must not be accessible

    def _set_docname_as_class(_reference_node, _node_docname):
        _node_docname = _node_docname or docname  # refuri==None <-> href="#"
        _reference_node.parent.parent['classes'].append(f'o_menu_{_node_docname.replace("/", "_")}')

    resolved_toc = old_resolve(tree, docname, *args, **kwargs)
    if resolved_toc:  # `resolve` returns None if the depth of the TOC to resolve is too high
        _update_toctree_nodes(resolved_toc)
    return resolved_toc


def extract_icon_classes(filename):
    """
    Return a list of icon classes from a CSS file.
    """
    icon_classes = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                match = re.search(r'\.([a-zA-Z0-9_-]+):before', line)
                if match:
                    icon_class = match.group(1)
                    icon_classes.append(icon_class)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")
    return icon_classes

def handle_error(inliner, rawtext, error_message, lineno):
    """
    Handle an error by creating a system message node.
    """
    error_node = nodes.system_message(
        lineno, backrefs=[], source=rawtext, type='error', level=1)
    error_node['message'] = inliner.reporter.error(error_message, line=lineno)
    return [error_node], []

def icon_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Custom role for adding icons to the documentation.
    """
    # Paths to icon sets used by the :icon: role
    odoo_ui_icon_path = 'extensions/odoo_theme/static/scss/_odoo_ui_icon.scss'
    font_awesome_icon_path = 'extensions/odoo_theme/static/scss/_font_awesome.scss'
    # Check which icon set the icon belongs to
    if 'oi-' in text:
        icon_file = odoo_ui_icon_path
    elif 'fa-' in text:
        icon_file = font_awesome_icon_path
    else:
        return handle_error(
            inliner, rawtext, f"'{text}' is not an 'oi-' or 'fa-' icon set", lineno)
    # Extract icon classes from the icon set
    icon_classes = extract_icon_classes(icon_file)
    # Check if the icon class is in the icon set and create the element
    if text in icon_classes:
        inline_node = nodes.inline(classes=[text])
        return [inline_node], []
    else:
        return handle_error(
            inliner, rawtext, f"Icon class '{text}' not found in {icon_file}", lineno)
