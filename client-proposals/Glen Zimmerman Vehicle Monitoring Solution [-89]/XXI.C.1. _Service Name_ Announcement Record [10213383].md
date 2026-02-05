21.3.1. <Service Name> Announcement Record

  


Requirements

*Done.

  


Overview: This is a custom record type, used to define and track announcements that are sent to end users.

  


Accessed via: 

  * "Announcements" embedded spreadsheet on the Account record (see corresponding spec)
  * Administrators | Announcements | New Announcement
  * "<Service Name> Announcements" report (see corresponding spec)



  


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
    * Prepared By (auto-set and read-only; list of "Short Display Name" values for Contacts; defaults to the Contact of the user who created the record) 
    * Prepared Date (required; date; defaults to the current date when the record is created) 



  


  * Email Details section (visible if "Type" = "Email"): 
    * Subject (read-only macro; displays the contents of the "Title" field) 
    * Email Body (contents are required if the memo is visible; memo)



  


  * Recipients section: 
    * Save the announcement to select recipients. (message in green font; visible before the initial Save) 
    * Select Recipients (link; with the following details / behaviors:
      * visible after the initial Save if "Status" = "Draft";
      * prompts the user to save the record, then opens the "Select Recipients" report with the "Add Recipients to Announcement" filter checkbox checked and any filter settings from the "Stored Recipients Filter Criteria" hidden field - see corresponding spec)
    * Stored Recipients Filter Criteria (hidden; plain text field; set via the ""Add Announcement Recipients from Report" automatic process; stores filter settings from the "Select Recipients" report, to pass through for copied Announcement records)



  


  * Recipients (visible after the initial Save; read-only "virtual" embedded spreadsheet with the following; tracks all Accounts / Primary Account Manager Contacts who are set as recipients for this Announcement: 
    * Columns: 
      * Account (auto-set and read-only; list field of "Account #" values for Account records; sets when the Recipient row is added; error on the field if the same "Account #" is selected for multiple rows: "An account can only be included once per announcement."; 
      * Contact (hidden; auto-set and read-only; list field of "Display Name" values for Contacts; sets when the Recipient row is added; this links the Recipient row to the Contact record; when set, "Recipient" is set to the "Short Display Name" for the Contact)
      * Recipient (auto-set and read-only; plain text field; sets based on the "Short Display Name" of the "Contact" at the time that the Recipient row is added)
      * Email (auto-set and read-only; sets to the "Traccar Login Email" of the "Contact" at the time that this Recipient row is added; error on Save if there are multiple rows with the same "Email": "The same email recipient is included multiple times: "<Email>"")
      * Address 1 (auto-set and read-only; sets based on the Primary Address of the "Contact" at the time that this Recipient row is added) 
      * Address 2 (auto-set and read-only; sets based on the Primary Address of the "Contact" at the time that this Recipient row is added) 
      * City (auto-set and read-only; sets based on the Primary Address of the "Contact" at the time that this Recipient row is added) 
      * State (auto-set and read-only; sets based on the Primary Address of the "Contact"  at the time that this Recipient row is added) 
      * Zip (auto-set and read-only; sets based on the Primary Address of the "Contact" at the time that this Recipient row is added) 
    * Automatically sorted by: "Account #" (sequentially)
    * Buttons to add/remove rows:
      * "Add": N/A (for Phase 1, rows are only added via the automatic process; in the future, an enhancement could be considered to manually add rows here as well);
      * "Delete": visible if "Status" = "Draft"; deletes the currently selected row;
    * Shows 20 rows without scrolling
    * Other Notes: 
      * note that the same Contact may be included multiple times if a Member of multiple Accounts that are receiving the same Announcement, but it would be with different "Account #" and Traccar Login Email")



  


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
  * Basic workflow: 
    * Set up a new Announcement from "New Announcement" on the menu or on the Announcements report
    * Enter the initial details, and save the announcement
    * Add recipients, via the "Select Recipients" link & report
    * Review the announcement & recipients and make any adjustments (i.e. remove any extra Recipients as needed, using the "Delete" button)
    * For emails: click the "Send Email" button to send
    * For direct mail: click the "Export Address List & Mark as Sent" button
  * Note that a future feature could be to allow sending Announcements to any Contact in the Silverloom system. The groundwork is being laid for this with the initial feature, but some changes would need to be made, such as:
    * Adding an "Announcements" virtual embedded spreadsheet to the Contact record to track Announcements for each Contact (similar to / same as the virtual embedded spreadsheet on the Account record).
    * Changes to the "Recipients" embedded spreadsheet on the Announcement record, specifically to handle recipients who are not linked to an Account (such as making "Account #" optional / changing "Primary Account Manager" to "Recipient", etc.).
    * Change the "Select Recipients" report to be a Contacts-level report with the necessary columns & filters.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1293606273#gid=1293606273](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1293606273#gid=1293606273)

  


_VA: Tim Reitz 02/05/2026: Consider whether to incorporate the Announcements feature into the main proposal, or to separate it as an optional add-on. It has grown into a large feature, well beyond the original request to document communications that are prepared (not sure if that was in the HLD, or earlier in the IDD). 

Tim Reitz 02/05/2026: At this point, I'm marking it as an optional add-on. 

  


  


Tim Reitz 01/29/2026: Per Jisan: For both "Send Email" and "Export Address List & Mark as Sent": Use the same modify records after export expression.
