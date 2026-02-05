8.2.12. Contact Record - <Service Name> Contact Settings

*. (except for service name) 

  


  * <Service Name> Contact Details section (custom section):



  


  * Is Master Administrator (custom; visible if "Is Organization" is not checked; read-only macro; checkbox;  with the following details / behaviors:
    * displays as checked if the linked User Profile has the "Full Access" Permission; 
    * note that this mainly functions as a label, rather than driving data access, since data access for these users is determined by the "Full Access" Permission;
    * also note that if a CCI Support user with the same Permission has a Contact record set up & linked with their User Profile, they will be set with this role)



  


  * Is Group Admin (custom; visible if "Is Organization" is not checked; macro; checkbox; with the following details / behaviors: 
    * editability: 
      * if "Is Master Administrator" is checked: read-only; displays as checked (since those users automatically have this role); 
      * otherwise (if "Is Master Administrator" not checked): editable for users with the "Full Access" Permission, to manually give the Contact / user the role of Group Admin; 
    * when manually set to checked / not checked, the hidden "Is Group Admin (Stored)" field is set accordingly - see corresponding spec; 
    * includes the following validation(s): 
      * error on the field if set to checked when "User ID" for the current Contact is saved as blank: "User ID must be set and saved prior to assigning this role."; in this case the user should uncheck this checkbox, set up the User Profile (if needed), set the User ID on the Contact record, and save, then check this checkbox; 
      * error on the field if set to not checked and if the Contact is included on the "Group Admins" embedded spreadsheet for one or more active Account Group records: "Remove this Contact from the Group Admins table on the linked active Group(s) before unchecking this box.") 
  * Is Group Admin (Stored) (custom; hidden field; checkbox; with the following details / behaviors: 
    * is set based on the "Is Group Admin" macro - see corresponding spec; 
    * on the first Save after this is set to checked or unchecked, the "Set User Group Based on User Role" triggered background process runs - see corresponding spec) 
  * For <#> Account Group(s) (custom; visible if "Is Group Admin" is checked; with the following details / behaviors: 
    * link; opens the Account Group directly if there is only one, otherwise opens the "Account Groups by Group Admin" report, filtered to this Group Admin; 
    * "<#>" displays the number of Account Groups for which the Contact is included on the "Group Admins" embedded spreadsheet)



  


  * Is Account Reseller (custom; always visible, regardless of whether the Contact is an individual or an organization; macro; checkbox; with the following details / behaviors: 
    * editability: 
      * if "Is Master Administrator" and/or "Is Group Admin" is checked: read-only; displays as checked (since those users automatically have this role); 
      * otherwise (if neither "Is Master Administrator" nor "Is Group Admin" is checked): editable for users with the "Full Access" Permission, to manually give the Contact / user the role of Account Reseller; 
    * when manually set to checked or not checked, the hidden "Is Account Reseller (Stored)" field is set accordingly - see corresponding spec;
    * includes the following validations: 
      * error on the field if set to checked when "User ID" for the current Contact is saved as blank: "User ID must be set and saved prior to assigning this role."; in this case the user should uncheck this checkbox, set up the User Profile (if needed), set the User ID on the Contact record, and save, then check this checkbox; 
      * error on the checkbox if set to not checked and if the Contact is set as the "Account Reseller" on one or more non-"Closed" Account records: "Remove this Contact from the Account Reseller field on the linked non-Closed Account(s) before unchecking this box."; 
      * error on the checkbox if set to not checked and if the Contact is set as the "Assigned Reseller" on one or more non-"Decommissioned" Device records: "Remove this Contact from the Assigned Reseller field on the linked non-Decommissioned Device(s) before unchecking this box.") 
  * Is Account Reseller (Stored) (custom; hidden field; checkbox; with the following details / behaviors: 
    * is set based on the "Is Account Reseller" macro - see corresponding spec; 
    * on the first Save after this is set to checked or unchecked, the "Set User Group Based on User Role" triggered background process runs - see corresponding spec) 
  * For <#> Account(s) (custom; visible if "Is Account Reseller" is checked; with the following details / behaviors:
    * link; opens the Account directly if there is only one, otherwise opens the "Accounts by Account Reseller" report, filtered to this Account Reseller; 
    * "<#>" displays the number of Accounts for which the Contact is set as the "Account Reseller") 



  


  * Is Reseller Admin (custom; visible if "Is Organization" is not checked; read-only macro; checkbox; with the following details / behaviors:
    * displays as checked if the Contact is set as the "Linked Contact" on one or more Traccar User sync records that meet the following conditions:
      * "Traccar Login Category" = "Reseller Rep" and 
      * "Reseller Admin" checkbox = checked) 
  * For <Reseller Name(s)> (custom; visible if "Is Reseller Admin" is checked; with the following details / behaviors: 
    * link; opens the organization "Account Reseller" Contact directly if there is only one, otherwise opens the "Resellers by Reseller Admin" report, filtered to this Contact; 
    * "<Reseller Name(s)>" displays the number of "Account Reseller" Contact(s) for which the Contact is a "Reseller Admin")



  


  * Is Reseller Rep (custom; visible if the Contact is not an organization; checkbox; with the following details / behaviors: 
    * editable for users with the "Full Access" Permission, to manually give the Contact / user the role of Reseller Rep;
    * includes the following validations: 
      * error on the field if set to checked when "User ID" for the current Contact is saved as blank: "User ID must be set and saved prior to assigning this role."; in this case the user should uncheck this checkbox, set up the User Profile (if needed), set the User ID on the Contact record, and save, then check this checkbox; 
      * on the first Save after this is set to checked or unchecked, the "Set User Group Based on User Role" triggered background process runs - see corresponding spec) 
  * For <Reseller Name(s)> (custom; visible if "Is Reseller Rep" is checked; with the following details / behaviors: 
    * link; opens the organization "Account Reseller" Contact directly if there is only one, otherwise opens the "Resellers by Rep" report, filtered to this Contact; 
    * "<Reseller Name(s)>" displays the number of organization "Account Reseller" Contact(s) for which the Contact is a "Rep") 



  


  * Is Primary Account Manager (custom; visible if "Is Organization" is not checked; read-only macro; checkbox; with the following details / behaviors:
    * displays as checked if the Contact is set as the "Linked Contact" on one or more Traccar User sync records that meet the following conditions:
      * "Traccar Login Category" = "Account Member" and 
      * "Primary Account Manager" checkbox = checked) 
  * For <#> Account(s) (custom; visible if "Is Primary Account Manager" is checked; with the following details / behaviors: 
    * link; opens the Account directly if there is only one, otherwise opens the "Accounts by Primary Account Manager" report, filtered to this Contact; 
    * "<#>" displays the number of Accounts for which this Contact is an "Account Manager")



  


  * Is Account Manager (custom; visible if "Is Organization" is not checked; read-only macro; checkbox; with the following details / behaviors:
    * displays as checked if the Contact is set as the "Linked Contact" on one or more Traccar User sync records that meet the following conditions:
      * "Traccar Login Category" = "Account Member" and 
      * "Account Manager" checkbox = checked) 
  * For <#> Account(s) (custom; visible if "Is Account Manager" is checked; with the following details / behaviors: 
    * link; opens the Account directly if there is only one, otherwise opens the "Accounts by Account Manager" report, filtered to this Contact; 
    * "<#>" displays the number of Accounts for which the Contact is an "Account Manager")



  


  * Is Driver (custom; visible if "Is Organization" is not checked; checkbox; read-only macro; with the following details / behaviors:
    * displays as checked if the Contact is set as the "Linked Contact" on one or more Traccar User sync records that meet the following conditions:
      * "Traccar Login Category" = "Account Member" and 
      * "Driver" checkbox = checked) 
  * For <#> Device(s) (custom; visible if "Is Driver" is checked; with the following details / behaviors: 
    * link; opens the Device directly if there is only one, otherwise opens the "Devices by Primary Driver" report, filtered to this Contact; 
    * "<#>" displays the number of Devices for which the Contact is set as the "Primary Driver") 



  


  


  * Other Notes: 
    * Note that an individual Contact may have none, one, multiple, or all of these checkboxes checked.


