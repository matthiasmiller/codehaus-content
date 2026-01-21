5.1.1. Contact Type Record

Overview: Contact Types are configured on Contact Type records and viewed on a Contact Types report (both Silverloom standard features). Note that any customizations are noted as such in the spec.  

  


Accessed via: Configure Contact Types Report

  


Sections and Fields: 

  * Active (checkbox; defaults to checked; a Contact Types cannot be deactivated if it is being used by an active Contact)
  * Type (required; plain text field; validates against duplicate Type names) 
  * Supported Entity Types (checkboxes; at least one of the first two is required to be filled:)
    * Individual (checkbox; defaults to checked)
    * Organization (checkbox)
    * Default to Organization (checkbox; editable if "Organization" is selected) 
  * Client? (custom field; required; drop-list of "Yes" / "No"; with the following details / behaviors: 
    * error on Save if changed to "No" when there is at least one active Contact that uses this Type: "Client type cannot be changed as there are one or more active contacts of this type.") 
  * Maximum Number of No-Charge Vehicles (custom field; visible and required if "Client?" = "Yes"; number; 0 decimals; with the following details / behaviors: 
    * error on Save if changed and there is at least one active Contact with the same number of No-Charge Vehicles as the new number:  "There is already one or more contacts with <New Value> No-Charge Vehicle(s). (Field: Maximum Number of No-Charge Vehicles)"; 
    * warning on Save if changed and there is at least one active Contact with more No-Charge Vehicles than the new number: "You cannot change it to <New Value>  as there is already one or more contacts with <Old Value> No-Charge Vehicle(s). (Field: Maximum Number of No-Charge Vehicles)")



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access:

  * Visibility: Custom: Admin only
  * Editability: Admin only



TODO_EM: Tim Reitz 07/26/2025: Should we change ZWA to use the new "Edit the Contact Type lookup record" Permission? If yes, we can switch to the standard approach of referencing that here ("users with the "Edit the Contact Type lookup record" Permission."). 

  


Custom: The Solution includes the following hard-coded Contact Types, which are included in the Solution automatically as read-only record (requiring coding work to edit): 

  * In-State Agent: Client - Yes, N/C Vehicles - 0



  


Other Notes: 

  * Note that additional custom Contact Types are set up on a per-Plan basis -- see Plan-specific spec notes. 
  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * Contact records may have certain custom sections and fields that are conditionally visible depending on their Contact Type (see corresponding sections in this proposal). 
  * Active Contact Types cannot be deleted.


