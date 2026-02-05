8.3.1.1. Account Overview - Account Details Fields

*Done. 

  


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
      * error on the field if set to "Closed" if there are any Account Members with "Traccar Login Enabled" set to checked: "Traccar Login Enabled must be unchecked for all Account Members before marking the Account as Closed."; 



TODO_VA: Tim Reitz 02/04/2026: Reconsider this validation, now that we are looking at the Traccar User sync records. Maybe keep it the same, looking at the macro. Or maybe change it to look at the "Disabled" checkbox on the sync record. 

  * error on the field if set to "Inactive" or "Closed" if there are any linked Devices with "Device Status" ≠ "Assigned - Disabled" or "Decommissioned": "Account cannot be set to this Status because there are one or more active Devices."; 
  * error on the field if set to "Paused" if there are any linked Devices with "Device Status" ≠ "Assigned - Paused" or "Assigned - Disabled" or "Lost" or "Decommissioned": "Account cannot be set to "Paused" because there are one or more active Devices. Mark all linked Devices as non-active or "Paused" to continue."; 
  * note that additional validations probably will be needed, to be determined in early use of Phase 1 and in design / early use for Phase 2;


  * when set the "Active", the following field(s) are affected:
    * "Service Start Date": sets to the current date;
  * on the first Save after this is set to "Closed", the following happen:
    * "End User Agreements for Account" embedded spreadsheet: all rows with "Agreed To Date" blank are removed;
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


