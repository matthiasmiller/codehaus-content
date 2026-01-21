7.3.3. Account Record - Devices Section

*

  


  * Devices section:
    * Linked Devices ("virtual" read-only embedded spreadsheet with the following, displaying all Device records that are or have been linked with this Account:  
      * Columns: 
        * Device Description (read-only macro; displays the "Device Description" from the Device record) 
        * Primary Driver (read-only macro; displays the "Primary Driver" from the Device record)
        * Device Status (read-only macro; displays the "Device Status" from the Device record)
        * Last __ Date & Time (read-only macro; displays __



TODO_JB: Tim Reitz 12/05/2025: What would be the best way to do something like this? I'm thinking the last event / connection.

  * Primary Vehicle (read-only macro; displays the Primary Vehicle details from the Device record, in the following format: "<Year> <Make>, <Model>")
  * Date Added (read-only macro; displays the "Date Added" from the hidden "Account Linking History" embedded spreadsheet on the Device record)
  * Date Removed (read-only macro; displays the "Date Removed" from the hidden "Account Linking History" embedded spreadsheet on the Device record)
  * View / Manage (link to open the Device record; displays as "Link")


  * Automatically sorted by: 
    * First by: 
      * Non-"Decommissioned" Devices currently linked to the Account at the top,
      * "Decommissioned" Devices currently linked to the Account,
      * Devices previously linked to the Account at the bottom; 
    * Second by: "Date Added" (alphabetically) 
  * Buttons to add/remove rows: N/A 
  * Shows 8 rows without scrolling
  * Other Notes: 
    * Rows display in gray font for Devices that meet the following criteria: 
      * Device is linked to the Account but "Device Status" = "Decommissioned", or 
      * Device is no longer linked to the Account)



  


  * Add Device (link; visible to "Upline Provider Roles" users for the Account; opens the "Add Device to Account" report, filtered to the current Account; an upline provider user can open this report to select a Device to link with the Account)


