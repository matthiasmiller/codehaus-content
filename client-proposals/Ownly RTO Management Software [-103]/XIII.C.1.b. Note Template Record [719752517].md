13.3.1.2. Note Template Record

Overview: This is a custom record type, used to keep track of Call Scripts and Letter Templates. This replaces Contract Scripts.

  


Accessed via: Settings | Configuration | Configure Note Templates

  


Welcome Script #1

Call Script #1

Welcome Script #1

Welcome Script #1

  


Sections and Fields: 

  * Name (auto-generated; "Title - RTOCompanyShortCode" i.e. Welcome Script #1)
  * Title (plain text; ID field)
  * Rental Company (required)
  * Note Type (required; list of Note Types)
  * Record Type (list of database level): 
    * Contact
    * Contract
    * Product
    * Payment
    * User
    * The template does not need to be supported on all levels, only the above.
  * Require Followup By Default (checkbox)
  * Contents (expression field memo for the appropriate level)



  


Modification History: This contains the following standard feature for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access: 

  * Edit Record: has "Edit Note Templates" permission
  * TODO_PERMISSION



  


Special Considerations: 

  * Copy Record: with "Edit Contract Scripts" permission
  * Delete Record: with "Edit Contract Scripts" permission
  * Merge Record: with "Edit Contract Scripts" permission



  


Notes:

  * This will be able to reference Contract fields. We will have links somewhere for people to pull up call scripts and letter templates.
  * On Copy: clear Creation Date and Completed


