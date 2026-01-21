5.6.4. Unscheduled Deliveries Report

  


Requirements

This is an editable report of all Delivery records that need to be scheduled, i.e. that meet one of the following criteria: 

  * "Scheduled" checkbox is not checked and "Quote / Order #" is blank, or 
  * "Scheduled" checkbox is not checked and "Quote / Order #" is set to an Order record with "Status" = "Order"



This report can be used to add Deliveries to the Production Calendar.

  


Accessed from: Triple D Truss | Deliveries | Unscheduled Deliveries 

  


Title: Unscheduled Deliveries

  


Columns: 

  * Scheduled (editable; checkbox)
  * Schedule Date (editable; displays the Schedule Date from the Delivery record)
  * Delivery ID (link to Delivery record)
  * Quote/Order # (link to Order record)
  * Customer (read-only; displays the Customer from the Delivery record)
  * Job Name (read-only; displays the Job Name from the Delivery record)
  * Area (read-only; displays the Area from the Delivery record)
  * Board Ft (editable; displays the Board Feet from the Delivery record)
  * Item (editable; displays the Item from the Delivery record)
  * Lum Pkg (ready-only; displays Yes / No based on the Lum Pkg checkbox on the Delivery record )
  * Mtl Pkg (read-only; displays as Yes / No based on the Mtl Pkg checkbox on the Delivery record ) 
  * Set (read-only; displays as Yes / No based on the Set checkbox on the Delivery record) 
  * Drop (read-only; displays as Yes / No based on the Drop checkbox on the Delivery record) 
  * Sm. Truck (read-only; displays as Yes / No based on the Small Truck checkbox on the Delivery record)
  * Info (editable; displays the Info field from the Delivery record)
  * Made (editable; checkbox; displays as Yes / No based on the "Made" checkbox on the Delivery record)
  * Delivery $ (editable; displays the Delivery $ from the Delivery record)
  * Permit (editable; checkbox; displays as Yes / No based on the Permit checkbox on the Delivery record)
  * Permits $ (editable; displays the Permits $ field from the Delivery record)
  * Escort (editable; checkbox; displays as Yes / No based on the Escort checkbox on the Delivery record)
  * Escorts $ (editable; displays the Escorts $ field from the Delivery record)
  * Overnights $ (editable; displays the Overnights $ from the Delivery record)



  


Grouped by: Unscheduled (if "Will Call" checkbox is unchecked) / Will Call ("Will Call" checkbox checked)

  


Sorted by: Schedule Date (oldest date at the top)

  


Filters: 

  * Order # (optional; number field; defaults to blank = all)
  * Delivery # (optional; number field; defaults to blank = all)
  * Schedule Date Start (date field; defaults to blank = all)
  * End (date field; defaults to blank = all)



  


Buttons:

  * "Save Changes" (when clicked, saves all changes that have been made to the report)



  


Save Type: Save Button

  


Other Notes:

  * N/A



  


Development Specification

Change Requests:

  * Ben Reitz 05/08/2025: [[[IN10789](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10791&)]] - ZTD - Allow for linking Orders and Deliveries
  * Ben Reitz 05/08/2025: [[[IN11336](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11338&)]] - ZTD - Unscheduled Deliveries report - Add "Info" and "Made" columns


