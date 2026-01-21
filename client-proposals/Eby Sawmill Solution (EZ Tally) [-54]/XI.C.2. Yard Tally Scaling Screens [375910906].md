11.3.2. Yard Tally Scaling Screens

  


Requirements

Yard Tallies List: 

If there are existing Yard Tallies, they will be displayed in a list showing the following: 

  * Status (displays as "(New)" for tallies created offline, until connection has been reestablished and they have been synced with the main database)
  * ID (link to open the Yard Tally Details screen for the ally)
  * Cr. Date (displays the Created Date) 
  * Source (displays the Vendor Name or Tract Name for the Yard Tally; if the name is too long to fit in the column, it will be truncated)
  * Email icon (visible only for Vendor-sourced tallies with Status of Confirmed; opens the Email Yard Tally prompt screen) 



  


Misc. Notes: 

  * This list will include tallies with a Status of Open and Confirmed, but not Closed. 



TODO_VA: Tim Reitz 01/16/2026: Update spec based on recent CR. 

  * The list will be sorted in the following sequence:
    * First by Status (Open, then Confirmed)
    * Next by Cr. Date (most recent at the top) (Note: This was originally specced to be by Tally ID) 
    * Exception: When the app is being used in offline mode, newly created tallies will appear at the top of the list with a temporary status of "(New)"; once internet connection has been reestablish and those records are synced to the main system, they will appear in the usual format.



  


There will also be the following button:

  * Create New Tally (button)



  


If the tally list is empty (such as the first time the app is used, or if all existing tallies have been closed) the first screen displayed when the Yard Tally Scaling button is clicked on the main menu will display the following along with the Create New Tally button:

  * Your Tally List is Empty (text)



  


Selecting a Tally from the list will advance the screen to the Yard Tally Details screen for the selected Tally. 

Selecting the Create New Tally button will open the Select Tally Source screen. 

  


Select Tally Source: 

This screen displays the following navigation description: "Yard Scaling > New Tally". Selecting "Yard Scaling" takes the user back to the Yard Tallies List (note that changes will be lost). 

  


This screen displays the following buttons:

  * Tract
  * Vendor



  


If Tract Based is selected, the Select Tract screen will be displayed; if Vendor Based is selected, the Select Vendor screen will be displayed.

  


Screens Specific to Vendor Based: 

Select Vendor:

This screen displays the following navigation description: "Yard Scaling > New Tally". Selecting "Yard Scaling" takes the user back to the Yard Tallies List (after a warning that changes will be lost). 

  


This screen displays the following:

  * Source: Vendor (button; editable to change the source if desired) 
  * Search (search bar; entered text filters the list of Vendor list below accordingly) 
  * List of active Vendor-type Contacts (filtered according to the entered Search text)
  * "New Vendor" option (always visible, regardless of the entered Search text)



  


Button actions:

  * If the user selects a Vendor from the list, the screen advances to Select Eby Freight (to begin the process of creating a new Yard Tally).
  * If the user selects the Add New Vendor button, the Select Vendor Type screen will be displayed (to begin the process of creating a new Vendor-type Contact).



  


Add Vendor - Select Vendor Type:

This screen displays the following navigation description: "Yard Scaling > New Tally". Selecting "Yard Scaling" takes the user back to the Yard Tallies List (after a warning that changes will be lost). 

  


This screen displays the following:

  * Source: Vendor (editable) 
  * Vendor Type (with options for "Individual" and "Organization")



  


If "Individual" is selected, the Individual Form screen will be displayed. If "Organization" is selected, the Organization Form screen will be displayed.

  


Add Vendor - Individual Form:

This screen displays the following navigation description: "Yard Scaling > New Tally". Selecting "Yard Scaling" takes the user back to the Yard Tallies List (after a warning that changes will be lost). 

  


This screen displays the following:

  * Source: Vendor (editable)



  


This screen also displays the following entry fields:

  * Vendor Type (always set to Individual for this screen)
  * First Name (required)
  * Last Name (required)
  * Email
  * Phone Number (required)
  * Address 1
  * Address 2
  * City
  * State
  * Zip



  


The screen also has a "Save New Vendor" button that will create the new Vendor-type Contact and return to the Select Vendor screen, where the new Vendor is now displayed.

  


Note that if a name is entered that is an exact duplicate of an existing Contact name in the database, a sequential number is added after the name (#2, #3, etc.) to help distinguish between the contacts. In the main system, this is done for individual Contacts by checking the "Override Name" checkbox on the Contact record and filling in the Display Name. 

  


Add Vendor - Organization Form:

This screen displays the following navigation description: "Yard Scaling > New Tally". Selecting "Yard Scaling" takes the user back to the Yard Tallies List (after a warning that changes will be lost). 

  


This screen displays the following:

  * Source: Vendor (editable)



  


This screen displays the following entry fields:

  * Vendor Type (always set to Organization for this screen)
  * Business Name (required)
  * Email
  * Phone Number (required)
  * Address 1
  * Address 2
  * City
  * State
  * Zip



  


The screen also has a "Save New Vendor" button that will create the new Vendor-type Contact and return to the Select Vendor screen, where the new Vendor is now displayed.

  


Note that if a name is entered that is an exact duplicate of an existing Contact name in the database, a sequential number is added after the name (#2, #3, etc.) to help distinguish between the contacts.  

  


Select Eby Freight:

This screen displays the following navigation description: "Yard Scaling > New Tally". Selecting "Yard Scaling" takes the user back to the Yard Tallies List (after a warning that any entered data will be lost). 

  


This screen also displays the following:

  * Source: Vendor (editable) 
  * Vendor: <Vendor Name> (editable)
  * Buttons for Yes and No



  


When a button is selected, the Yard Tally Details screen is displayed.

  


Specific to Tract Based: 

Select Tract:

This screen displays the following navigation description: "Yard Scaling > New Tally". Selecting "Yard Scaling" takes the user back to the Yard Tallies List (after a warning that any entered data will be lost). 

  


This screen displays the following:

  * Source: Tract (editable)
  * List of all Tracts with Status of Harvest Started, sorted alphabetically. 



  


When the user selects a Tract from the list, the Select Logger screen will be displayed.

  


Select Logger:

This screen displays the following navigation description: "Yard Scaling > New Tally". Selecting "Yard Scaling" takes the user back to the Yard Tallies List (after a warning that any entered data will be lost). 

  


This screen displays the following:

  * Source: Tract (editable)
  * Tract: <Selected Tract> (editable)
  * List of all Logger Contacts for the selected Tract, sorted alphabetically. If there is only one Logger for the Tract, it defaults to that one. Cleared immediately if Tract is changed to a Tract that does not have the selected Logger. 



  


When the user selects a Logger from the list, the Yard Tally Details screen is displayed.

  


Common to Both Vendor and Tract Based:

Yard Tally Details:

This screen displays the following navigation description: "Yard Scaling > Tally #<ID>". Selecting "Yard Scaling" takes the user back to the Yard Tallies List (after a warning that any entered data will be lost if the Tally has not yet been saved). 

  


This screen displays the following information below the navigation description:

  * Source (auto-set and read-only) 
  * Tract / Vendor Name (auto-set and read-only) 
  * Eby Freight (if Source = Vendor; auto-set and read-only)
  * Status (auto-set and read-only)
  * Logger Name (if Source = Tract; auto-set and read-only)
  * Total Net BF (auto-set and read-only)
  * Total Value (auto-set and read-only)
  * Average Price ($/MBF) (auto-set and read-only; <Total Value> / <Net BF> * 1000, rounded to the nearest 2 decimal places; note that this is the same as the total row for the corresponding column in the bottom right pane of the Yard Tallies Report)
  * Remarks (editable) 
  * Logs (table of entered logs with columns for the following details, all auto-set and read-only:
    * Sequence # (link to open the "Log Entry - Log Details" screen for that log) 
    * Species (displays the abbreviation) 
    * Length 
    * Diameter 
    * Grade 
    * Price (displays the Price category for the log, based on the Grade) 
    * Net BF (whole number) 
    * Value (includes the dollar sign))



  


The following also are displayed:

  * Enter New Log (button; visible if Status is Open; logs cannot be added if "Status" = "Confirmed" or "Closed")
  * Confirmed (checkbox; with the following behaviors: 
    * visible if "Status" = "Open" and there is at least one log entered on the tally; 
    * if there are no logs for the tally, the following message is displayed in red text: "This Yard Tally cannot be confirmed because there are no logs on it."; 
    * if checked, this checkbox can be unchecked to "unconfirm" the tally, changing Status back to Open and allowing the user to add more logs)
  * Save Tally (button; always visible)



Tim Reitz 01/17/2024: This is on hold (not currently present). 

  * Save Tally & Return (button; always visible)
  * Download Yard Tally Summary (this opens the Yard Tally Summary Printout PDF on the mobile device so the user can then print the document directly to the printer from the device (or save it or share it), then return to the app) 
  * Email Yard Tally Summary (button; visible if "Source" = "Vendor" and "Status" = "Confirmed" or "Closed")



  


Button actions: 

  * If Enter New Log is selected, the Log Entry - Species screen is displayed.
  * If the Confirmed checkbox is checked, the current date is displayed beside the checkbox, the Status is changed to Confirmed, and the tally details become read-only)  
  * If Save Tally is selected, the tally is saved and the screen does not change.



Tim Reitz 01/17/2024: This is on hold (not currently present). 

  * If Save Tally & Return is selected, the tally is saved and the screen advances to the Tallies List for the same Booking.
  * Email Yard Tally Summary is selected, a prompt is displayed: "You are about to email the Yard Tally Summary for this tally.", with options for "Cancel" and "OK". Selecting "OK" sends the email, saves changes to the Yard Tally, and advances the screen to the Yard Tallies List. 



  


Log Entry - Species:

This screen displays the following navigation description: "Yard Scaling > <Yard Tally ID> > Enter Log". Selecting "Yard Scaling" takes the user back to the Yard Tallies List and selecting the Tally ID takes the user back to the Yard Tally Details screen for the Tally (both give a warning that changes will be lost / the log will be removed from the tally). 

  


This screen displays the tally details summary at the top of the screen:

  * Tally ID
  * Logs (number of logs)
  * Total Net BF (sum of all logs)
  * Average Price ($/MBF) (auto-set and read-only; <Total Value> / <Net BF> * 1000, rounded to the nearest 2 decimal places; note that this is the same as the total row for the corresponding column in the bottom right pane of the Yard Tallies Report)
  * Last Log (displays the same details as the Logs table on the Tally Details screen, but for the most recently-entered log for the tally; with the following special behaviors: 
    * For the first log on a tally this is blank / hidden since there are no other logs on the tally;  
    * If opening a previously-entered log, this does not display any details since it is not opening in the entry process.) 



  


This screen also will include the following field for data entry:

  * Species



  


The species will be displayed below the field, broken into two lists:

  * Primary Species (hotkeys 1-9)
  * Other Species (hotkeys 01-09)



  


When a 1 or 2 digit hotkey is entered to set the Species, the Log Dimensions screen will be displayed.

  


Other Notes: 

  * A log should not count toward the total calculations (i.e. Average Price) until it is completely entered (if it is counted as 0 as soon as log entry begins, it skews the calculations until the log is complete).



  


Log Entry - Log Dimensions:

This screen displays the following navigation description: "Yard Scaling > <Yard Tally ID> > Enter Log". Selecting "Yard Scaling" takes the user back to the Yard Tallies List and selecting the Tally ID takes the user back to the Yard Tally Details screen for the Tally (both give a warning that changes will be lost / the log will be removed from the tally). 

  


This screen displays the tally details summary at the top of the screen.

  


This screen will display the following entry fields:

  * Length (ft)
  * Cutback (ft)
  * Diameter (in)



  


The focus initially is on the Length field. A 1-digit or 2-digit length may be entered within the following parameters:

  * One digit: Numbers 6-9
  * Two digits: Numbers 10-59



  


When a Length is entered the focus moves to Diameter. 

  * If a 2-digit Diameter is entered, the Grade and Subgrade screen is displayed. 
  * If a "9" is entered for Diameter:
    * The focus moves backwards to Cutback and the 9 is be cleared from Diameter.
    * When Cutback is entered (numbers 6-9 or 10-59, as for Length) the focus will move back to Diameter.
    * When a two digit Diameter is entered, the Grade and Subgrade screen will be displayed.



  


Above the data entry fields, the log summary list is displayed, showing the following:

  * Species



  


Log Entry - Grade and Subgrade:

This screen displays the following navigation description: "Yard Scaling > <Yard Tally ID> > Enter Log". Selecting "Yard Scaling" takes the user back to the Yard Tallies List and selecting the Tally ID takes the user back to the Yard Tally Details screen for the Tally (both give a warning that changes will be lost / the log will be removed from the tally). 

  


This screen displays the tally details summary at the top of the screen.

  


This screen will include the following entry fields:

  * Base Grade
  * Subgrade 



  


The focus will initially be on Base Grade. When a 1-digit Base Grade is entered, the focus will move to Subgrade. If a Base Grade of 0 through 4 is selected, a list of the following will be displayed for reference below the Subgrade field:

  * Subgrade 
  * Value (in $/mbf)



Note that these details are not displayed for Base Grade 5 because its Subgrade numbers directly correlate to the price (see corresponding section of the proposal). 

  


Above the data entry fields, the log summary list will be displayed, showing the following:

  * Species
  * Length
  * Cutback
  * Diameter



  


When both Base Grade and Subgrade have been entered, the screen will advance to the Log Condition screen.

  


Log Entry - Log Condition:

This screen displays the following navigation description: "Yard Scaling > <Yard Tally ID> > Enter Log". Selecting "Yard Scaling" takes the user back to the Yard Tallies List and selecting the Tally ID takes the user back to the Yard Tally Details screen for the Tally (both give a warning that changes will be lost / the log will be removed from the tally). 

  


This screen displays the tally details summary at the top of the screen.

  


This screen will display the following data entry field:

  * Condition



  


Below the data entry field, a list of available Log Conditions is displayed in the following format: "<Hotkey> \- <Description>".

  


If 0-8 is entered, the corresponding pre-set log condition will be selected. If 9 is entered, an "Other Condition" text field will become visible and editable (and required).

  


Above the data entry fields, the log summary list will be displayed, showing the following:

  * Species
  * Length
  * Cutback
  * Diameter
  * Base Grade
  * Subgrade



  


Once the condition is entered the Confirm Log screen will be shown.

  


Log Entry - Confirm Log:

This screen displays the following navigation description: "Yard Scaling > <Yard Tally ID> > Enter Log". Selecting "Yard Scaling" takes the user back to the Yard Tallies List and selecting the Tally ID takes the user back to the Yard Tally Details screen for the Tally (both give a warning that changes will be lost / the log will be removed from the tally). 

  


This screen displays the tally details summary at the top of the screen. 

  


The log summary list will be displayed, showing the following:

  * Species
  * Length
  * Cutback
  * Diameter
  * Base Grade
  * Subgrade
  * Condition
  * Other Condition



  


The user is able to select each piece of information and enter the editing process from that point.

  


This screen has the following buttons:

  * Enter New Log
  * Finish Scaling
  * Delete Log



  


Button actions:

  * If Enter New Log is selected, the log entry process will start over again for a new log for the same tally.
  * If Finish Scaling is selected, the Yard Tally Details screen will be displayed.
  * If Delete Log is selected, a confirmation prompt will be displayed, with options to either delete the log or cancel.



  


Log Entry - Log Details:

This screen the tally details summary at the top of the screen. 

  


The log summary list will be displayed, showing the following:

  * Species
  * Length
  * Cutback
  * Diameter
  * Base Grade
  * Subgrade
  * Condition
  * Log Condition



  


If the Tally Status = Open, the user is able to select each piece of information and enter the editing process from that point.

If the Tally Status = Confirmed, the details on this screen are read-only. 

  


This screen has the following buttons:

  * Enter New Log (if Status = Open) 
  * Finish Scaling (if Status = Open) 
  * Delete Log (if Status = Open) 
  * Return to Summary (if Status = Confirmed) 



  


Email Yard Tally:

This is a confirmation prompt message: "You are about to email the Yard Tally Summary for this tally" and options for "Cancel" and "OK". 

  


When the user confirms, the email will be sent from the AppHosting software, and the Yard Tallies List screen is displayed.

  


Development Specification

Depending on the UI for the entry, we could use another symbol to start cutbacks, such as "/" or "-".

  


TODO_TR - How important is the "Email sent" notification? We can queue it up, but the platform doesn't tell us when it's literally sent.

and the original prompt and button will be replaced with a confirmation message: "Email sent".

Tim Reitz 01/11/2024: It looks like we're not able to do the confirmation.

  


  


Change Requests: 

  * Tim Reitz 06/10/2024: [[[IN9365](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9367&)]] - ZET - Yard App - Misc items after initial deployment walkthrough
  * Tim Reitz 06/20/2024: [[[IN9428](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9430&)]] - ZET - Yard App - Improve Displayed Log Details (prev. Client Feedback 2/5/24)
  * Tim Reitz 06/20/2024: [[[IN9540](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9542&)]] - ZET - Yard App - Yard Scaling - Add "Download Yard Tally Summary" option
  * Tim Reitz 08/07/2024: [[[IN9985](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9987&)]] - ZET - Yard App - Yard Scaling - Change Average Price Calculation (prev. "Incorrect averages")
  * Tim Reitz 08/07/2024: [[[IN9541](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9543&)]] - ZET - Yard App - Yard Scaling - Average Price field: Veneer logs not being accounted for 
  * Tim Reitz 08/31/2024: [[[IN9386](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9388&)]] - ZET - Yard App - Yard Tallies List - Display Tract / Vendor Names
  * Tim Reitz 08/31/2024: [[[IN9387](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9389&)]] - ZET - Yard App - New Yard Tally - Add Search for Vendor Selection 
  * Tim Reitz 10/04/2025: [[[IN10650](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10652&)]] - ZET - Yard App - Yard Tally - Clear Logger Field if Tract is Changed
  * Tim Reitz 10/04/2025: [[[IN10543](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10545&)]] - ZET - Yard App - New Yard Tally - Only Include Active Vendors in List


