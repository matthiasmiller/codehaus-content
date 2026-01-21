5.1. Phase 1 - Inventory / POS

  


Requirements

  


  


Development Specification

TODO_IDD - Divorce Sales Forms from Lists

  


  


TODO_IDD - Need x30 triggers to keep inventory updated

  


  


TODO_CCI: SalesFormTempNumber should be SalesFormCopiedFromNumber or something similar. Consider adding a macro with a ListExpand or something similar to allow you to view all sales forms connected to the current ones (i.e. the one it was copied from, as well as ones copied from it).

  


TODO_IDD: Regarding the change for Sales Forms to use SKUs instead of Sales Items: Is this a standard feature that would be turned on for ZTK? Matthias's original notes in the HLD would indicate that. 

  


TODO_IDD: Spell out Invoice / RMA and RMA / Credit Memo linking.

  


Here is a good way to conceptualize this:

  


  
| Purchase / Decrease Inventory| Refund / Increase Inventory  
---|---|---  
Pending| Estimate| Return Request (i.e. customer service ticket)  
Authorized| Sales Order| RMA  
Finalized| Invoice| Credit  
  
  


\--

  


The Solution will use the standard Estimates.

  


The Estimates report will have an option to exclude any estimates that have already been linked to a Sales Order or Invoice (checked by default).

  


TODO_IDD/TODO_CCI - How hard is this to do? It seems like after an estimate has a SO/IN, we should archive it, no?

  


\--

  


The Solution will use the standard Invoices feature. An invoice can be one of three subtypes:

  * Sales Order
  * Invoice
  * Return Merchandise Authorization



  


Sales Orders & Invoices: 

  


The Sales Order record will be converted into an Invoice by specifying an Invoice Date. This allows deposits / payments to be included on the same record.

  


Return Merchandise Authorization (RMAs): 

  


The Solution will include an option to create a new RMA. When the Contact is selected on the RMA, it will show an embedded spreadsheet of returnable items and their remaining quantities. It will show:

  


  * Return (checkbox)
  * Date (reverse sort)
  * Invoice Number
  * SKU
  * Description
  * Qty
  * Price



  


Clicking the "Return" checkbox will add the item with a negative entry to the itemization spreadsheet.

  


The itemization spreadsheet should also show a "Return Reason", which would be a configurable list of return reasons. This would also show a Return Fee % and a Return Fee $ column for each line items. The subtotal and totals in the RMA would show a negative amount.

  


The RMA will have an "Approved" or "Received" checkbox/date to turn the RMA into a credit that adjusts the customer balance.
