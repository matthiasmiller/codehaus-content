3.3.3.1. Vehicle - <Collision> Section

  


Requirements

*Documented. Tim Reitz 08/19/2025

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


<Alternate text for Collision - Long label> section (visible if the Vehicle Type uses <Collision> coverage or if <Collision> coverage is active):

  * Coverage (number; two decimals; only editable if <Collision> coverage is not activated)
  * Premium (number; two decimals; auto-calculated and read-only; displays the full annual premium for the entered Coverage amount, based on the Plan-specific <Collision> Premium format for the Solution (Flat Rate only or Percentage only or Flat Rate + Percentage), as configured in the System Switches)
  * Status (auto-set and read-only; Active or Inactive; based upon Activation Date and Deactivation Date)
  * Activation Date (date; editable for admin and the owner's agent if <Collision> coverage is not active and the vehicle is not in the process of being transferred to a new owner; clears Deactivation Date when set) 
  * Deactivation Date (date; editable for admin and the owner's agent if an Activation Date is entered and the vehicle is not in the process of being transferred to a new owner)
  * Date Entered (uneditable; set by the Activate button)
  * Current Period (label)
    * Start Date (auto-calculated and read-only; displays 07/01/yyyy; the current year if the date is later than July 1, otherwise the previous year)
    * End Date (auto-calculated and read-only; displays 06/01/yyyy, the year is the year of the start date incremented by one)
  * Next Period (label)
    * Start Date (auto-calculated and read-only; displays Current Period Start Date incremented by one year)
    * End Date (auto-calculated and read-only; displays Current Period End Date incremented by one year)
  * Activate (button; visible for admin and the owner's agent if Activation Date is not blank and the vehicle has not yet been activated and the vehicle is not in the process of being transferred to a new owner and Coverage is not zero; see the corresponding process in the Background Processes section)
  * Deactivate (button; visible for admin and the owner's agent if the vehicle is not in the process of being transferred to a new owner and <Collision> Coverage is not equal to zero and Deactivation Date is not blank; see the corresponding process in the Background Processes section)



  


Additional Validations:

  * Warning on change: if Coverage is equal to zero.
    * Message: "<Alternate text for Collision - Long label> coverage amount should be greater than 0."
  * Warning on save: if Vehicle Loss Sharing coverage is active and Coverage exceeds the limit for the subtype.
    * Message: "The <Alternate text for Collision - Long label> Coverage Amount on this vehicle exceeds the limit set for this Subtype. (Field: Coverage)"
  * Error on save: if Vehicle Loss Sharing coverage is not active and Coverage exceeds the limit for the subtype.
    * Message: ""Max <Alternate text for Collision - Long label> coverage amount for "Personal Vehicle" is <amount>"
  * Error on change: if Activation Date is more than one year in the past or more than one day in the future.
    * Message: "The entered date cannot be more than one year ago."
  * Warning on change: if an Activation Date is entered and Coverage is equal to zero.
    * Message: "<Alternate text for Collision - Long label> coverage amount should be greater than 0."
  * Error on change: if Activation Date is prior to Deactivation Date.
    * Message: "Activation date must be after the last deactivation date <deactivation date>.
  * Error on change: if Deactivation Date is prior to Activation Date.
    * Message: "Deactivation date must not be prior to the activation date."
  * Error on change: if Deactivation Date is more than 180 days in the future.
    * Message: "Deactivation date must be within 180 days from today."
  * Warning on change: if Deactivation Date is changed. 
    * Message: "Reminder: Changes to the Deactivation Date should be documented in the Notes."



  


Development Specification

Ellis Miller 09/05/2024:  Nothing to code. This change will happen in calculations.
