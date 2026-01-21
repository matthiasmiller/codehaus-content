13.3.6. Payment Record

Overview: This is a custom record type, used to keep track of customer payments. This record tracks the total payment amount, but the details of how the payment was split apart are recorded on the contract records. Payments are only edited through the "Take a Payment" menu option and never interactively.

  


  


  * Payment Overview (section)
    * Payment For (required; list of "Contract" and "Invoice")
    * Customer (required; list of customers)
    * Rental Company (required)
    * Date (required)
    * Payment Amount (required) 
    * Payment Method (required; list of Cash, Check, Credit Card, Debit Card, ACH, Other)
    * Debit Card/Credit Card/ACH (string; required for Debit Card, Credit Card, and ACH; will be a droplist from the payment processor in the WSGI)
    * Reference Number (string field; required for Check and Other) 
    * Confirmation ID
    * Internal ID
    * NSF Date (date; only visible if set)



  


  * One-Time Payment Method Details (section)
    * ACH Account Type
    * ACH Account Last Four
    * ACH Routing Number
    * Card Issuer
    * Card Last Four
    * Additional Info



  


  * Notes (section)
    * "This record must be saved before creating a linked note." (label, visible for new unsaved records)
    * New Note (opens a new note record; populates the Type + Linked Record, visible if the record has been saved)
    * View Notes (report link; opens the My Notes report)
    * Notes (read-only memo that concats based on record Type + record ID, sorted in order of Note ID; newest first)



  


Modification History: This contains the following standard feature for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access: 

  * TODO_PERMISSIONS: Needs some kind of permission to prevent people from editing the payment history, but we do need a superpower/admin level, but we need admin levels below that. We need
    * Can create payments (editable if new record as long as creation date = today)
      * Can edit historical payments
    * Duane Burkholder 07/21/2025: Not sure what we are going to call our user levels yet but I would say anybody above a view only level should be able to input a payment. In order to edit a payment it would need to be a payment you entered and the same day as entry. In order to edit historical payments you would need to have the "Superpower" level. :-)



  


Special Considerations: TODO_PERMISSIONS: 

  * Copy Record: __ (think: does it make sense to allow copies? what fields are retained / cleared on copy?) 
  * Delete Record: __ (think: allow deletion? under what circumstances?)
  * Merge Record: __ (think: does it make sense for this record to be merged since the initiating one is deleted completely?; if we disallow deletion across the board, probably disallow merging)


