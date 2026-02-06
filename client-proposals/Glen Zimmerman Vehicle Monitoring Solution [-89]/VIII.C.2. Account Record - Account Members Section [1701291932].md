8.3.2. Account Record - Account Members Section

  


Requirements

*.

  


TODO_VA: Tim Reitz 02/02/2026: We're re-speccing our approach to Traccar User linking, since we need to link Traccar User sync records to multiple different record types: 

[ ] Account record (Account Members RG) 

[ ] Account Group record (Group Admins RG) 

[ ] Contact record (Reseller Reps RG) 

[ ] Contact record (__ (Traccar Logins?) RG) 

[ ] New approach: 

  * Store all of the information on the Traccar User sync record 
  * Virtual RGs on the various other records 
  * To create: 
    * Link w/autopush report to open a new Traccar User record (some fields defaulted) 
    * Make selections / changes 
    * Save 
    * Go back to the main record & see it there on the RG 
  * To unlink or edit: 
    * We can do an x30 
      * "Disable Traccar Login" 
      * "Remove from Account" 
      *   * [ ] Find references to "Account Members" embedded spreadsheet, to update other related specs as needed
  * Other details: 
    * We can still satisfy the requirement for 1 and only 1 Primary Account Manager; the provider will need to complete the changes before being able to save the Account (can make the changes in either order)
    * 


TODO_VA: Tim Reitz 02/04/2026: Note that we could also consider having an "Account Members" editable bottom report on the Account, to allow users to make edits directly there (rather than needing to open the Traccar User record every time).

  


  * Account Members section (all fields in this section are editable for "Upline Provider Roles" users for the Account): 



  


  * Account Members (no label; "virtual" embedded spreadsheet with the following, displaying rows for Traccar User sync records that are linked to this Account; note that this parallels other Traccar User embedded spreadsheets on other records, and changes should be considered for both:
    * Columns: 
      * Name (read-only macro; displays the "Name" from the linked Traccar User sync record) required; drop list of "Display Names" for all active Individual Contacts; with the following details / behaviors: 
        * validations:
          * error on Save if changed from a saved value (to prevent changing the member's name): "Account Member's Name cannot be changed. Use the Add / Remove buttons to manage Account Members."; 
          * error on Save if "Date of Birth" is blank on the Contact record of any of the Account Members: "Date of Birth is required for one or more Account Members: <Short Display Name>, <Short Display Name>. Click the "View/Edit Contact" link to add this data before saving the Account changes."; 
          * error on Save if "Gender" is blank on the Contact record of any of the Account Members: "Gender is required for one or more Account Members: <Short Display Name>, <Short Display Name>. Click the "View/Edit Contact" link to add this data before saving the Account changes."; 
        * data synced with Traccar, via the Traccar User sync record) 
      * View / Edit Contact (link to open the corresponding Contact record; displays as "Link")
      * Account Manager (read-only macro; checkbox; displays the value of the "Account Manager" checkbox from the linked Traccar User sync record; defaults to not checked; with the following details / behaviors: 
        * error on Save if no rows have "Account Manager" checked: "At least one Account Manager is required."; 



Tim Reitz 02/04/2026: This validation is not needed, since there's already validation for Primary.

  * note that when this checkbox is checked for a row, the "Is Account Manager" checkbox macro on the corresponding Contact record is checked; 



_NM: Tim Reitz 02/04/2026: Thoughts on whether the "Is Account Manager" macro on the contact should look at the virtual RG here on the Account, or at the corresponding field on the Traccar User sync record?

Same question for the next two as well. 

_VA: Tim Reitz 02/04/2026: On the Traccar User record -- it's for the specific person, rather than for the specific Account.

  * data synced with Traccar (as User permission), via the Traccar User sync record) 


  * Primary Account Manager (read-only macro; checkbox; displays the value of the "Primary Account Manager" checkbox from the linked Traccar User sync record; editable if "Account Manager" is checked for the same row; defaults to not checked; with the following details / behaviors:
    * warning on Save if there is more than one linked Traccar User sync record with "Primary Account Manager" checked: "Only one Account Manager can be set as Primary.";
    * error on the field if checked when "Primary" is already checked for another row: "Only one Account Manager can be set as Primary.";
    * error on Save if there is no linked Traccar User sync record with "Primary Account Manager" checked: "A Primary Account Manager is required."; 
    * error on Save if no row is marked as Primary: "A Primary Account Manager is required."; 



_NM: Tim Reitz 02/04/2026: Validations: Thoughts on where this validation should happen -- here or on the Traccar User sync record?

_VA: Tim Reitz 02/04/2026:

[X] Account: error on Save if there is more than 1 Primary

[X] Traccar User:

[X] warning on Save if another User already is Primary for the linked Account

[X] error on Save if there is no Primary for the linked Account

[X] Report alert for the Reseller if there are any Account records with more than 1 linked Traccar User sync record with "Primary Account Manager" checkbox checked: "Accounts with multiple Primary Account Managers"

Tim Reitz 02/04/2026: Adding a proposal row for this.

  * note that when this checkbox is checked for a row, the "Is Primary Account Manager" checkbox macro on the corresponding Contact record is checked; 



_VA: Tim Reitz 02/04/2026: Pending answer on Account Manager: Update spec here / Traccar User / Contact.

Tim Reitz 02/04/2026: On the Traccar User record -- it's for the specific person, rather than for the specific Account.

  * data synced with Traccar (as User permission), via the Traccar User sync record)


  * Driver (read-only macro; checkbox; displays the value of the "Driver" checkbox from the linked Traccar User sync record; defaults to not checked; with the following details: 
    * note that when this checkbox is checked for a row, the "Is Driver" checkbox macro on the corresponding Contact record is checked; 



_VA: Tim Reitz 02/04/2026: Pending answer on Account Manager: Update spec here / Traccar User / Contact.

Tim Reitz 02/04/2026: On the Traccar User record -- it's for the specific person, rather than for the specific Account.

  * warning on Save if no rows have "Driver" checked: "This Account does not have any Drivers."; 



_VA: Tim Reitz 02/04/2026: Validations: Pending answer on Account Manager: Update spec here / Traccar User.

Tim Reitz 02/04/2026: Let's do a warning on Save both places.

  * data synced with Traccar (as User permission), via the Traccar User sync record) 


  * Mobile Phone (read-only macro; displays the "Mobile Phone" from the linked Traccar User sync record; required; drop list of phone numbers for the selected Contact with "Type" = "Mobile"; with the following details / behaviors: 
    * note that at least one mobile phone number is required for Account Members - see special validation spec below; 



_VA: Tim Reitz 02/04/2026: Consider where this validation should happen. 

Tim Reitz 02/04/2026: This is done via making Mobile Phone" required on the Traccar User record.

  * data synced with Traccar, via the Traccar User sync record) 


  * Traccar Login Email (read-only macro; displays the "Traccar Login Email" from the linked Traccar User sync record; required; drop list of email addresses from the Contact's "Email" embedded spreadsheet; with the following details / behaviors:
    * error on the field if an email address is selected that has already been saved as the "Traccar Login Email" on any Account in the Solution (including the current Account): "This email address has already been used for another Traccar login (User: <Contact Short Display Name>; Account #: <Account #>). Click the View / Edit Contact link to add a new email.";
    * this is the email address that is set as the login email for this person's User login in Traccar; 
    * note that at least one email address is required for Account Members - see special validation spec below; 



_VA: Tim Reitz 02/04/2026: Consider where this validation should happen. 

Tim Reitz 02/04/2026: This is happening via the Traccar User record (email is required there). 

  * data synced with Traccar, via the Traccar User sync record)


  * Primary Address (read-only macro; with the following details / behaviors: 
    * displays the primary Address for the linked Contact, as a combined string in the following format: "<Address>, <Address 2>, <City>, <State> <Zip>"; 
    * note that the column width might be narrower than the full address, to save space; 
    * note that at least one address is required for Account Members - see special validation spec below)



TODO_VA: Tim Reitz 02/04/2026: Consider where this validation should happen. 

  * View / Edit Traccar Login (link to open the linked Traccar User sycn record; displays as "Link")
  * Traccar Login Enabled (read-only macro; checkbox; displays the value of the "Traccar Login Enabled" checkbox from the linked Traccar User sync record); with the following details / behaviors: 
    * defaults to checked; 
    * data synced with Traccar, via the Traccar User sync record) 


  * Automatically sorted by:
    * First by: Role:
      * "Primary Account Manager" (the row with "Primary" checked sorts to the top),
      * "Account Manager",
      * "Driver";
    * Second by: Name (alphabetically)
  * Buttons to add/remove rows: N/A (rows are added automatically when a linked Traccar User sync record is saved)  
    * "Add Member" (visible to "Upline Provider Roles" users for the Account) 
    * "Remove Member" (visible to "Upline Provider Roles" users for the Account; hidden if the account member is set as the "Primary Driver" on a Vehicle for the Account; note that an on-screen explanation message is displayed when the button is hidden - see spec below) 
  * Shows 7 rows without scrolling
  * OnChange and OnSave Behaviors:



_NM: Tim Reitz 02/04/2026: I'm thinking that the "Create/Update Traccar User Records" trigger / import can be removed now (since the users would manually set a lot of fields there). But how would things like Category, Permissions, etc., be set? OnInit via the autopush (see prompt / autopush spec below)? 

TODO_VA: Tim Reitz 02/04/2026: It's autopush report button. No x30 for creating the record/settings fields.

TODO_VA: Tim Reitz 02/04/2026: Review & update the following: 

  * On the first Save after one or more new rows are added, the following happen for each newly-added row:  
    * the "Create/Update Traccar User Records" triggered automatic process runs to create and/or update Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec; 
    * a new row is added to the "End User Agreements for Account" embedded spreadsheet for that Member, with the following set: 
      * "Effective Date": sets to the "Upload / Effective Date" for the top row of the "End User Agreements" embedded spreadsheet in Silverloom Settings (the current EUA);
      * "Contact ID": sets to the "Contact ID" for the new Account Member;
    * the "Send "New Account Member Welcome" Email" triggered automatic process runs, to send the "New Account Member Welcome" email - see corresponding specs; 
  * On the first Save after one or more rows are removed, the following happen for each removed row: 
    * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec; 
    * any rows for the Contact on the "End User Agreements for Account" embedded spreadsheet with "Agreed To Date" blank are removed. 
  * On the first Save after "Account Manager" is checked for one or more rows, the following happen for each edited row:
    * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec; 
    * the "Send "Account Manager Changes" Email" triggered automatic process runs, to send the "Account Manager Changes" Email" - see corresponding specs;
  * On the first Save after "Account Manager" is unchecked for one or more rows, the following happen for each edited row:
    * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec;
    * the "Send "Account Manager Changes" Email" triggered automatic process runs, to send the "Account Manager Changes" Email" - see corresponding specs;
  * On the first Save after "Driver" is checked for one or more rows, the following happen for each edited row:
    * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec;
  * On the first Save after "Driver" is unchecked for one or more rows, the following happen for each edited row:
    * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec;
  * On the first Save after "Primary Account Manager" is changed (specifically, after "Primary Account Manager" is checked for an existing row where it was not saved as checked), the following happen: 
    * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec; 
    * a new row is added to the "End User Agreements for Account" embedded spreadsheet for the new Primary Account Manager, with the following set: 
      * "Effective Date": sets to the "Upload / Effective Date" for the top row of the "End User Agreements" embedded spreadsheet in Silverloom Settings (the current EUA);
      * "Contact ID": sets to the "Contact ID" for the new Primary Account Manager; 
    * the "Send "Account Manager Changes" Email" triggered automatic process runs, to send the "Account Manager Changes" Email" - see corresponding specs;
  * On the first Save after any of the other editable fields (i.e. "Mobile Phone", "Traccar Login Email", "Traccar Login Enabled") are changed for one or more rows, the following happen for each edited row:
    * the "Create/Update Traccar User Records" triggered automatic process runs to update the linked Traccar User sync record(s) in the background (to be synced to Traccar the following time that the sync runs) - see corresponding automatic process spec; 


  * Additional Validations: 
    * On the first Save after the "Account Manager" or "Primary Account Manager" checkboxes are checked or unchecked:
      * warning on Save: "Changes have been made to the Account Managers. The "Account Manager Changes Email" will be sent to all affected users on Save.";
      * the "Account Manager Changes Email" is sent to all affected users -- see corresponding spec) 



TODO_VA: Tim Reitz 02/04/2026: These would go to the Traccar User record. 

  * On the first Save after a new row has been added:
    * warning on Save: "One or more new Account Members have been added. The "New Account Member Welcome Email" will be sent upon saving the record.";



TODO_VA: Tim Reitz 02/04/2026: This would go to the Traccar User record. 

  * On the first Save after a row has been removed:
    * warning on Save: "One or more Account Members have been removed. Corresponding user(s) will have their login access disabled upon saving the record.")



TODO_VA: Tim Reitz 02/04/2026: This would go to the Traccar User record. 

  * Other Notes: 
    * Note that this does not track historical Account Members.



  


  * "Add Member" (visible to "Upline Provider Roles" users for the Account; link; opens the "Select Traccar Login Email" screen, with the following: 
    * Contact (required; drop list of "Display Name" values for all active individual Contacts)
    * If the desired contact is not listed, return to the account screen and use one of the "New Contact" links to create a new individual contact before trying again." (visible if "Contact" is blank; on-screen message in gray font)



_NM: Tim Reitz 02/04/2026: Can we do a conditionally-visible message on this child screen? (related note: should this be an on-screen prompt, rather than a child screen?) 

_VA: Tim Reitz 02/05/2026: Nic is thinking that an x30 prompt screen is better practice for coding simplicity, trumping user interface benefits. 

And yes, it can be conditionally visible. 

  * Traccar Login Email (required; drop list of email addresses from the Email" embedded spreadsheet for the selected "Contact") 
  * If the desired email address is not listed, it might need to be added to the contact. Return to the account screen and use the "Find Contact" link to find & add the email to the contact." (visible if "Contact" is not blank and "Traccar Login Email" is blank; on-screen message in gray font) 



_NM: Tim Reitz 02/04/2026: What would be the workflow for a missing email? (if we do an on-screen prompt, could we have a "View / Edit Contact" link beside the Contact selection field, for them to go add info right away?) 

_VA: Tim Reitz 02/05/2026: Same for email as for Contact. 

  * Continue (button; when this button is clicked: 
    * if there is an existing Traccar User sync record with a matching "Traccar Login Email" and with "Traccar Login Category" = blank: opens that record, with fields defaults as when a new record is created (see spec below); 



_NM: Tim Reitz 02/04/2026: A wrinkle here: What if the record is currently active (linked to another record)? Shall we give an error on the prompt / on the Continue button in that case (like we do on the Traccar Login Email field)? 

_VA: Tim Reitz 02/04/2026: Error when you click Continue. Could be on the report (as a preface in red font): "The email you entered is already in use for an active login...". Tell the user to change the existing one or try a different email.

_NM: Tim Reitz 02/04/2026: And if there record is not currently active, I'm thinking we go ahead and pass through the details from the current Account like we would for a new record -- sound correct? 

_VA: Tim Reitz 02/04/2026: Yes, we can just pass through the details and set/update it.

  * otherwise, if there is an existing Traccar User sync record with a matching "Traccar Login Email" and with "Traccar Login Category" = not blank: opens the "__" report, with a preface in red: "The email address you entered is already in use for an active Traccar login. Please return to "Add Member" and try again with a different email address."; 



TODO_VA: Tim Reitz 02/05/2026: Spec this report. 

  * otherwise, if there is no record with a matching "Traccar Login Email": opens a new blank record with the following fields defaulted: 
    *  __) 



TODO_VA: Tim Reitz 02/05/2026: Spec the defaults, based on the old x30. 

  


  * Disable Traccar Login (visible to "Upline Provider Roles" users for the Account if a row is selected on the "Account Member" embedded spreadsheet with "Traccar Login Enabled" checked; button; runs the "__" user-initiated automatic process to disable the Traccar login for the selected Account Member - see corresponding spec) 
  * Enable Traccar Login (visible to "Upline Provider Roles" users for the Account if a row is selected on the "Account Member" embedded spreadsheet with "Traccar Login Enabled" not checked; button; runs the "__" user-initiated automatic process to enable the Traccar login for the selected Account Member - see corresponding spec)  



_NM: Tim Reitz 02/04/2026: Sound good to have this be the same x30 for both of these? 

TODO_VA: Tim Reitz 02/04/2026: Yes, same one. Spec the x30. "Set Traccar Login". Prompt for activate/deactivate.

  * Remove from Account (visible to "Upline Provider Roles" users for the Account if any row is selected on the "Account Member" embedded spreadsheet; button; runs the "__" user-initiated automatic process to __) 



_NM: Tim Reitz 02/04/2026: How would this work, to unlink a Traccar User record from the Account? An x30 button to clear the "Linked Account" field (and maybe the "Category" field) on the Traccar User record? And sets "Disabled". (that way it would be available to be used again) 

TODO_VA: Tim Reitz 02/04/2026: Yes. Spec the x30. 

TODO_VA: Tim Reitz 02/04/2026: Additional conditions from the old spec, to consider: hidden if the account member is set as the "Primary Driver" on a Vehicle for the Account; note that an on-screen explanation message is displayed when the button is hidden - see spec below

  


  * "One or more Account Members are lacking a Mobile phone #. Click the corresponding "View / Edit Contact" link to add, before saving the Account." (on-screen message in red font; with the following details / behaviors:
    * visible if there is one or more Contact selected on the "Account Members" embedded spreadsheet with no "Mobile"-type Phone number specified;
    * error on Save with the same wording if the same condition exists)



Tim Reitz 02/04/2026: No longer relevant, now that we're using validation on the Traccar User record. 

  * "One or more Account Members are lacking an eligible email address. Click the corresponding "View / Edit Contact" link to add, before saving the Account." (on-screen message in red font; with the following details / behaviors:
    * visible if there is one or more Contact selected on the "Account Members" embedded spreadsheet with no Email specified;
    * error on Save with the same wording if the same condition exists)



Tim Reitz 02/04/2026: No longer relevant, now that we're using validation on the Traccar User record. 

  * "One or more Account Members are lacking an address. Click the corresponding "View / Edit Contact" link to add, before saving the Account." (on-screen message in red font; with the following details / behaviors:
    * visible if there is one or more Contacts on the "Account Members" embedded spreadsheet with no Address specified;
    * error on Save with the same wording if the same condition exists)



TODO_VA: Tim Reitz 02/04/2026: Consider whether to keep this here or put the validation on the Traccar User record. 

  


  * Account member is set as the Primary Driver for one or more vehicles for this account. Change the Primary Driver to remove the account member from the account. (on-screen message in green font; visible if the Contact for the currently-selected row of the "Account Members" embedded spreadsheet is set as the "Primary Driver" on one or more Vehicles for the Account)



  


  * Find Contact (link; opens the "<Service Name> Main Contacts Report"; to be used for finding a Contact, to add an email address before adding them as an Account Member, etc.) 
  * New Contact for Household Member (link; visible if "Account Type" = "Household"; visible to "Upline Provider Roles" users for the Account; opens a new Contact record, with "Last Name" and any/all Addresses defaulted based on the Primary Account Manager Contact) 
  * New Contact for Non-Household Member (link; visible if "Account Type" = "Household"; visible to "Upline Provider Roles" users for the Account; opens a new blank Contact record) 
  * New Contact (link; visible if "Account Type" = "Business"; visible to "Upline Provider Roles" users for the Account; opens a new blank Contact record)



  


Development Specification

TODO_M: Tim Reitz 02/05/2026: Ready for updating. 

  


_JB: Tim Reitz 01/07/2026: Also note that for Providers, I think we'll want to store the following on the Silverloom Contact record instead of on an Account record: 

  * Traccar Login Email (auto-set and read-only or macro; sets to the login email for the Contact's Silverloom User Profile) 
  * Traccar Login Status (drop list; editable only for users with the "Full Access" Permission) 



Does that sound right to you? Is it a problem for the sync to be looking at two different record types for Traccar login details? 

_VA: Tim Reitz 01/15/2026: We utilize the "Traccar User" sync record. We can enter the details in either the Account or Contact record, have an x30 that creates the Traccar User record, and then the sync runs from there.

DONE_JB (research): Tim Reitz 01/15/2026: Jonathan wasn't sure how to initiate the 2nd import (to sync to Traccar), since we can't have one trigger run from another trigger.

_VA: Jonathan Bergen 01/21/2026: We can't have the second one run in real-time. However, we could have the sync watch for these and create the user withing 5 minutes. Is this reasonable?

DONE_JB (research): Tim Reitz 01/27/2026: Yes, that's reasonable, at least for Phase 1. We maybe could look at a faster approach for Phase 2 (if there are any faster options).

Jonathan Bergen 02/02/2026: Yeah, I have some ideas, but I like the approach of simple for Phase 1, especially while the design is fluid.
