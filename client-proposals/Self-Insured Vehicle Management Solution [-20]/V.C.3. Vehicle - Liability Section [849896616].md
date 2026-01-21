5.3.3. Vehicle - Liability Section

  


Requirements

*Done. 

  


  * Liability section (visible if the selected "Vehicle Type" has the "Uses & Requires Liability Coverage" checkbox checked, or if there is active Liability coverage (note that the latter can be true in cases where the checkbox is unchecked on the Vehicle Type while there is still at least one Vehicle with active Liability coverage): 



  


  * Vehicle Type (read-only macro; dynamically displays the selection in the "Vehicle Type" field)
  * Classes (visible and required if the selected "Vehicle Type" has the "Uses Classes" checkbox checked; number; no decimals; with the following details / behaviors:
    * editable there is no active Liability coverage; 
    * if this is set to a number higher than the "Included Classes #" for the selected Vehicle Type, an additional fee is assessed with the Liability Premium, based on the "Additional Classes $" for the Vehicle Type)
  * Premium (read-only macro; number; 2 decimals; with the following details / behaviors:
    * if "No-Charge Vehicle" = "Yes": displays "0.00"; 
    * if the selected "Vehicle Type" has "Uses Classes" not checked: displays the "Premium Amount $" for the Vehicle Type;
    * if the the selected "Vehicle Type" has "Uses Classes" checked:
      * if the number in "Classes" for the Vehicle is less than or equal to the number in "Included Classes #" for the Vehicle Type: displays the "Premium Amount $" for the Vehicle Type;
      * if the number in "Classes" for the Vehicle is greater than the number in "Included Classes #" for the Vehicle Type: displays the sum of the following: <"Premium Amount $" for the Vehicle Type> \+ <<# of extra Classes> * <"Additional Classes $" for the Vehicle Type>>)
  * Liability Coverage Is Active (hidden field; sets to "Yes" when the "Activate" button is clicked for the coverage; sets to "No" when the "Deactivate" button is clicked for the coverage) 
  * Status (read-only macro; displays "Active" if "Liability Coverage Is Active" = "Yes"; displays "Inactive" if "Liability Coverage Is Active" = "No") 



  


  * Activation Date (date; with the following details / behaviors:
    * editable for Admin users and the Owner's current Agent if there is no active Liability coverage and if the vehicle is not in the process of being transferred to a new owner; 
    * when set, the following other field(s) are affected:
      * "Deactivation Date": clears;
    * includes the following validations:
      * error on the field if more than one day in the future: "Activation date cannot not be a future date past tomorrow."; 
      * error on the field if more than one year in the past: "The entered date cannot be more than one year ago."; 
      * error on the field if set to a date prior to "Deactivation Date": "Activation date must be after the last deactivation date <Deactivation Date>." (i.e. to prevent reactivating a Vehicle to a date earlier than the most recent Deactivation Date);
      * warning on Save if "Activation Date" is in the months of May or June and the current date is after "Activation Date" and the current date is not in May or June: "Liability coverage has been renewed for the current period automatically. Please print insurance cards for both the prior and current periods."; 
      * warning on Save if both "Activation Date" and the current date are in the months of May or June of the same calendar year: "Liability coverage has been renewed for the upcoming period automatically. Please print insurance cards for both the current and upcoming periods.";
      * error on Save if not blank and the corresponding coverage is not active: "Inactive coverage(s) with activation date must be activated or must have the date removed.") 
  * Activate (button; with the following details / behaviors:
    * visible to the "Owner's Agent" and all Admin users if the Vehicle is not in the process of being transferred to a new owner and Liability coverage is not active and "Activation Date" is not blank;
    * when clicked, the Liability Coverage is activated - see the details in the "Activate Coverage Actions" portion of this spec; 
    * error on the button if the user user attempts to activate coverage on a Vehicle that has no Subtype but is of a Vehicle Type that requires it: "Error: "Subtype" is a required field.")



  


  * Deactivation Date (date; with the following details / behaviors:
    * editable for Admin users and the Owner's current Agent if Liability coverage is active and if the Vehicle is not in the process of being transferred to another owner;
    * includes the following validations:
      * error on the field if not within 180 days of the current date: "Deactivation date must be within 180 days from today.";
      * error on the field if before "Activation Date": "Deactivation date must not be prior to the activation date."
      * warning on the field if changed from a non-blank date: "Reminder: Changes to the Deactivation Date should be documented in the Notes.")
  * Deactivate (button; with the following details / behaviors: 
    * visible to the "Owner's Agent" and all Admin users if the vehicle is not in the process of being transferred to a new owner and "Deactivation Date" is not blank and Liability coverage is active; 
    * when clicked, the Liability Coverage is deactivated - see the details in the "Deactivate Coverage Actions" portion of this spec)



  


  * Date Entered (auto-set and read-only; date; auto-sets to the current date when the "Activate" button is clicked) 
  * Current Period (static label for the following two dates) 
  * Start Date (underlying name is "Current Period Start Date"; read-only macro; displays the first date of the current Period Year in the M/D/YYYY format) 
  * End Date (underlying name is "Current Period End Date"; read-only macro; displays the last date of the current Period Year in the M/D/YYYY format) 
  * Next Period (static label for the following two dates) 
  * Start Date (underlying name is "Next Period Start Date"; read-only macro; displays the first date of the upcoming Period Year in the M/D/YYYY format) 
  * End Date (underlying name is "Next Period Start Date"; read-only macro; displays the last date of the upcoming Period Year in the M/D/YYYY format)



  


Development Specification

TODO_CR: Tim Reitz 08/22/2025: [applies to all 3 Coverage sections] Why do we have a separate macro for the current period start / end date, rather than displaying the values from Silverloom Settings? Would it be good to switch this, to centralize things more? And to add macros to Silverloom Settings for Next Period Start / End Dates as well? 

  


TODO_: Tim Reitz 08/22/2025: [applies to all 3 Coverage sections] Consider expanding the spec for the Start Dates and End Dates, to include how the displayed dates are being calculated.
