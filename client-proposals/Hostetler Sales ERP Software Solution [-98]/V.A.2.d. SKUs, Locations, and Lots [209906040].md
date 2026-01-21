5.1.2.4. SKUs, Locations, and Lots

  


Requirements

SKU

  * Standard Fields
    * SKU
    * Description
    * Category
    * Track Inventory (checkbox)
    * Vendors
  * Customization
    * UOM - Add a checkbox for creating a SKU Lot for each item (i.e. for pallet UOM)
  * Custom Fields
    * Target Stock Quantity
    * Target Stock UOM
    * Stock Shelf Space
    * Color
    * Special Item (checkbox; inventoried but not stocked)
    * Override Lead Time (checkbox)
    * SKU Freeze Inventory Lead Time (weeks) (number; editable & required if Override Lead Time; otherwise, show system-wide/vendor default)
    * SKU Order Lead Time (weeks) (number; editable & required if Override Lead Time; otherwise, show system-wide/vendor default))



  


SKU Lot Locations (used to handle inventory at multiple locations)

  * Standard Fields
    * Name
    * Active (checkbox)
    * Some standard fields are omitted



  


SKU Lots

One of the major pain points is being able to locate inventory within the warehouse, with ~1800 pallet spaces.

  * Custom Fields
    * Shelf Space



  


Development Specification

_MOCKUPS:

  * SM: Sean Miller 03/12/2025: Done.
  * Detail Screens:
    * SKU Detail Screen
    * SKU Lot Location Detail Screen
    * SKU Lot Detail Screen
  * Reports:
    * SKU Inventory Amount
      * Prompts (all optional; blank = all)
        * SKU (list)
        * Location (list)
        * Shelf Space
      * Columns
        * SKU
        * Location
        * Shelf Space
        * Quantity
        * UOM
      * Sort By:
        * Shelf Space
    * Inventory Adjustment (same thing as SKU Inventory but with a column for a Last Checked read-only date (before Quantity) and Quantity being editable)
      * Also add a "Last Checked Before" date prompt
      * Add a column for inventory age (Today - SkuLotAcqDate)


