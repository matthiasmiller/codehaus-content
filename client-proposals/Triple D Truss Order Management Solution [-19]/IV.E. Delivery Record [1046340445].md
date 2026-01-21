4.5. Delivery Record

  


Requirements

TODO_AP: Tim Reitz 03/04/2025: Check row 10 of [https://zch.apphosting.zone/Detail/Edit/2?RecordType=ClientProposals&NumberID=-45&State=ISwSvCyE0ts&](https://zch.apphosting.zone/Detail/Edit/2?RecordType=ClientProposals&NumberID=-45&State=ISwSvCyE0ts&), to see if anything there seems useful to add here. 

  


Overview: The Delivery record is a custom record, and is used to track all the necessary details for scheduling the delivery of an order.

  


Accessed via: 

  * Triple D Truss | Deliveries | Production Calendar
  * Triple D Truss | Deliveries | Main Production Schedule
  * Triple D Truss | Deliveries | Starlight Production Schedule
  * Triple D Truss | Deliveries | Unscheduled Deliveries
  * "<X> Linked Delivery(s)" link on the Quote / Order record
  * etc.



  


Sections and Fields: 

  * Delivery section:
    * New Delivery (link; displayed above the section header; opens blank new Delivery record with "Will Call" checkbox checked)
    * Delivery ID (displays the unique identifier for the record; located on the right side of the Delivery section header)
      * Note that this is simply making the existing hidden ID field visible and locating it here.  
    * Quote / Order # (optional; number field; validation on the field if a number is entered that does not correspond with any existing Quote or Order records; when a valid Quote or Order number is entered, the following fields are copied from the corresponding record if the "Scheduled" checkbox is not checked on the Delivery record: 
      * Customer
      * Schedule Date (from "Delivery / Pickup Date")
      * Job Name
      * Item (from Quantity + Description of the top item from the Truss RG ) 
      * Lum Pkg
      * Mtl Pkg
      * Area (from City + ", " \+ ST)
      * Set
      * Drop
      * Small Truck
      * Travel Time)
    * View <"Quote" or "Order"> (link; visible if a valid Quote or Order number is entered in the "Quote / Order #" field; dynamically updates when linked to a Quote or Order)
    * Scheduled (checkbox; with the following behaviors: 
      * editable only by Users with the "Manage Delivery Scheduling" Permission;
      * defaults to unchecked; 
      * when checked, the the following fields are affected: 
        * "Schedule Date" is set to the following:
          * if "Quote / Order #" is blank, defaults to the current date;
          * if "Quote / Order #" is not blank, defaults to the Delivery / Pickup Date on the linked record; 
        * "Will Call" checkbox is unchecked; 
      * when unchecked, clears the "Schedule Date" field;
      * error on the field if the checkbox is checked while the Delivery is linked to an Order record with "Status" = "Quote": "Deliveries for Quotes cannot be added to the Production Calendar.";
      * can be set interactively or via the "Scheduled" column on the Unscheduled Deliveries report; 
      * is automatically unchecked if the "Will Call" checkbox is checked; 
      * when checked, the Delivery is included on the Production Calendar
      * see spec for Production Calendar regarding logic for which Delivery records are included on the Calendar)
    * Will Call (optional; checkbox; with the following behaviors: 
      * editable only by Users with the "Manage Delivery Scheduling" Permission;
      * defaults to unchecked; 
      * used to communicate that the Customer will call when they're ready for the delivery; 
      * when checked, the following fields are affected, and the Delivery is included in the "Will Call" grouping on the Production Calendar: 
        * "Schedule Date" is cleared; 
        * "Scheduled" checkbox is unchecked; 
      * error on the field if the checkbox is checked while the Delivery is linked to an Order record with "Status" = "Quote": "Deliveries for Quotes cannot be added to the Production Calendar.";
      * automatically unchecks if the Schedule Date field is filled or if the "Scheduled" checkbox is checked)
    * Schedule Date (date field; defaults to the current date; with the following behaviors: 
      * editable only by Users with the "Manage Delivery Scheduling" Permission;
      * required if "Scheduled" checkbox is checked, otherwise is optional; 
      * when manually set, the following field(s) are affected: 
        * "Will Call" checkbox is unchecked; 
      * note that setting this date does not check the "Scheduled" checkbox;
      * if blank, automatically sets to the current date when Scheduled checkbox is checked;
      * if "Quote / Order #" is not blank, sets to the Delivery / Pickup Date on the linked record;
      * if linked to a record with "Status" = "Quote", is read-only, automatically updating every time the Quote record is saved;
      * if linked to a record with "Status" = "Order", is editable, automatically updated one final time on the first save after "Status" was set to "Order")
    * Customer (optional; drop list of all Contacts; includes an ellipsis button beside to to view / create Contact; defaults to blank;
      * if "Quote / Order #" is not blank, sets to the Customer on the linked record;
      * if linked to a record with "Status" = "Quote", is read-only, automatically updating every time the Quote record is saved;
      * if linked to a record with "Status" = "Order", is editable, automatically updated one final time on the first save after "Status" was set to "Order") 
    * Job Name (optional; plain text field; defaults to blank; 
      * if "Quote / Order #" is not blank, sets to the Job Name on the linked record;
      * if linked to a record with "Status" = "Quote", is read-only, automatically updating every time the Quote record is saved;
      * if linked to a record with "Status" = "Order", is editable, automatically updated one final time on the first save after "Status" was set to "Order") 
    * Area (optional; plain text field; defaults to blank; 
      * if "Quote / Order #" is not blank, sets to the "City, ST" from the linked record;
      * if linked to a record with "Status" = "Quote", is read-only, automatically updating every time the Quote record is saved;
      * if linked to a record with "Status" = "Order", is editable, automatically updated one final time on the first save after "Status" was set to "Order") 
    * Item (required; plain text field; defaults to blank; 
      * if "Quote / Order #" is not blank, sets to the Quantity + Description of the top item from the Truss RG on the linked record;
      * if linked to a record with "Status" = "Quote", is read-only, automatically updating every time the Quote record is saved;
      * if linked to a record with "Status" = "Order", is editable, automatically updated one final time on the first save after "Status" was set to "Order") 
    * Lum Pkg (optional; checkbox; defaults to unchecked; 
      * if "Quote / Order #" is not blank, sets to checked if the "Lumber Order" checkbox on the linked record is checked;
      * if linked to a record with "Status" = "Quote", is read-only, automatically updating every time the Quote record is saved;
      * if linked to a record with "Status" = "Order", is editable, automatically updated one final time on the first save after "Status" was set to "Order") 
    * Mtl Pkg (optional; checkbox; defaults to unchecked; 
      * if "Quote / Order #" is not blank, sets to checked if the "Metal Order" checkbox on the linked record is checked;
      * if linked to a record with "Status" = "Quote", is read-only, automatically updating every time the Quote record is saved;
      * if linked to a record with "Status" = "Order", is editable, automatically updated one final time on the first save after "Status" was set to "Order") 
    * Time (optional; plain text field)
    * Info (optional; plain text field)
    * Starlight (optional; checkbox; defaults to unchecked)
    * Priority (optional; checkbox; defaults to unchecked)



  


  * Logistics section (located to the right of the Delivery section):
    * Trailer (optional; drop list of Delivery Trailers)
    * Other Trailer (optional; plain text field; disappears if a selection is made in the Trailer drop list)
    * Trucker (optional; drop list of all active Contacts with type = Trucker)
    * Travel Time (optional; number field allowing 2 decimal places; defaults to blank; 
      * if "Quote / Order #" is not blank, sets to the Travel Time from the linked record;
      * if linked to a record with "Status" = "Quote", is read-only, automatically updating every time the Quote record is saved;
      * if linked to a record with "Status" = "Order", is editable, automatically updated one final time on the first save after "Status" was set to "Order") 
    * Available Hours (visible if a Trucker is selected; auto-set and read-only; displays the trucker's total available hours for the day, based on the Available Hours embedded spreadsheet on the Contact record; located beneath "Travel Time")
    * Remaining Hours (visible if a Trucker is selected; auto-set and read-only; takes the Available Hours for the day, subtracts the Travel Time for all other deliveries for that trucker that day, and subtracts the current delivery's Travel Time; located beneath "Available Hours"; displays in red if negative)
    * Legacy Trucker (formerly the original Trucker field; optional; visible and editable if non-blank; drop list of Truckers)
    * Other Trucker (visible if no Trucker is selected; optional; plain text field)
    * Board Feet (optional; number field)



  


  * Production Hours section (located below the Logistics section):
    * Production Hours (optional; plain next field)



  


  * Status section (located to the right of the Logistics section):
    * Set (optional; checkbox; defaults to unchecked; toggles with "Drop" checkbox)
    * Drop (optional; checkbox; defaults to unchecked; toggles with "Set" checkbox)
    * Permit (optional; checkbox; defaults to unchecked)
    * Escort (optional; checkbox; defaults to unchecked)
    * Called (optional; checkbox; defaults to unchecked; includes a date field that defaults to the current date when the checkbox is checked)
    * Confirmed (optional; checkbox; defaults to unchecked; includes a date field that defaults to the current date when the checkbox is checked)
    * Made (optional; checkbox; defaults to unchecked; includes a date field that defaults to the current date when the checkbox is checked)
    * Status (auto-set and read-only; displays the following:
      * if Made checkbox is unchecked: In Progress;
      * if Made checkbox is checked and the Schedule Date is the current date or in the future: Made
      * if Made checkbox is checked and the Schedule Date is in the past: Delivered)



  


  * Cost section (located to the right of the Status section):
    * Small Truck (optional; checkbox; defaults to unchecked; with the following behaviors: 
      * if "Quote / Order #" is not blank, sets to checked if the Small Truck checkbox on the linked record is checked;
      * if linked to a record with "Status" = "Quote", is read-only, automatically updating every time the Quote record is saved;
      * if linked to a record with "Status" = "Order", is editable, automatically updated one final time on the first save after "Status" was set to "Order") 
    * Delivery $ (optional; number field; 0 decimals; defaults to blank) 
    * Permits $ (optional; number field; when filled, automatically checks the "Permit" checkbox; 0 2 decimals; defaults to blank)
    * Escorts $ (optional; number field; when filled, automatically checks the "Escort" checkbox; 0 2 decimals; defaults to blank)
    * Overnights $ (optional; number field; 0 decimals)
    * Miles (optional; number field)



  


Data Access: 

  * Visible to all users



  


Special Considerations:  

  * Copy Record: Copy all fields for any Status
  * Delete Record: N/A
  * Merge Record: N/A



  


Other Notes:

  * Include a "Production Calendar" button in the record header that leaves the current record and takes the user to the Production Calendar.
  * Note that time will not be tracked for "Other Trucker".
  * Note that this record includes a link to access Modification History.
  * Edits made to a Delivery record are not reflected onto the linked Order record.



  


Development Specification

CHANGE REQUESTS:

  * Tim Reitz 07/20/2024: [[[IN9790](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9792&)]] - ZTD - Delivery Record & Calendar - Changes to Travel Time (prev. Changes to Hours fields)
  * Ben Reitz 10/30/2024: [[[IN8901](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8903&)]] - ZTD - Adding Hours fields to Production Calendar
  * Ben Reitz 05/08/2025: [[[IN10789](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10791&)]] - ZTD - Allow for linking Orders and Deliveries
  * Ben Reitz 05/08/2025: [[[IN10788](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10790&)]] - ZTD - Delivery record - Allow copying Delivery records
  * Ben Reitz 05/08/2025: [[[IN11274](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11276&)]] - ZTD - Order / Delivery linking - Change behavior based on "Scheduled" checkbox
  * Ben Reitz 11/26/2025: [[[IN11979](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11981&)]] - ZTD - Add new "Clipboard Sheet" printout


