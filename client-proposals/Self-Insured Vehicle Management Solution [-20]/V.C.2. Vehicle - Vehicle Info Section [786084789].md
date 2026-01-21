5.3.2. Vehicle - Vehicle Info Section

  


Requirements

*Done. 

  


  * Vehicle Info section:



Left side:

  * Vehicle Type (drop-list of active Vehicle Types; with the following behaviors / details: 
    * required if the Vehicle is active (i.e. if one or more Coverages are active); 
    * editable if the Vehicle is inactive (i.e. if no Coverages are active); 
    * if changed to a new Vehicle Type that requires a VIN and "VIN" is blank and "Serial #" is not blank, the following fields are affected: 
      * "VIN": is set to the value of "Serial #"; 
      * "Serial #": is cleared; 
    * if changed to a Vehicle Type that does not require a VIN and "Serial #" is blank and "VIN" is not blank, the following fields are affected: 
      * "Serial #": is set to the value of "VIN"; 
      * "VIN": is cleared; 
    * when changed (regardless of VIN requirements), the following field(s) are affected: 
      * "Subtype": is cleared; 
      * "Guidelines Compliance" embedded spreadsheet: rows are added or removed, based on the selected "Vehicle Type" and the "Guidelines Compliance Questions" configuration in Silverloom Settings) 
  * Subtype (visible if the selected "Vehicle Type" uses Subtypes; drop list of Subtype items from the selected "Vehicle Type; with the following behaviors / details:
    * editable if blank or if there are no active Coverages for the Vehicle (becomes read-only as soon as an "Activate" button is clicked for a coverage);
    * when set, the following field(s) are affected: 
      * "Guidelines Compliance" embedded spreadsheet: rows are added, based on the selected "Subtype" and the "Guidelines Compliance Questions" configuration in Silverloom Settings; 
    * warning on Save if blank and the selected "Vehicle Type" has "Uses Subtypes" checked and has at least one row in the "Subtypes" embedded spreadsheet and the Vehicle has at least one active Coverage: "This vehicle does not have a Subtype.";
    * warning on Save if the Vehicle has active <Collision> Coverage exceeds the limit for the selected Subtype (i.e. if the "Max <Collision> Coverage Amount" is lowered on the Subtype when a higher amount already exists on a vehicle with that Subtype): "The <"Alternate text for Collision - Long label"> Coverage Amount on this vehicle exceeds the limit set for this Subtype."



  


  * Year (required; number; with the following additional behaviors / details:
    * the entered value must match the VIN year, if applicable - error on Save: "The VIN year is <Year 1> or <Year 2>, but the vehicle year is <Year 3>. Please contact an administrator to assign a non-standard VIN.";
    * error message on the field if an invalid value is entered: "Please enter a valid year.")
  * Make (editable macro; required; drop list of "Vehicle Make" list items) 
  * Model (editable macro; required; drop list of "Vehicle Model" list items, filtered to include ones that have been used for the selected "Make")



  


  * Serial # (visible if the selected "Vehicle Type" does not have the "Requires VIN" checkbox checked; with the following behaviors / details: 
    * optional; 
    * plain text field that accepts numbers and letters; 
    * any letters entered in lower case are automatically capitalized; 
    * no validation against duplicates) 
  * VIN (visible if the selected "Vehicle Type" does have the "Requires VIN" checkbox checked: with the following behaviors / details: 
    * required; 
    * plain text field that accepts numbers and letters;  
    * any letters entered in lower case are automatically capitalized;  
    * read-only for non-Admin users if the "Non-Standard VIN - Admin-Only" checkbox is checked; 
    * includes the following "VIN validating" validations (based on the guidelines specified at [https://en.wikipedia.org/wiki/Vehicle_identification_number](https://en.wikipedia.org/wiki/Vehicle_identification_number)): 
      * the VIN must be 17 digits long - error on Save: "The VIN should be 17 digits long. Please contact an administrator to assign a non-standard VIN."; 
      * the letters "I", "O", and "Q" must not be used in any part of the VIN - error on Save: "The following letters are not valid VIN characters: I, O, Q. Please contact an administrator to assign a non-standard VIN.";
      * the following characters may not be used in the 10th digit of the VIN: "U", "Z", "0" (zero) - error on Save: "<character> is not a valid VIN year code. Please contact an administrator to assign a non-standard VIN."; 
      * the check digit (the 9th digit) must be correct - error on Save: "The entered VIN is not valid. Please contact an administrator to assign a non-standard VIN."; 
    * when set, the following field(s) are affected:  
      * "VIN Validated": checkbox is checked if all "VIN validating" validations for the "VIN" field are met; unchecked if any of the criteria are not met; 
    * additional validations: 
      * the entered "Year" for the Vehicle record must match the VIN year - error on Save: "The VIN year is <Year 1> or <Year 2>, but the vehicle year is <Year 3>. Please contact an administrator to assign a non-standard VIN."; 
        * note that the the "Year" may be subsequently changed to a different year after the VIN has been set, without additional validation errors; 
      * for vehicles created manually in the system, the same VIN may not be used for multiple vehicles in the system - error on Save: "This VIN has already been entered for another vehicle.";  
      * for vehicles created via import, there is a warning (not an error) on Save for vehicles with duplicate VINs: "This VIN has already been entered for another vehicle."; 
      * if the entered "Year" for the Vehicle record is "1982" or earlier, there are no validations (warnings or errors) for the entered VIN except for duplicate VIN validations; 
      * if the "Non-Standard VIN - Admin-Only" checkbox is filled, there are no validations (warnings or errors) for the entered VIN except for the duplicate VIN validations) 
  * VIN Validated (visible if the selected "Vehicle Type" has the "Requires VIN" checkbox checked; checkbox; with the following details / behaviors: 
    * auto-set and read-only; 
    * is automatically checked if the "VIN" field is set to a value that meets all of the "VIN validating" validation criteria - see corresponding spec; 
    * note that this does not take the "Year", "Make", or "Model" fields into account, so if those are set to values that do not match the entered VIN information, this checkbox remains checked as long as the VIN validation criteria are met) 
  * Non-Standard VIN - Admin-Only (checkbox; with the following behaviors / details:
    * visible and editable for Admin users if the selected "Vehicle Type" has the "Requires VIN" checkbox checked;
    * visible for non-Admin users if checked;
    * checking this checkbox makes the VIN field read-only for non-Admin users; 
    * checking this checkbox suppresses most of the usual validations on the VIN/Serial # field, with the exception of the validation against duplicate VINs)  
  * View Vehicle Details (visible if "VIN Validated" is checked; link; opens the URL specified in the "VehicleVINDecoderURL" System Switch, with the VIN for the current Vehicle passed through)
  * View / Create Claims (link; prompts the user to save the record, then opens the "All Claims" report, filtered to the current Vehicle)



  


  


Right side:

  * License Plate (plain text; with the following details / behaviors:
    * automatically removes dashes and auto-capitalizes lower-case letters;
    * warning on Save if blank and the selected "Vehicle Type" requires a license plate: "Vehicle license plate is missing.")
  * Vehicle Primary Driver (required; drop list of "Household Drivers" for the selected Owner, and an option for "(Other/Non-household Driver)")
  * New Household Driver (button; prompts the user to save the record before opening the "Add New Household Driver" child screen - see corresponding spec below) 
  * Other Driver First Name (visible and required if "Vehicle Primary Driver" = "Other/Non-household Driver"; plain text; error on Save if visible and blank: ""Other Driver First Name" is a required field.")
  * Middle Name (visible if "Vehicle Primary Driver" = "Other/Non-household Driver"; plain text) 
  * Last Name (visible and required if "Vehicle Primary Driver" = "Other/Non-household Driver"; plain text; error on Save if visible and blank: ""Last Name" is a required field.")
  * Other Driver DOB (visible if "Vehicle Primary Driver" = "Other/Non-household Driver"; date; warning on Save if visible and blank and the Vehicle "Status" = "Active": "Other Driver DOB is missing.")



  


  * "New Household Driver" Child Screen (includes the following):
    * Close (button; closes the child screen when clicked)
    * First Name (required; plain text)
    * Middle Name (plain text)
    * Last Name (required; plain text; defaults to the last name of the Vehicle Owner)
    * Date of Birth (date)
    * Notes (multi-line plain text)
    * Run Import (button; when clicked, the "Add New Household Driver" automatic process runs, to add a row to the "Household Drivers" embedded spreadsheet on the Owner's Contact record with the entered details - see corresponding spec)



  


Development Specification

TODO_CR: Tim Reitz 08/22/2025: For the "Add New Household Driver" child screen, let's change the run button text from "Run Import" to "Confirm New Household Driver" (using a word from [HS0000836](https://clientscope.invtools.com/Detail/View/2?RecordType=HelpDrafts&NumberID=-853&State=XPSMmJcy76s&_=X3eXw& "https://clientscope.invtools.com/Detail/View/2?RecordType=HelpDrafts&NumberID=-853&State=XPSMmJcy76s&_=X3eXw&")). 

Alternatively, we could see about adding "Add" to the list, and change this button to "Add New Household Driver"...

  


TODO_: Tim Reitz 08/22/2025: For "Make" and "Model", let's work on speccing out the full story better -- it looks like the visible controls on the screen are macros, with hidden fields. I'd like to get the full spec at some point, but what we have specced now should work. Would need input from CCI. 

  


Change Requests: 

  * Austin Priest 02/21/2023: [[[IN7494](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-7496&)]] - ZWA - Admin-only checkbox for Non-Standard VINs 
  * Tim Reitz 06/03/2025: [[[IN11415](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11417&)]] - ZWA - Pre-ZWI? - Vehicle - Clean Up "Subtype" Validation
  * Tim Reitz 08/23/2025: [[[IN9943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9945&)]] - ZWA - Pre-ZWW - Vehicle Record - Fees & Credits - Add "Dismiss" Option for Fees
  * Tim Reitz 08/23/2025: [[[IN11238](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11240&)]] - ZWA - Pre-ZWW - Clean up various validations


