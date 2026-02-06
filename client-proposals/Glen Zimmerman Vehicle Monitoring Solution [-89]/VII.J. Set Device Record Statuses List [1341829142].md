7.10. Set Device Record Statuses List

  


Requirements

*Done. 

  


Overview: This is a custom non-editable simple list used for setting the manually-set portion of the Device Record Status. 

  


It includes the following items: 

  


  * see the "Set Device Status" field in the Device Details section on the Device Record



  


This list is universal for all users.

  


Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

  


This list will be set up by CodeCrafters as part of the main development. If changes need to be made to this list, it will require some coding work.

  


Development Specification

  * "General Inventory" (if "Assigned Reseller" = blank; this is for Devices that are not assigned to a Reseller or linked to an Account);
  * "Available" (if "Assigned Reseller" ≠ blank and "Set Device Status" = "Available"; this is for Devices that are linked with a Reseller and are available to be assigned to an Account) 
  * "Assigned - Online" (if "Account" ≠ blank and "Traccar Device Status" = "Online"; this is for Devices that are linked with an Account, are not paused, and are currently transmitting data (as of the most recent sync with Traccar)) 
  * "Assigned - Offline" (if "Account" ≠ blank and "Traccar Device Status" = "Offline"; this is for Devices that are linked with an Account, are not paused, and are not currently transmitting data (as of the most recent sync with Traccar)) 
  * "Assigned - Paused" (if "Account" ≠ blank and "Set Device Status" = "Paused"; this is a temporary status for Devices that are linked with an Account and have been paused)
  * "Assigned - Lost" (if "Account" ≠ blank and "Set Device Status" = "Lost"; this is a temporary status for Devices that have been misplaced, etc.; after a Device has had this Status for a while, a user should eventually mark it as "Decommissioned" if it is not found)  
  * "Assigned - Disabled" (if "Account" ≠ blank and "Set Device Status" = "Disabled in Traccar"; this is for Devices that are still linked to inactive Accounts but have not been reclaimed by / returned to the Reseller; the user would mark it as "Decommissioned" once reclaimed or after a reasonable period of time)
  * "Lost" (if "Account" = blank and "Set Device Status" = "Lost"; this is for Devices that were lost / misplaced while not linked to an Account (i.e. while in inventory, etc.))
  * "Decommissioned" (if "Set Device Status" = "Decommissioned"; this is for Devices that are thrown away, no longer available to be used, etc.)


