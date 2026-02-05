8.5.3. Available Devices Report

*. 

  


Overview: This is a custom report of Device records that are assigned to a Reseller but are not linked wiht an Account (specifically, "Device Status" ≠ "Available"). It is used by Resellers (and other Provider users) to select a Device to add it to an Account.

  


Accessed from: 

  * "Add Device to Account" link on the Account record
  * Providers | Accounts | Available Devices (opens the filter screen)



  


Title: "Available Devices" 

  


Preface: N/A

  


Columns: 

  * Device Type 
  * Device ID (link to record; __) 
  * Device Name 



  


Row-Specific Buttons: N/A

  


Grouped by: N/A

  


Sorted by: Device ID (alphabetically) 

  


Filters: 

  * Provider (required; editable for users with the "Full Access" Permission; drop list of "Display Names" for all Account Resellers, Group Admins, and Master Administrators; defaults to the current user)
  * Add to Account (optional; drop list of "Account #" values for Accounts that are editable for the selected "Provider"; defaults to blank = N/A when opened from the menu (when opened from an Account record, defaults to that Account); note that this is passed through to the "Add Device to Account" button & action - see spec)



  


Buttons: 

  * New Device (opens a new Device record, with "Account" defaulted to the selection in the "Add to Account" filter; note that this can be used if a "Traccar Client App"-type Device is needed, or if the desired Device is not yet in the database) 
  * Add Device to Account (opens a prompt screen with the following:
    * Account # (drop list of "Account #" values for Accounts that are editable for the selected "Provider"; defaults to the selection in the "Add to Account" filter) 
    * Device (read-only; list of "Device ID" values; defaults to the last-selected row on the report) 
    * Continue (button; sets the "Account" on the selected "Device" record, and opens that record) 



  


_NM: Tim Reitz 01/30/2026: I'm speccing out a semi-automated process to set "Account" on the Device record. How much more work is this, compared to making the user open the Device record from this report to set "Account" manually?

TODO_VA: Tim Reitz 01/30/2026: We could use a modify record (no prompt screen). Button would be visible if "Add Device to Account" is not blank. BUT it would not open the record automatically. 

So, let's just have the user open the Device record, with the "Account" set automatically.  

  


Menu Visibility: All users

  


Other Notes:

  * N/A


