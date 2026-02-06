8.5.1. All Devices Report

  


Requirements

Overview: This is a custom report of all Device records, with various filters. Pre-filtered versions of this report can be opened from different locations (see corresponding specs).

  


Accessed from:

  * Providers | Devices | All Devices (opens the report directly, bypassing the filter screen) 
  * Providers | Devices | Device Search (opens the filter screen) 
  * Other menu options & report links (see corresponding specs)



  


Title: 

  * If "Search Mode" filter is set to checked: "Device Search"
  * Otherwise:
    * Main title: "Devices"
    * Prefixes:
      * N/A for now
    * Suffixes:
      * If "Account" filter is not blank: " for Account <Account #>"
      * If "Group" filter is not blank: " (Group: <Group Name>)"
      * If "Reseller" filter is not blank: " (Reseller: <Account Reseller>)"
  * Examples:
    * "Search Mode"
    * "Devices"
    * "Devices for Account 1234"
    * "Devices for Account 1234 (Group: Friendly Families (14))"
    * "Devices for Account 1234 (Reseller: John Doe)"
    * "Devices for Account 1234 (Group: Friendly Families (14)) (Reseller: John Doe)"
    * "Devices (Reseller: John Doe)"
    * etc.



  


Preface: 

  * "General Inventory Devices Available: <X>" (included as an easy visual reference for users to know how many are available for request)



_NM: Tim Reitz 10/04/2025: Is this doable while also hiding "General Inventory" devices / rows from users without the "Edit General Inventory Devices" Permission?

TODO_VA: Tim Reitz 10/06/2025: Since we're not using restricted data for this, Nic thinks we can do this. 

Or would it be better to have a dedicated "General Inventory" menu option that opens a super simple report, showing just this information? Maybe also a mailto link so the user can request more devices?

  


Columns: 

  * Device Status
  * Device Type
  * Device ID
  * Device Name (link to the Device record)
  * Primary Driver
  * Account
  * Reseller
  * Account Group



  


_GZ: Tim Reitz 12/11/2025: Would you want to have the same background colors here as we're using for the on-screen message on the Device record? 

  * "Assigned - Offline": red;
  * "Assigned - Paused": blue;
  * "Assigned - Lost": yellow;
  * "Lost": yellow; 



TODO_VA: Tim Reitz 12/18/2025: Per Glen today, it could be nice to have the same color-coding on the report. 

  


Row-Specific Buttons:

  * __ (accessed by hovering over the first column in the right pane; row-specific; __



TODO_VA: Tim Reitz 10/04/2025: Probably not any, unless we add a "Switch Accounts" button, to change the "Account"...

  


Grouped by: The selection in the "Group By" filter:

  * If "Device Status": Grouped by "Device Status" (standard sequence);
  * If "Account Group": Grouped by "Account Group" (alphabetically);
  * If "Reseller": Grouped by "Reseller" (alphabetically);
  * If "Account": Grouped by "Account" (alphabetically);
  * If blank: no grouping



  


Sorted by: Device ID

  


Filters: 

_NM: Tim Reitz 10/04/2025: I'm thinking that all of these ask prompts would be hidden for basic Account Managers and Drivers. Does that sound fine?

Tim Reitz 10/06/2025: Per Nic, yes, that works. Hide the ask prompts for certain users. 

_GZ (mockup): Tim Reitz 10/06/2025: Do you want Account Managers & Drivers to be able to see the report filters? They would only have a few devices... 

TODO_VA: Tim Reitz 10/23/2025: Per Glen today, yes, definitely hide the filters from these users to decrease the clutter. It'll be unlikely to get a customer large enough to have so many vehicle that they'll need filtering. 

  * Search Mode (hidden; checkbox; defaults to not checked; when not checked, Device records with "Devices Status" = "General Inventory" are hidden for users who do not have the "Edit General Inventory Devices" Permission; is set to checked when the report is opened from the "Device Search" menu option)



_NM: Tim Reitz 10/04/2025: Does this sound right to have a hidden "Search Mode" ask prompt, to allow resellers / group admins to view "General Inventory" Devices? It would be nice to avoid having 2 separate reports, duplicating a lot of the same columns and ask prompts...

TODO_VA: Tim Reitz 10/06/2025: We can skip this. We can say that if "Device ID" is blank, the records are hidden. If "Device ID" is not blank, it can show all matches (including General Inventory). 

  * Group (visible to Group Admins and Master Administrators; drop list of __; defaults to blank = all)
  * Reseller (visible to Group Admins and Master Administrators; drop list of __; defaults to blank = all)
  * Account (visible to Account Resellers, Group Admins, and Master Administrators; drop list of __ that the current user can ; defaults to blank = all)
  * Device ID (visible to Account Resellers, Group Admins, and Master Administrators; drop list of __; defaults to blank = all)



TODO_VA: Tim Reitz 10/06/2025: Don't allow searching by partial (to prevent users from seeing extra General Inventory devices when they search). 

  * Account Manager (optional; drop list of "Display Name" values for Account Managers; defaults to blank = all; if a selection is made here, the report includes Devices linked to Accounts for which the selected Contact is included on the "Account Managers" embedded spreadsheet)  
  * Primary Driver (optional; drop list of "Display Name" values for Drivers; defaults to blank = all)
  * Primary Vehicle (optional; drop list of "Vehicle Description" values for all Vehicles; defaults to blank = all)
  * Device Status (visible to Account Resellers, Group Admins, and Master Administrators; multi-select drop list of "Device Statuses" list items; defaults to all selected; the "General Inventory" item is hidden for users who do not have the "Edit General Inventory Devices" Permission)
  * Group By (visible to Account Resellers, Group Admins, and Master Administrators; drop list of "Device Status" / "Account" / "Account Group" / "Account Reseller" / blank = none; defaults to __)



_GZ (mockup): Tim Reitz 10/06/2025: Preference for default grouping? 

TODO_VA: Tim Reitz 10/23/2025: Per Glen today, probably "Device Status" (like Accounts report). 

TODO_VA: Tim Reitz 10/06/2025: Once we have a default, we need to review the filtered versions and determine which need to have a different grouping. 

_NM: Tim Reitz 10/04/2025: Better to define these on the report, or have a simple list?

TODO_VA: Tim Reitz 10/08/2025: Nic prefers a simple list. To prevent breakage if list items change, etc. "Device Report Groupings". 

  


Buttons: 

  * New Device (opens a blank new Device record)
  * Transfer Selected Devices (__



_GZ: Tim Reitz 10/04/2025: Thoughts on an option to batch-transfer Devices from one (or multiple) Accounts to a different (single) Account? Would this be useful or scary? If useful, which users should be able to do it? Or save for a possible future item?

TODO_VA: Tim Reitz 10/09/2025: Glen doesn't see much likelihood for this to happen from multiple Accounts. But it could happen where all Devices in one Account go to a different Account. It could happen where 5 or 10 Devices would need to be transferred. This could be saved for a possible future item. 

  


TODO_VA: Tim Reitz 10/09/2025: For Accounts: If a Reseller is going out of business, all of their Accounts would need to go somewhere. Let's save this as a possible future item. 

  


Menu Visibility: Based on the individual menus / menu items (see corresponding specs)

  


Other Notes:

  * This is an "auto-push" report, meaning that if there is only 1 row, it opens that record directly.
  * Note that users without the "Edit General Inventory Devices" Permission (i.e. most Resellers and Group Admins) are not able to view "General Inventory" Devices on the non-search versions of this report. This is to limit them from viewing all "General Inventory" Devices at the same time. They can, however, individual "General Inventory" Devices via the "Device Search" if they have the Device ID.



  


TODO_ NM: Tim Reitz 10/04/2025: We need to make sure that users cannot see the wrong Devices here (based on Reseller, Group, Account, etc.). I think this would be covered by the user / data restrictions, but wanted to confirm.

Tim Reitz 10/04/2025: Actually, all Resellers should be able to see all Devices (to be able to provide support for other Accounts, etc.)....

TODO_VA: Tim Reitz 12/10/2025: Is this still relevant? 

Also for:

[ ] Groups

[ ] Accounts

[ ] Contacts

[ ] ??

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=966430724#gid=966430724](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=966430724#gid=966430724)
