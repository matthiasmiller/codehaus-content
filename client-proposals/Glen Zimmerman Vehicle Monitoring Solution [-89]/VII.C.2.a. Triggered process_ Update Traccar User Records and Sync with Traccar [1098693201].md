7.3.2.1. Triggered process: Update Traccar User Records and Sync with Traccar

  


Requirements

  * On the first Save after one or more new rows are added, or one or more existing saved rows are deleted, or one or more existing saved rows are edited, the "Update Traccar User Records and Sync with Traccar" triggered automatic process runs to create and/or update Traccar User sync records in the background and sync with Traccar, updating the Account Member's details in Traccar and their login access there - see corresponding automatic process spec; 



TODO_VA: Tim Reitz 01/19/2026: Triggered automatic process: "Update Traccar User Records and Sync with Traccar"

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

TODO_NM: Tim Reitz 01/19/2026: How to spec this? 

  


TODO_VA: Tim Reitz 01/19/2026: Let's make sure to spec out the trigger & details for syncing from the Contact record. 

  


\---------------------

  


  * Name: "Update Traccar User Records and Sync with Traccar"
    * Description: Creates and updates Traccar User records based on Silverloom Contact records and Account records, and syncs that data to Traccar.
    * Action(s): 
      * Creates new Traccar User records as needed (if no User exists in Traccar with the same __), setting the following: 
        * "Name": sets to the __; 
        * "Email": sets to the "Traccar Login Email"; 
        * "Phone" sets to __; 
        * TODO_VA
      * Update Traccar User records as needed, setting the following: 
        * "Name": __; 
        * "Email": __; 
        * "Phone": __; 
        * TODO_VA
      * Runs the Silverloom-to-Traccar sync
      * __ (TODO_VA: Brief description of what each included .x30 or .r20 does, followed by the .x30 / .r20 name in parenthesis - usually can be set to "TBD" in the initial spec, with a note for the developers to determine this and for us to document it after coding) 
    * Trigger Name (to be enabled at deployment):
      * Update Traccar User Records from Accounts & Sync with Traccar
      * Update Traccar User Records from Contacts & Sync with Traccar
    * Report Path:
      * From Accounts: __ (TBD in coding)
      * From Contacts: __ (TBD in coding)
    * Initiated:
      * From Accounts: On every Save of the Account record or On the first Save after: 



TODO_NM: Tim Reitz 01/20/2026: Do you know which would be better? Or is that a question for JB? 

  * one or more new rows are added, or 
  * one or more existing saved rows are deleted, or 
  * one or more existing saved rows are edited 


  * From Contacts: On every Save of the Account record or On the first Save after: 



TODO_NM: Tim Reitz 01/20/2026: Same as above: Do you know which would be better? Or is that a question for JB? 

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
