7.4.2. Account Group Record - Group Admins Section

*Done. 

  


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


