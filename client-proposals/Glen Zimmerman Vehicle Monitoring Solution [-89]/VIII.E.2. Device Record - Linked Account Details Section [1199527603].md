8.5.2. Device Record - Linked Account Details Section

  


Requirements

*Done. 

  


  * Current Account Details section: 
    * Account (editable macro; with the following details / behaviors: 
      * required if "Device Status" ≠ "Available" or "Decommissioned";
      * drop list of "Account #" items for all Accounts that meet the following criteria:
        * "Account Status" = "In Setup" or "Active" and 
        * are editable for the current user - see corresponding spec;
      * displays:
        * if there is no row in the "Account Linking History" non-embedded spreadsheet or if there is at least one row and "End Date" for the top row is blank: displays blank;
        * otherwise (if there is at least one row in the "Account Linking History" non-embedded spreadsheet and "End Date" for the top row is not blank): displays the value in the "Account #" field for the top row;
      * editability:
        * if saved as blank (see "displays" spec above): editable for "All Provider Roles" users;
        * if saved as not blank (see "displays" spec above): editable for "Upline Provider Roles" users for the linked Account (note that this means that Resellers and Group Admins may switch a Device to an Account that they do not manage, but after saving the changes they will no longer be able to bring it back);
      * when set to either blank or non-blank, the following field(s) are affected on change:
        * the following is set on the top existing row of the "Account Linking History" non-embedded spreadsheet: 
          * "End Date": if blank, sets to the current date; 
        * "Device General Notes": is cleared;
      * when set to non-blank (from any saved value), the following field(s) are affected on change: 
        * "Account Linking History" non-embedded spreadsheet: a new row is added, with the following set:
          * "Account #": sets to the Account # selected here;
          * "Start Date": sets to the current date;
          * note that a new row is not added if "Account" is set to blank; 
        * "Set Device Status": sets to "Assigned"; 
      * when set to blank, the following field(s) are affected on change: 
        * "Set Device Status": sets to "Available"; 
        * on the top existing row of the "Primary Driver History" non-embedded spreadsheet: "End Date": if blank, sets to the current date (note that this clears the "Primary Driver" macro - see corresponding specs); 
        * on the top existing row of the "Primary Vehicle History" non-embedded spreadsheet: "End Date": if blank, sets to the current date (note that this clears the "Primary Driver" macro - see corresponding specs); 
      * on the first Save after this is set to either blank or non-blank, the following things happen: 
        * data synced with Traccar via the Traccar Device sync record;



TODO_VA: Tim Reitz 02/04/2026: trigger work on Save (linking with the corresponding Users / Drivers); 

  * following happen as needed:
    * the "Send "Device Linked with Account" Email" triggered automatic process runs, sending the "Device Linked with Account" Email Merge (see corresponding email spec);
    * the "Send "Device Unlinked from Account" Email" triggered automatic process runs, sending the "Device Unlinked from Account" Email Merge (see corresponding email spec); 


  * note that additional details (validations, etc.) will need to specced out for the Subscription Management feature (Phase 2))



  


  * Clear Account (button; with the following details / behaviors:
    * visible in Edit Mode if "Account" ≠ blank; 
    * visible to "Upline Provider Roles" users for the linked Account; 
    * when clicked, the following field(s) are affected:
      * "Clear Account Mode": sets to checked, which makes the "Clear Account On-Screen Prompt" visible - see corresponding spec)
  * Clear Account Mode (hidden; checkbox; with the following details / behaviors:
    * set to checked via the "Clear Account" button (making the data entry fields visible) and unchecked via the "Cancel" or "Confirm" buttons (hiding the transfer fields) - see corresponding specs; 
    * error on Save if this checkbox is checked: "Device cannot be saved while Clear Account is in progress."; this prevents data from being saved in the fields) 



  


  * Clear Account On-Screen Prompt:
    * Cancel (button; with the following details / behaviors: 
      * visible to "Upline Provider Roles" users for the linked Account; 
      * visible in the location of the "Clear Account" button if "Clear Account Mode" checkbox is checked, 
      * when clicked, the following field(s) are affected: 
        * "Clear Account Mode": sets to not checked, which makes the "Clear Account On-Screen Prompt" hidden, causing the data entry field(s) to be cleared)  
    * End Date (visible if "Clear Account Mode" checkbox is checked; date; defaults to the current date)
    * Confirm (visible if "Clear Account Mode" checkbox is checked; button; with the following details / behaviors: 
      * when clicked with required data entry field(s) filled, the following happen:
        * "End Date" for the top row in the "Account Linking History" non-embedded spreadsheet: sets to the current date;
        * note that the "Account" macro on the main screen is cleared when "End Date" is set - see corresponding spec for the "Account" macro;
      * on the first Save after this button is clicked (specifically, after "Account" is cleared), the "Send "Device Unlinked from Account" Email" triggered automatic process runs, sending the "Device Unlinked from Account" Email - see corresponding spec)  



  


  * Prim. Account Mgr. (read-only macro; displays the Primary Account Manager for the "Account") 
  * Account Group (read-only macro; displays the "Account Group" for the "Account"; data synced with Traccar) 



TODO_VA: Tim Reitz 02/04/2026: trigger work

  * View/Edit Account (visible if "Account" is not blank; link; opens the corresponding Account record) 



  


  * Account Linking History (button; visible to "All Provider Roles" users; opens the "Account Linking History" child screen - see corresponding spec) 



  


  * Device Transfer Comments (label displays as "Device Transfer Comments (included in the emails to the Account Managers of the previous and new Accounts)"; editable macro; memo; with the following details: 
    * visible until the first Save after "Account" is changed from a saved non-blank value; 
    * required;
    * displays / sets the "Device Transfer Comments" memo field for the new row on the "Account Linking History" non-embedded spreadsheet)



  


  * Account Linking History Child Screen (contains the following: 
    * Account Linking History (non-embedded spreadsheet with the following: 
      * Columns: 
        * Account # (auto-set and read-only; list field of "Account #" items; sets from the "Account" editable macro on the main screen when a new row is added - see corresponding spec) 
        * Start Date (auto-set and read-only; date; sets to the current date when the row is added via the "Account" editable macro) 
        * End Date (auto-set and read-only; date; the top row is always blank unless "Account" is set to blank, and automatically sets to the current date when "Account" is changed or cleared - see corresponding specs) 
        * Device Transfer Comments (button; opens a lightbox screen with an auto-set and read-only memo field; automatically set from the "Primary Vehicle Change Comments" editable macro - see corresponding spec; the contents here are included in the ""Device Linked with Account" Email" and the ""Device Unlinked from Account" Email" \- see corresponding specs) 
      * Automatically sorted by: "Start Date" (most recent at the top) 
      * Buttons to add/remove rows: N/A (rows are automatically added & removed) 
      * Shows 6 rows without scrolling
      * Other Notes: 
        * see spec on the "Account" editable macro for details about how rows are added and how fields are set; 
        * on every Save, the Solution checks this embedded spreadsheet, and removes any rows where "Start Date" = "End Date" for the same row; this eliminates duplicate rows when "Account" is changed multiple times in the same day, since there is not a need to retain multiple Accounts with the same "Start Date", as it would normally would only happen by mistake)



  


Development Specification

TODO_MOCKUPS: Tim Reitz 01/14/2026: I think I recently did some updating on this spec. Could you confirm that that mockups match? Thanks! 

  


Tim Reitz 10/29/2025: Account Linking History RG: Per Nic, use a field change expression to remove duplicate rows (on every save, remove any rows where "Date Added" = "End Date" for the same row).
