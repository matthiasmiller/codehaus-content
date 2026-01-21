7.4. Account Group Record

  


Requirements

*. 

  


Overview: This is a custom record type, used to track Account Groups. This allows for grouping of Accounts for support and supervision, and allows the Group Admins to manage the Accounts in their Group.

  


Account Groups can be "nested", creating a series of "upline" and "downline" Groups. An Account Group can have only one direct upline, but may have multiple downlines.

  


The Solution include ones or more general or "catch-all" Account Group records, administered by Master Administrators, for Accounts that do not correspond to any of the main Account Groups. Note that an initial "catch-all" Account Group would be set up by CodeCrafters at deployment.

  


Accessed via: 

  * "Account Groups" reports
  * "Account Group" field on the Account record 
  * Providers | Account Groups | New Group (opens a new Account Group record) 



  


Sections and Fields: 

  * Account Group Details section:
    * Left side:
      * Group Name (required; plain text; with the following details / behaviors: 
        * editable for users who can edit the record; 
        * validate against duplicates - error on the field: "This Group Name is already being used by another Group."; 
        * data synced with Traccar)
      * Group State (read-only macro; displays the "State" from the primary address of the Primary Group Admin for the Group; this is for region-based reporting and notifications) 



  


  * Right side:
    * Active (checkbox; defaults to checked; editable only for users with the "Full Access" Permission; error on the field when unchecked if there are any linked Accounts with "Status" = anything except "Closed": "Group cannot be deactivated because it has one or more non-closed Accounts.") 



  


  


  * Group Admins section:
    * Group Admins (no label; embedded spreadsheet; editable for users who can edit the record; with the following: 
      * Columns: 
        * Group Admin Contact ID (hidden; auto-set and read-only; list field of "Contact ID" values; sets to the "Contact ID" for the Contact selected in the "Name" field for the same row - see corresponding spec) 
        * Name (required; with the following details / behaviors:
          * drop list of "Display Name" values for active Contacts with the "Is Group Admin" checkbox checked; 
          * when set, the following field(s) are affected: 
            * "Contact ID" for the same row: sets to the "Contact ID" for the Contact) 
        * Primary (checkbox; defaults to not checked; with the following details / behaviors:
          * error on the field if checked when "Primary" is already checked for another row: "Only one Group Admin can be set as Primary.";
          * error on Save if no row is marked as Primary: "A Primary Group Admin is required.")
        * Phone (read-only macro; displays the Primary Phone for the selected Contact)
        * Email (read-only macro; displays the Primary Email address for the selected Contact)
        * Address (read-only macro; displays the Address for the selected Contact, as a combined string in the following format: "<Address>, <Address 2>, <City>, <State> <Zip>"; note that the column width might be narrower than the full address, to save space)
        * View/Edit (column visible to users who can edit the record (see "Editability Details" spec below); link to open the selected Contact record; displays as "Link")
      * Automatically sorted by:
        * First by: "Primary" (the row with "Primary" checked sorts to the top) 
        * Second by: Name (alphabetically)
      * Buttons to add/remove rows: "Add" / "Remove" (buttons are visible only to users who can edit the record) 
      * Shows 5 rows without scrolling
      * Special OnChange / OnSave Behaviors:
        *  On the first Save after one or more of the following changes are made to the "Group Admins" embedded spreadsheet: 
          * a row is added, 
          * a row is removed, 
          * an existing row has the "Primary" checkbox set to checked, 
          * an existing row has the "Primary" checkbox set to not checked,  
          * then corresponding row(s) are added to the "Group Admin Changes Email Recipients" embedded spreadsheet with the following set: 
            * "Recipient Contact ID": sets to the value of the "Group Admin Contact ID" for all affected rows, including deleted rows; 
      * Other Notes: 
        * Note that this does not track historical Group Admins (rows are removed to remove a Contact from their Group Admin role for the Group).



  


  * Changes have been made to the Group Admins. Save the record, then send the "Group Admin Changes" email. (on-screen message in green font; visible to users who can edit the record; visible before the first Save if any of the following changes have been made to the "Group Admins" embedded spreadsheet:
    * a row is added, 
    * a row is removed, 
    * an existing row has the "Primary" checkbox set to checked, 
    * an existing row has the "Primary" checkbox set to not checked) 
  * Changes have been made to the Group Admins. Send the "Group Admin Changes" email. (on-screen message in green font; visible to users who can edit the record; visible if there are any saved rows in the "Group Admin Changes Email Recipients" embedded spreadsheet) 



  


  * Group Admin Changes Email Recipients (hidden; embedded spreadsheet with the following: 
    * Columns: 
      * Recipient Contact ID (auto-set and read-only; list field of "Contact ID" values for all Contacts; set when certain changes are made to the "Group Admins" embedded spreadsheet - see corresponding spec) 
    * Automatically sorted by: N/A (none - rows retain the sequence in which they were added) 
    * Buttons to add/remove rows: N/A (none) 
    * Shows 8 rows without scrolling 
    * Other Notes: 
      * rows are automatically added with the first Save after changes are made to the "Group Admins" embedded spreadsheet -- see the corresponding spec; 
      * rows are automatically deleted when the email is sent (via the "Send "Group Admin Changes" Email" automatic process -- see the corresponding spec), not retained to keep a history of people who were sent the email) 



  


  * Select Recipients & Send Email (button; visible to users who can edit the record; visible if there are any saved rows in the the "Group Admin Changes Email Recipients" embedded spreadsheet; clicking this button forces the user to save the record again (to prevent lost data), then opens a prompt screen with the following: 
    * Recipients (multi-select drop list of "Display Name" values for the Contacts included in the "Group Admin Changes Email Recipients" embedded spreadsheet; defaults to all checked/selected) 
    * The "Group Admin Changes" email will be sent to all selected recipients and all Master Administrators. (message in gray font) 
    * Send Email (button; runs the "Send Group Admin Changes Email" automatic process, to send the email and clear the hidden "Group Admin Changes Email Recipients" embedded spreadsheet - see corresponding automatic process spec; note that the user will need to refresh the Account Group screen after this process runs) 



  


  


  * Group Hierarchy section:  
    * Direct Upline Group (optional; drop list of active "Account Group" records that are not in the "Downline Group(s)" list for the current Group; with the following details / behaviors:
      * editable for users who can edit the record; 
      * drop list filtering: 
        * for users with the "Full Access" Permission: the drop list is not filtered further; 
        * for Group Admins: the drop list is filtered to include only Account Groups that the user can edit; 
      * used to select the "parent" / direct upline Group for the current Group) 
    * Group Hierarchy (visible if "Direct Upline Group" is not blank; read-only memo; displays the hierarchy of linked Groups, with the following details: 
      * displays all Upline Groups and all Downline Groups, based on the "Direct Upline Group" fields; 
      * displays the "Group Name" for each included Group; 
      * the row for the current Group is displayed in bold text) 



  


  


  * Record History section (visible to users who can edit the record):
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (visible only to users with the "Full Access" Permission; link to open the report for the record)



  


  


  * Linked Accounts Bottom Report (displays the "Accounts by Group" report (see corresponding spec), filtered to the current Group)



  


  


Data Access: 

  * Visibility: Can be viewed by: 
    * Users with the "Full Access" Permission can view the screen & all included items.  
    * All other users can view, but some sections / fields may be hidden.
  * Editability: Can be edited by (with some additional conditions specced on individual items): 
    * Users with the "Full Access" Permission (one or more items limited to only these users). 
    * The linked "Account Group Admin" users for the Group and "Upline Group(s)" 



  


Special Considerations:

  * Copy Record: Allowed for users who can edit the record; the following field(s) are cleared on the new record:
    * Group Name
  * Delete Record: Allowed for users with the "Full Access" Permission if the Group is not active and does not have any linked Accounts.
  * Merge Record: Allowed for users with the "Full Access" Permission. Note that the record from which the merge is initiated is completely replaced by the other (deleting all data for the first record).



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * Unless otherwise noted, all fields that become hidden for any reason retain their values. If they should be cleared, that is noted specifically in the field specs. 
  * Heading color (custom): This record type uses a light orange color for section headings.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=757234751#gid=757234751](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=757234751#gid=757234751)

  


  


  


  


Tim Reitz 10/30/2025: It would probably be an extra $500-700 to send it conditionally, choosing who to send it to (would include an extra RG to track who could receive it, with options to change). Probably extra $200-300 if we simply choose whether or not to send it at all ("Send Email on Next Save" checkbox). Is it worth it to you? 

Tim Reitz 11/06/2025: Glen likes the option of choosing who to send the email to. 

Tim Reitz 12/30/2025: Retaining these notes for reference during pricing, etc. 

  


  


_EM - Does CCI care about liability of having this much tracking information, and what happens from a publicity/legal standpoint if something goes awry?

Tim Reitz 08/21/2025: This is a note from before the IDD.

TODO_: Tim Reitz 10/30/2025: Per Ellis, some of this could depend on how much of the Traccar data is pulled into Silverloom. 

TODO_: Tim Reitz 10/30/2025: We should also discuss the liability aspect with Glen before pricing (data leaked, lawsuit, etc.). And clearly note that with agreement text, etc.
