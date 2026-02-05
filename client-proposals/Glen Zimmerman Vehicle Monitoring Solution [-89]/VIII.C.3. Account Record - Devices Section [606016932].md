7.3.3. Account Record - Devices Section

*Done. 

  


  * Devices section:
    * Linked Devices ("virtual" read-only embedded spreadsheet with the following, displaying all Device records that are or have been linked with this Account:  
      * Columns: 
        * Device ID (read-only macro; displays the "Device ID" from the Device record) 
        * Device Name (read-only macro; if "Account" for the Device record = this Account, displays the "Device Name" from the Device record; otherwise (if "Account" is blank), this is blank) 
        * Primary Driver (read-only macro; if "Account" for the Device record = this Account, displays the "Primary Driver" from the Device record)
        * Device Status (read-only macro; if "Account" for the Device record = this Account, displays the "Device Status" from the Device record) 
        * Last Event Date & Time (read-only macro; displays the date and time for the last linked Event record, specifically "<Event Date>"; <Event Time>" from the top row of the "Device Events" embedded spreadsheet on the Device record) 
        * Primary Vehicle (read-only macro; if "Account" for the Device record = this Account, displays the Primary Vehicle details from the Device record, in the following format: "<Year> <Make>, <Model>")
        * Date Added (read-only macro; displays the "Date Added" from the hidden "Account Linking History" embedded spreadsheet on the Device record)
        * Date Removed (read-only macro; displays the "Date Removed" from the hidden "Account Linking History" embedded spreadsheet on the Device record)
        * View / Manage (link to open the Device record; displays as "Link")
      * Automatically sorted by: 
        * First by: Account / Device linking (Devices currently linked to the Account at the top; Devices not currently linked to the Account at the bottom) 
        * Second by: "Device Status" (standard sequence of the "Device Record Statuses" list - "Decommissioned" at the bottom) 
        * Second by: "Date Added" (alphabetically) 
      * Buttons to add/remove rows: N/A 
      * Shows 8 rows without scrolling
      * Other Notes: 
        * Text color: 
          * Rows display in gray font for Devices that meet the following criteria: 
            * Device is linked to the Account but "Device Status" = "Decommissioned", or 
            * Device is no longer linked to the Account; 
          * Other rows display in standard black font)



  


  * Add Device (link; visible to users who can edit the Account; opens the "Available Devices" report, filtered to the current Account; the Reseller or another Upline Provider user can open this report to select a Device to link with the Account)


