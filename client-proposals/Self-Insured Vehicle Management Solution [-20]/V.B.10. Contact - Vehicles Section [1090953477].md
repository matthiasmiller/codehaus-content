5.2.10. Contact - Vehicles Section

  


Requirements

  * Vehicles section (custom section; visible if visible if the selected "Contact Type" for the record has "Client?" = "Yes or if there are any rows in the Vehicles embedded spreadsheet): 



  


  * Vehicles (no label; read-only embedded spreadsheet with the following; displays all Vehicles for which the Contact is the current "Owner" (both active and inactive Vehicles), and Vehicles for which the Contact was previously the "Owner":) 
    * Columns: 
      * Year (read-only macro; displays the Vehicle Year)
      * Make (read-only macro; displays the Vehicle Make) 
      * Model (read-only macro; displays the Vehicle Model) 
      * VIN/Serial # (read-only macro; displays the Vehicle VIN/Serial #) 
      * License Plate # (read-only macro; plain text; with the following details / behaviors: 
        * if Vehicle is active and the Contact is the current "Owner": displays the Vehicle "License Plate"; 
        * otherwise: blank)
      * Vehicle Type (read-only macro; plain text; with the following details / behaviors: 
        * if Vehicle is active and the Contact is the current "Owner": displays the "Vehicle Type"; 
        * otherwise: blank) 
      * Liability (read-only macro; checkbox; with the following details / behaviors: 
        * if Vehicle is active and the Contact is the current "Owner": checked if the Vehicle has active Liability Coverage; 
        * otherwise: not checked)
      * <Alternate text for Collision - Short label> (read-only macro; checkbox; with the following details / behaviors: 
        * if Vehicle is active and the Contact is the current "Owner": checked if the Vehicle has active <Collision> Coverage; 
        * otherwise: not checked)
      * Cargo (read-only macro; checkbox; with the following details / behaviors: 
        * if Vehicle is active and the Contact is the current "Owner": checked if the Vehicle has active Cargo Coverage; 
        * otherwise: not checked)
      * N/C (checkbox; with the following details / behaviors: 
        * if Vehicle is active and the Contact is the current "Owner": checked if the "No-Charge Vehicle" is set to "Yes" on the Vehicle; 
        * otherwise: not checked) 
      * Reason (read-only expression; plain text; with the following details / behaviors: 
        * if Vehicle is active and the Contact is the current "Owner": blank; 
        * otherwise: displays the most recent "Vehicle Deactivation Reason" for the corresponding Owner on the Vehicle; 
        * displays approximately 10 characters as a preview of the text of the field on the Vehicle screen) 
      * View (displays as "Link"; link to open the Vehicle record)
    * Automatically sorted by: 
      * First by: Active / Inactive 
      * Second by: Vehicle activation or deactivation date (most recent at the top)
    * Buttons to insert/append/remove rows: N/A (see "Add Vehicle" button below) 
    * Show 7 rows without scrolling
    * Other Notes: 
      * Rows for "Inactive" Vehicles with the Client still set as "Owner" and for Vehicles for which the Client was previously the "Owner" are displayed in gray font.



  


  * Add Vehicle (button; visible for the contact's agent or admins if the contact is active; prompts the user to save the record before opening; opens a new vehicle record, setting Owner and Vehicle Primary Driver)



  


Visibility: if the current contact is the owner of one or more vehicles.

  


Development Specification

Change Requests: 

  * Tim Reitz 08/23/2025: [[[IN10774](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10776&)]] - ZWA - Pre-ZWW - Contact - Vehicles Section - Keep Transferred Vehicles on the List


