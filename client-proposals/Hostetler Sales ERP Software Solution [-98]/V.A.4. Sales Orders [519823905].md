5.1.4. Sales Orders

  


Requirements

The solution will be using the standard Silverloom Sales Forms feature with some modifications.

  


The Solution will use the Silverloom Inventory Management feature (SKUs), rather than the Sales Items feature. There will be an option added for Sales Forms to use SKUs instead of Sales Items. 

  


Sales Reports will need to update to allow filtering and grouping by SKU.

  


In addition, all Estimates, Sales Orders, Invoices, and Returns will all be linked together.

  


Job

  * Silverloom ID (required & auto-numbered)
  * Customer
  * Job Name
  * Active (checkbox; default to checked)



  


Sales Orders

  * Customer
  * Job (list of active Jobs for the customer)
  * Operation (list of Operation Descriptions matching the Job ID)
  * Deadline Date (read-only; automatically pulled from JobPack Operation)
  * Status 
    * Special Item Order Status (none/some/all)
    * Picking Status (none/some/all)
  * SKUs
    * SKU
    * Qty
    * UOM
    * Description
    * Price
    * Amount (read-only; auto-calculated)
    * Status (read-only; auto-calculated); options of:
      * (blank)
      * Ordered
      * Picked
    * Qty Picked
    * Picked By (read-only)
    * Pallet # (all items for a SKU are tied to 1 pallet, even if it's split out in real life)
    * Stock Shelf Space (read-only from SKU)
    * Overstock Shelf Spaces (read-only from SKU Lots)
    * Color (read-only from SKU)
  * Purchase Orders (list of associated purchase orders)



  


Notifications:

  * Notify if SKUs are added or removed (including quantity); see User Groups
  * Notify if any SKUs are backordered



  


Additional Notes:

  * For the deadline date, we need configurable time periods for when it should be ordered, delivered, picked, and shipped.



  


  * Shelf Spaces are formatted like AAB1F1L30. These can be sorted by splitting it into a series of alphabetical and numeric sequences, and sorting them alphabetically and numerically by their parts.



  


  * Inventory Picking Process via the Tablet. This can be accessible via the Sales Order.
    * This will be an interface that is sorted by shelf space. It will show:
      * Read-Only:
        * Stock Shelf Space
        * Stock Quantity
        * Stock UOM
        * Overstock Shelf Spaces, Quantity, and UOM
        * Stock SKU link (saves record and/or opens new tab to move the SKU from Overstock to Stock)
        * SKU
        * Color
        * Order Quantity
        * Order UOM
      * Editable:
        * Pick Shelf Space
        * Pick Quantity
        * Pick UOM
        * Pallet #
        * Picked By (filled in when editing pick Quantity and UOM)
        * [ ] More Stock Available (when checked, the Next button moves to a blank row for the same SKU)
        * [ ] Flag as Backorder
        * Next/Prev buttons
      * Buttons:
        * Complete Picking (error if any items are not filled but are not flagged as backordered)
        * Confirm Picking



  


  * Send notifications for any backordered items. These will also show up in the inventory reports.



  


Reports:

  * Sales Orders
    * Filters
      * Customer
      * Job
      * Operation
      * Special Item Order Status
      * Picking Status
      * Shipping Status



  


Development Specification

TODO_IDD: There are two ways we can do the linking:

  * Set the originating record ID when copying sales forms (like from estimate to SO, or SO to Invoice), then do a ListExpand
  * Set a Sales Form Collection ID that links all sales forms together.
  * Simply field Customer + Job and have an NdxFind (simplest, but it would be nice to have a warning when changing the customer or oder)



  


TODO_IDD: I think we can simply convert AAB1F1L30 into something like this for sorting:

  * AAB
  * 00000001 << i.e. NumberSortString
  * F
  * 00000001 <<
  * L
  * 00000030 <<


