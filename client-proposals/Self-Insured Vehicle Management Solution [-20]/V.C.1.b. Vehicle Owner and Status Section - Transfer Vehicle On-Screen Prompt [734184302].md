5.3.1.2. Vehicle Owner and Status Section - Transfer Vehicle On-Screen Prompt

*Done. 

  


The following are visible with a gray background when the "Transfer Vehicle" button is clicked (see corresponding spec):

  


  * Cancel Transfer (button; visible in the location of the "Transfer Vehicle" button if "Vehicle Transfer Mode" = "Yes"; when clicked, sets the hidden "Vehicle Transfer Mode" field to "No", which hides the below transfer-related items, and any data that was entered in them is cleared, and the "Transfer Vehicle" button is visible again (replacing the "Cancel Transfer" button))
  * New Owner (required; drop list; for admins, this includes all active Client-type Contacts; for non-admins, this includes only the clients of the current user; defaults to blank) 
  * No-Charge Vehicle for New Owner (required; drop list of "Yes" / "No"; defaults to the vehicle's current "No-Charge Vehicle" field) 
  * Transfer coverage to household member (required; drop list of "Yes" / "No"; defaults to blank) 
  * <"Alternate text for Collision - Short label" System Switch> Coverage for New Owner? (visible and required if Collision coverage is currently active for the vehicle; drop list of "Yes" / "No"; defaults to blank; only visible if the prior owner has active Collision coverage)
  * New <"Alternate text for Collision - Short label" System Switch> Coverage (visible and required if the "Collision Coverage for New Owner?" prompt = "Yes"; number; 2 decimals; defaults to the current Collision coverage "Coverage" amount)



  


  * Confirm (button; with the following details / behaviors:
    * cannot be clicked if any of the above required prompt fields are blank - error on the button: "<Field> cannot be empty." (displays the label of the top blank required field);
    * when clicked with all required prompts filled in, the following fields are affected on change (but the changes are not saved yet):
      * "Owner": is set to the "New Owner" selection;
      * "Prior Owner": is set to the name of the previous "Vehicle Owner";
      * "Primary Driver": is set to the "Primary Driver" for the new "Owner";
      * "License Plate": is cleared;
      * the "Guideline Compliance" embedded spreadsheet is reset (existing rows are removed and new rows are added, based on the "Vehicle Type" and "Vehicle Subtype");
      * Liability "Deactivation Date": is cleared;
      * Collision "Deactivation Date": is cleared; 
      * Cargo "Deactivation Date": is cleared; 
      * Liability "Activation Date": is set to the current date; 
      * Collision "Activation Date": is set to the current date if "<"Alternate text for Collision - Short label" System Switch> Coverage for New Owner?" = "Yes"; 
      * row(s) are added to the "Fees and Credits" embedded spreadsheet for Entry and Premium fees (as applicable) for the New Owner - see corresponding spec in "Transfer Vehicle Actions"; 
      * a row is added to the "Vehicle Coverage Deactivation History" embedded spreadsheet for the current date and the new "Prior Owner" - see corresponding spec in "Transfer Vehicle Actions";
    * from the time the button is clicked, until the first subsequent Save:
      * the "Transfer Vehicle" button and prompts are hidden; 
      * all coverage-specific "Activate" and "Deactivate" buttons are hidden; 
      * the following fields are read-only: 
        * all fields in the "Vehicle Owner and Status" section except "No-Charge Vehicle"; 
        * all fields in the "Liability" section if Liability Coverage was active for the Prior Owner (if it was not active for the Prior Owner, "Activation Date" is editable to allow the user to activate the Coverage before finalizing the transfer); 
        * all fields in the "<Collision>" section if <Collision> Coverage was active for the Prior Owner (if it was not active for the Prior Owner, "Coverage" and "Activation Date" are editable to allow the user to activate the Coverage before finalizing the transfer); 
        * all fields in the "Cargo" section except "Coverage" if Cargo Coverage was active for the Prior Owner (if it was not active for the Prior Owner, "Coverage" and "Activation Date" are editable to allow the user to activate the Coverage before finalizing the transfer); 
    * note that if the new "Prior Owner" has any uninvoiced items in the "Fees and Credits" embedded spreadsheet, the "Previous owner <Full Name> has a credit/balance..." message and the "Create Invoice" button become visible in the "Fees and Credits" section - see corresponding spec)


