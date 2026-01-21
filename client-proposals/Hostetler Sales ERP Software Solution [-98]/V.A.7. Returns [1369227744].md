5.1.7. Returns

  


Requirements

Permission:

  * "Approve Returns"



  


Return Reason

  * Name
  * Active (checkbox)
  * Restock (required; list of Yes/No)



Return:

  * Customer
  * Job Name (list of active jobs)
  * Products
    * SKU
    * Qty Shipped (read-only)
    * Qty Returned
    * UOM
    * Price (read-only)
    * Amount (read-only)
    * Return Reason
      * Credit
      * Damaged
      * Waste
      * Wrong Product
    * Restock Shelf Space
    * Restock Fee %
    * Restock Fee $
    * Approved (with date)



  


Notes:

  * When restocking:
    * If we're restocking to a location with a lot currently assigned, add the inventory to that lot, even if it's not the same lot as the PO.
    * If we're restocking to a location that does not have a lot assigned:
      * If the original lot is empty, assign it to the original lot and update the lot's location (if needed)
      * If the original lot is not empty, create a new lot in the specified location.
  * Automatically Create a Credit



  


Additional Processes:

  * Add a "Restock" process for returns
    * Items to Restock
    * Restocked Shelf Space
  * Export to QuickBooks after Approval (both for credits and for restocks)



  


Reports

  * Returns by Item
    * Filters
      * Date Range
      * Group By
        * Project Manager
        * Crew
        * Return Reason
    * Columns
      * SKU
      * # of Returns
      * Qty Returned
      * Return reason
    * Sort by:
      * # of Returns (descending)
  * Returns Needing Approval (with notification for)



  


Development Specification

_MOCKUPS:

  * SM: Sean Miller 03/14/2025: Done.
  * Models Sales Forms


