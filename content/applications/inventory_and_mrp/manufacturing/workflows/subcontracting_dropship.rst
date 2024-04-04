=========================
Dropship to subcontractor
=========================

.. |PO| replace:: :abbr:`PO (Purchase Order)`
.. |POs| replace:: :abbr:`PO (Purchase Orders)`
.. |RfQ| replace:: :abbr:`RfQ (Request for Quotation)`
.. |BoM| replace:: :abbr:`BoM (Bill of Materials)`

In manufacturing, subcontracting is the process of a company engaging a third-party manufacturer, or
subcontractor, to manufacture products that are then sold by the contracting company.

In Odoo, the *Dropship Subcontractor on Order* route is used to purchase the necessary components
for a subcontracted product from the vendor, and have them delivered directly to the subcontractor,
each time a purchase order (PO) for that product is confirmed.

The subcontractor then uses the components to manufacture the desired product, before shipping it
back to the contracting company.

Configuration
=============

To use the *Dropship Subcontractor on Order* route, navigate to :menuselection:`Manufacturing app
--> Configuration --> Settings`, and enable the checkbox next to :guilabel:`Subcontracting`, under
the :guilabel:`Operations` heading.

Once the *Subcontracting* setting is enabled, it is also necessary to properly configure the
subcontracted product's |BoM| and the components listed on the |BoM|.

Configure bill of materials
---------------------------

To configure a |BoM| for the *Dropship Subcontractor on Order* route, navigate to
:menuselection:`Manufacturing app --> Products --> Bills of Materials`, and select the |BoM| for the
subcontracted product, or create a new |BoM| by clicking :guilabel:`New`.

.. seealso::

   For a full overview of |BoM| configuration, see the :doc:`Bill of materials
   <../basic_setup/bill_configuration>` documentation.

In the :guilabel:`BoM Type` field, select the :guilabel:`Subcontracting` option. Then, add one or
more subcontractors in the :guilabel:`Subcontractors` field that appears below.

.. image:: subcontracting_dropship/bom-type.png
   :align: center
   :alt: The "BoM Type" field on a BoM, configured to manufacture the product using subcontracting.

Finally, make sure that all necessary components are specified on the :guilabel:`Components` tab. To
add a new component, click :guilabel:`Add a line`, select the component in the :guilabel:`Component`
drop-down menu, and specify the required quantity in the :guilabel:`Quantity` field.

Configure Components
--------------------

To configure components for the *Dropship Subcontractor on Order* route, navigate to each component
from the |BoM| by selecting the component's name in the :guilabel:`Components` tab, and clicking the
:guilabel:`➡️ (right arrow)` button to the left of the name.

Alternatively, navigate to each component by going to :menuselection:`Inventory app --> Products -->
Products`, and selecting the component.

On the component product form, select the :guilabel:`Purchase` tab, and add a vendor by clicking
:guilabel:`Add a line`, selecting the vendor in the :guilabel:`Vendor` field, and adding the price
they sell the product for in the :guilabel:`Price` field. This is the vendor that sends components
to the subcontractor, once they are purchased.

Then, click on the :guilabel:`Inventory` tab and select the :guilabel:`Dropship Subcontractor on
Order` route in the :guilabel:`Routes` section.

Repeat the process for every component that must be dropshipped to the subcontractor.

Dropship subcontractor on order workflow
========================================

The dropship subcontractor on order workflow consists of three steps:

#. Create a |PO| to purchase the finished product from the subcontractor (*subcontractor* |PO|);
   doing so creates a request for quotation (RfQ) to purchase the components from the vendor, as
   well as a receipt order.
#. Confirm the |RfQ| to turn it into a second |PO| (*vendor* |PO|); doing so creates a *Dropship
   Subcontractor* order.
#. Process the *Dropship Subcontractor* order once the vendor has sent the components to the
   subcontractor.
#. Process the receipt once the subcontractor has finished manufacturing the subcontracted product,
   and shipped it back to the contracting company.

Create purchase order
---------------------

To create a *subcontractor* |PO|, navigate to :menuselection:`Purchase app --> Orders --> Purchase
Orders`, and click :guilabel:`New`.

Begin filling out the |PO| by selecting a subcontractor from the :guilabel:`Vendor` drop-down menu.

In the :guilabel:`Products` tab, click :guilabel:`Add a product` to create a new product line.
Select a product produced by the subcontractor in the :guilabel:`Product` field, and enter the
quantity in the :guilabel:`Quantity` field.

Finally, click :guilabel:`Confirm Order` to confirm the *subcontractor* |PO|.

When a |PO| is confirmed for a product that requires dropshipping components to a subcontractor, a
receipt is automatically created, and can be accessed from the :guilabel:`Receipt` smart button that
appears at the top of the *subcontractor* |PO|.

In addition, an |RfQ| is created for the components that are purchased from the vendor and sent to
the subcontractor. However, the |RfQ| **IS NOT** automatically linked to the *subcontractor* |PO|.

Once the |RfQ| is confirmed and becomes a *vendor* |PO|, a *Dropship Subcontractor* order is
created. This order is linked to both the *vendor* |PO| and the *subcontractor* |PO|.

Confirm RfQ
-----------

To access the |RfQ| created by confirming the *subcontractor* |PO|, navigate to
:menuselection:`Purchase app --> Orders --> Requests for Quotation`. Select the |RfQ| that lists the
correct vendor in the :guilabel:`Vendor` field, and the reference number of the receipt that was
created after confirming *subcontractor* |PO|, in the :guilabel:`Source Document` field.

Click :guilabel:`Confirm Order` to turn the |RfQ| into a *vendor* |PO|, and confirm the purchase of
components from the vendor. After doing so, a :guilabel:`Dropship` smart button appears at the top
of the *vendor* |PO|, and a :guilabel:`Resupply` smart button appears at the top of the
*subcontractor* |PO|.

Process Dropship Subcontractor order
------------------------------------

Once the components have been delivered to the subcontractor, navigate to :menuselection:`Purchase
app --> Orders --> Purchase Orders`, and select the *vendor* |PO| or the *subcontractor* |PO|. Then,
click the :guilabel:`Dropship` smart button or the :guilabel:`Resupply` smart button, respectively.

Clicking either button opens the *Dropship Subcontractor* order. Click the :guilabel:`Validate`
button at the top of the order to confirm that the subcontractor has received the components.

Process receipt
---------------

Once the subcontractor has manufactured the finished product and shipped it to the contracting
company, navigate to :menuselection:`Purchase app --> Orders --> Purchase Orders`, and select the
*subcontractor* |PO|.

Click the :guilabel:`Receive Products` button at the top of the *subcontractor* |PO| to open the
receipt. Then, click :guilabel:`Validate` at the top of the receipt to register the product into
inventory.

Alternatively, select the :guilabel:`Receipt` smart button at the top of the *subcontractor* |PO|,
and click :guilabel:`Validate` at the top of the receipt.
