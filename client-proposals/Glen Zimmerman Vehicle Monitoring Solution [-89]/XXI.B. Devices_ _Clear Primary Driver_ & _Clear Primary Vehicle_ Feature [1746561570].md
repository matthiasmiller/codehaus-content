21.2. Devices: "Clear Primary Driver" & "Clear Primary Vehicle" Feature

  


Requirements

Overview: This is an optional add-on feature that can be added to the "Primary Driver & Vehicle" section of the Device record, to facilitate easy clearing of the "Primary Driver" and "Primary Vehicle" editable macros. 

  


"Clear Primary Driver": 

  


  * Clear Primary Driver (button; with the following details / behaviors:
    * visible in Edit Mode if "Primary Driver" ≠ blank; visible to "Upline Provider Roles" users for the linked Account; 
    * when clicked, the following field(s) are affected:
      * "Clear Primary Driver Mode": sets to checked, which makes the "Clear Primary Driver On-Screen Prompt" visible - see corresponding spec) 
  * Clear Primary Driver Mode (hidden; checkbox; with the following details / behaviors:
    * set to checked via the "Clear Primary Driver" button (making the data entry fields visible) and unchecked via the "Cancel" or "Confirm" buttons (hiding the transfer fields) - see corresponding specs; 
    * error on Save if this checkbox is checked: "Device cannot be saved while Clear Primary Driver is in progress."; this prevents data from being saved in the fields) 



  


  * Clear Primary Driver On-Screen Prompt:
    * Cancel (button; visible in the location of the "Clear Primary Driver" button if "Clear Primary Driver Mode" checkbox is checked, 
      * when clicked, the following field(s) are affected: 
        * "Clear Primary Driver Mode": sets to not checked, which makes the "Clear Primary Driver On-Screen Prompt" hidden, causing the data entry field(s) to be cleared)  
    * End Date (visible if "Clear Primary Driver Mode" checkbox is checked; date; defaults to the current date)
    * Confirm (visible if "Clear Primary Driver Mode" checkbox is checked; button; with the following details / behaviors: 
      * when clicked with required data entry field(s) filled, the following happen:
        * "End Date" for the top row in the "Primary Driver History" non-embedded spreadsheet: sets to the current date;
        * note that the "Primary Driver" macro on the main screen clears when "End Date" is set - see corresponding spec for the "Primary Driver" macro)



  


  


"Clear Primary Vehicle": 

  


  * Clear Primary Vehicle (button; with the following details / behaviors:
    * visible in Edit Mode if "Primary Vehicle" ≠ blank; visible to "Upline Provider Roles" users for the linked Account; 
    * when clicked, the following field(s) are affected:
      * "Clear Primary Vehicle Mode": sets to checked, which makes the "Clear Primary Vehicle On-Screen Prompt" visible - see corresponding spec)
  * Clear Primary Vehicle Mode (hidden; checkbox; with the following details / behaviors:
    * set to checked via the "Clear Vehicle Driver" button (making the data entry fields visible) and unchecked via the "Cancel" or "Confirm" buttons (hiding the transfer fields) - see corresponding specs; 
    * error on Save if this checkbox is checked: "Device cannot be saved while Clear Primary Vehicle is in progress."; this prevents data from being saved in the fields) 



  


  * Clear Primary Vehicle On-Screen Prompt:
    * Cancel (button; visible in the location of the "Clear Primary Vehicle" button if "Clear Primary Vehicle Mode" checkbox is checked, 
      * when clicked, the following field(s) are affected: 
        * "Clear Primary Vehicle Mode": sets to not checked, which makes the "Clear Primary Vehicle On-Screen Prompt" hidden, causing the data entry field(s) to be cleared)  
    * End Date (visible if "Clear Primary Vehicle Mode" checkbox is checked; date; defaults to the current date)
    * Confirm (visible if "Clear Primary Vehicle Mode" checkbox is checked; button; with the following details / behaviors: 
      * when clicked with required data entry field(s) filled, the following happen:
        * "End Date" for the top row in the "Primary Vehicle History" non-embedded spreadsheet: sets to the current date;
        * note that the "Primary Vehicle" macro on the main screen clears when "End Date" is set - see corresponding spec for the "Primary Vehicle" macro)



  


Development Specification

Tim Reitz 01/13/2026: If we add these, consider whether we should set a comments field (either the existing "Change" comments fields, or a new column with a "Cleared" field).
