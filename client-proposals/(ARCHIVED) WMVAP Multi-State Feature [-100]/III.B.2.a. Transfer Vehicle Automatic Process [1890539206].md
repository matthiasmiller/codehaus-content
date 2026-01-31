3.2.2.1. Transfer Vehicle Automatic Process

  


Requirements

*Documented. Tim Reitz 08/18/2025

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Transfer Vehicle Automatic Process: 

  


Overview: This process occurs when the user clicks the "Confirm" button in the "Transfer Vehicle" feature (in the "Vehicle Owner and Status" section of a Vehicle record). 

  


Who can initiate a transfer:

  * All agents can transfer a vehicle for their own client.
  * Admins can transfer a vehicle for any client.



  


Transferring Ownership: 

In the Vehicle Owner and Status section, there is a Transfer Vehicle button (see corresponding spec). When the button is clicked, several prompt fields are made visible:

  * Cancel Transfer (button; visible in the location of the "Transfer Vehicle" button; if clicked, the below items are hidden again and any data that was entered in them is cleared, and the "Transfer Vehicle" button is visible again (replacing the "Cancel Transfer" button))
  * New Owner (required; drop-list of active Client-type Contacts; defaults to blank) 
  * No-Charge Vehicle for New Owner (required; drop list of Yes/No; defaults to the vehicle's current No-Charge state) 
  * Transfer coverage to household member (required; drop list of Yes/No; defaults to blank) 
  * Collision Coverage for New Owner? (visible if the prior owner has active Collision coverage; required drop list of Yes/No/blank; defaults to blank)  
  * New Collision Coverage (visible and required if the "Collision Coverage for New Owner?" prompt is set to "Yes"; number field to defaults to the current Collision Coverage amount 
  * Confirm (button; cannot be clicked if any of the above required prompt fields are blank - error on the button)



  


When the "Confirm" button is clicked, and all prompts above are filled in, it applies the following changes to the record (but the changes are not saved yet):

  * Vehicle Owner is set to the "New Owner" selection.
  * Prior Owner is set to the name of the previous "Vehicle Owner".
  * Primary Driver is set to the Primary Driver for the new owner.
  * Agent is set to the agent of the new owner.
  * License Plate is blanked out.
  * A row is added to the Deactivation History spreadsheet for the current date and the new "Prior Owner". 
  * All of the rows in the Fees and Credits embedded spreadsheet linked to the new "Prior Owner" are displayed in gray text.
  * The Guideline Compliance embedded spreadsheet is reset, based on the current configuration of the Vehicle Type. 
  * If the new "Prior Owner" has any uninvoiced fees/credits, the following are displayed (visible only to Admin users):  
    * The "Previous owner has a credit/balance" message is displayed a message is displayed ("Previous owner <Name> has a credit/balance of $<positive or negative amount>."). 
    * The "Create Invoice" button is displayed beside the message. 
  * New row(s) are added to the Fees and Credits embedded spreadsheet for Entry/Premium fees for the coverages for the new owner, as applicable (see details below).
  * All coverage-specific deactivation dates are cleared.



  


While the full transfer is in progress (after the Confirm button is clicked but before the changes to the Vehicle record are saved):

  * All Activate/Deactivate buttons are hidden.
  * All fields in the Coverage sections are read-only.
  * All fields in the Vehicle Owner and Status section are read-only.
  * The transfer button and prompts are hidden.



  


The transfer becomes effective when the user saves the Vehicle record.

  * When the vehicle is transferred to a household member of the previous owner, active coverage amounts are not changed. Coverages are technically deactivated for the Prior Owner and reactivated for the New Owner, but no credits are generated for the Prior Owner.
  * When the vehicle is transferred to a non-household member, the Deactivate button is triggered for any active coverages to create the appropriate credits for the Prior Owner and blank out all coverage information, to start with a clean slate for the New Owner.



  


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

When "Collision Coverage for New Owner?" is set to "No":

  * The coverage becomes inactive for the new owner.
  * Refunds/credits are generated for unused portions of the old coverage. The rows for Prior Owner have negative amounts for both Entry Fee and Premium. Default credit option is "Refund".



 

When "Collision Coverage for New Owner?" is set to "Yes":

In the Fees and Credits spreadsheet:

For Household transfer:

  * If the Solution uses Collision Entry Fees: If the Vehicle had Collision coverage for the prior owner, a row is added for with Coverage Type = Collision and Fee Type = Entry Fee for the new owner with a $0 amount.
  * A row is added with Coverage Type = Collision and Fee Type = Premium for the new owner with a $0 amount.
  * The active coverages for the Prior Owner are made inactive for them, and all rows for the Prior Owner are displayed in gray text.
  * No refunds/credits are generated for the Prior Owner. 



For Non-Household transfer:

  * If the Solution uses Collision Entry Fees: A row is added Coverage Type = Collision and Fee Type = Entry Fee for the New Owner with full amount (5 years).
  * A row is added with Coverage Type = Collision and Fee Type = Premium for the New Owner with remaining prorated Premium amount for the current period (no Entry Fee is charged). 
  * The active coverages for the Prior Owner are made inactive for them, and all rows for the Prior Owner are displayed in gray text.
  * Refunds/credits are generated for unused portions of the old coverage. The rows for Prior Owner have negative amounts for both Entry Fee and Premium. Default credit option is "Refund".



  


In the Coverage History spreadsheet:

For Non-Household transfer

  * The Status is "Used" for rows of prior owner.
  * A row is added with "Active" status for the new owner.



  


In the Deactivation History spreadsheet:

For Non-Household transfer

  * A row is added for the prior owner with the current date.



  


Transferring Cargo coverage:

  * Cargo Premium and Cargo Entry Fee (if applicable) are never transferred.
  * Refunds/credits are generated for unused portions of the old coverage. The rows for Prior Owner have negative amounts for both Entry Fee and Premium. Default credit option is "Refund".



  


Transferring a No-Charge vehicle:

  * Prior Owner No-Charge + New Owner No-Charge
    * For increased Collision coverage, there will not be an extra charge.
    * There will be no credit rows for the Collision Entry Fee (if applicable) or the Cargo coverage for the prior owner.



  


  * Prior Owner No-Charge + New Owner Charge
    * For increased Collision coverage, there will be an extra charge.
    * There will be no credit rows for the Collision Entry Fee (if applicable) or the Cargo coverage for the prior owner.



  


  * Prior Owner Charge + New Owner No-Charge
    * For increased Collision coverage, there will not be an extra charge.
    * There will be credit rows for the Collision Entry Fee (if applicable) or the Cargo coverage for the prior owner.



  


Transferring an inactive vehicle:

  * No new row is added in the Deactivation History table.



  


Development Specification

Ellis Miller 09/04/2024: 

  


2 Days -- Pair Program

[ ] Note that this should be coded after all system switches are done. It should be tested with both settings of the system switch.

[ ] Also make sure that we respect switches both when activating/deactivating individual policies and when transferring ownership.
