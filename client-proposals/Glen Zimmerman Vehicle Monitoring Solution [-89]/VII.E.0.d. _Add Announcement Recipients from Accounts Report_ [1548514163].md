7.5.0.4. "Add Announcement Recipients from Accounts Report"

*Done.

  


  * Name: "Add Announcement Recipients from Accounts Report"
    * Description: This automatic process sets the Accounts report to add rows to the "Recipients" embedded spreadsheet on an Announcement record.
    * Prompts: 
      * Announcement "Internal ID"
    * Initiated:
      * When the "Add Recipients" button on the Accounts report
    * Action(s): 
      * Adds rows to the "Recipients" embedded spreadsheet on the Announcement record, with the following set:
        * "Account": sets to the "Account #";
        * "Primary Account Manager": sets to the "Primary Account Manager" for the Account;
        * "Email": sets to the "Traccar Login Email" for the corresponding "Primary Account Manager" from the Account; if there is already a row with the same email address, the current one will be skipped; 
        * "Address": sets to the "Address" for the corresponding "Primary Account Manager" from the Account


