5.3.1.1. Vehicle Owner and Status Section - Main Fields

  


Requirements

*Done. 

  


  * Left Side: 
    * Status (read-only macro; displays "Active" if the Vehicle has any active coverage (Liability, <Collision>, or Cargo); otherwise displays "Inactive")
    * Owner (with with following details / behaviors:
      * for a new Vehicle record (prior to the initial Save):
        * required;
        * drop-list of active non-snoozed Client-type Contacts;
      * after the initial Save:
        * non-editable link to the Contact record;
        * can be changed via the "Transfer Vehicle" feature)
    * Owner's Agent (read-only macro; dynamically displays the current Agent for the "Owner") 



  


  * Owner's Primary Contact (visible if "Owner" is an Organization; read-only macro; displays the "Primary Cont." on the Organization Contact record) 
  * "This organization does not have a primary contact." (visible if the "Owner" is an Organization and "Primary Cont." for the Organization is blank; on-screen message in red text) 



  


  * Transfer Vehicle (visible in Edit Mode after the initial Save if "Vehicle Transfer Mode" = "No"; button; with the following details / behaviors:
    * when clicked, sets the hidden "Vehicle Transfer Mode" field to "Yes", which opens the "Transfer Vehicle On-Screen Prompt" \- see corresponding spec; 
    * error on the button when clicked if the Vehicle has one or more active coverages with "Deactivation Date" in the past: "This vehicle has one or more active coverages with the Deactivation Date set in the past. Please deactivate the corresponding coverage(s) or clear the Deactivation Date(s) before proceeding.") 
  * Vehicle Transfer Mode (hidden field; with the following details / behaviors:
    * is set to "Yes" by the "Transfer Vehicle" button (making the transfer fields visible); is set to "No" by the "Cancel Transfer" button (hiding the transfer fields) - see corresponding specs;
    * error on Save if the Vehicle is in the middle of being transferred (specifically, if this field = "Yes", meaning that the transfer has not been canceled or completed): "Vehicle cannot be saved when transfer is in progress."; this prevents data from being saved in the transfer fields) 



  


  * Right Side: 
    * Date Entered (auto-set and read-only; date field; on the initial Save, sets to the date the record was created) 
    * Prior Owner (visible if the Vehicle has been transferred to a new owner; auto-set and read-only; is set to the prior owner as part of the "Transfer Vehicle" actions) 
    * Prior Owner's Agent (visible if the Vehicle has been transferred to a new owner; read-only macro, dynamically displays the current Agent for the "Prior Owner") 
    * No-Charge Vehicle (optional; drop-list of "Yes" / "No"; with the following details / behaviors:
      * defaults to "No"; 
      * determines whether the Vehicle is a N/C vehicle, which provides free coverages to the Owner;
      * error on Save if = "Yes" and the Owner is not allowed to have N/C Vehicles (specifically, if "Maximum Number of No-Charge Vehicles" = "0" for the Owner's Contact Type: "The vehicle owner is not allowed to have a no-charge vehicle.";
      * error on Save if = "Yes" and the Owner has reached the "Maximum Number of No-Charge Vehicles" for their Contact Type: "This cannot be a no-charge vehicle because the vehicle owner has already reached the maximum number of allowed no-change vehicles.")



  


Development Specification

Change Requests: 

  * Tim Reitz 08/23/2025: [[[IN9943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9945&)]] - ZWA - Pre-ZWW - Vehicle Record - Fees & Credits - Add "Dismiss" Option for Fees
  * 


  


TODO_CCI: Tim Reitz 08/20/2025: [error on the Transfer Vehicle button] Is this based on the hidden VehicleTransferModeIsActive field, or something else?

Sagar Sagar 12/10/2025: I am guessing you are saying about "This vehicle has one or more active coverages with the Deactivation Date set in the past...." error. This validation on Transfer Vehicle button is based on the coverage and deactivation date. If there is any coverage that is active and also there is a deactivation date for this coverage which is before today then you will see this validation.

  


TODO_: Tim Reitz 08/06/2025: how can we be more specific about the wording that we use for the activate / deactivate coverages specs for all 3 coverage types: "is not in the process of being transferred to a new owner"? What specific field is set in that case? 

Tim Reitz 08/20/2025: Maybe something like "is not in the process of being transferred to a new owner" (specifically if "Vehicle Transfer Mode" = "No")"
