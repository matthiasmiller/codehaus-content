7.3.2. Account Record - Account Members Section

  


Requirements

*

  


TODO_VA / TODO_JB: Tim Reitz 01/15/2026:

  * Use "sync point" keyword for any actions that kick off the sync
  * Use "data synced with Traccar" keyword for all fields that get synced + use purple font



  


TODO_VA: Tim Reitz 01/15/2026: Jonathan is thinking we could run the sync from Traccar every 5 min.

  


  * Account Members section (all fields in this section are editable for "Upline Provider Roles" users for the Account): 



  


  * Account Members (no label; embedded spreadsheet with the following:
    * Columns: 
      * Name (required; drop list of "Display Names" for all active Individual Contacts; with the following details / behaviors: 
        * error on Save if changed from a saved value (to prevent changing the member's name): "Account Member's Name cannot be changed. Use the Add / Remove buttons to manage Account Members."; 
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



_JB: Tim Reitz 01/07/2026: Also note that for Providers, I think we'll want to store the following on the Silverloom Contact record instead of on an Account record: 

  * Traccar Login Email (auto-set and read-only or macro; sets to the login email for the Contact's Silverloom User Profile) 
  * Traccar Login Status (drop list; editable only for users with the "Full Access" Permission) 



Does that sound right to you? Is it a problem for the sync to be looking at two different record types for Traccar login details? 

TODO_VA: Tim Reitz 01/15/2026: We utilize the "Traccar User" sync record. We can enter the details in either the Account or Contact record, have an x30 that creates the Traccar User record, and then the sync runs from there.

TODO_JB (research): Tim Reitz 01/15/2026: Jonathan wasn't sure how to initiate the 2nd import (to sync to Traccar), since we can't have one trigger run from another trigger.

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
    * "Remove Member" (visible to "Upline Provider Roles" users for the Account) 
  * Shows 7 rows without scrolling
  * OnChange and OnSave Behaviors: 
    * On the first Save after one or more new rows are added, or one or more existing saved rows are deleted, or one or more existing saved rows are edited, the "Update Traccar User Records and Sync with Traccar" triggered automatic process runs to create and/or update Traccar User sync records in the background and sync with Traccar, updating the Account Member's details in Traccar and their login access there - see corresponding automatic process spec; 
    * On the first Save after one or more new rows are added, the following happen for each newly-added row: 



TODO_VA: Tim Reitz 01/20/2026: For all of these following on save items, consider whether they should be here or on the automatic process spec. 

  * login access to Traccar is enabled:
    * if an existing Traccar User exists with the same "Traccar Login Email" address:
      * the User is activated;
      * details are updated based on the current Account details;
    * otherwise,
    * a new User is set up in Traccar, with fields set based on the following: 
      * "Traccar Login Email" 
      * current Account details;
  * a new row is added to the "End User Agreements for Account" embedded spreadsheet for that Member, with the following set: 
    * "Effective Date": sets to the "Upload / Effective Date" for the top row of the "End User Agreements" embedded spreadsheet in Silverloom Settings (the current EUA);
    * "Contact ID": sets to the "Contact ID" for the new Account Member;
  * the "Send "New Account Member Welcome" Email" triggered automatic process runs, to send the "New Account Member Welcome" email - see corresponding specs;


  * On the first Save after one or more rows are removed, the following happen for each removed row: 
    * login access in Traccar is disabled;
    * any rows for the Contact on the "End User Agreements for Account" embedded spreadsheet with "Agreed To Date" blank are removed. 
  * On the first Save after "Account Manager" is checked for a row:
    * permissions in Traccar are updated;
    * the "Send "Account Manager Changes" Email" triggered automatic process runs, to send the "Account Manager Changes" Email" - see corresponding specs;
  * On the first Save after "Account Manager" is unchecked for a row:
    * permissions in Traccar are updated;
    * the "Send "Account Manager Changes" Email" triggered automatic process runs, to send the "Account Manager Changes" Email" - see corresponding specs;
  * On the first Save after "Driver" is checked for a row:
    * permissions in Traccar are updated;
  * On the first Save after "Driver" is unchecked for a row:
    * permissions in Traccar are updated;
  * On the first Save after "Primary Account Manager" is changed (specifically, after "Primary Account Manager" is checked for a row where it was not saved as checked), the following happen: 
    * permissions in Traccar are updated for new Primary Account Manager, and for the previous Primary Account Manager if they are still included on the "Account Members" embedded spreadsheet;
    * a new row is added to the "End User Agreements for Account" embedded spreadsheet for the new Primary Account Manager, with the following set: 
      * "Effective Date": sets to the "Upload / Effective Date" for the top row of the "End User Agreements" embedded spreadsheet in Silverloom Settings (the current EUA);
      * "Contact ID": sets to the "Contact ID" for the new Primary Account Manager; 
    * the "Send "Account Manager Changes" Email" triggered automatic process runs, to send the "Account Manager Changes" Email" - see corresponding specs;


  * Additional Validations: 
    * On the first Save after the "Account Manager" or "Primary" checkboxes are checked or unchecked:
      * warning on Save: "Changes have been made to the Account Managers. The "Account Manager Changes Email" will be sent to all affected users on Save.";
      * the "Account Manager Changes Email" is sent to all affected users -- see corresponding spec) 
    * On the first Save after a new row has been added:
      * warning on Save: "One or more new Account Members have been added. The "New Account Member Welcome Email" will be sent.";
      * the "New Account Member Welcome Email" is sent to the "Traccar Login Email" address for any new rows -- see corresponding spec)
    * On the first Save after a row has been removed:
      * warning on Save: "One or more Account Members have been removed. Corresponding user(s) will have their login access disabled.")
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



  


  * New Contact for Household Member (link; visible if "Account Type" = "Household"; visible to "Upline Provider Roles" users for the Account; opens a new Contact record, with "Last Name" and any/all Addresses defaulted based on the Primary Account Manager Contact) 
  * New Contact for Non-Household Member (link; visible if "Account Type" = "Household"; visible to "Upline Provider Roles" users for the Account; opens a new blank Contact record) 
  * New Contact (link; visible if "Account Type" = "Business"; visible to "Upline Provider Roles" users for the Account; opens a new blank Contact record)



  


Development Specification

Tim Reitz 12/15/2025: I think we need to track a Account Login Email and Account Password on these RGs. The same Contact could be a user on multiple different Accounts, so they would need separate Passwords (and possibly separate emails) to be able to log into Traccar. And also separate emails to be able to receive the OTP for logging into the portal. 

_NM: Tim Reitz 12/15/2025: Does this sound right? 

_VA: Tim Reitz 12/16/2025: Yes, we need separate email addresses for separate Traccar User profiles. 

  


Tim Reitz 12/16/2025: Nic would rather not store passwords. At first we thought we might need to (in order to pass it through to Traccar & send the email to the end user), but here's a different approach: 

  * Traccar User is created via the API (set Name, Email, and Password) 



TODO_JB: Tim Reitz 12/16/2025: Have the WSGI generate a random string, so that it never gets stored in Silverloom. 

Tim Reitz 01/15/2026: Actually, we might not need to generate any password at all. 

  * The email that goes to the new user includes the Password Reset link ([https://x6rildfvs.traccar.com/reset-password](https://x6rildfvs.traccar.com/reset-password)). The end user resets their password with this (they can't get in otherwise, since they don't have the initial password).


