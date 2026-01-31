7.6.3.2. Primary Vehicle Fields

  * Primary Vehicle (editable macro; with the following details / behaviors: 
    * editable if "Account" ≠ blank;
    * required if "Device Status" ≠ "Decommissioned" or "Lost";
    * drop list of "Vehicle Description" values for all Vehicle records;
    * displays:
      * if there is no row in the "Primary Vehicle History" non-embedded spreadsheet or if there is at least one row and "End Date" for the top row is blank: displays blank;
      * if there is at least one row in the "Primary Vehicle History" non-embedded spreadsheet and "End Date" for the top row is not blank: displays the value in the "Primary Vehicle" field for the top row;
    * when set to either blank or non-blank, the following field(s) are affected on change:
      * the following is set on the top existing row of the "Primary Vehicle History" non-embedded spreadsheet: 
        * "End Date": if blank, sets to the current date; 
    * when set to non-blank, the following happen to the "Primary Vehicle History" non-embedded spreadsheet on change: 
      * a new row is added, with the following set:
        * "Primary Vehicle": sets to the Vehicle selected here;
        * "Start Date": sets to the current date;
      * note that a new row is not added if "Primary Vehicle" is set to blank
    * on the first Save after this is set to either blank or non-blank, the following things happen:
      * ??data synced with Traccar on Save (Traccar's "Vehicle" field);



Done_JB (research): Tim Reitz 01/16/2026: Is there anything on the Traccar Device to link a VIN / Vehicle? If not, we'd just be doing the linking in Silverloom.

TODO_VA: Jonathan Bergen 01/21/2026: No, and I think we should rely on the link in Silverloom. If we want to have the vehicle info tied to it in Traccar, we could use the "name" field or add an "attribute" to the device to store this. [https://www.traccar.org/api-reference/#tag/Devices/paths/~1devices~1%7Bid%7D/put](https://www.traccar.org/api-reference/#tag/Devices/paths/~1devices~1%7Bid%7D/put)

  * on the first Save after this is set to either blank or non-blank, the following things happen:
    * the "Send "Primary Vehicle Change" Email" triggered automatic process runs, to send the "Primary Vehicle Change" Email Merge - see corresponding specs;
  * includes the following additional validations:
    * warning on Save if "Device Status" = "Decommissioned" and "Primary Vehicle" ≠ blank: "Confirm whether the linked Primary Vehicle's "Current Owner" should be changed.";
    * warning on Save if "Account" has been changed and "Primary Vehicle" has not been changed: "Confirm whether the linked Primary Vehicle's "Current Owner" should be changed.";
  * note that additional details (validations, etc.) will need to specced out for the Subscription Management feature (Phase 2)) 



  


  * VIN (read-only macro; displays the "VIN" for the selected Vehicle) 
  * Year (read-only macro; displays the "Year" for the selected Vehicle)
  * Make (read-only macro; displays the "Make" for the selected Vehicle)
  * Model (read-only macro; displays the "Model" for the selected Vehicle)
  * License Plate (read-only macro; displays the "License Plate" for the selected Vehicle)
  * View/Edit Vehicle (visible if "Primary Vehicle" ≠ blank; link; opens the linked Contact record) 
  * Primary Vehicle Change Comments (label displays as "Primary Vehicle Change Comments (included in the emails to the Primary Account Manager)"; editable macro; memo; with the following details: 
    * visible until the first Save after "Primary Vehicle" is changed from a saved non-blank value; 
    * required;
    * displays / sets the "Primary Vehicle Change Comments" memo field for the new row on the "Primary Vehicle History" non-embedded spreadsheet)



  


  * Primary Vehicle History (button; opens the "Primary Vehicle History Child Screen" - see corresponding spec) 



  


  


  * Primary Vehicle History Child Screen (contains the following: 
    * Primary Vehicle History (non-embedded spreadsheet with the following: 
      * Columns: 
        * Primary Vehicle (auto-set and read-only; list field of "Vehicle Description" values for all Vehicle records; automatically sets from the "Primary Vehicle" macro on the main screen - see corresponding spec) 
        * Start Date (auto-set and read-only; date; automatically sets to the current date when the row is added via the "Primary Vehicle" macro) 
        * End Date (auto-set and read-only; date; required if the row is not the top row; is always blank for the top row unless "Primary Vehicle" is set to blank, and automatically sets to the current date when "Primary Vehicle" is changed - see corresponding spec) 
        * Primary Vehicle Change Comments (button; opens a lightbox screen with an auto-set and read-only memo field; automatically set from the "Primary Vehicle Change Comments" editable macro - see corresponding spec; the contents here are included in the "Primary Vehicle Change" Email - see corresponding spec) 
      * Automatically sorted by: "Start Date" (most recent at the top) 
      * Buttons to add/remove rows: N/A (rows are automatically added & removed) 
      * Shows 6 rows without scrolling
      * Other Notes: 
        * see spec on the "Primary Vehicle" editable macro for details about how rows are added and how fields are set; 
        * on every Save, the Solution checks this embedded spreadsheet, and removes any rows where "Start Date" = "End Date" for the same row; this eliminates duplicate rows when "Primary Vehicle" is changed multiple times in the same day, since there is not a need to retain multiple Primary Vehicles with the same "Start Date", as it would normally would only happen by mistake)


