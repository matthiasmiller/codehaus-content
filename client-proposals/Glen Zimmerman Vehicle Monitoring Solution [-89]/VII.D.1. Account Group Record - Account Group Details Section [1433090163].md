7.4.1. Account Group Record - Account Group Details Section

*Done. 

  


  * Account Group Details section:
    * Left side:
      * Group Name (required; plain text; with the following details / behaviors: 
        * editable for users who can edit the record; 
        * validate against duplicates - error on the field: "This Group Name is already being used by another Group."; 
        * data synced with Traccar)
      * Group State (read-only macro; displays the "State" from the primary address of the Primary Group Admin for the Group; this is for region-based reporting and notifications) 



  


  * Right side:
    * Active (checkbox; defaults to checked; with the following details / behaviors:
      * editable only for users with the "Full Access" Permission;
      * validations:
        * error on the field when set to not checked (deactivated) if there are any linked Accounts with "Status" = anything except "Closed": "Group cannot be deactivated because it has one or more non-closed Accounts.";
        * error on the field when set to not checked (deactivated) if any rows in the "Group Admins" embedded spreadsheet are for Contacts that are active: "Group cannot be deactivated because one or more Group Admins are active Contacts.";
        * error on the field when set to checked (reactivated) if any rows in the "Group Admins" embedded spreadsheet are for Contacts that are inactive or do not have the "Is Group Admin" checkbox checked: "Group cannot be reactivated because one or more rows in the Group Admins table are inactive Contacts, or are not Group Admins.";
      * note that Group Admins can have )


