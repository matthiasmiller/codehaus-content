7.5. <Service Name> Announcement Record

  


Requirements

From the Account record: 

_NM: Tim Reitz 12/12/2025: Per Glen yesterday, he thinks it would make sense to send the emails from Silverloom. Would this warrant a separate "Announcement" record to store information / contents? Maybe the recipients would be stored on that record, with a virtual RG on the Account (instead of adding rows to the RG on the Account). 

TODO_VA / TODO_T/J: Tim Reitz 12/16/2025: Discussed with Nic. Let's plan toward an Announcement record: 

  * [ ] Announcement record: 
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
  * [ ] On the "Document Account Announcements" report
    * [ ] Update the spec to create these records & send the emails, etc. 
  * [ ] Account Announcement email merge: 
    * [ ] To: "Traccar Login Email" addresses in the Recipients RG
    * [ ] CC: 



TODO_GZ: Tim Reitz 01/15/2026: Do you want to CC the reseller on this? (would mean a lot of emails) 

  * [ ] BCC: 



TODO_GZ: Tim Reitz 01/15/2026: Do you want to BCC an internal email address for documentation? 

  * [ ] Body: 



  


TODO_GZ: Tim Reitz 01/15/2026: However, discuss further: Is this for a one-time announcement, or would the same one be sent multiple times? 

TODO_T/J: Tim Reitz 01/15/2026: If multiple times, we probably would want to store the recipients on the Announcement, so that the record can be copied with the recipients retained... 

Or, would we give the option to "Resend" the same Announcement? 

Tim Reitz 01/15/2026: Probably not resend the same one -- we would need to store multiple send dates, etc. 

  


TODO_GZ: Tim Reitz 01/15/2026: Also, would the Announcements ever be sent to individual Contacts - Resellers, Group Admins, or end users? 

Tim Reitz 01/20/2026: Choose types, including options for all Account Managers / Drivers? 

Tim Reitz 01/20/2026: If yes, have a special report (other than a filtered version of the All Accounts report): repeat by RG, multi-select drop list of Account Members... 

  


  


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
    * Ensure that the announcement is ready to send before clicking this button. (visible if "Type" = "Email and "Status" = "Draft"; on-screen message in italicized red font)
    * Mark as Sent (visible if "Type" = "Direct Mail" and "Status" = "Draft"; button; sets "Status" to "Sent") 



  


  * Email Details section (visible if "Type" = "Email"): 
    * Subject (read-only macro; displays the contents of the "Title" field) 
    * Email Body (contents are required if the memo is visible; memo)



  


  * Prepared Date & Recipients section: 
    * Prepared By (auto-set and read-only; list of "Short Display Name" values for Contacts; defaults to the Contact of the user who created the record) 
    * Prepared Date (required; date; defaults to the current date when the record is created) 
    * Save the announcement to select recipients. (message in green font; visible before the initial Save) 
    * Select Recipients (visible after the initial Save; link; prompts the user to save the record, then opens the "All Accounts" report with the "Add Recipients to Announcement" filter checkbox checked - see corresponding spec)
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
    * "Recipients" __



TODO_GZ: Tim Reitz 01/20/2026: Would you want to clear or retain the Recipients list?

  * Delete Record: Allowed with no restrictions.
  * Merge Record: Disallowed. 



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.  
  * Unless otherwise noted, all fields that become hidden for any reason (based on other fields, user permissions, etc.) retain their values. If they should be cleared, that is noted specifically in the field specs, with a "clear if hidden" or similar note.
  * Heading color: This record type uses the standard Silverloom blue color for section headings.



  


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

Mockup: 

TODO_MOCKUPS: Tim Reitz 01/15/2026: This is ready for an initial mockup.

  


Tim Reitz 01/20/2026: Per Jisan, for sending the email + modifying the record: Use modify record after export setting (modify expression).
