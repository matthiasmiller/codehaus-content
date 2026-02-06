8.5.3.1. Primary Driver Fields

*Done. 

  


  * Primary Driver (editable macro; with the following details / behaviors:
    * editable if "Account" ≠ blank;
    * required if "Device Status" ≠ "Decommissioned" or "Lost";
    * drop list of "Display Name" values for all Drivers for the current Account;
    * displays:
      * if there is no row in the "Primary Driver History" non-embedded spreadsheet or if there is at least one row and "End Date" for the top row is blank: displays blank;
      * if there is at least one row in the "Primary Driver History" non-embedded spreadsheet and "End Date" for the top row is not blank: displays the value in the "Primary Driver" field for the top row;
    * when set to either blank or non-blank, the following field(s) are affected on change:
      * the following is set on the top existing row of the "Primary Driver History" non-embedded spreadsheet: 
        * "End Date": if blank, sets to the current date; 
    * when set to non-blank, the following happen to the "Primary Driver History" non-embedded spreadsheet on change: 
      * a new row is added, with the following set:
        * "Primary Driver": sets to the Contact selected here;
        * "Start Date": sets to the current date;
      * note that a new row is not added if "Primary Driver" is set to blank
    * on the first Save after this is set to either blank or non-blank, the following thing(s) happen:
      * data synced with Traccar via the Traccar Device sync record; 



TODO_VA: Tim Reitz 02/04/2026: trigger work: on Save (Traccar's "Driver" field); 

  * on the first Save after this is set to non-blank, the following things happen:
    * the "Send "Primary Driver Change" Email" triggered automatic process runs, to send the "Primary Driver Change" Email - see corresponding specs;
  * note that additional details (validations, etc.) will need to specced out for the Subscription Management feature (Phase 2))



  


  * Age (read-only macro; number; 1 decimal; displays the "Age" for the selected Contact)
  * Address (read-only macro; displays the primary Address for the selected Contact)
  * Phone (read-only macro; displays the primary Phone Number for the selected Contact)
  * Email (read-only macro; displays the primary Email Address for the selected Contact) 
  * New Contact (visible if "Primary Driver" is blank; link; opens a blank new Contact record)
  * View/Edit Contact (visible if "Primary Driver" ≠ blank; link; opens the linked Contact record) 
  * Primary Driver Change Comments (label displays as "Primary Driver Change Comments (included in the emails to the Primary Account Manager and the new Primary Driver)"; editable macro; memo; with the following details: 
    * visible until the first Save after "Primary Driver" is changed from a saved non-blank value; 
    * required;
    * displays / sets the "Primary Driver Change Comments" memo field for the new row on the "Primary Driver History" non-embedded spreadsheet)



  


  * Primary Driver History (button; opens the "Primary Driver History Child Screen" - see corresponding spec) 



  


  


  * Primary Driver History Child Screen (contains the following: 
    * Primary Driver History (non-embedded spreadsheet with the following: 
      * Columns: 
        * Primary Driver (auto-set and read-only; list field of "Display Name" items for all individual Contacts; automatically sets from the "Primary Driver" macro on the main screen - see corresponding spec) 
        * Start Date (auto-set and read-only; date; automatically sets to the current date when the row is added via the "Primary Driver" macro) 
        * End Date (auto-set and read-only; date; required if the row is not the top row; is always blank for the top row unless "Primary Driver" is set to blank, and automatically sets to the current date when "Primary Driver" is changed - see corresponding spec) 
        * Primary Driver Change Comments (button; opens a lightbox screen with an auto-set and read-only memo field; automatically set from the "Primary Driver Change Comments" editable macro - see corresponding spec; the contents here are included in the "Primary Driver Change" Email - see corresponding spec) 
      * Automatically sorted by: "Start Date" (most recent at the top) 
      * Buttons to add/remove rows: N/A (rows are automatically added & removed) 
      * Shows 6 rows without scrolling
      * Other Notes: 
        * see spec on the "Primary Driver" editable macro for details about how rows are added and how fields are set; 
        * on every Save, the Solution checks this embedded spreadsheet, and removes any rows where "Start Date" = "End Date" for the same row; this eliminates duplicate rows when "Primary Driver" is changed multiple times in the same day, since there is not a need to retain multiple Primary Drivers with the same "Start Date", as it would normally would only happen by mistake)


