7.2.4. Contact Record - Email Section

*Done. 

  


  * Email section (standard): 



  


  * Email (no label; embedded spreadsheet with the following; can track multiple email addresses, and one or more can be designated as "Primary"):
    * Columns:
      * Email address
      * Primary (checkbox; if there are rows in the embedded spreadsheet and no row is marked as primary, the first row will be automatically marked as primary upon Save) 
      * Notes (plain text field) 
      * Send Email (link, opens the user's default email client with the email address in the selected row as the recipient.)
    * Buttons to add / delete rows: "✚" / "🞭"
      * custom behavior: delete button is hidden for email addresses that are selected as the "Traccar Login Email" on the "Account Members" embedded spreadsheet on any Account records;
    * Sorted by:
      * Primary/Non-primary
    * Other Notes:
      * Custom behavior: at least one email address is required if "User ID" is not blank - error on Save: "At least one address is required because this Contact has login access."; 
      * Custom behavior: at least one email address is required if the Contact is selected on the "Account Members" embedded spreadsheet for any Account records - error on Save: "At least one email address is required because this Contact is included as an Account Member for one or more Accounts."; note that if the person does not have an email address, one for a related contact (i.e. the Account Manager) can be entered to satisfy this requirement, but it would need to be distinct from other Traccar Login Emails.)


