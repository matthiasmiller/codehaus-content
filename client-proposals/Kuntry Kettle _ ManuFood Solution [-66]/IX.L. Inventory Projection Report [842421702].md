9.12. Inventory Projection Report

The goal is to see what was changed by an order:

  * SKU
  * Description
  * Quantity on Hand
  * Allocated Quantity (across all orders)
  * Accrued Quantity (final balance)
  * Reorder Level
  * Optimal Reorder Quantity



  


Filters:

  * Sales Order (optional; blank = all)
  * Production Date (optional; blank = all)



  


The Work Orders should be filtered based on the matching Sales Order (if specified) or based on the Production Date (if specified). If neither of these is specified, show all Work Orders.

  


Group By:

  * Items with an accrued quantity that is less than zero or below the SKU's reorder level


