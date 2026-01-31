7.3.2. Account Record - Account Members Section

  


Requirements

*Done.

  


  * Account Members section (all fields in this section are editable for "Upline Provider Roles" users for the Account): 



  


  * Account Members (no label; embedded spreadsheet with the following; note that this parallels the "Account Members" embedded spreadsheet on the Account record, and changes should be considered for both:
    * Columns: 
      * Name (required; drop list of "Display Names" for all active Individual Contacts; with the following details / behaviors: 
        * validations:
          * error on Save if changed from a saved value (to prevent changing the member's name): "Account Member's Name cannot be changed. Use the Add / Remove buttons to manage Account Members."; 
          * error on Save if "Date of Birth" is blank on the Contact record of any of the Account Members: "Date of Birth is required for one or more Account Members: <Short Display Name>, <Short Display Name>. Click the "View/Edit Contact" link to add this data before saving the Account changes."; 
          * error on Save if "Gender" is blank on the Contact record of any of the Account Members: "Gender is required for one or more Account Members: <Short Display Name>, <Short Display Name>. Click the "View/Edit Contact" link to add this data before saving the Account changes."; 
        * data synced with Traccar, via the Traccar User sync record) 
      * Account Manager (checkbox; defaults to not checked; with the following details / behaviors: 
        * error on Save if no rows have "Account Manager" checked: "At least one Account Manager is required."; 
        * note that when this checkbox is checked for a row, the "Is Account Manager" checkbox on the corresponding Contact record is checked; 
        * data synced with Traccar (as User permission), via the Traccar User sync record) 
      * Primary Account Manager (checkbox; editable if "Account Manager" is checked for the same row; defaults to not checked; with the following details / behaviors:
        * error on the field if checked when "Primary" is already checked for another row: "Only one Account Manager can be set as Primary.";
        * error on Save if no row is marked as Primary: "A Primary Account Manager is required."; 
        * data synced with Traccar (as User permission), via the Traccar User sync record)
      * Driver (checkbox; defaults to not checked; with the following details: 
        * note that when this checkbox is checked for a row, the "Is Driver" checkbox on the corresponding Contact record is checked; 
        * warning on Save if no rows have "Driver" checked: "This Account does not have any Drivers."; 
        * data synced with Traccar (as User permission), via the Traccar User sync record) 
      * Mobile Phone (required; drop list of phone numbers for the selected Contact with "Type" = "Mobile"; with the following details / behaviors: 
        * note that at least one mobile phone number is required for Account Members - see special validation spec below; 
        * data synced with Traccar, via the Traccar User sync record) 
      * Traccar Login Email (required; drop list of email addresses from the Contact's "Email" embedded spreadsheet; with the following details / behaviors:
        * error on the field if an email address is selected that has already been saved as the "Traccar Login Email" on any Account in the Solution (including the current Account): "This email address has already been used for another Traccar login (User: <Contact Short Display Name>; Account #: <Account #>). Click the View / Edit Contact link to add a new email.";
        * this is the email address that is set as the login email for this person's User login in Traccar; 
        * note that at least one email address is required for Account Members - see special validation spec below; 
        * data synced with Traccar, via the Traccar User sync record)
      * Primary Address (read-only macro; with the following details / behaviors: 
        * displays the primary Address for the selected Contact, as a combined string in the following format: "<Address>, <Address 2>, <City>, <State> <Zip>"; 
        * note that the column width might be narrower than the full address, to save space; 
        * note that at least one address is required for Account Members - see special validation spec below)
      * View / Edit Contact (link to open the selected Contact record; displays as "Link")
      * Traccar Login Enabled (checkbox; with the following details / behaviors: 
        * defaults to checked; 
        * data synced with Traccar, via the Traccar User sync record) 
    * Automatically sorted by:
      * First by: Role:
        * "Primary Account Manager" (the row with "Primary" checked sorts to the top),
        * "Account Manager",
        * "Driver";
      * Second by: Name (alphabetically)
    * Buttons to add/remove rows: 
      * "Add Member" (visible to "Upline Provider Roles" users for the Account) 
      * "Remove Member" (visible to "Upline Provider Roles" users for the Account; hidden if the account member is set as the "Primary Driver" on a Vehicle for the Account; note that an on-screen explanation message is displayed when the button is hidden - see spec below) 
    * Shows 7 rows without scrolling
    * OnChange and OnSave Behaviors: 
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
      * On the first Save after a new row has been added:
        * warning on Save: "One or more new Account Members have been added. The "New Account Member Welcome Email" will be sent upon saving the record.";
      * On the first Save after a row has been removed:
        * warning on Save: "One or more Account Members have been removed. Corresponding user(s) will have their login access disabled upon saving the record.")
    * Other Notes: 
      * Note that this does not track historical Account Members.



  


  * "One or more Account Members are lacking a Mobile phone #. Click the corresponding "View / Edit Contact" link to add, before saving the Account." (on-screen message in red font; with the following details / behaviors:
    * visible if there is one or more Contact selected on the "Account Members" embedded spreadsheet with no "Mobile"-type Phone number specified;
    * error on Save with the same wording if the same condition exists)
  * "One or more Account Members are lacking an eligible email address. Click the corresponding "View / Edit Contact" link to add, before saving the Account." (on-screen message in red font; with the following details / behaviors:
    * visible if there is one or more Contact selected on the "Account Members" embedded spreadsheet with no Email specified;
    * error on Save with the same wording if the same condition exists)
  * "One or more Account Members are lacking an address. Click the corresponding "View / Edit Contact" link to add, before saving the Account." (on-screen message in red font; with the following details / behaviors:
    * visible if there is one or more Contact selected on the "Account Members" embedded spreadsheet with no Address specified;
    * error on Save with the same wording if the same condition exists)



  


  * Account member is set as the Primary Driver for one or more vehicles for this account. Change the Primary Driver to remove the account member from the account. (on-screen message in green font; visible if the Contact for the currently-selected row of the "Account Members" embedded spreadsheet is set as the "Primary Driver" on one or more Vehicles for the Account)



  


  * New Contact for Household Member (link; visible if "Account Type" = "Household"; visible to "Upline Provider Roles" users for the Account; opens a new Contact record, with "Last Name" and any/all Addresses defaulted based on the Primary Account Manager Contact) 
  * New Contact for Non-Household Member (link; visible if "Account Type" = "Household"; visible to "Upline Provider Roles" users for the Account; opens a new blank Contact record) 
  * New Contact (link; visible if "Account Type" = "Business"; visible to "Upline Provider Roles" users for the Account; opens a new blank Contact record)



  


Development Specification

_JB: Tim Reitz 01/07/2026: Also note that for Providers, I think we'll want to store the following on the Silverloom Contact record instead of on an Account record: 

  * Traccar Login Email (auto-set and read-only or macro; sets to the login email for the Contact's Silverloom User Profile) 
  * Traccar Login Status (drop list; editable only for users with the "Full Access" Permission) 



Does that sound right to you? Is it a problem for the sync to be looking at two different record types for Traccar login details? 

_VA: Tim Reitz 01/15/2026: We utilize the "Traccar User" sync record. We can enter the details in either the Account or Contact record, have an x30 that creates the Traccar User record, and then the sync runs from there.

DONE_JB (research): Tim Reitz 01/15/2026: Jonathan wasn't sure how to initiate the 2nd import (to sync to Traccar), since we can't have one trigger run from another trigger.

_VA: Jonathan Bergen 01/21/2026: We can't have the second one run in real-time. However, we could have the sync watch for these and create the user withing 5 minutes. Is this reasonable?

TODO_JB (research): Tim Reitz 01/27/2026: Yes, that's reasonable, at least for Phase 1. We maybe could look at a faster approach for Phase 2 (if there are any faster options).
