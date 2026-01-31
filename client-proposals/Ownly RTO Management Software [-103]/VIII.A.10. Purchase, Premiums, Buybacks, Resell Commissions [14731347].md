8.1.10. Purchase, Premiums, Buybacks, Resell Commissions

TODO_SETH - Ready to Go

  


  


Existing Assets:

  * Rename "Asset" to "Accounting Asset" and use "AcctAsset" as the field prefix
  * Rename the "Silverloom Asset Management" catalog/folder to "Silverloom Accounting Asset Management"



Seth Miller 01/27/2026: TODO_Jasper: [[PC0189379]]

  


Bill Itemization:

  * Remove "Ownly" from the drop list items in BillItemizationEntryTypes.
    * TODO_SETH: I propose AssetItemizationEntryTypes. Instead of Other, we would just leave it blank. If we want other itemization types, we'll deal with that design later.



  


On the Bill:

  * Add to Bill itemization drop list
    * "Asset Sale"
    * "Asset Commission"



  


On Bills/Invoice

  * Validate that the balance never drops below zero.
    * "Balance" means Invoices Minus Bills for Asset Sale
    * "Balance" means Bills Minus Invoices for Asset Expense, Asset Premium, Asset Purchase, Asset Commission
    * NOTE - I propose a way to add a macro for:
      * AssetItemizationIsNormallyInvoiced
      * AssetItemizationIsNormallyBilled (defined as NOT Normally Invoiced)



  


On the Invoice:

  * Add the same drop list of itemization for assets; this needs to be used when calculating balances on the Asset



  


On the Asset

  


  * Asset
    * Entry Date (use the record creation date as a date expression; read-only; can be hidden for new records)



  


  * Change the Purchase Financials to include:
    * Purchase Date (date; required)
    * Asset Value (number; 2 decimals; required value)
      * NOTE: Migrate the Purchase Amount into this field.
    * Amount Held by Seller (number; 2 decimals)
    * Purchase Amount (read-only; Asset Value minus Amount Held by Seller)
    * Premium Paid $ (read-only; calculated off invoices/bills linked to this Asset)
    * Expenses Paid $ (read-only; calculated off invoices/bills linked to this Asset)



  


  * Cash Collected - Rename to "Sale of Asset"
    * Sale Price Paid $ (calculated from Asset Sale invoice+bills)
    * Show macros for
      * Invoice Date
      * Invoice Amount
    * New Invoice link
      * New Invoice needs to default the RTO Company on the invoice.
      * If the asset has an active contract, hide the New Invoice link and add validation against creating an invoice. Same thing if it already has an invoice.
    * Commission Paid $ (based on bills/invoices)



  


  * NOTE:
    * Depreciation Start Date must be on or after the purchase date.



  


Contact:

  * Add the Premium % RG to Dealers as well
  * Add the Resell Percentage RG to Dealers and Salespeople as well



  


Bill:

  


  * Itemization RG:
    * For Premium, add MRG fields:
      * Asset Value (look up from asset)
      * Calculated Premium % (look up from payee RG)
      * Calculated Premium $ (look up from payee RG)
      * Override (checkbox)
      * Actual Premium % (calculated as Amount / Asset Value * 100; 2 decimals)
      * Amount (editable if Override)
    * For Commission, add MRG fields:
      * Sale Price (look up from asset)
      * Calculated Resell Commission % (look up from payee RG)
      * Calculated Resell Commission $ (look up from payee RG)
      * Override (checkbox)
      * Actual Commission % (calculated as Amount / Resell Price * 100)
      * Amount (editable if Override)



  


  * For Asset Purchase, filter the list with: active buildings that have a non-zero balance (excluding this record) where the contact manufacturer or dealer matches the payee, and populate the amount with the balance.
  * For Asset Premium:
    * use the same contact filter
    * for inactive buildings, include any with a non-zero Premium Paid $ -- if it's not too slow, otherwise let's talk
    * for active buildings, include any without a bill tied to it, and if the selected contact has a premium assigned to them as of the building date
  * Add Asset Commission:
    * also match on Salesperson
    * everything else is the same as Asset Premium



  


Add buttons for

  * Add Unpaid Asset Purchases (add new rows for any ones that aren't in the RG already; basically, use the helper list)
  * Add Unpaid Asset Premiums (same as above)



  


Reports

  * Unpaid Assets
  * Unpaid Premiums



  


TODO_PERMISSION - We need to add a permission for "Can Delete Record" lock down deletes to high permission
