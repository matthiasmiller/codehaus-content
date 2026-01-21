4.8.2.1. Device - Device Details Section

  


Requirements

  * Device Details section (visible for all Device records): 
    * Device Record ID (hidden; auto-number; unique identifier for the Device, since Description is not always unique and the visible Device ID can change) 



TODO_EM: Tim Reitz 08/22/2023: Are you good with this, or good with just using the visible Device ID as the unique identifier? 

  * Device Description (auto-set and read-only; used to identify Devices on lists and reports throughout the solution, using the following format: "<Device ID> \- <Numeric Model>"; this will auto-update if the Device ID changes; if a Device does not have a Device ID, i.e. if Status = Available or End of Life, this displays only the Numeric Model) 



  


  * Device ID (auto-filled and read-only; automatically sets on Save each time a new Customer is assigned to the Device record; uses the following convention for the ID:)
    * One or more prefixes:
      * "C" prefix if Type = Customer Printer
      * "L" prefix if Type = Leased Printer or Leased Other
      * "M" prefix if the Managed checkbox is checked (included after the "C" or "L" prefix)
    * Sequential numeric # (starting with 4 digits, i.e. "0001"; will roll over to 5 digits when needed; auto-number; shared between all Device Types)
      * Example: CM4021 (Customer-owned, Managed by Think Ink, number 4021)
  * Historical Device IDs (button; opens a child screen with the following embedded spreadsheet:) 
    * Columns: 
      * Customer (auto-set and read-only; filled when a new Customer is set on the record)
      * Install Date (auto-set and read-only; filled when the Install Date is changed)
      * Device ID (auto-set and read-only; filled when the Device ID is set on the record)
    * Automatically sorted by: N/A (retains the sequence in which the rows were added)
    * Button to remove rows (admin-only) ("-")
    * Show 4 rows without scrolling
    * Other Notes:
      * A row is added automatically when the record is saved following a change in the Customer field.
      * Rows can be deleted manually by an admin if needed. Note that this can result in reporting discrepancies, etc. 
      * Because historical IDs are being tracked, inactive / historical managed devices can be included in reporting (e.g. to view what devices a customer had in the past).



  


  * Model (required; drop list of active Device Models, displaying the Sales Item Descriptions; warning on Save if a Device is reactivated while its Model is inactive - "The Device Model for this device currently is inactive.") 
  * New Device Model (link; visible for Admin users if no Model is selected; opens a new blank Device Model record) 
  * View/Edit Model (link; visible for Admin users if a Model is selected; opens the corresponding Model record)



  


  * Device Type (required; drop list of Device Types; defaults to Customer Printer; validation error on Save if blank - "Device Type is required") 



  


  * Manged (checkbox; auto-checked and read-only if the "Always Managed" checkbox is checked on the selected Device Type; unchecked and editable if the "Always Managed" checkbox is not checked on the selected Device Type) 
  * Sold by Think Ink (visible if Device Type = Customer Printer; checkbox; defaults to checked) 



TODO_EM: Tim Reitz 08/18/2023: thoughts on these checkboxes? esp being based on the selected Type..

  


  * Needs Review (visible if Managed checkbox is checked; checkbox; see the details below)
  * Needs Review Reason(s) (visible if "Needs Review" checkbox is checked; auto-set and read-only; displays a comma-separated list of the reasons for checking the checkbox; see the details below)



TODO_EM: Ben Reitz 09/12/2023: Are you fine with this?

  * Needs Review Notes (visible if "Needs Review" checkbox is checked; optional; plain text field; used to document an explanation of why the checkbox is checked; defaults to blank, even for page count above/below average)



  


  * TI Purchase Date (visible and required if Device Type = Leased Printer or Leased Other; date; defaults to the current date)
  * Customer Purchase Date (visible and required if Device Type is or previously was Customer Printer; date; defaults to the current date)



  


  * Device Tags (multi-select drop list of Device Tag items for the corresponding Device Type)
  * Tags (button that opens a child screen displaying all selected Tags)
    * Embedded spreadsheet with the following:
      * Columns:
        * Tags (drop list of Device Tag items for the corresponding Device Type)
      * Automatically sorted by: N/A
      * Show 10 rows without scrolling
    * Buttons (displayed underneath the embedded spreadsheet):
      * \+ Insert Row ("+" is a green unicode character)
      * \+ Append Row ("+" is a green unicode character)
      * X Delete Row ("X" is a red unicode character)



  


  * Serial # (plain text field; long enough for 20 characters; required if the Managed checkbox is checked; for email accounts, this field should be set to the email address; error on Save if the same Serial # is already used on another Device: "This Serial # has already been used for another Device record.") 
  * Device Nickname (optional; plain text field; long enough for 20 characters; used to easily identify a printer in conversation with a customer) 
  * Device Status (required; drop list of Device Status items; defaults to blank for new records:)
    * Status details / automation:
      * Active: Option for all Device Types.
      * Available: Option if Device Type = Leased Printer or Leased Other; if changed to this status, "Customer" and "Device ID" are cleared.
      * End of Life: Option for all Device Types; if changed to this status, "Customer" and "Device ID" are cleared; if changed to this status, show a warning on Save: "Are you sure you want to deactivate this device?".
  * Customer (required if Device Status = Active; drop list of all Customer-type Contacts; filters down as you type)
  * Location (optional; plain text field)
  * Special Instructions (optional; single-line plain text; full width of section)
  * Service Incidents for Device (link; opens the Service Incidents report, filtered to this Device; see details in corresponding section of this proposal) 
  * All Incidents for Device (link; opens the Incidents by Device report, filtered to this Device; see details in corresponding section of this proposal)
  * Device Notes (memo; can be used for attaching documents such as a printer status PDF to the Device record)



  


  


Details for the Needs Review checkbox:

  * Automatically checked if one of the following is true:
    * If the number in the Black Pages Used field for an uninvoiced row in the Page Counts embedded spreadsheet is beyond the Above/Below % threshold (compared to the Average Black Usage for the Device).
      * Reason text: "Black Pages Used"
    * If the number in the Color Pages Used field for an uninvoiced row in the Page Counts embedded spreadsheet is beyond the Above/Below % threshold (compared to the Average Color Usage for the Device).
      * Reason text: "Color Pages Used"
    * If the Device is missing page counts when the billing process is started (i.e. if the device has no uninvoiced page counts row). 
      * Reason text: "Missing Page Counts"
    * If the Prepay End Date is in the past.
      * Reason text: "Prepay End Date"
  * Can be manually checked if there is any other reason that a Device needs review or should be withheld from being billed with a normal billing cycle.
    * Reason text: "Manual"
  * If checked, the Device and the whole Agreement that the Device is part of are not included in billing (so the checkbox must be cleared to be able to bill for the Agreement).
  * Always is manually unchecked.
  * When unchecked, does not automatically get checked again until the next time an abnormal row is added to the Page Counts embedded spreadsheet. 
  * See notes about the Above/Below % System Switch in the corresponding section of the proposal.



TODO_EM: Tim Reitz 08/31/2023: What do we need to spec out for background behavior to make all of this work?

  


Development Specification

Device Types:

  * Customer Printer
  * Leased Printer
  * Leased Other


