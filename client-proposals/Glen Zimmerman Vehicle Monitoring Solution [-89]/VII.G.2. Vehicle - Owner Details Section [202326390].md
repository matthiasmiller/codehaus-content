7.7.2. Vehicle - Owner Details Section

  * Owner Details section: 



  


  * Current Owner (read-only macro; this can be used to track the owner of a Vehicle, especially in situations where the Owner is different from the Account Manager; with the following details / behaviors: 
    * if "End Date" is blank for the top row of the "Owner History" embedded spreadsheet: displays the "Owner" from the top row; 
    * otherwise (i.e. if there are no rows, or if the top row has a non-blank "End Date"): displays "(None specified)") 
  * Current Owner Start Date (read-only macro; displays the "Start Date" from the top row on the "Owner History" embedded spreadsheet)



  


  * Change / Clear Owner (visible to and editable for "All Provider Roles" users; button; with the following details / behaviors: 
    * when clicked, the following field(s) are affected: 
      * "Change Owner Mode": sets to checked, which causes the "Change Owner On-Screen Prompt" to become visible - see corresponding specs) 
  * Cancel Owner Change (button; visible in the location of the "Change / Clear Owner" button if "Change Owner Mode" checkbox is checked; with the following behaviors / details:
    * when clicked, the following field(s) are affected: 
      * "Change Owner Mode": sets to not checked, which causes the "Change Owner On-Screen Prompt" to be hidden, causing the data entry fields to be cleared)  
  * Change Owner Mode (hidden; checkbox; with the following details / behaviors:
    * set to checked (making the "Change Owner On-Screen Prompt" data entry fields visible) via the "Change / Clear Owner" button;
    * set to unchecked (hiding the data entry fields) via the "Cancel Owner Change" button and the "Confirm Owner Change" button - see corresponding specs;
    * error on Save if this checkbox is checked: "Vehicle cannot be saved while Owner Change is in progress."; this prevents data from being saved in the data entry fields) 



  


  * Change Owner On-Screen Prompt:
    * Clear Owner (visible if the "Change Owner Mode" checkbox is checked) 
    * New Owner (visible if the "Change Owner Mode" checkbox is checked and "Clear Owner" on-screen prompt is not checked; required; drop list of "Display Names" for all Contacts in the Solution) 



_NM: Tim Reitz 12/09/2025: Easy to include an item at the top of the list for "(None specified)"? Thinking of times when a client's vehicle gets sold to someone outside the service and we no longer want to track a specific owner. 

_NM: Tim Reitz 12/09/2025: Or, should we just have them go to the RG and set the "End Date"?? That's a different workflow from what we're doing elsewhere in the software, so I'm not excited about it, but we could do it if it's enough simpler...

Tim Reitz 12/10/2025: Add a button for "End Ownership" or "Clear Current Owner" or ??, which opens a prompt for "End Date" and "Confirm" sets the End Date for the top row.

_NM: Tim Reitz 01/14/2026: I'd like to avoid adding another on-screen prompt here. Thoughts on adding a "Clear Owner" checkbox on the existing on-screen prompt? See purple spec here.

TODO_VA: Tim Reitz 01/15/2026: Per Nic, this is good. Clean up the spec. 

  * New Owner Start Date (visible if the "Change Owner Mode" checkbox is checked and "Clear Owner" on-screen prompt is not checked; required; date; defaults to the current date) 
  * Confirm Owner Change (visible if the "Change Owner Mode" checkbox is checked; button; with the following details / behaviors: 
    * error on the button if clicked when "Clear Owner" on-screen prompt is not checked and "New Owner" and/or "New Owner Start Date" is blank: "New Owner and Start Date are required to change the owner."; 
    * when clicked with the required data entry fields are filled, the following happen: 
      * "End Date" for the existing top row in the "Owner History" embedded spreadsheet: sets to the value in "New Owner Start Date"; 
      * if "Clear Owner" on-screen prompt is not checked: a new row is added to the "Owner History" embedded spreadsheet, with the following set: 
        * "Owner": sets to the current value in "New Owner"; 
        * "Start Date": sets to the value in "New Owner Start Date"; 
      * "Change Owner Mode": sets to not checked; 
      * the "Owner has been been changed..." on-screen message appears - see corresponding spec) 



  


  * Owner has been changed. Confirm whether License Plate and Vehicle Name also need to change. (on-screen message in orange font; visible until the first Save after "End Date" has been set for the top row of the "Owner History" embedded spreadsheet; note that this covers both clearing the current owner and changing to a new owner) 



  


  * Owner History (embedded spreadsheet of the following; visible to "All Provider Roles" users:
    * Columns: 
      * Owner (required; drop list of "Display Names" for all Contacts in the Solution; sets based on the "New Owner" data entry field when a row is added) 
      * Start Date (required; date; with the following details / behaviors:
        * sets based on the "New Owner Start Date" data entry field when a row is added; 
        * includes the following validation(s): 
          * cannot be set to a date earlier than any "End Date" on the embedded spreadsheet - error on the field: "Start Date cannot be before any End Date") 
      * End Date (date; with the following details / behaviors: 
        * defaults to blank for new rows; 
        * includes the following validations: 
          * required if another row exists with a "Start Date" later the the "Start Date" for the current row - error on Save: "End Date is required for Owner "<Display Name>""; 
          * cannot be set to a date earlier than the "Start Date" for the same row - error on the field: "End Date cannot be before Start Date for the same row.") 
      * View Contact (link; displays as "Link"; opens the corresponding Contact record)
    * Automatically sorted by: Start Date (latest at the top) 
    * Buttons to add/remove rows: N/A (rows are automatically added & removed)
    * Shows 4 rows without scrolling
    * Additional Validations:
      * Warning on Save after a new row has been added if there are any rows on the "Vehicle Photos" embedded spreadsheet: "Current Owner has been changed. Make changes to Vehicle Photos as needed."; 
    * Other Notes: 
      * see spec on the "Current Owner" editable macro for details about how rows are added and how fields are set; 
      * on every Save, the Solution checks this embedded spreadsheet, and removes any rows where "Start Date" = "End Date" for the same row; this eliminates duplicate rows when "Current Owner" is changed multiple times in the same day, since there is not a need to retain multiple Owners with the same "Start Date" as it normally would only happen by mistake)


