8.9. Sales Orders Record

  


Requirements

There are a few customers who have multiple ship to addresses, and we need to handle that. The ship to phone number does not need to be on the sales order, but it should be listed on the packing slip.

  


  * Status (i.e. Order/In Progress, Complete; based on the statuses of the linked Work Orders)
  * Order Date
  * Customer Name, Address, & Phone (automatic & read-only; from Customer record)
  * Shipping Name, Address, & Phone (selected from list of addresses on Customer record)
  * Customer Contact (automatic and read-only; based on Customer)
  * Ship Via (list of Ship Via)
  * Requested Ship Date (date; optional)
  * Customer PO (text)
  * Packages; embedded spreadsheet of:
    * Package Number
    * Description (automatic & read-only)
    * # of Batches (number; 0 decimals)
    * Est. Yield (case yield * number of batches)
    * Shipped Cases (TBD)
    * Price / Unit
  * Items; embedded spreadsheet of:
    * SKU
    * Description (automatic & read-only)
    * Quantity
    * Price/Unit (automatic & read-only)



  


The Price / Unit would be displayed after the work order is complete. It would be calculated based on the price on the package.

  


If any packages have line changeovers (based on the item SKU Category), show those line items (with quantities) on the sales order.

  


NOTE:

  * The sales order will be printed twice: once when it's pending, and once when it's complete. The price should only be shown after it's complete.
  * The sample sales order includes a total line at the bottom. It does NOT need to be included.
  * The sales order will automatically create the appropriate work orders. It will create 1 or 2 work orders per batch. If a package requires another package (for example, mild salsa requiring the base salsa), that package will generate two work order per batch (one for the base package and one for the end product).
  * If there are changeovers in any of the batches, show them as separate line items on the printout with the SKU and Qty of changeovers that they've got. This helps to inform both production and customer
  * The sales order must include SKUs and Quantities to cover all work orders that have started or completed production. All other line items may be edited.



  


The Sales Order should information about Customer Labels (total, used, and remaining). This maybe would also be sent out in an email to the customer with each Sales Order.

  


Development Specification

TODO_IDD: We currently don't have a standard Sales Order record, but we've spun them up for various clients (ZTD, ZFP). We could consider standardizing.

  


TODO_IDD - figure out how editability works
