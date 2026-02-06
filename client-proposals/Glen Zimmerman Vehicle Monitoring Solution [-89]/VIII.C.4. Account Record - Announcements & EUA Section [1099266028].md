8.3.4. Account Record - Announcements & EUA Section

  


Requirements

*Done.

  


  * Announcements & EUA section: 



  


  * Announcements for Account (read-only "virtual" embedded spreadsheet with the following, displaying details from Announcement records; used to track notices that have been prepared for the Primary Account Manager via direct mail or email:
    * Columns: 
      * Prepared Date (read-only; date; displays the "Prepared Date" from the Announcement record) 
      * Type (read-only; displays the "Type" from the Announcement record)
      * Category (read-only; displays the "Category" from the Announcement record) 
      * Title / Subject (read-only; displays the "Title" from the Announcement record) 
      * Additional Notes (read-only; displays the "Additional Notes" from the Announcement record) 
      * View (column visible to "Upline Provider Roles" users for the Account; link; displays as "Link"; opens the corresponding Announcement record) 
      * Prepared By (read-only; displays the "Prepared By" from the Announcement record)
    * Automatically sorted by: "Prepared Date" (most recent at the top)
    * Buttons to add/remove rows: 
      * Add: N/A (rows are added automatically) 
      * Delete: N/A (rows cannot be manually deleted in Phase 1, though this ability could be added as a future enhancement, probably to be limited to certain users) 
    * Shows 5 rows without scrolling 
    * Other Notes: 
      * N/A



  


  * View Current EUA (link; opens the file from the top row of the "End User Agreements for Account" embedded spreadsheet in Silverloom Settings, which is the current End User Agreement) 



  


  * End User Agreements for Account (embedded spreadsheet with the following: 
    * Columns: 
      * Effective Date (auto-set and read-only; date; automatically sets to the corresponding date on the top row of the "End User Agreements" embedded spreadsheet in Silverloom Settings at the time that a row is added)
      * View (link; displays as "Link"; opens the corresponding End User Agreement file for the row, from Silverloom Settings) 
      * Contact ID (hidden; auto-set and read-only; list field of "Contact ID" values for all individual Contacts; automatically sets when the row is added - see corresponding specs)
      * Account Member (read-only macro; list of "Short Display Name" values for all Contacts; displays the "Short Display Name" for the Contact set in the "Contact ID" hidden column / field)
      * Agreed To Date (date; with the following details / behaviors: 
        * required if "Agreed to By Name" is not blank; 
        * editable for "Upline Provider Roles" users for the Account and editable via import; 
        * to be set by the end users via the End User Portal, or manually here by an "Upline Provider Role" user; 
        * can be cleared manually if a user needs to re-agree to an EUA; 
        * warning on the field if changed from a saved non-blank value: "Use caution when editing this date.")
      * Agreed To By Name (plain text; with the following details / behaviors: 
        * required if "Agreed to Date" is not blank; 
        * editable for "Upline Provider Roles" users for the Account and editable via import; 
        * to be set by the end users via the End User Portal, or manually here by an "Upline Provider Role" user; 
        * can be cleared manually if a user needs to re-agree to an EUA; 
        * warning on the field if changed from a saved non-blank value: "Use caution when editing this name."; 
        * when set to a non-blank value, the following field(s) are affected; 
          * "Agreed To By User": sets to the "User ID" of the user who set this field)
      * Agreed To By User (read-only macro; displays the following: 
        * if "Agreed To By Silverloom User ID" is not blank: displays that; 
        * otherwise, if "Agreed To By Portal User Email" is not blank: displays that; 
        * otherwise (if both are blank): displays blank) 
      * Agreed To By Silverloom User ID (plain text field; with the following details / behaviors:
        * auto-set and read-only interactively; 
        * editable via import; 
        * automatically sets to the "User ID" of the Silverloom user who manually set the "Agreed To Name" (when manually set))  
      * Agreed To By Portal User Email (plain text field; with the following details / behaviors:
        * auto-set and read-only interactively; 
        * editable via import; 
        * automatically sets to the "Traccar Login Email" used to log into the Portal (when set by a user from the Portal))  
    * Automatically sorted by:
      * First by: "Effective Date" (latest at the top)
      * Second by: "Account Member" (alphabetical)
    * Buttons to add/remove rows:
      * Add: N/A (rows are only added automatically - see notes below);
      * Delete: N/A (rows are only deleted automatic process - see notes below; certain fields can be edited / cleared if needed)
    * Shows 5 rows without scrolling
    * Other Notes: 
      * End users must agree to the <Service Name> End User Agreement. This is done at various points in time: 
        * When an end user (Account Manager or Driver) becomes an Account Member on an Account. 
        * When an existing Account Member becomes the "Primary Account Manager". 
        * Annually on the Renewal Date for the Account (only the "Primary Account Manager" for the Account). 
        * Note that if a new EUA is uploaded to the software, end users do not need to agree to it immediately (they can wait until their next renewal).
      * Rows are added automatically:
        * On the first Save after a new row is added to the "Account Members" embedded spreadsheet - see corresponding spec. 
        * On the first Save after the "Primary Account Manager" is changed on the "Account Members" embedded spreadsheet - see corresponding spec. 
        * Annually at the renewal date, via the "Prepare Annual Renewals" automatic process - see corresponding spec. 
      * Rows with "Agreed To Date" = blank are removed automatically: 
        * On the first Save after the corresponding Contact row is removed from the "Account Members" embedded spreadsheet - see corresponding spec. 
        * On the first Save after an Account is deactivated (specifically, after "Stored Account Status" is set to "Closed") - see corresponding spec)



  


Development Specification

"End User Agreements for Account" RG: 

"Link" column Dev Spec: 

  * To open the PDF from Silverloom Settings: Pull the appropriate file path from doc archive based on date. 
  * Use a report with an autopush link action with a type of view documented. Pass in the file path and use in link action parameter.



TODO_PRICING: Tim Reitz 01/06/2026: This part could be coded by CCUSA.
