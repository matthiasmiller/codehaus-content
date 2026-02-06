8.3.2.1. Triggered process: Create/Update Traccar User Records

  


Requirements

*. 

DONE_JB (research): Tim Reitz 01/31/2026: FYI / note that this currently would run from two different but parallel RGs - one on the Account record and one on the Contact record. It's possible that we will need to add more parallel RGs in the future to handle Account Groups, etc., but I'm hoping to keep it simpler & stick to 2 for Phase 1. 

I've tried to specify things that are different; you can assume if neither RG is specified, the spec applies to both the same. 

Jonathan Bergen 02/02/2026: Ok

  


  


  * Name: "Create/Update Traccar User Records"
    * Description: Creates and updates Traccar User records based on the following:
      * rows on the "Account Member" embedded spreadsheet on Account records,
      * rows on the "Provider Traccar Logins" embedded spreadsheet on Contact records; 
      * details on Contact records linked to these embedded spreadsheets



DONE_JB (research): Tim Reitz 01/29/2026: If something changes on a linked Contact record (i.e. name changes), presumably those changes should carry over to the sync record and Traccar. 

How should we do this? Nightly process to check for changes? Part of the Traccar sync that runs every 5 minutes?

Jonathan Bergen 02/02/2026: I think this could be a every 5 minutes thing. In general, anything that is human-initiated we can/should move over ASAP. It's the machine-generated stuff that'll get big and might be better nightly.

  * Action(s): 
    * for new rows that are added: TODO_VA (later): Tim Reitz 01/31/2026: Spec out the rest, once we have the details settled on the Traccar User sync record. 
      * if no existing Traccar User record exists with the same "Traccar Login Email" address: creates a new Traccar User record, with the following set: 
        * "Silverloom Details" section: 
          * "Record ID": __ TBD; 
          * "Linked Contact": sets to the "Display Name" of the Contact selected in the embedded spreadsheet "Name" field; 
          * "Linked Account": 
            * if from "Account Members", sets to the "Account #"; 
            * otherwise: N/A; 
        * "Traccar User Details" section: 
          * "Unique ID": sets to __ TBD; 
          * "Name": sets to the "Short Display Name" of the Contact in the embedded spreadsheet "Name" field; 
          * "Email": sets to the "Traccar Login Email" selected in the embedded spreadsheet; 
        * "Traccar User Preferences" section: 
          * "Phone": sets to "Mobile Phone" selected in the embedded spreadsheet; 
          * __ others TBD
        * "Traccar User Location" section: 
          * __ TBD; 
        * "Traccar User Permissions" section: 
          * "Expiration": retains default of "01/01/2099"; 
          * "Device Limit": retains default of "-1"; 
          * "User Limit": retains default of "-1"; 
          * "Disabled": 
            * if "Traccar Login Enabled" is checked: sets to / retains default of not checked; 
            * if "Traccar Login Enabled" is not checked: sets to checked; 
          * "Admin": 
            * if "Master Administrator" = checked (on the "Provider Traccar Logins" table on Contacts): sets to checked; 
            * for all other users: sets to not checked; 
          * "Read-only": retains default of not checked (this is to allow all users to make basic edits to their own User login in Traccar); 



DONE_JB (research): Tim Reitz 01/31/2026: I had originally been planning to set "Read-only" to true for all non-Master Administrator users. But then people can make any changes at all - not even adjusting their notification settings, map preferences, etc. However, I am a bit "worried" that this might allow them to make some edits that we don't want -- I guess we'll have to give it a try! Unless you have any other thoughts? 

Jonathan Bergen 02/02/2026: I think that we need to allow users to set their own settings, so we shouldn't use this setting widely. We'll have to test this to make sure that they can't make edits that we don't want, but there are ways to configure permissions that we'll just have to figure out.

  * "Device Read-only": 
    * if "Master Administrator" = checked (on the "Provider Traccar Logins" table on Contacts): sets to not checked; 
      * note that this allows Master Administrators to temporarily make changes, though those changes will be overridden the next time the Traccar sync runs 
    * for all other users: sets to checked; 
  * "Limit Commands": 
    * if "Master Administrator" = checked (on the "Provider Traccar Logins" table on Contacts): sets to not checked; 
      * note that this allows Master Administrators to temporarily make changes, though those changes will be overridden the next time the Traccar sync runs; 
    * for all other users: sets to checked; 
  * "Disable Reports": retains default of not checked; 
  * "No Email Change": 
    * if "Master Administrator" = checked (on the "Provider Traccar Logins" table on Contacts): retains default of not checked; 
      * note that this allows Master Administrators to temporarily make changes, though those changes will be overridden the next time the Traccar sync runs) 
    * for all other users: sets to checked (to require email changes to happen in Silverloom); 
  * "Traccar User Attributes" section: 
    * __ TBD; 
  * "Traccar User Connections" section 
    * __ TBD; 


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

TODO_JB / CCI: Please document the Report Path and Import Path, and confirm Trigger Name and Priority, & let us know, so that we can update the spec accordingly. Thanks!
