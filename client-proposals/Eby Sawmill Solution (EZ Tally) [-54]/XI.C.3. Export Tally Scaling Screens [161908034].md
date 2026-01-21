11.3.3. Export Tally Scaling Screens

  


Requirements

Bookings List:

This screen displays a list of all Bookings with a Status of "Open", with the following columns:

  * Booking ID
  * Description
  * Action ("Select" button to open the Booking)



  


When a Booking is selected, screen advances to the Tallies List screen.

  


Export Tallies List:

This screen displays the following navigation description: "Export Scaling > <Booking ID>". Selecting "Export Scaling" takes the user back to the Bookings List.

  


This also displays a list of all Export Tally IDs for the selected Booking with the following columns:

  * Tally ID
  * Status
  * Action ("Edit" icon & label)



  


This list is sorted in the following order: Open, Confirmed, Loaded, Closed

  


Clicking on an Export Tally will display the Tally Details screen for the selected Tally.

  


Above the list there is a "New Tally" button, visible only for admin users, that creates a new Export Tally record for the current Booking (opens a blank new Export Tally Details screen).

  


Export Tally Details:

This screen displays the following navigation description: "Export Scaling > <Booking ID>". Selecting the Booking ID takes the user back to the Tallies List; selecting "Export Scaling" takes the user back to the Bookings List. 

  


This screen also displays the following details:

  * Tally ID (displays as "(New)" for new tallies being created)
  * Status (displays as "(Unsaved)" for new tallies being created)
  * Early Return Date (from the Booking)
  * Cutoff Date (from the Booking)
  * Total Loads (from the Booking)
  * Target BF for Grade (A) 
    * Grade A: editable field; drop list of Base Grades 1-5; does not allow duplicates on the same tally
    * Target Board Feet A: visible, editable, and required if a corresponding Base Grade is selected; number with no decimals; wide enough to show 5 digits) 
  * Target BF for Grade (B) (visible if a Grade is selected for Target A) 
    * Grade B: editable field; drop list of Base Grades 1-5; does not allow duplicates on the same tally
    * Target Board Feet B: visible, editable, and required if a corresponding Base Grade is selected; number with no decimals; wide enough to show 5 digits) 
  * Target BF for Grade (C) (visible if a Grade is selected for Target B) 
    * Grade C: editable field; drop list of Base Grades 1-5; does not allow duplicates on the same tally
    * Target Board Feet C: visible, editable, and required if a corresponding Base Grade is selected; number with no decimals; wide enough to show 5 digits) 
  * Total Target Board Feet  
  * Total Net Board Feet (for the Tally)
  * Total Gross Board Feet (for the Tally)
    * This will be shown in orange if it is more than X board feet less than the target.
    * This is shown in red if it exceeds the target total by more than X board feet, and a message will be displayed: "The Total Gross Board Feet exceeds the target total by more than <X> board feet. Reduce the total board feet to continue."
    * This is shown in red if it exceeds the target total by more than X board feet; the user is able select "Save and Return", but is not able to mark the Tally as Confirmed (see the spec for Confirmed checkbox); and a message will be displayed: "The Total Gross Board Feet exceeds the target total by more than <X> board feet. Reduce the total board feet to continue."
    * The value represented here as "X" is the value set on the "Export tally target warning threshold" System Switch. This normally would be 100 board feet. 
  * Logs (table of entered logs with columns for the following details, all auto-set and read-ony):
    * Tag # (link to open the "Log Entry - Log Details" screen for that log)
    * Species (displays the abbreviation)
    * Length (displays the abbreviation)
    * Diameter (displays the abbreviation)
    * Base Grade
    * Net BF (whole number)



  


The following also are displayed:

  * Enter New Log (button; visible if Status is Open; logs cannot be added if status is Confirmed, Loaded, or Closed) 
  * Confirmed (checkbox; with the following behaviors:
    * visible if Status is Open and there is at least one log entered on the tally and the Total Gross Board Feet does not exceed the target by more than the value of the "Export tally target warning threshold";
    * if there are no logs for the tally, the following message is displayed in red text: "This Export Tally cannot be confirmed because there are no logs on it.";
    * if the Total Gross Board Feet exceeds the target by more than the threshold, the following message is displayed in red text: "The Total Gross Board Feet exceeds the target total by more than <X> board feet. Reduce the total board feet to continue.";
      * note that in this situation the user must remove one or more logs to reduce the board footage, or have the Target Board Feet changed in order to continue with confirming the Tally; 
    * if checked, this checkbox can be unchecked to "unconfirm" the tally, changing Status back to Open and allowing the user to add more logs)
  * Save Tally (button; always visible)



Tim Reitz 01/17/2024: This is on hold (not currently present).

  * Save Tally & Return (button; always visible)



  


Button actions: 

  * If Enter New Log is selected, the Tag Number screen is displayed.
  * If the Confirmed checkbox is checked, the current date is displayed beside the checkbox, the Status is changed to Confirmed, and the tally details become read-only.
  * If Save Tally is selected, the tally is saved and the screen does not change.



Tim Reitz 01/17/2024: This is on hold (not currently present).

  * If Save Tally & Continue is selected, the tally is saved and the screen advances to the Tallies List for the same Booking.



  


Log Entry - Tag Number:

This screen displays the following navigation description: "Export Scaling > <Booking ID>". Selecting the Booking ID takes the user back to the Tallies List; selecting "Export Scaling" takes the user back to the Bookings List (after a warning that changes will be lost). 

  


This screen will display the tally details summary at the top of the screen:

  * Tally: (ID)
  * Grade <#> BF Remaining (as applicable; calculations done as in the main system - see corresponding spec)
  * Grade <#> BF Remaining (as applicable; calculations done as in the main system - see corresponding spec)
  * Grade <#> BF Remaining (as applicable; calculations done as in the main system - see corresponding spec)
  * Total BF Remaining (calculations done as in the main system - see corresponding spec)



  


This screen displays the following data entry field:

  * Tag Number (with the following details: 
    * required; 
    * defaults to blank for the first log of a Tally; 
    * for subsequent logs, defaults to 1 greater than the previous log's Tag #; 
    * validate against blank Tag #'s - error message when the "Continue" button is selected: "Empty or invalid tag number."; 
    * validate against duplicate Tag #'s on the same Export Tally - message when the "Continue" button is selected: "This log duplicates a tag number.")



  


When the "Continue" button is selected, the Species screen is displayed.

  


Log Entry - Species:

This screen displays the following navigation description: "Export Scaling > <Booking ID>". Selecting the Booking ID takes the user back to the Tallies List; selecting "Export Scaling" takes the user back to the Bookings List (after a warning that changes will be lost). 

  


This screen displays the tally details summary at the top of the screen.

  


This screen also includes the following field for data entry:

  * Species



  


The species are displayed below the field, broken into two lists (each list displays the hotkey and the species abbreviation):

  * Primary Species (hotkeys 1-9)
  * Other Species (hotkeys 01-09)



  


This screen also shows the following log summary information as a reference:

  * Tag Number



  


When a 1 or 2-digit hotkey is entered to set the Species, the Log Dimensions screen will be displayed.

  


Log Entry - Log Dimensions:

This screen displays the following navigation description: "Export Scaling > <Booking ID>". Selecting the Booking ID takes the user back to the Tallies List; selecting "Export Scaling" takes the user back to the Bookings List (after a warning that changes will be lost). 

  


This screen displays the tally details summary at the top of the screen.

  


This screen displays the following entry fields:

  * Length (ft)
  * Cutback (ft)
  * Diameter (in)



  


This screen also shows the following log summary information as a reference:

  * Tag Number
  * Species



  


The focus initially is on the Length field. A 1-digit or 2-digit length may be entered within the following parameters:

  * One digit: Numbers 6-9
  * Two digits: Numbers 10-59



  


When a Length is entered, the focus moves to Diameter. 

  * If a 2-digit Diameter is entered, the Grade screen is displayed. 
  * If a "9" is entered:
    * The focus moves backwards to Cutback and the 9 is cleared from Diameter.
    * When a Cutback is entered (numbers 6-9 or 10-59, as for Length) the focus moves to Diameter.
    * When a 2-digit Diameter is entered, the Base Grade screen is displayed.



  


Log Entry - Base Grade:

This screen displays the following navigation description: "Export Scaling > <Booking ID>". Selecting the Booking ID takes the user back to the Tallies List; selecting "Export Scaling" takes the user back to the Bookings List (after a warning that changes will be lost). 

  


This screen displays the tally details summary at the top of the screen.

  


This screen includes the following data entry field:

  * Base Grade



  


This screen also shows the following log summary information as a reference:

  * Tag Number
  * Species
  * Length
  * Cutback
  * Diameter



  


When the 1-digit Base Grade is entered, the Review Log Information screen is displayed.

  


Log Entry - Review Log Information:

This screen displays the following navigation description: "Export Scaling > <Booking ID>". Selecting the Booking ID takes the user back to the Tallies List; selecting "Export Scaling" takes the user back to the Bookings List (after a warning that changes will be lost). 

  


This screen displays the tally details summary at the top of the screen.

  


This screen displays the following list of information for the entered log:

  * Tag Number 
  * Species
  * Length
  * Cutback
  * Diameter
  * Base Grade



  


The user is able to select each piece of information and enter the editing process from that point.

  


This screen displays the following buttons:

  * Enter New Log
  * Finish Scaling
  * Delete Log



  


Button actions: 

  * If Delete Log is selected, a confirmation prompt will be displayed, with options to either delete the log or cancel.
  * If Finish Scaling is selected, the Export Tally Details screen will be displayed.
  * If Enter New Log is selected, the scaling process starts over for a new log for the same Tally.



  


Log Details:

This screen displays the following navigation description: "Export Scaling > <Booking ID>". Selecting the Booking ID takes the user back to the Tallies List; selecting "Export Scaling" takes the user back to the Bookings List (after a warning that changes will be lost). 

  


This screen will display the tally details summary at the top of the screen. 

  


The log summary list will be displayed, showing the following:

  * Tag Number
  * Species
  * Length
  * Cutback
  * Diameter
  * Base Grade



  


If the Tally Status = Open, the user is able to select each piece of information for the log and enter the editing process from that point.

If the Tally Status = Confirmed or Loaded, the details on this screen are read-only. 

  


This screen has the following buttons:

  * Enter New Log (if Status = Open) 
  * Finish Scaling (if Status = Open) 
  * Delete Log (if Status = Open) 
  * Return to Summary (if Status = Confirmed or Loaded)



  


Development Specification

Change Requests: 

  * Tim Reitz 06/10/2024: [[[IN9365](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9367&)]] - ZET - Yard App - Misc items after initial deployment walkthrough 
  * Tim Reitz 06/19/2024: [[[IN9516](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9518&)]] - ZET - Yard App - Permissions - Fix Issues for Non-Admin Users 
  * Tim Reitz 08/28/2024: [[[IN9377](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9379&)]] - ZET - Yard App - Export Loading - Prevent Duplicate Tag Numbers 
  * Tim Reitz 08/31/2024: [[[IN10234](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10236&)]] - ZET - Yard App - Export Scaling & Loading - Tally Details Screen - Add Log Details Table
  * Tim Reitz 10/04/2025: [[[IN10522](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10524&)]] - ZET - Yard App - Export Scaling - Tag # Not Required Immediately


