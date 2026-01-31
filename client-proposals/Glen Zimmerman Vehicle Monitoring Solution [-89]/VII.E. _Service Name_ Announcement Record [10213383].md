7.5. <Service Name> Announcement Record

  


Requirements

From the Account record: 

_NM: Tim Reitz 12/12/2025: Per Glen yesterday, he thinks it would make sense to send the emails from Silverloom. Would this warrant a separate "Announcement" record to store information / contents? Maybe the recipients would be stored on that record, with a virtual RG on the Account (instead of adding rows to the RG on the Account). 

TODO_T/J: Tim Reitz 12/16/2025: Discussed with Nic. Let's plan toward an Announcement record: 

  * [X] Announcement record: 
    * Announcement section: 
      * Type (required; drop list of "Announcement Types" list items; __) 
      * Category (required; __
      * Title (required; plain text; __
      * Additional Notes (visible and required if "Type" = "Direct Mail"; plain text field; __
    * Email Details section (visible if "Type" = "Email"): 
      * Draft (checkbox; __
      * Subject (read-only macro; displays the contents of the "Title" field) 
      * Contents (required if visible; memo; __
    * Prepared Date & Recipients section: 
      * Prepared By (__ 
      * Prepared Date (__
      * Recipients (read-only embedded spreadsheet with the following: 
        * __
  * [ ] Announcements report
  * [ ] On the Account record: 
    * [ ] Change the Announcements RG to be a virtual RG 
  * [ ] "Select Recipient" report
  * [ ] "Add Announcement Recipients from Report" x30 / automatic process
  * [ ] Account Announcement email merge: 
    * [ ] To: "Traccar Login Email" addresses in the Recipients RG
    * [ ] CC: 
    * [ ] BCC: 
    * [ ] Body: 
  * [ ] "Announcement Address List" Excel file
  * [ ] Workflow notes



  


\------------

  


Overview: This is a custom record type, used to define and track announcements that are sent to end users.

  


Accessed via: 

  * "Announcements" embedded spreadsheet on the Account record 
  * "<Service Name> Announcements" report



  


Sections and Fields: 

  


  * Announcement section: 
    * Internal ID (hidden; auto-set and read-only; numeric; automatically incremented; this is the unique identifier for the record)
    * Type (required; drop list of "Announcement Types" list items) 
    * Category (required; drop list of "Announcement Categories" list items)
    * Title (required; plain text; no validation against duplicates)
    * Additional Notes (visible and required if "Type" = "Direct Mail"; plain text field) 
    * Status (auto-set and read-only; list field of "Draft" / "Sent"; with the following details / behaviors:
      * defaults to "Draft"; set by buttons / automatic process - see corresponding specs; 
      * note that the whole record become read-only on the first Save after this is set to "Sent";
      * warning on the first Save after this is set to "Sent": "Please ensure that details are correct. Announcement will become non-editable after saving.") 
    * Send Email (visible if "Type" = "Email and "Status" = "Draft"; button; prompts the user to exit edit mode, then sends the "<Service Name> Announcement" email (see corresponding spec) and sets "Status" to "Sent") 
    * Export Address List & Mark as Sent (visible if "Type" = "Direct Mail" and "Status" = "Draft"; button; prompts the user to exit edit mode, then generates the "Announcement Address List" Excel file export and sets "Status" to "Sent") 
    * Ensure that the announcement is ready to send before clicking this button. (visible if "Status" = "Draft"; on-screen message in italicized red font)



  


  * Email Details section (visible if "Type" = "Email"): 
    * Subject (read-only macro; displays the contents of the "Title" field) 
    * Email Body (contents are required if the memo is visible; memo)



  


  * Prepared Date & Recipients section: 
    * Prepared By (auto-set and read-only; list of "Short Display Name" values for Contacts; defaults to the Contact of the user who created the record) 
    * Prepared Date (required; date; defaults to the current date when the record is created) 
    * Save the announcement to select recipients. (message in green font; visible before the initial Save) 
    * Select Recipients (link; with the following details / behaviors:
      * visible after the initial Save if "Status" = "Draft";
      * prompts the user to save the record, then opens the "All Accounts" report with the "Add Recipients to Announcement" filter checkbox checked and any filter settings from the "Stored Recipients Filter Criteria" hidden field - see corresponding spec)
    * Stored Recipients Filter Criteria (hidden; plain text field; set via the "__" automatic process; stores filter settings from the "Select Recipients" report, to pass through for copied Announcement records)
    * Recipients (visible after the initial Save; read-only "virtual" embedded spreadsheet with the following; tracks all Accounts / Primary Account Manager Contacts who are set as recipients for this Announcement: 
      * Columns: 
        * Account (required; drop list of Accounts; with the following details / behaviors: 
          * list to select displays in the following format: "<Account #> \- <Primary Account Manager Display Name>"; 
          * when an item is selected, only the "Account #" is displayed/stored in the field; 
          * error on the field if the same "Account #" is selected for multiple rows: "An account can only be included once per announcement."; 
          * when set, the following field(s) are affected on change: 
            * "Primary Account Manager": sets to the "Short Display Name" for the Primary Account Manager for the selected Account; 
            * "Email": sets to the "Traccar Login Email" of the Primary Account Manager; 
            * "Address": sets to the "Address" of the Primary Account Manager) 
        * Primary Account Manager (auto-set and read-only; list field of "Short Display Name" values; sets to the "Short Display Name" of the Primary Account Manager for the selected "Account" at the time that the Recipient row is added)
        * Email (auto-set and read-only; sets to the "Traccar Login Email" of the "Primary Account Manager" at the time that this Recipient row is added; error on Save if there are multiple rows with the same "Email": "The same email recipient is included multiple times: "<Email>"")
        * Address (auto-set and read-only; sets to the "Address" of the "Primary Account Manager" at the time that this Recipient row is added) 
      * Automatically sorted by: "Account #" (sequentially)
      * Buttons to add/remove rows: "Add" / "Delete"
      * Shows 20 rows without scrolling
      * Other Notes: 
        *         * note that the same Contact may be included multiple times if a Member of multiple Accounts that are receiving the same Announcement, but it would be with different "Account #" and Traccar Login Email")



  


  * Record History section (visible to users with the "Full Access" Permission): 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: All users can view. 
  * Editability: Users with the "Full Access" Permission can edit if "Status" = "Draft" (whole record becomes read-only on the first Save after "Status" = "Sent"). 



  


Special Considerations:

  * Copy Record: Allowed. When copied, the following fields are cleared:
    * "Status" (resets to "Draft")
    * "Prepared Date" (resets to the current date)
    * "Recipients" embedded spreadsheet (though the recipients filter settings are retained, for the user to reselect the same subset of recipients)
  * Delete Record: Allowed with no restrictions.
  * Merge Record: Disallowed. 



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.  
  * Unless otherwise noted, all fields that become hidden for any reason (based on other fields, user permissions, etc.) retain their values. If they should be cleared, that is noted specifically in the field specs, with a "clear if hidden" or similar note.
  * Heading color: This record type uses the standard Silverloom blue color for section headings.
  * Note that a future feature could be to allow sending Announcements to any Contact in the Silverloom system. The groundwork is being laid for this with the initial feature, but some changes would need to be made, such as:
    * Adding an "Announcements" virtual embedded spreadsheet to the Contact record to track Announcements for each Contact (similar to / same as the virtual embedded spreadsheet on the Account record).
    * Changes to the "Recipients" embedded spreadsheet on the Announcement record, specifically to handle recipients who are not linked to an Account (such as making "Account #" optional / changing "Primary Account Manager" to "Recipient", etc.).
    * Change the "Select Recipients" report to be a Contacts-level report with the necessary columns & filters.



  


\--------- 

Workflow: 

  * __ 
  * Set up the Announcement 
  * Save 
  * Add recipients: 
    * Batch: Click the link, open the prompt screen, set the prompts to filter the recipients, run the report, click the button to run x30 to add all of the report results to the Recipients RG on the Announcement 
      * If this is run multiple times for the same Announcement, do not add the same Recipient multiple times (email addresses) 
    * Individual: Click the RG "Add" button, select the Recipient from a drop list 
  * Remove any extra Recipients as needed (using the "Delete" button)



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1293606273#gid=1293606273](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1293606273#gid=1293606273)

  


  


Tim Reitz 01/29/2026: Per Jisan: For both "Send Email" and "Export Address List & Mark as Sent": Use the same modify records after export expression.
