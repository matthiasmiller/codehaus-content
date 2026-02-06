8.6.2. Vehicle - Owner Details Section

  


Requirements

*. 

  


  * Owner Details section: 
    * Current Owner (read-only macro; this can be used to track the owner of a Vehicle, especially in situations where the Owner is different from the Account Manager; with the following details / behaviors: 
      * if "End Date" is blank for the top row of the "Owner History" embedded spreadsheet: displays the "Owner" from the top row; 
      * otherwise (i.e. if there are no rows, or if the top row has a non-blank "End Date"): displays "(None specified)") 
    * Current Owner Start Date (read-only macro; displays the "Start Date" from the top row on the "Owner History" embedded spreadsheet)



  


  * Change / Clear Owner (visible to and editable for "All Provider Roles" users; button; with the following details / behaviors: 
    * when clicked, the following field(s) are affected: 
      * "Change / Clear Owner Mode": sets to checked, which causes the "Change Owner On-Screen Prompt" to become visible - see corresponding specs) 
  * Cancel Owner Change (button; visible in the location of the "Change / Clear Owner" button if "Change / Clear Owner Mode" checkbox is checked; with the following behaviors / details:
    * when clicked, the following field(s) are affected: 
      * "Change / Clear Owner Mode": sets to not checked, which causes the "Change Owner On-Screen Prompt" to be hidden, causing the data entry fields to be cleared)  
  * Change / Clear Owner Mode (hidden; checkbox; with the following details / behaviors:
    * set to checked (making the "Change Owner On-Screen Prompt" data entry fields visible) via the "Change / Clear Owner" button;
    * set to unchecked (hiding and clearing the data entry fields) via the "Cancel Owner Change" button and the "Confirm Owner Change" button - see corresponding specs;
    * error on Save if this checkbox is checked: "Vehicle cannot be saved while Owner Change is in progress."; this prevents data from being saved in the data entry fields) 



  


  * Change Owner On-Screen Prompt:
    * Clear Owner (visible if the "Change / Clear Owner Mode" checkbox is checked) 
    * New Owner (visible if the "Change / Clear Owner Mode" checkbox is checked and the "Clear Owner" on-screen prompt is not checked; required; drop list of "Display Names" for all Contacts in the Solution) 
    * New Owner Start Date (visible if the "Change / Clear Owner Mode" checkbox is checked and the "Clear Owner" on-screen prompt is not checked; required; date; defaults to the current date) 
    * Confirm Owner Change (visible if the "Change / Clear Owner Mode" checkbox is checked; button; with the following details / behaviors: 
      * error on the button if clicked when the "Clear Owner" on-screen prompt is not checked and "New Owner" and/or "New Owner Start Date" is blank: "New Owner and Start Date are required to change the owner."; 
      * when clicked with the required data entry fields are filled, the following happen: 
        * "End Date" for the existing top row in the "Owner History" embedded spreadsheet: sets to the value in "New Owner Start Date"; 
        * if the "Clear Owner" on-screen prompt is not checked: a new row is added to the "Owner History" embedded spreadsheet, with the following set: 
          * "Owner": sets to the current value in "New Owner"; 
          * "Start Date": sets to the value in "New Owner Start Date"; 
        * "Change / Clear Owner Mode": sets to not checked; 
        * the "Owner has been been changed..." on-screen message appears - see corresponding spec) 



  


  * Owner has been changed. Confirm whether License Plate and Vehicle Name also need to change. (on-screen message in orange font; visible until the first Save after "End Date" has been set for the top row of the "Owner History" embedded spreadsheet; note that this covers both clearing the current owner and changing to a new owner) 



  


  * Owner History (visible to "All Provider Roles" users; embedded spreadsheet of the following:
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



TODO_VA (later): Tim Reitz 01/31/2026: Follow up here once the Vehicle Photos feature is finalized - minor spec adjustment might be needed (RG vs. memo). 

  * Other Notes: 
    * see spec on the "Current Owner" editable macro for details about how rows are added and how fields are set; 
    * on every Save, the Solution checks this embedded spreadsheet, and removes any rows where "Start Date" = "End Date" for the same row; this eliminates duplicate rows when "Current Owner" is changed multiple times in the same day, since there is not a need to retain multiple Owners with the same "Start Date" as it normally would only happen by mistake)



  


Development Specification

TODO_NM (review): Tim Reitz 01/31/2026: We're taking multiple (2?) different approaches for setting RG rows on different records. I'm wondering if we should make it more consistent. Details: 

  * Some places (like "Current Owner" / "Owner History" here), we have a read-only macro on the detail screen + button/on-screen prompts to add the RG rows. 
    * This is necessary (I think) for the "Account Reseller" on the Account record, since that requires confirmation before it officially takes effect. 
  * Other places (like "Primary Driver" / "Primary Driver History" on the Device record), we have an editable macro that adds the RG rows directly. 



Concerns from a coding or UI/UX perspective on having different approaches different places?
