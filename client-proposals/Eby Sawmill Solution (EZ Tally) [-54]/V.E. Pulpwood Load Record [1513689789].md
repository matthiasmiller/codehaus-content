5.5. Pulpwood Load Record

  


Requirements

Overview: This record is used to track Pulpwood Loads.

  


Accessed via: The Pulpwood Loads report

  


Sections and Fields: 

  * Status (displayed in the header of the record; displays the following:)  
    * Unpaid: If no "Paid" checkboxes are checked 
    * Partially Paid: If both "Paid" checkboxes are visible and only one is checked 
    * Paid: If all visible "Paid" checkboxes are checked 



  


  * Pulpwood Load section: 
    * Tract (required; drop list of Tract Names for all Tracts with Status = "Harvest Started")
    * Load ID (auto-numbered and sequential, starting at 100001; read-only; unique identifier) 
    * Landowner(s) (visible if Source = Tract; auto-filled and read-only based on selected Tract; comma-separated list; same as on the Yard Tally) 
    * Landowner Pulpwood Rate (auto-set and read-only; displays the Landowner Pulpwood Rate from the selected Tract for the selected Logger; value is copied in when the Tract is selected on the Pulpwood Load; this value does not change if edited on the Tract, but does change if the Tract is changed on the Pulpwood Load)
    * Logger (required; drop list of Logger-type contacts for this Tract; if there is only one Logger for the Tract, auto-fill to that Logger)
    * Logger Pulpwood Rate (auto-set and read-only; displays the Logger Pulpwood Rate from the selected Tract for the selected Logger; value is copied in when the Logger is selected on the Pulpwood Load; this value does not change if edited on the Tract, but does change if the Logger is changed on the Pulpwood Load)
    * Date Processed (required; default to blank)
    * Location (required; drop list of Pulpwood Locations included on the Pulpwood Prices table for the selected Tract; if there is only one Location for the Tract, auto-fill to that Location; if there are no Locations for the Tract, the user should add to the Pulpwood Prices table)
    * Pulpwood Price/Ton (auto-set and read-only; displays the Pulpwood Price/Ton from the selected Tract for the selected Location; value is copied in when the Tract is selected on the Pulpwood Load; this value does not change if edited on the Tract, but does change if the Tract is changed on the Pulpwood Load)
    * Tons (required; number to 2 decimals)
    * Amount (dollar amount; number to 2 decimals; auto-calculated and read-only; Tons * Pulpwood Location Price)
    * Notes (plain text field)



  


  * Payments section (like the Payments section on the Yard Tally, this section is laid out in a table-like format, with a row for each Payment type and a column for each field type): 
    * Rows: 
      * Landowner (label; label and row visible if Purchase Type for the selected Tract = Adjustable Tiered Percentages; if Purchase Type = Flat Payments, the landowner-related fields are hidden since the Landowner does not receive payment for pulpwood) 
      * Logger (label; label and row are always visible, since Pulpwood Loads are always tied out to a Logger) 



  


  * Columns
    * Amount (dollar amount; number to 2 decimals; auto-set and read-only; this is the amount that is added to the Payment record) 
      * For Landowner: Tons * Landowner Pulpwood Rate
      * For Logger: Tons * Logger Pulpwood Rate 
    * Payment ID (auto-set and read-only; displays as a link to open the corresponding Payment record;
      * if an "Open Unpaid" Payment record exists for the Type + Tract + Payee , this is set or cleared on Save (see details below);
      * if no "Open Unpaid" Payment exists, set via the "Create Payment" link (see details below); 
      * auto-linking details:
        * For Landowner: on the first Save after the Landowner field is set, this sets to the corresponding "Open Unpaid"; 
        * For Logger: on the first Save after the Logger field is set, sets to the corresponding "Open Unpaid") 
      * validate against saving if the Payment ID is blank (to avoid having the item linked back to the same Payment in the event that the Payment is the "Open Unpaid" one) -- error message on Save: "Payment ID cannot be blank since it was previously set. Select a Payment or create & set a new one to continue."; 
      * validate against saving if attempting to link to a Paid Payment - error message on Save: "This item cannot be linked to the selected Payment, as it has been marked as Paid." 
      * Note: This is similar, but not identical, to the Payment ID field on the Yard Tally record) 
    * Select Payment (button; displays as an ellipsis button to the right of the Payment ID; visible in Edit Mode if the Pulpwood Load Status is not "Paid" and (if the item is already linked to a Payment) if the Status of the linked Payment is not "Paid"; opens the "Select Payment Choice Report" as a child screen -- see corresponding details in the Yard Tally section of the proposal / living spec) 
    * Create Payment (link; visible with the first Save after Landowner or Logger (as applicable) is set, in the location of the Payment ID, if there is no "Open Unpaid" Payment record for the same Type + Tract + Payee; clicking this link runs the "Create and Link All Payments" background process to create a new Payment record and link the Pulpwood Load record to it; 
      * Note that after clicking this button, a manual refresh of the Pulpwood Load page is needed to allow further editing of the page and to display the new Payment ID; 
      * Note: This is like the Create Payment link on the Yard Tally record) 
    * Check # (auto-set and read-only; from the corresponding Payment record; wide enough for 6 digits)
    * Paid (checkbox; auto-set and read-only; from the corresponding Payment record)
    * Payment Date (auto-set and read-only; from the corresponding Payment record
    * Payee (auto-set and read-only; displays the Payee for the corresponding Payment record when a Payment is linked; link to open the corresponding Contact's record)



  


Data Access: 

  * View record: For users with the View Tracts, Yard Tallies, and Pulpwood Loads permission
  * Edit and Delete record: For users with the Edit All Pulpwood Loads permission



  


Special Considerations: 

  * Copy Record: Disallow copying 
  * Delete Record: Disallow deleting the record if Status = Partially Paid or Paid -- validation error message: "This record cannot be deleted because its status is Partially Paid or Paid." 
  * Merge Record: Disallow merging 



  


Other Notes:

  * Tract Status: The Status will be set automatically based on the following criteria:
    * Quote: If "Contract Signed" = blank (this is the default status on creation of the Tract record)
    * Archived: If "Contract Signed" = "No"
    * Contract Signed: If "Contract Signed" = "Yes"
    * Harvest Started: If "Contract Signed" = "Yes" and the "Harvest Start Date" checkbox is checked
    * Harvest Paused: If "Contract Signed" = "Yes" and the "Harvest Pause Date" checkbox is checked
    * Harvest Complete: If "Contract Signed" = "Yes" and the "Harvest End Date" checkbox is checked
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Change Requests: 

  * Tim Reitz 08/31/2024: [[[IN10286](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10288&)]] - ZET - Pulpwood Load Record - Improve "Tract" Drop List
  * Tim Reitz 10/07/2024: [[[IN10236](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10238&)]] - ZET - Rework Payment Linking
  * 


  


  


  


Mockup:

  


  


Tim Reitz 11/15/2023: Added in [[[IN8780](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8782&)]] - ZET - Add Pulpwood Loads Record & Report (and related / subsequent jobs).
