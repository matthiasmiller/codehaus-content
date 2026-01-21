7.3.1. Account Record - Account Overview Section

*. 

  


  * Account Overview section:
    * Account Status (on the right-hand side of the section header; label displays as "Status:"; read-only macro; displays the current selection from the "Stored Account Status" drop list - see corresponding spec; note that this is to be updated once the Subscriptions feature is added) 
    * Account # (auto-set and read-only; number; 0 decimals; this is the unique identifier for the record; this also is used as a reference number throughout the Solution and by users) 
    * Stored Account Status (label displays as "Set Account Status"; drop list of "Account Statuses" list items; with the following details / behaviors:
      * this field is intended as a temporary field to set the displayed "Account Status" macro in the section heading, until the Subscriptions feature is added in Phase 2 (which is expected to set this automatically); 
      * editable for "Upline Provider Roles" users for the Account; 
      * list items and intended use cases for Phase 1 are as follows:
        * "In Setup": in the process of being set up; Devices can be added and activated, Drivers/users can be invited and added, and other details can be added to the Account, but the end users do not have access to the Account;
        * "Active": live for the end users and ready to be used / in use;
        * "Paused": for Phase 1, same as "Inactive";
        * "Inactive": Account is still accessible to end users, but there are no active Devices; new Devices / users can be added to the Account (for example, under investigation or in the process of being closed out, etc.);
        * "Closed": not accessible to the end users; all Devices are inactive; new Devices / users cannot be added to the Account;
      * includes the following validations: 
        * error on the field if set to "Inactive" or "Closed" if there are any linked Devices with "Device Status" ≠ "Assigned - Disabled" or "Decommissioned" \- error on the field: "Account cannot be set to this Status because there are one or more active Devices."; 
        * error on the field if set to "Paused" if there are any linked Devices with "Device Status" ≠ "Assigned - Paused" or "Assigned - Disabled" or "Lost" or "Decommissioned" \- error on the field: "Account cannot be set to "Paused" because there are one or more active Devices. Mark all linked Devices as non-active or "Paused" to continue."; 
        * note that additional validations probably will be needed, to be determined in early use of Phase 1 and in design / early use for Phase 2;
        * __; TODO_GZ: what other validations? 
      * when set the "Active", the following field(s) are affected:
        * "Service Start Date": sets to the current date;
      * on the first Save after this is set to "Closed", the following happen:
        * login access to Traccar and the Portal is automatically disabled for all Account Members;  



_JB: Tim Reitz 01/07/2026: Sync point. What notes should we have here? 

Tim Reitz 01/08/2026: We would want the "Traccar Login Status" on the RG to be set.

_VA: Tim Reitz 01/15/2026: Include "sync point" in the spec for all of these. 

TODO_VA: Tim Reitz 01/15/2026: For this one, maybe have an onchange to set the member rows, then sync from there. 

  * all rows on the "End User Agreements for Account" embedded spreadsheet with "Agreed To Date" blank are removed;
  * "Service Start Date" sets to cleared) 



  


  * Account Type (required; drop list of "Account Types" list items; with the following details / behaviors:
    * for new (unsaved) records: editable for "All Provider Roles" users; 
    * if saved as not blank: editable for "Upline Provider Roles" users for the Account; 
    * defaults to "Household" (note that users need to manually change this to "Business" when needed, but this is not expected to be very common);
    * when edited, the following field(s) are affected:
      * "Account Owner": is cleared;
    * warning on Save if changed from a saved non-blank value: "Account Type has been changed.") 



  


  * Account Owner (required; with the following details / behaviors:
    * drop list of Contacts, filtered as follows: 
      * if "Account Type" = "Household": includes all active individual Contacts; 
      * if "Account Type" = "Business": includes all active organization Contacts; 
    * for new (unsaved) records: editable for "All Provider Roles" users; 
    * if saved as not blank: editable for "Upline Provider Roles" users for the Account:
    * warning on Save if changed from a saved non-blank value: "Account Owner has been changed.") 



  


  * New Individual (visible if "Account Type" = "Household" and "Account Owner" = blank; link; opens a new blank Contact record) 
  * New Business (visible if "Account Type" = "Business" and "Account Owner" = blank; link; opens a new Contact record with the "Is Organization" checkbox checked) 



  


  * Account Reseller (macro; with the following details / behaviors: 
    * if there are no rows on the "Account Reseller History" non-embedded spreadsheet (i.e. for brand new Account records):
      * required; 
      * drop list of all active Account Resellers (Contacts with the "Is Account Reseller" checkbox checked);
      * defaults to:  
        * if the creating user is an "Account Reseller" or a "Reseller Rep": defaults to the Contact for the "Account Reseller"; 
        * otherwise: defaults to blank; 
      * when set, the following field(s) are affected:
        * a row is added to the "Account Reseller History" non-embedded spreadsheet, with the following fields set:
          * "Account: set to the current Account;
          * "Requested By": set to the current user;
          * "Requested Date": set to the current date;
          * "Reason / Comments": set to "Initial Reseller for Account";
          * "New Reseller": set to the selection in this drop list;
          * "Transfer Complete Date": set to the current date; 
      * note that this immediately becomes read-only when set (see spec below), meaning that if it is set incorrectly, the user must either refresh the screen before saving or request a transfer to change it; 
    * if there is at least one row on the "Account Reseller History" non-embedded spreadsheet (i.e. the editable macro has been set, either manually or defaulted, at which point the Reseller Transfer feature must be used):
      * read-only;
      * displays the following:
        * if "Transfer Approved" checkbox is checked for the top row: displays the "New Reseller" from the top row of the "Account Reseller History" non-embedded spreadsheet - see corresponding spec, and see the spec for the "Request Reseller Transfer" feature); 
        * if "Transfer Approved" checkbox is not checked for the top row: displays the "New Reseller" for the second-from-the-top row;
      * displays as a link to open the selected record) 
  * Account Reseller Phone (label displays as just "Phone"; read-only macro; displays the primary Phone number for the selected "Account Reseller" Contact; link to dial the number directly, if the user has that capability on their device) 
  * Account Reseller Email (label displays as just "Email"; read-only macro; displays the primary Email address for the selected "Account Reseller" Contact; link to open an email draft with the "To:" defaulted in the user's default email client)
  * Account Reseller Address (label displays as just "Address"; read-only macro; displays the primary Address for the selected "Account Reseller", in the standard multi-line format without the addressee name)



  


  * Request Reseller Transfer (Upline) (label displays as "Request Reseller Transfer"; button; with the following details / behaviors:
    * visible in Edit Mode after the initial Save to "Upline Provider Roles" users (users who can edit the Account) if the top row in the "Account Reseller History" non-embedded spreadsheet has the "Transfer Complete" checkbox checked (i.e. if there is not a pending transfer in progress); 
    * when clicked, the following field(s) are affected:
      * "Reseller Transfer Mode": set to checked, which makes the "Request Reseller Transfer On-Screen Prompt" visible - see corresponding specs)
  * Reseller Transfer Mode (hidden; checkbox; with the following details / behaviors:
    * set to checked via the "Request Reseller Transfer" button (making the transfer fields visible) and unchecked via the "Cancel Transfer Request" or "Submit Transfer Request" buttons (hiding the transfer fields) - see corresponding specs; 
    * error on Save if this checkbox is checked: "Account cannot be saved while Reseller Transfer is in progress."; this prevents data from being saved in the transfer fields) 



  


  * "A Reseller Transfer has been requested for this account." (on-screen message in green font; visible if there is a row in the "Account Reseller History" non-embedded spreadsheet with the "Transfer Complete" checkbox not checked; displays in the location of the "Request Reseller Transfer" button) 



  


  * Request Reseller Transfer (Non-Upline) (label displays as "Request Reseller Transfer"; button; with the following details / behaviors:
    * visible out of Edit Mode to non-"Upline Provider Roles" users (users who can not edit the Account) if the top row in the "Account Reseller History" non-embedded spreadsheet has the "Transfer Complete" checkbox checked (i.e. if there is not a pending transfer in progress); 
    * when clicked, opens the "Request Reseller Transfer (Non-Upline)" child screen -- see corresponding spec)
  * Approve Reseller Transfer (button; with the following details / behaviors:
    * visible out of Edit Mode if the top row in the "Account Reseller History" non-embedded spreadsheet has the "Transfer Complete" checkbox not checked (i.e. if there is a pending transfer in progress); visible to the "New Reseller" (if individual) or a "Reseller Rep" for the "New Reseller" Contact (if organization);
    * when clicked, runs the "Approve Reseller Transfer (Non-Upline)" user-initiated automatic process -- see corresponding spec)



  


  * Account Reseller History (button; visible to "Upline Provider Roles" users; opens the "Account Reseller History" child screen - see corresponding spec) 



  


  * Account Group (required; drop list of active Account Groups, displaying the "Group Name"; with the following details / behaviors:
    * editable for "Upline Provider Roles" users for the Account;
    * on the first Save after this is changed from its previously-saved non-blank value, the "Account Group Changed" email is sent to the impacted parties (the Account Reseller, the Primary Group Admin for both the old and the new Groups, and the Account Managers) - see corresponding spec)
  * View Account Group (visible if "Account Group" is not blank; link; opens the selected Account Group record) 
  * New Account Group (visible to all "Group Admins" for the selected "Account Group" and "Upline Groups" and to all users with the "Full Access" Permission if "Account Group" = blank; link; opens a new Account Group record)
  * Contact a Group Admin or Master Administrator if a new Group is needed. (on-screen message in gray text; visible to the linked "Account Reseller" / "Reseller Reps" if "Account Group" = blank) 



  


  * Account Address (read-only macro; displays the Primary address for the "Primary Account Manager", in the standard multi-line format without the addressee name)
  * Church Affiliation (read-only macro; displays the "Church Affiliation", or "Other Church Affiliation" if "Church Affiliation" = "Other", for the "Primary Account Manager") 



  


  * Service Start Date (date; with the following details / behaviors: 
    * editable if "Stored Account Status" = "In Setup", "Active", "Paused", or "Inactive";
    * required if "Stored Account Status" = "Active", "Paused", or "Inactive";
    * defaults to the current date when "Stored Account Status" is set to "Active" \- see corresponding spec; 
    * error on the field if set to a date more than 3 months in the past or more than 3 months in the future: "Must be within 3 month (past or future) of today.";
    * is cleared on the first Save after "Stored Account Status" is set to "Closed" \- see corresponding spec; 
    * note that in Phase 2, this likely will be moved to a separate section with other Subscription management-related fields) 
  * Renewal Anniversary Date (hidden; read-only macro; date; with the following details / behaviors: 
    * displays the first date of the month of the "Service Start Date"; i.e., if "Service Start Date" = "08/14/2026", this displays "08/01/2026"; 
    * this is used to drive the "Renewal Anniversary" macro and as a reference point for the annual renewal and the "Prepare Annual Renewals" automatic process - see corresponding specs; 
    * note that in Phase 2, additional capabilities could be added to this; 
    * note that in Phase 2, this likely will be moved to a separate section with other Subscription management-related fields) 
  * Renewal Anniversary (read-only macro; plain text; with the following details / behaviors: 
    * displays the first day of the month for the "Service Start Date", in the following format: "MMMM D"; i.e., if "Service Start Date" = "08/14/2026", this displays " August 1"; 
    * note that there is no year associated with this, as the renewal is a recurring annual event; 
    * note that in Phase 2, this likely will be moved to a separate section with other Subscription management-related fields)


