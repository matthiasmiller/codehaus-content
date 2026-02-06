3.3.3.2. Vehicle - Cargo Section

  


Requirements

*Documented. Tim Reitz 08/19/2025

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Cargo section (visible if Cargo coverage is active or the selected Vehicle Type uses Cargo coverage):

  * Coverage (number; two decimals; required if Status is Active; editable if the coverage is not active and the vehicle is not in the process of being transferred to a new owner)
  * Premium (number; two decimals; auto-calculated and read-only)
    * 0.00 if No-Charge is set to "Yes"
    * Otherwise, Coverage multiplied by the Cargo Premium % for the selected vehicle type
    * Otherwise, displays the full annual premium for the entered Coverage amount, based on the Plan-specific Cargo Premium format for the Solution (Flat Rate only or Percentage only or Flat Rate + Percentage), as configured in the System Switches)
  * Status (auto-set and read-only; Active or Inactive; based upon Activation Date and Deactivation Date)
  * Activation Date (date; editable for admin and the owner's agent if cargo coverage is not active and the vehicle is not in the process of being transferred to a new owner; clears Deactivation Date when set) 
  * Deactivation Date (date; editable for admin and the owner's agent if an Activation Date is entered and the vehicle is not in the process of being transferred to a new owner)
  * Date Entered (uneditable; set by the Activate button)
  * Current Period (label)
    * Start Date (auto-calculated and read-only; displays 07/01/yyyy; the current year if the date is later than July 1, otherwise the previous year)
    * End Date (auto-calculated and read-only; displays 06/01/yyyy, the year is the year of the start date incremented by one)
  * Next Period (label)
    * Start Date (auto-calculated and read-only; displays Current Period Start Date incremented by one year)
    * End Date (auto-calculated and read-only; displays Current Period End Date incremented by one year)
  * Activate (button; visible for admin and the owner's agent if Activation Date is not blank and the vehicle has not yet been activated and the vehicle is not in the process of being transferred to a new owner and Coverage is not zero; see the corresponding process in the Background Processes section)
  * Deactivate (button; visible for admin and the owner's agent if the vehicle is not in the process of being transferred to a new owner and Cargo Coverage is not equal to zero and Deactivation Date is not blank; see the corresponding process in the Background Processes section)



  


Validation:

  * Error on change: if Coverage is negative.
    * Error Message: ""Cargo coverage" cannot be negative."
  * Warning on change: if Activation Date is set and Coverage is equal to zero.
    * Message: "Cargo coverage amount should be greater than 0."
  * Error on change: if Activation Date is prior to Deactivation Date.
    * Message: "Activation date must be after the last deactivation date <VehicleCargoDeactivationDate>.
  * Error on change: if Deactivation Date is prior to Activation Date.
    * Message: "Deactivation date must not be prior to the activation date."
  * Error on change: if Deactivation Date is more than 180 days in the future.
    * Message: "Deactivation date must be within 180 days from today."
  * Warning on change: if Deactivation Date is not blank and is modified. 
    * Message: "Reminder: Changes to the Deactivation Date should be documented in the Notes."



  


Development Specification

Ellis Miller 09/05/2024:  Nothing to code. This change will happen in calculations.
