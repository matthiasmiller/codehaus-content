2.1. Sales Forms

  


Requirements

The solution will be using the standard Silverloom Sales Forms feature (Estimates/Sales Orders/Invoices) with some modifications.

  


The Solution will use the Silverloom Inventory Management feature (SKUs), rather than the Sales Items feature. Note that currently the Solution is not using either SKUs or Sales Items, but they also have been in consideration in Phase 3 design (for tracking devices, models, etc.). 

  


There will be an option added for Sales Forms to use SKUs instead of Sales Items. 

  


Only SKUs that have the "Is Sales Item" checkbox checked should be available in Sales Forms.

  


Sales Reports will need to update to allow filtering and grouping by SKU.

  


Linking Sales Forms: All Sales Forms will be linked to the originating sales form:

  * A Sales Order will be linked to the originating Estimate
  * An Invoice will be linked to the originating Estimate or Sales Order



  


Each sales form will have a way to find the linked sales forms, in either direction.

  


Development Specification

TODO_CCI: SalesFormTempNumber should be SalesFormCopiedFromNumber or something similar. Consider adding a macro with a ListExpand or something similar to allow you to view all sales forms connected to the current ones (i.e. the one it was copied from, as well as ones copied from it).

  


TODO_IDD: Regarding the change for Sales Forms to use SKUs instead of Sales Items: Is this a standard feature that would be turned on for ZTK? Matthias's original notes in the HLD would indicate that. 

  


TODO_IDD: Spell out Invoice / RMA and RMA / Credit Memo linking.

  


Here is a good way to conceptualize this:

  


  
| Purchase / Decrease Inventory| Refund / Increase Inventory  
---|---|---  
Pending| Estimate| Return Request (i.e. customer service ticket)  
Authorized| Sales Order| RMA  
Finalized| Invoice| Credit  
  
  

