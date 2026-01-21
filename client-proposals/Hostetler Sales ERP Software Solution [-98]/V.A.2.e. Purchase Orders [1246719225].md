5.1.2.5. Purchase Orders

  


Requirements

Purchase Orders

  * Standard Fields
    * Ship To (SKU Lot Location)
    * Bill To (NOTE: single company; not required)
    * Vendor
    * ID (to be confirmed, but tentatively, this could be automatic with "STOCK" for stock POs, and "Customer - Job Name" for Special POs)
    * Ship Date
    * Projected Reception Date (Ship Date + Vendor Ship Time; editable & will auto-update Ship Date)
    * Reception Date
    * SKUs
      * Order Qty
      * UOM
      * Received (customized to be read-only; replaced with Shelf Spaces below)
    * Some standard fields are omitted
  * Custom Fields
    * Type (required)
      * Stock
      * Special
    * Customer (visible & required if Special; list of customers with active jobs)
    * Job Name (visible & required if Special; list of active jobs for the selected customer)
    * Shelf Spaces
      * SKU
      * Received
      * UOM
      * Shelf Space



  


Additional Items:

  * Inventory Reception Process via the Tablet
    * Pull up PO
    * Enter SKU
    * Enter Qty Received
    * Select Shelf Space (RECEIVING by default)
    * Finalize entire inventory as received
  * PO Export to QuickBooks
  * Customize the "Auto-Create SKU Lots" to create one SKU Lot per bulk item (this might be configured on the SKU's UOM)
  * POs will be received into a "RECEIVING" shelf space, then moved into its warehouse location (stock or overstock).
  * Add a way to move SKU Lots from one location to another location, and from one shelf space to another
    * Enter SKU
    * Current Location / New Location (to handle transfers between locations)
    * Can Old Shelf Space
    * Scan New Shelf Space
    * Confirm



  


Development Specification

_MOCKUPS:

  * SM: Sean Miller 03/13/2025: Done.
  * Detail Screens
    * Purchase Orders
  * Report
    * Purchase Order Search
      * Model [https://insite.apphosting.zone/Reports/Standard/cStd_Purchase_Orders?State=JufFQe6CFww&_=RIKc5&](https://insite.apphosting.zone/Reports/Standard/cStd_Purchase_Orders?State=JufFQe6CFww&_=RIKc5&) but ONLY with standard fields OR client-customized fields. It looks like everything is fine from this sample report, however.
    * Receive Inventory
      * TODO_IDD: Can we have them go through the PO Search, then click Receive Inventory from the PO?
        * Virtual RG on PO
          * SKU (drop list of SKUs)
          * UOM
          * Qty Received
          * Received By (read-only; current user)
          * Received On (date; default to today)
          * Received Shelf Space (list of shelf spaces; default to RECEIVING)
        * Reception Complete checkbox (with a read-only date)
        * Warn on save if all SKUs have been received but it hasn't been marked as Reception Complete
    * Stock Inventory
      * If we are stocking entire lots, we can use an editable report
      * Prompt For
        * Location (default to user's location)
        * Shelf Space (required)
        * SKU (list of SKUs in the space)
      * Columns
        * SKU
        * Location
        * Shelf Space (editable)
        * UOM
        * Quantity
    * Move Inventory
      * Prompt For:
        * Location (default to user's location)
        * Shelf Space (required)
        * SKU (list of SKUs in the space)
      * Columns
        * SKU
        * Location
        * Shelf Space
        * UOM
        * Quantity
      * Button - Move Inventory
        * Prompt:
          * New Location (default to current)
          * New Shelf Space (default to current)
          * New UOM (default to current)
          * New Quantity (default to Current)



  


TODO_IDD: Are Shelf Spaces locked to a single location?

NOTE: We need to handle multiple lots per shelf space to correctly handle restocking vans, partial inventory moves, etc.

  


Further design required:

  * We need to make sure that we correctly handle need dates (i.e. when it needs to be on-site, when it needs to be shipped, when it needs to be picked/staged, when it needs to arrive, when it needs to be ordered)
  * We'll want to make sure the reception process is streamlined.


