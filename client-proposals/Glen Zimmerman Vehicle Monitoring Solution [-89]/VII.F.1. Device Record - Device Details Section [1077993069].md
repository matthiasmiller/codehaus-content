7.6.1. Device Record - Device Details Section

  


Requirements

*. 

  


  * Device Details section (section heading displays as "Device Details:" (with a colon, to preface the displayed "Device Description" macro - see corresponding spec)):



  


  * Items in the section heading:
    * Device Description (no label; displays after the section heading; located in the left-hand end of the section heading; read-only macro; displays "<Device Name> (<Device ID>)", i.e. "John's Car (ABCDXYZ)")



  


  * Device Status (no label; located in right-hand end of the section heading; read-only macro; dynamically displays items from the "Device Record Statuses" list, with the following logic:
    * "General Inventory" (if "Assigned Reseller" = blank; this is for Devices that are not assigned to a Reseller or linked to an Account);
    * "Available" (if "Assigned Reseller" ≠ blank and "Set Device Status" = "Available"; this is for Devices that are linked with a Reseller and are available to be assigned to an Account) 
    * "Assigned - Online" (if "Account" ≠ blank and "Traccar Device Status" = "Online"; this is for Devices that are linked with an Account, are not paused, and are currently transmitting data (as of the most recent sync with Traccar)) 
    * "Assigned - Offline" (if "Account" ≠ blank and "Traccar Device Status" = "Offline"; this is for Devices that are linked with an Account, are not paused, and are not currently transmitting data (as of the most recent sync with Traccar)) 
    * "Assigned - Paused" (if "Account" ≠ blank and "Set Device Status" = "Paused"; this is a temporary status for Devices that are linked with an Account and have been paused)
    * "Assigned - Lost" (if "Account" ≠ blank and "Set Device Status" = "Lost"; this is a temporary status for Devices that have been misplaced, etc.; after a Device has had this Status for a while, a user should eventually mark it as "Decommissioned" if it is not found)  
    * "Assigned - Disabled" (if "Account" ≠ blank and "Set Device Status" = "Disabled in Traccar"; this is for Devices that are still linked to inactive Accounts but have not been reclaimed by / returned to the Reseller; the user would mark it as "Decommissioned" once reclaimed or after a reasonable period of time)
    * "Lost" (if "Account" = blank and "Set Device Status" = "Lost"; this is for Devices that were lost / misplaced while not linked to an Account (i.e. while in inventory, etc.))
    * "Decommissioned" (if "Set Device Status" = "Decommissioned"; this is for Devices that are thrown away, no longer available to be used, etc.) 



  


  * Items on the left side:
    * Device Type (required; drop list of "Device Types" list items; defaults to "OBD-II")
    * Device ID (required; plain text; with the following details / behaviors:
      * validate against duplicates across the whole Solution;
      * warning on the field if changed from non-blank: "Warning: Changing this will change the corresponding ID in Traccar and throughout Silverloom.";
      * data synced with Traccar on Save (Traccar's Device "Identifier" field); 
      * note that this is the unique ID for the record)
    * Device Name (required; plain text; with the following details / behaviors:
      * validates against duplicates within the same Account - error on Save: "This Device Name is already used by another device in the same Account.";
      * warning on the field if changed from non-blank: "Changing this will change the corresponding Name in Traccar.";
      * data synced with Traccar on Save (Traccar's Device "Name")) 



  


  * Reseller (macro; with the following details / behaviors:
    * if "Account" is blank:
      * label displays as "Assigned Reseller";
      * drop list of active "Account Reseller" Contacts; 
      * displays / sets the hidden "Assigned Reseller" stored field (see corresponding spec);
      * conditional editability: 
        * fully editable for users with the "Edit General Inventory Devices" Permission; 
        * if saved as blank (i.e. current "Status" = "General Inventory"), editable for all Account Resellers and all Group Admins; 
        * if saved as non-blank (i.e. current "Status" = "Available"), editable for the selected Account Reseller; 
        * for all other users: read-only; 
      * conditionally optional / required:
        * optional if the editing user has the "Edit General Inventory Devices" Permission (to allow for tracking items in "General Inventory");
        * required for other users who can edit the field but do not have the above Permission (to require them to set the field when entering the Device into the Solution); 
    * if "Account" is not blank:
      * label displays as "Account Reseller";
      * read-only macro;
      * displays the "Account Reseller" for the selected "Account";
    * includes the following validation(s), regardless of "Account" setting: 
      * error on Save if "Device Status" has changed from "Decommissioned" to something else and the linked "Reseller" is not an active Contact with "Is Account Reseller" checkbox checked: "Device cannot be reactivated because the linked Reseller is not active."; this is to prevent inactive Account Resellers from remaining linked with Devices that are reactivated)



  


  * Assigned Reseller (hidden field; drop list of active "Account Reseller" Contacts; set by the "Reseller" macro - see corresponding spec) 



TODO_JB: Tim Reitz 01/13/2026: "Reseller" and "Assigned Reseller" would have bearing on editability in Traccar (if we allow users to edit Devices interactively in Traccar...). 

Tim Reitz 01/16/2026: I'm inclined to not allow most users to edit Devices interactively in Traccar. Maybe just "Full Access" Silverloom users. 

  


  


  * Items on the right Side:
    * Set Device Status (required; drop list of "Set Device Record Statuses" list items; used to set the manual portion of the "Device Status" macro - see corresponding spec; with the following details:
      * defaults to "Available";
      * items include the following, with the corresponding details:
        * "Available":
          * see notes under "Device Status" for explanation; 
          * automatically sets to this when "Account" is set to blank - see corresponding spec; 
          * error on the field if set to this and "Account" ≠ blank: "Device cannot be set as available while linked to an Account."; 
          * on the first Save after set to this, Traccar's Device "Disabled" checkbox field is updated to checked; 
        * "Assigned": 
          * see notes under "Device Status" for explanation;  
          * automatically sets to this when "Account" is set to non-blank - see corresponding spec; 
          * on the first Save after set to this, Traccar's Device "Disabled" checkbox field is updated to not checked; 
        * "Paused": 
          * see notes under "Device Status" for explanation; 
          * error on the field if set to this and "Account" = blank: "Device cannot be set as paused while not linked to an Account."; 
          * Traccar's Device "Disabled" checkbox field remains unchanged;
        * "Lost": 
          * see notes under "Device Status" for explanation;  
          * can be set to this whether "Account" is blank or non-blank;
          * Traccar's Device "Disabled" checkbox field remains unchanged;
        * "Disabled in Traccar": 
          * see notes under "Device Status" for explanation;  
          * can be set to this whether "Account" is blank or non-blank; 
          * on the first Save after set to or from this, Traccar's Device "Disabled" checkbox field is updated to match; 
        * "Decommissioned":
          * see notes under "Device Status" for explanation; 
          * error on the field if set to this and "Account" ≠ blank: "Device cannot be decommissioned while linked to an Account.";
          * on the first Save after set to or from this, Traccar's Device "Disabled" checkbox field is updated to match; 
      * data synced with Traccar on Save (Traccar's Device "Disabled" checkbox)) 



  


  * "Device is offline." (on-screen message in white font with red background; visible if "Device Status" = "Assigned - Offline") 
  * "Device is lost." (on-screen message in black font with yellow background; visible if "Device Status" = "Assigned - Lost" or "Lost") 
  * "Device is paused." (on-screen message in black font with blue background; visible if "Device Status" = "Assigned - Paused")



  


Development Specification

TODO_MOCKUPS: Tim Reitz 01/14/2026: I've done some updating on this spec. Could you confirm that that mockups match? Thanks! (the messages with colored backgrounds don't all need to be on the mockup) 

  


  


TODO_PRICING: Tim Reitz 01/13/2026: I think we factor in some "fear, uncertainty, and doubt" when estimating this section, especially validations and behaviors for "Device Status", "Set Device Status", and "Account Reseller".
