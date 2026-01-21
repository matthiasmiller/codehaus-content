17.0.0.1. Vehicle - Transferring Ownership Process Sub-section

  


Requirements

Who can initiate a transfer:

  * All agents can transfer a vehicle for their own client.
  * Admins can transfer a vehicle for any client.



  


  


Transferring Ownership

In the Vehicle Owner and Status section, there is a Transfer Vehicle button (see corresponding spec). When the button is clicked, several prompt fields are made visible:

  * Cancel Transfer (button; visible in the location of the "Transfer Vehicle" button; if clicked, the below items are hidden again and any data that was entered in them is cleared, and the "Transfer Vehicle" button is visible again (replacing the "Cancel Transfer" button))
  * New Owner (required; drop-list of active Client-type Contacts; defaults to blank) 
  * No-Charge Vehicle for New Owner (required; drop list of Yes/No; defaults to the vehicle's current No-Charge state) 
  * Transfer coverage to household member (required; drop list of Yes/No; defaults to blank) 
  * Collision Coverage for New Owner? (required drop list of Yes/No; defaults to blank; only visible if the prior owner has active Collision coverage)
  * New Collision Coverage (visible and required if the "Collision Coverage for New Owner?" prompt is set to "Yes"; number field to defaults to the current Collision Coverage amount
  * Confirm (button; cannot be clicked if any of the above required prompt fields are blank - error on the button)



  


DONE_NM: Tim Reitz 07/22/2024: Spec out the automatic process & move to its own section (like ZSB/ZET proposals). 

When the "Confirm" button is clicked, and all prompts above are filled in, it applies the following changes to the record (but the changes are not saved yet):

  * Vehicle Owner is set to the "New Owner" selection.
  * Prior Owner is set to the name of the previous "Vehicle Owner".
  * Primary Driver is set to the Primary Driver for the new owner.
  * Agent is set to the agent of the new owner.
  * License Plate is blanked out.
  * A row is added to the Deactivation History spreadsheet for the current date and the new "Prior Owner". 
  * All of the rows in the Fees and Credits embedded spreadsheet linked to the new "Prior Owner" are displayed in gray text.
  * The Guideline Compliance embedded spreadsheet is reset. 
  * If the new "Prior Owner" has any uninvoiced fees/credits, the following are displayed (visible only to Admin users):  
    * The "prior owner has a credit/balance" message is displayed a message is displayed ("Previous owner <Name> has a credit/balance of $<posititive or negative amount>."). 
    * The "Create Invoice" button is displayed beside the message. 
  * New row(s) are added to the Fees and Credits embedded spreadsheet for Entry/Premium fees for the new owner (see details below).
  * All coverage-specific deactivation dates are cleared.



  


After the Confirm button is clicked and before the record is saved:

  * All activate/deactivate buttons are hidden.
  * All fields in the coverage sections are read-only.
  * All fields in the Vehicle Owner and Status section are read-only.
  * The transfer button and prompts are hidden.



  


The transfer becomes effective when the user saves the Vehicle record.

  * When the vehicle is transferred to a household member of the previous owner, active coverages are not changed.
  * When the vehicle is transferred to a non-household member, the Deactivate button is triggered for any active coverages to create the appropriate credits and blank out all coverage information.



  


  


Transferring Liability coverage:

In the Fees and Credits spreadsheet:

For household transfer:

  * A row is added for the new owner with a $0 amount.



For non-household transfer:

  * A row is added for the new owner with remaining prorated amount for the current period.



  


In the Coverage History spreadsheet:

For non-household transfer:

  * A row is added for the prior owner with Used status.
  * A row is added for the new owner with Active status.



  


In the Deactivation History table:

For non-household transfer:

  * A row is added for the prior owner with the current date.



  


  


Transferring Collision coverage:

When Collision Coverage for New Owner? is set to "No":

  * The coverage becomes inactive for the new owner.



 

  


When Collision Coverage for New Owner? is set to "Yes":

In the Fees and Credits spreadsheet:

For Household transfer:

  * A row is added for entry fee for the new owner with a $0 amount.
  * A row is added for premium for the new owner with a $0 amount.
  * The active coverage rows for the prior owner are displayed in gray text.



For Non-Household transfer:

  * A row is added for entry fee for the new owner with full amount (5 years).
  * A row is added for premium for the new owner with remaining prorated amount for the current period
  * The rows for prior owner and collision coverages turns gray colored.
  * The rows for prior owner have negative amounts for both entry fee and premium. Default credit option is "Refund".



  


In the Coverage History spreadsheet:

For Non-Household transfer

  * The Status is "Used" for rows of prior owner.
  * A row is added with "Active" status for the new owner.



  


In the Deactivation History spreadsheet:

For Non-Household transfer

  * A row is added for the prior owner with the current date.



  


  


Transferring Cargo coverage:

  * Cargo Premium and Entry Fee are never transferred.



  


  


Transferring a No-Charge vehicle:

Prior Owner No-Charge + New Owner No-Charge

  * For increased collision coverage, there will be no extra charge.
  * There will be no credit rows for the collision entry fee or the cargo coverage.



  


Prior Owner No-Charge + New Owner Charge

  * For increased collision coverage, there will be an extra charge.
  * There will be no credit rows for the collision entry fee or the cargo coverage for the prior owner.



  


Prior Owner Charge + New Owner Charge

  * For increased collision coverage, there will be an extra charge.
  * There will be credit rows for the collision entry fee or the cargo coverage for the prior owner. 



  


Prior Owner Charge + New Owner No-Charge

  * For increased collision coverage, there will be no extra charge.
  * There will be credit rows for the collision entry fee or the cargo coverage for the prior owner.



  


  


Transferring an inactive vehicle:

  * No new row is added in the Deactivation History table.



  


Development Specification

TODO_DEV: Could/should VehicleTransferConfirmBtnIsClicked be a detail variable instead of a field?

  


TODO_: Tim Reitz 07/22/2024: I think we should consider whether more should be hidden / made read-only.'

Niccolas Miller 08/01/2024: That is, whether more fields should be uneditable or hidden when an ownership transfer is in process.
