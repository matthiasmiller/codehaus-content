12.1.0.1. Vehicle - Vehicle Owner and Status Section

Tim Reitz 08/28/2024: I don't think there are any changes to this section at this point. Not sure why I copied it in. Archiving. 

  


Make the following changes (full spec included here, with changes notes with blue and strike-through): 

  


Vehicle Owner and Status:

  * Owner (with with following special behaviors:
    * for a new Vehicle record (prior to the initial Save: required; drop-list of active non-snoozed Client-type Contacts;
    * after the initial Save: non-editable link to the Contact record; can be changed via the Transfer Vehicle process)
  * Primary Contact (visible if owner is an Organization; auto-set and read-only; displays the Primary Contact on the Organization Contact record; dynamically updates if the Primary Contact is changed on the Organization)
  * Date Entered (auto-set and read-only; displays the date the record was created)
  * Prior Owner (auto-set and read-only; visible if the Vehicle has been transferred to a new owner; is set to the prior owner when the Transfer Vehicle process is completed)
  * Status (auto-set and read-only; Active or Inactive; displays "Active" if the vehicle has any active Liability, Collision, or Cargo coverage)
  * Transfer Vehicle (button; visible in Edit mode after the initial Save; opens the "Transferring Ownership Process Sub-section" \- see corresponding section of the proposal; also makes additional fields read-only while the sub-section is visible)
  * No-Charge Vehicle (optional; drop-list of Yes/No; defaults to "No"; determines whether the Vehicle is a N/C vehicle)



  


Validation:

  * Error on save: if the current user is not an agent for the vehicle's owner and attempts to save the record. "This vehicle does not belong to any of your clients and therefore cannot be saved."
  * Error on save: if the vehicle is being transferred to a new owner and there are uninvoiced credits or fees for the prior owner.
  * Error on save: No-Charge Vehicle is set to Yes and the owner is not allowed to have no-charge vehicles or has reached their maximum number of no-charge vehicles.
  * Error: if the Transfer Vehicle button is pressed and the vehicle has active coverages with the Deactivation Date in the past.



  


Other Notes:

  * A red label is displayed if the Owner is an organization and does not have a primary contact: "This organization does not have a primary contact."


