5.3.5. Vehicle - Cargo Section

  


Requirements

*Done. 

  


  * Cargo section (visible if Cargo coverage is active or the selected Vehicle Type uses Cargo coverage):
    * Coverage (number; two decimals; Coverage (number; two decimals; with the following details / behaviors:
      * editable if Cargo Coverage "Status" = "Inactive" and if the vehicle is not in the process of being transferred to a new owner;
      * required if Cargo Coverage "Status" = "Active";
      * includes the following validation(s):
        * error on the field if negative: ""Cargo coverage" cannot be negative.")
    * Premium (ead-only macro; number; 2 decimals; with the following details / behaviors:
      * if "No-Charge Vehicle" = "Yes": displays "0.00"; 
      * otherwise, displays the full annual premium for the entered Coverage amount, based on the following: 
        * the Plan-specific Cargo Premium format for the Solution (Flat Rate only, or Percentage only, or Flat Rate + Percentage), as configured in the System Switches; 
        * the Cargo-related fields on the selected Vehicle Type record, depending on their visibility & settings: 
          * Cargo Entry Fee %; 
          * Cargo Premium $; 
          * Cargo Premium %) 
    * Cargo Coverage Is Active (hidden field; sets to "Yes" when the "Activate" button is clicked for the coverage; sets to "No" when the "Deactivate" button is clicked for the coverage) 
    * Status (read-only macro; displays "Active" if "Cargo Coverage Is Active" = "Yes"; displays "Inactive" if "Cargo Coverage Is Active" = "No") 



  


  * Activation Date (date; with the following details / behaviors:
    * editable for Admin users and the Owner's current Agent if the following conditions are all true:
      * there is no active Cargo coverage and 
      * the Vehicle is not in the process of being transferred to a new owner;
    * when set, the following other field(s) are affected:
      * "Deactivation Date": clears;
    * includes the following validations:
      * error on the field if more than one day in the future: "Activation date cannot not be a future date past tomorrow."; 
      * error on the field if more than one year in the past: "The entered date cannot be more than one year ago."; 
      * warning on the field if set when "Coverage" = "0.00": "Cargo coverage amount should be greater than 0.";
      * error on the field if set to a date prior to "Deactivation Date": "Activation date must be after the last deactivation date <Deactivation Date>.";
      * error on Save if not blank and the corresponding coverage is not active: "Inactive coverage(s) with activation date must be activated or must have the date removed.") 
  *  Activate (button;  with the following details / behaviors:
    * visible to the "Owner's Agent" and all Admin users if the following conditions are all true:
      * Cargo coverage is not active and 
      * "Activation Date" is not blank and 
      * "Coverage" ≠ "0.00" and 
      * the Vehicle is not in the process of being transferred to a new owner;
    * error on the button if clicked when "Coverage" = blank: Cargo coverage cannot be blank.";
    * when clicked, the Cargo Coverage is activated - see the details in the "Activate Coverage Actions" portion of this spec; 
    * error on the button if the user user attempts to activate coverage on a Vehicle that has no Subtype but is of a Vehicle Type that requires it: "Error: "Subtype" is a required field.")



  


  


  * Deactivation Date (date; with the following details / behaviors:
    * editable for Admin users and the Owner's current Agent if the following conditions are all true:
      * Cargo coverage is active and 
      * the Vehicle is not in the process of being transferred to another owner;
    * includes the following validations:
    * error on the field if set to a date prior to "Activation Date": "Deactivation date must not be prior to the activation date.";
    * error on the field if set to a date more than 180 days in the future: "Deactivation date must be within 180 days from today.";
    * warning on change if changed from a saved non-blank value to blank or another date: "Reminder: Changes to the Deactivation Date should be documented in the Notes.";
    * warning on Save if not blank and <Collision> coverage is still active: "The cargo coverage will NOT be automatically renewed at the end of the current period.")
  * Deactivate (button; with the following details / behaviors: 
    * visible to the "Owner's Agent" and all Admin users if the following conditions are all true:
      * the Vehicle is not in the process of being transferred to a another owner and 
      * "Deactivation Date" is not blank and 
      * "Coverage" ≠ "0.00"; 
    * when clicked, the Cargo coverage is deactivated - see the details in the "Deactivate Coverage Actions" portion of this spec) 



  


  * Date Entered (auto-set and read-only; date; auto-sets to the current date when the "Activate" button is clicked) 



  


  * Current Period (static label for the following two dates) 
  * Start Date (underlying name is "Current Period Start Date"; read-only macro; displays the first date of the current Period Year in the M/D/YYYY format) 
  * End Date (underlying name is "Current Period End Date"; read-only macro; displays the last date of the current Period Year in the M/D/YYYY format) 
  * Next Period (static label for the following two dates) 
  * Start Date (underlying name is "Next Period Start Date"; read-only macro; displays the first date of the upcoming Period Year in the M/D/YYYY format) 
  * End Date (underlying name is "Next Period Start Date"; read-only macro; displays the last date of the upcoming Period Year in the M/D/YYYY format)



  


Development Specification

TODO_CR: Tim Reitz 08/22/2025: Capitalize "cargo" in the following warning for the Deactivation Date field: "The cargo coverage will NOT be automatically renewed at the end of the current period."

  


Change Requests: 

  * Tim Reitz 08/19/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident


