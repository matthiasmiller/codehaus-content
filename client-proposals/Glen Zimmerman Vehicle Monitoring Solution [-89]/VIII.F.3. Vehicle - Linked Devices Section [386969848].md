7.7.3. Vehicle - Linked Devices Section

*Done. 

  


  * Linked Devices section 
    * Linked Devices (no label; read-only "virtual" embedded spreadsheet of the following:
      * Columns: 
        * Device ID (read-only macro; displays the "Device ID" from the corresponding Device record)
        * Is Primary Vehicle for Device (read-only macro; checkbox; displays as checked if the current Vehicle record is set as the "Primary Vehicle" on the corresponding Device record, specifically, if it is the top row of the "Primary Vehicle History" non-embedded spreadsheet on the Device) 
        * View Device (link; displays as "Link"; opens the corresponding Device record)
        * Account # (read-only macro; displays the current "Account #" from the corresponding Device record) 
        * Primary Account Manager (read-only macro; displays the "Display Name" for the Primary Account Manager from the corresponding Device record)
        * Primary Driver (read-only macro; displays the "Display Name" for the current Primary Driver from the corresponding Device record)
        * View Account (link; displays as "Link"; opens the corresponding Account record)
      * Automatically sorted by: "Device ID" (alphabetically)
      * Buttons to add/remove rows: N/A
      * Shows 4 rows without scrolling
      * Other Notes: 
        * Automatically includes a row for each Device that has logged activity for this Vehicle, specifically each Device record that is set as the "Traccar Device ID" on a Traccar Event Record that is linked to this Vehicle (via the "Device Primary Vehicle" field))
    * This list includes all Devices that have linked Traccar Events in <Service Name>. (on-screen message in black font)



  


  * Primary Vehicle for <X> Device(s) (with the following details / behaviors: 
    * link; opens the "Devices by Primary Vehicle" report, filtered to this Vehicle - see corresponding spec)
    * "<X>" displays the number of Device records for which this Vehicle is selected as the "Primary Vehicle")


