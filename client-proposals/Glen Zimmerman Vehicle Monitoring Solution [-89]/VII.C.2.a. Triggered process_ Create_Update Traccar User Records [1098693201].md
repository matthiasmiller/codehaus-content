7.3.2.1. Triggered process: Create/Update Traccar User Records

  


Requirements

  * On the first Save after one or more new rows are added, or one or more existing saved rows are deleted, or one or more existing saved rows are edited, the "Update Traccar User Records and Sync with Traccar" triggered automatic process runs to create and/or update Traccar User sync records in the background and sync with Traccar, updating the Account Member's details in Traccar and their login access there - see corresponding automatic process spec; 



_VA: Tim Reitz 01/19/2026: Triggered automatic process: "Update Traccar User Records and Sync with Traccar"

[X] On every Save of the Account record or On the first Save after: 

[X] one or more new rows are added, or 

[X] one or more existing saved rows are deleted, or 

[X] one or more existing saved rows are edited 

[X] Actions: 

[X] Creates new Traccar User records as needed (based on the "Traccar Login Email" and __) 

[X] Updates details if changed on the Account Members RG

[X] Sync with Traccar

_NM: Tim Reitz 01/19/2026: Can the same x30 be triggered from / look at two different record types, or do we need a separate x30 for each? (Specifically, a triggered x30 that updates the "Traccar User" sync records that update Traccar. Can it be triggered by certain changes to both the Account records and the Contact records, or do we need two separate ones?

Nic: You need two trigger + report combos, but just one x30 (Seth and I believe)

_NM: Tim Reitz 01/19/2026: How to spec this? 

TODO_VA: Tim Reitz 01/22/2026: Like I'm doing below. Be clear about what sets from each place. 

  


TODO_VA: Tim Reitz 01/19/2026: Let's make sure to spec out the trigger & details for syncing from the Contact record. 

  


\---------------------

  


  * Name: "Create/Update Traccar User Records"
    * Description: Creates and updates Traccar User records based on the following:
      * rows on the "Account Member" embedded spreadsheet on Account records,
      * rows on the "Provider Traccar Logins" embedded spreadsheet on Contact records;
      * details on Contact records linked to these embedded spreadsheets



TODO_JB (research): Tim Reitz 01/29/2026: If something changes on a linked Contact record (i.e. name changes), presumably those changes should carry over to the sync record and Traccar. How should we do this? Nightly process to check for changes? Part of the Traccar sync that runs every 5 minutes?

  * Action(s): 
    * for new rows that are added: TODO_VA: Tim Reitz 01/29/2026: Spec out the rest
      * if no existing Traccar User record exists with the same "Traccar Login Email" address: creates a new Traccar User record, with the following set: 
        * "Unique ID": sets to __; 
        * "Linked Contact": sets to the "Display Name" of the Contact selected in the embedded spreadsheet "Name" field; 
        * "Linked Account": if linked to an "Account Member", sets to the "Account #"; 
        * "Name": sets to the "Short Display Name" of the Contact selected in the embedded spreadsheet "Name" field; 
        * "Email": sets to the "Traccar Login Email" selected in the embedded spreadsheet; 
        * "Phone": sets to "Mobile Phone" selected in the embedded spreadsheet; 
        * __
        * Permissions: 
          * if "Master Administrator" = checked: __; 
          * if "Master Administrator" = not checked: __; 
          * if "Group Admin" = checked: __; 
          * if "Group Admin" = not checked: __; 
          * if "Account Reseller" = checked: __; 
          * if "Account Reseller" = not checked: __; 
          * if "Account Manager" = checked: __; 
          * if "Account Manager" = not checked: __; 
          * if "Primary Account Manager" = checked: __; 
          * if "Primary Account Manager" = not checked: __; 
          * if "Driver" = checked: __; 
          * if "Driver" = not checked: __; 
      * if an existing Traccar User record exists with the same "Traccar Login Email" address: updates the existing Traccar User record with the following from the corresponding Account record and/or Contact record: 
        * "Login Disabled": sets to not checked; 
        * all other fields mentioned in the spec for newly-added rows: update as specced for newly added rows (above)
    * for existing saved rows that are deleted: updates the linked Traccar User record: 
      * "Login Disabled": sets to checked; 
    * for existing saved rows that are edited: updates the linked Traccar User record:
      * sets fields to match, as specced for newly-added rows (above);
  * Trigger Name (to be enabled at deployment):
    * Create/Update Traccar User Records from Accounts
    * Create/Traccar User Records from Contacts
  * Report Path:
    * From Accounts: __ (TBD in coding)
    * From Contacts: __ (TBD in coding)
  * Initiated:
    * From Accounts: On the first Save after: 
      * one or more new rows are added, or 
      * one or more existing saved rows are deleted, or 
      * one or more existing saved rows are edited 
    * From Contacts: On the first Save after: 
      * one or more new rows are added, or 
      * one or more existing saved rows are deleted, or 
      * one or more existing saved rows are edited  
  * Priority:
    * From Accounts: 1 (to runs before the "Send "New Account Member Welcome" Email" triggered process and others) 
    * From Contacts: 2 (to run after the "Set User Group Based on User Role" triggered process)
  * Run as User: "Administrator" 
  * Import Path: __ (TBD in coding)



  


Development Specification

TODO_CCI: Please document the Report Path and Import Path, and confirm Trigger Name and Priority, & let us know, so that we can update the spec accordingly. Thanks!
