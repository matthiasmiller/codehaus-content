7.2.9. Contact Record - Provider Traccar Logins Section

  


Requirements

  * Provider Traccar Logins (custom section; visible on individual Contacts if any of the following checkboxes are checked: "Is Master Administrator", "Is Group Admin", "Is Account Reseller", "Is Reseller Rep"; visible to __; editable for users with the "Full Access" Permission) 
    * Provider Traccar Logins (no label; embedded spreadsheet with the following:
      * __



TODO_VA: Tim Reitz 01/27/2026: Spec this out once we have the details finalized for the "Account Members" RG.

Tim Reitz 01/20/2026: I'm thinking an RG similar to the "Account Members" RG (with the same synced fields, etc.). Could have multiple rows since the same provider could wear multiple hats (Reseller on his own / for a company, plus a Group Admin for a Group...).

TODO_VA: Tim Reitz 01/27/2026: Consider whether this should be an RG on the main screen, or behind a button to save space (especially since this is a really wide RG on the Account record).

  


TODO_NM: Tim Reitz 01/30/2026: I think ideally this login info would actually be stored on different records: 

\- Group Admins: on the Group record (this allows the same person to be an admin for multiple distinct Groups) 

\- Resellers (individuals): On this main RG on the Contact (maybe allow only 1??) 

\- Reseller Reps: on the Reseller org's Reps RG (this allows the same person to be a rep for multiple different Resellers) 

\- Master Administrator: On this main RG on the Contact (allow only 1)

However, this feels complex and cumbersome to add at this point. 

I'm thinking that for Phase 1, we keep it all here on the main RG and allow only 1 row, and the Traccar permissions look at the highest level of permissions (either Master Administrator or Reseller/Group Admin) - I think this works since I'm planning toward making most/all Providers read-only in Traccar. 

And we save the full feature for a future enhancement. 

  * Provider Traccar Logins (no label; embedded spreadsheet with the following; note that this parallels the "Account Members" embedded spreadsheet on the Account record, and changes should be considered for both:
    * Columns: 
      * __ (required; __; used to document the "reason" for this login
      * Name (required; auto-set and read-only; defaults to the "Display Name" for the current Contact when a row is added; data synced with Traccar, via the Traccar User sync record) 
      * Master Administrator (checkbox; editable if "Is Master Administrator" is checked for the current Contact record; data synced with Traccar (as User permission), via the Traccar User sync record) 
      * Group Admin (checkbox; editable if "Is Group Admin" is checked for the current Contact record; defaults to not checked; data synced with Traccar (as User permission), via the Traccar User sync record)
      * Account Reseller (checkbox; editable if "Is Account Reseller" is checked for the current Contact record; defaults to not checked; data synced with Traccar (as User permission), via the Traccar User sync record) 
      * Mobile Phone (required; drop list of phone numbers for the current Contact with "Type" = "Mobile"; data synced with Traccar, via the Traccar User sync record) 
      * Traccar Login Email (required; drop list of email addresses from the Contact's "Email" embedded spreadsheet; with the following details / behaviors:
        * error on the field if an email address is selected that has already been saved as the "Traccar Login Email" on any Account or Contact in the Solution (including the current one): "This email address has already been used for another Traccar login. Please use a different email.";
        * this is the email address that is set as the login email for this person's User login in Traccar; 
        * data synced with Traccar, via the Traccar User sync record)
      * Primary Address (read-only macro; with the following details / behaviors: 
        * displays the primary Address for the current Contact, as a combined string in the following format: "<Address>, <Address 2>, <City>, <State> <Zip>"; 
        * note that the column width might be narrower than the full address, to save space)
      * Traccar Login Enabled (checkbox; with the following details / behaviors: 
        * defaults to checked; 
        * data synced with Traccar, via the Traccar User sync record) 
    * Automatically sorted by:
      * First by: Role:
        * "Master Administrator",
        * "Group Admin",
        * "Account Reseller";
      * Second by: Name (alphabetically)
    * Buttons to add/remove rows: 
      * "Add Login" (visible to users with the "Full Access" Permission) 
      * "Remove Login" (visible to users with the "Full Access" Permission; with the following details:
        * hidden if any of the following are true for the Contact:
          * is set as the "Account Reseller" on any Account records;
          * is set as the "Reseller" on any Device records;
          * is set as a "Group Admin" on any Account Group records;
        * note that an on-screen explanation message is displayed when the button is hidden -see spec below) 
    * Shows 3 rows without scrolling
    * OnChange and OnSave Behaviors: 
      * On the first Save after one or more new rows are added, the following happen for each newly-added row:  
        * the "Create/Update Traccar User Records" triggered automatic process runs to create and/or update Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec; 
      * On the first Save after one or more rows are removed, the following happen for each removed row: 
        * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec; 
      * On the first Save after "Account Reseller" is checked for one or more rows, the following happen for each edited row:
        * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec; 
      * On the first Save after "Account Reseller" is unchecked for one or more rows, the following happen for each edited row:
        * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec;
      * On the first Save after "Group Admin" is checked for one or more rows, the following happen for each edited row:
        * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec;
      * On the first Save after "Group Admin" is unchecked for one or more rows, the following happen for each edited row:
        * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec;
      * On the first Save after "Master Administrator" is checked, the following happen: 
        * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec; 
      * On the first Save after any of the other editable fields (i.e. "Mobile Phone", "Traccar Login Email", "Traccar Login Enabled") are changed for one or more rows, the following happen for each edited row:
        * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec; 
    * Additional Validations: 
      * On the first Save after any changes are made to this embedded spreadsheet: warning on Save: "Changes have been made to Traccar Logins.";
    * Other Notes: 
      * N/A



  


  * This Traccar Login cannot be deleted because it is associated with one or more Accounts and/or Devices and/or Account Groups. Resolve these connections to remove the Traccar Login. (on-screen message in green font; visible if the Contact meets the criteria for the "Remove Login" button to be hidden - see corresponding spec)



  


Development Specification

TODO_MOCK
