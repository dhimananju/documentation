======================
Resupply subcontractor
======================

.. |PO| replace:: :abbr:`PO (Purchase Order)`
.. |POs| replace:: :abbr:`PO (Purchase Orders)`
.. |BoM| replace:: :abbr:`BoM (Bill of Materials)`

In manufacturing, subcontracting is the process of a company engaging a third-party manufacturer, or
subcontractor, to manufacture products that are then sold by the contracting company.

In Odoo, the *Resupply Subcontractor on Order* route is used to deliver the necessary components for
a subcontracted product to the subcontractor, each time a purchase order (PO) for that product is
confirmed.

The subcontractor then uses the components to manufacture the desired product, before shipping it
back to the contracting company.

Configuration
=============

To use the *Resupply Subcontractor on Order* route, navigate to :menuselection:`Manufacturing app
--> Configuration --> Settings`, and enable the checkbox next to :guilabel:`Subcontracting`, under
the :guilabel:`Operations` heading.

Once the *Subcontracting* setting is enabled, it is also necessary to properly configure the
subcontracted product's |BoM| and the components listed on the |BoM|.

Configure bill of materials
---------------------------

To configure a |BoM| for the *Resupply Subcontractor on Order* route, navigate to
:menuselection:`Manufacturing app --> Products --> Bills of Materials`, and select the |BoM| for the
subcontracted product, or create a new |BoM| by clicking :guilabel:`New`.

.. seealso::

   For a full overview of |BoM| configuration, see the :doc:`Bill of materials
   <../basic_setup/bill_configuration>` documentation.

In the :guilabel:`BoM Type` field, select the :guilabel:`Subcontracting` option. Then, add one or
more subcontractors in the :guilabel:`Subcontractors` field that appears below.

.. image:: subcontracting_resupply/bom-type.png
   :align: center
   :alt: The "BoM Type" field on a BoM, configured to manufacture the product using subcontracting.

Finally, make sure that all necessary components are specified on the :guilabel:`Components` tab. To
add a new component, click :guilabel:`Add a line`, select the component in the :guilabel:`Component`
drop-down menu, and specify the required quantity in the :guilabel:`Quantity` field.

Configure Components
--------------------

To configure components for the *Resupply Subcontractor on Order* route, navigate to each component
from the |BoM| by selecting the component's name in the :guilabel:`Components` tab, and clicking the
:guilabel:`➡️ (right arrow)` button to the left of the name.

Alternatively, navigate to each component by going to :menuselection:`Inventory app --> Products -->
Products`, and selecting the component.

On the component product form, click on the :guilabel:`Inventory` tab and select the
:guilabel:`Resupply Subcontractor on Order` route in the :guilabel:`Routes` section.

Repeat the process for every component that must be sent to the subcontractor.

Resupply subcontractor on order workflow
========================================

The resupply subcontractor on order workflow consists of three steps:

#. Create a |PO| to purchase the finished product from the subcontractor; doing so creates a
   *Resupply Subcontractor* order, as well as a receipt.
#. Process the *Resupply Subcontractor* order once components for the subcontracted product have
   been sent to the subcontractor.
#. Process the receipt once the subcontractor has finished manufacturing the subcontracted product,
   and shipped it back to the contracting company.

.. important::

   While the *Resupply Subcontractor on Order* route can be used to automatically resupply a
   subcontractor upon confirmation of a |PO|, it is also possible create a resupply order manually.
   This workflow is useful when it is necessary to resupply the subcontractor without creating a
   |PO|.

   To resupply a subcontractor manually, navigate to the :menuselection:`Inventory` app, and click
   on the :guilabel:`Resupply Subcontractor` card. Create a new *Resupply Subcontractor* order by
   clicking :guilabel:`New`.

   In the :guilabel:`Delivery Address` field, select the subcontractor to whom the components should
   be sent.

   Then, add each component to the :guilabel:`Operations` tab by clicking :guilabel:`Add a line`,
   selecting the component in the :guilabel:`Product` drop-down field, and specifying a quantity in
   the :guilabel:`Demand` field.

   Finally, click :guilabel:`Mark as Todo` to register the order. Once the components have been sent
   to the subcontractor, click :guilabel:`Validate` to confirm that the order has been sent.

Create purchase order
---------------------

To create a |PO| for a subcontracted product, navigate to :menuselection:`Purchase app --> Orders
--> Purchase Orders`, and click :guilabel:`New`.

Begin filling out the |PO| by selecting a subcontractor from the :guilabel:`Vendor` drop-down menu.

In the :guilabel:`Products` tab, click :guilabel:`Add a product` to create a new product line.
Select a product in the :guilabel:`Product` field, and enter the quantity in the
:guilabel:`Quantity` field.

Finally, click :guilabel:`Confirm Order` to confirm the |PO|.

Process Resupply Subcontractor order
------------------------------------

Once the subcontracted product's components have been sent to the subcontractor, navigate to
:menuselection:`Purchase app --> Orders --> Purchase Orders`, and select the |PO|.

Click the :guilabel:`Resupply` smart button at the top of the screen to open the *Resupply
Subcontractor* order, then click :guilabel:`Validate` to confirm that the components have been sent
to the subcontractor.

Process receipt
---------------

Once the subcontractor has manufactured the finished product and shipped it to the contracting
company, navigate to :menuselection:`Purchase app --> Orders --> Purchase Orders`, and select the
|PO|.

To register the product into inventory, click the :guilabel:`Receive Products` button at the top of
the |PO|, to open the receipt. Then, click :guilabel:`Validate` at the top of the receipt.

Alternatively, select the :guilabel:`Receipt` smart button at the top of the page, and click
:guilabel:`Validate` at the top of the receipt.
