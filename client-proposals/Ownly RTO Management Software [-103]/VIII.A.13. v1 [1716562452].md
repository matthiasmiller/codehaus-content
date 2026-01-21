8.1.13. v1

On the Asset

  


  * Store Resell Price on the asset; New Invoice references it; validate that it matches if it's Invoiced or Paid, i think but not completely sure



RG:

  


  


  * Add to Bill itemization drop list
    * Ownly Asset Resell



  


  * Invoices
    * Add the same drop list of itemization for assets; this needs to be used when calculating balances on the Asset



  


  * Asset
    * Entry Date (use the record creation date as a date expression; read-only; can be hidden for new records)



  


  * Change the Purchase Financials to include:
    * Purchase Date (date; required)
    * Asset Value (number; 2 decimals; required value)
      * NOTE: Migrate the Purchase Amount into this field.
    * Amount Held by Seller (number; 2 decimals)
    * Purchase Amount (read-only; Asset Value minus Amount Held by Seller)
    * NOTE: You can only have 1 bill for the purchase of the building



  


  * Premium
    * Calculated Premium % (based on the manufacturer) 
    * Calculated Premium $ (based on the asset value times the premium %)
    * Override Premium
    * Premium $
    * Premium Paid $ (based on the bill)



  


  * Cash Collected - Rename to "Cash Sale"
    * Resell Price (number; 2 decimals)
    *     * Show macros for
      * Invoice Date
      * Invoice Amount
    * New Invoice link
      * New Invoice needs to default the RTO Company on the invoice.
      * If the asset has an active contract, hide the New Invoice link and add validation against creating an invoice. Same thing if it already has an invoice.
    * Commission Paid $ (based on bills)



  


  * NOTE:
    * Depreciation Start Date must be on or after the purchase date.



  


Contact:

  * Add the Premium % RG to Dealers as well
  * Add the Resell Percentage RG to Dealers and Salespeople as well



  


Bill:

  


  * For Asset Purchase, filter the list with buildings that have a non-zero balance (excluding this record) where the contact manufacturer or dealer matches the payee, and populate the amount with the balance
  * For Asset Premium, do the same but with non-zero premiums
  * Add Only Asset Commission to the list and do the same for commissions that have never received payment, but also match on salesperson
    * Default the payment based on the Purchase Amount * the Resell %



  


  


  


Add buttons for

  * Add Unpaid Asset Purchases (add new rows for any ones that aren't in the RG already)
  * Add Unpaid Asset Premiums



  


  


TODO_HLD: Sales tax on sales invoices
