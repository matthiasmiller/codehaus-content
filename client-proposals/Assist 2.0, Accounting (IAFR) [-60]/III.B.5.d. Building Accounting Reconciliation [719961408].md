3.2.5.4. Building Accounting Reconciliation

  


Requirements

Assist will automatically reconcile the accounting system with the building records and sales orders. This is done by:

  * linking each line item to a building record
  * determining the building's current impact to the financials
  * determining the building's total expected impact to the financials
  * creating a delta transaction to reconcile these amounts



  


This will be every night before midnight.

  


This process will prompt for:

  * Transaction Date (required; default to today)
  * STINs (blank = all)



  


NOTE:

  * We need to be sure to reverse the accounting impact for sales orders that are canceled.
  * When running this for all STINs, be sure to include all STINs that have an accounting record associated with it, even if it is no longer in the current district. This will be used to handle buildings moving from one district to another.



  


It will use the Building Accounting Impact to create a single transaction to reconcile accounting with the building record.

  


It will use the Sales Order Accounting Impact to do the same thing for all sales orders linked to the specified STINs.

  


Development Specification

Niccolas Miller 04/26/2023: [[PC0153614]] - ZFP - FGI: Building Accounting Reconciliation (T&M)
