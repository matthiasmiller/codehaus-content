17.2.2. Set User Group Based on User Role

  


Requirements

*Done. 

  


  * Name: Set User Group Based on User Role
    * Description: Runs from a Contact record to add or remove a User Group from the linked User Profile, based on checkboxes on the Contact record. 
    * Action(s): 
      * If the "Is Group Admin (Stored)" checkbox was edited, adds or removes the "Group Admin" User Group from the User Profile record. 
      * If the "Is Account Reseller (Stored)" or "Is Reseller Rep" checkboxes were edited, adds or removes the "Reseller" User Group from the User Profile record. 
    * Trigger Name (to be enabled at deployment): __ (TBD in coding) 
    * Report Path: __ (TBD in coding) 
    * Initiated:
      * On the first Save after the "Is Group Admin" checkbox is edited on the Contact record. 
      * On the first Save after the "Is Account Reseller" checkbox is edited on the Contact record. 
      * On the first Save after the "Is Reseller Rep" checkbox is edited on the Contact record. 
    * Priority: N/A 
    * Run as User: "Administrator" 
    * Import Path: __ (TBD in coding)



  


Development Specification

Tim Reitz 10/28/2025: Nic is thinking this is 1 triggered report and x30 that runs to do all of this. 

  


TODO_CCI: Please document the Trigger Name, Report Path, and Import Path & let us know, so that we can update the spec accordingly. Thanks!

  * Trigger Name (to be enabled at deployment): __ (TBD in coding) (This is the name of the Database Trigger to be set up - usually can be set to "TBD in coding" in the initial spec, with a note for the developers to determine this and for us to document it after coding) 
  * Report Path: __ (TBD in coding) (This is the "Trigger Report" \-- usually can be set to "TBD is coding", with the note below for the developers to determine & for us to document it after coding)
  * Import Path: __ (TBD in coding) (This is the "Import Report" \-- usually can be set to "TBD is coding", with the note below for the developers to determine & for us to document it after coding)


