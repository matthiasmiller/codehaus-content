7.9.1. Event - <Event Type> Overview Section

  


Requirements

  * "<Event Type> Overview" section (visible on all Event Types; visibility for users based on "Event Status" and the "Event Visibility" field selection): 



  


  * Event Status (read-only; displays in the section header; options are Tentative, Scheduled, Complete, Canceled:)
    * Tentative: default status for new records; if none of the following checkboxes are filled: Scheduled, Complete, Canceled; Events with this status are only visible to Regional Reps and Super Admins. 
    * Scheduled: if the Event Scheduled checkbox is filled; Events with this status are visible based on the "Event Visibility" selection.
    * Complete: if the Event Complete checkbox is filled; Events with this status are visible based on the "Event Visibility" selection.
      * Error on the field if set to "Complete" and any of the linked Registration records meet the following criteria: "Registration Status" = "Attending" or "Tentative", and "Attended" = blank: "One or more registrations are lacking attendance information."
      * Warning on Save if set to "Complete" and the Event was already saved as "Complete": "You are about to save changes to a completed Event."
    * Canceled: if the Event Canceled checkbox is filled; Events with this status are visible based on the "Event Visibility" selection.
      * Error on the field if set to "Canceled" and there are any linked Registration records that meet the following criteria: "Registration Status" = "Attending" or "Tentative": "This Event has at least 1 open registration(s). Click on "View/Manage Event Registrations" and set all to "Canceled". Then try again to cancel the event, and notify the registrants."
  * Event ID (displayed throughout the Solution as a visible identifier for the event;  
    * If Event Name is not set: N/A (it is empty); 
    * If Event Name is set but Event Date is not set: "<Event Name> (Unscheduled)" (e.g. "Lancaster Info Meeting (Unscheduled)");  
    * If Event Name and Event Date are set: "<Event Name> (<Event Date in the MMMM, D, YYYY format>)" (e.g. "Lancaster Info Meeting (January 1, 2025)");  
    * validation against duplicate Event IDs-- error message on Save: ""Duplicate Event names are not allowed: <Event ID>") 
  * Event Type (required; drop list of Event Type list items; with the following behaviors / details: 
    * defaults to blank or as set by the creation link; 
    * when an option is selected (either initially or changed), the Event Visibility is immediately updated to match the Type's "Default Event Visibility", if one is set; 
    * warning on the field if changed after the initial save:  "Changing the Type for an existing Event may cause fields to be blanked out when the record is saved."; 
    * when out of Edit Mode, this field is not a link)
  * Event Name (required; plain text field)
  * Event Focus (optional; plain text field) 
  * Event Visibility (required; drop list of Event Visibility list items - see corresponding section of the proposal; with the following behaviors / details: 
    * defaults to the selection on the Event Type record for the selected Type; 
    * this controls the visibility of all non-Regional Rep / Super Admin fields on the record, as follows: 
      * Public: Visible to all Symbiz members, and eventually could be included on the public Symbiz website to be viewed by all visitors to the website.;
      * All Members: Visible for all Symbiz members.;
      * Invitation Only: Visible only for members with their name on the Registration embedded spreadsheet and all their uplines.;
    * field visible to all contacts who have a Registration record for the Event and to all Regional Reps and Super Admins) 



  


  * Event Scheduled (checkbox; defaults to cleared; to be checked via the "Schedule Event" button when the date is confirmed; unchecking the checkbox makes the Schedule Event button visible) 
  * Schedule Event (button; visible in the location of the Event Scheduled checkbox, if the checkbox is unchecked; clicking the button checks the corresponding checkbox and unchecks the Event Canceled or Event Complete checkbox, if one is checked; if "Event Date" is blank, clicking this button displays an error message on the button: "Please add an event date."; the button is hidden after if it clicked, specifically, if the checkbox is checked; visible for Regional Reps and Super Admins) 
  * Event Canceled (checkbox; defaults to unchecked; if checked, Event Status is set to Canceled; note that fields on the record will still be editable; if the checkbox is checked, warning on save if the Event was already saved as "Canceled": "You are making changes to a canceled Event.")
  * Cancel Event (button; visible in the location of the Event Canceled checkbox, if the checkbox is unchecked; clicking the button checks the corresponding checkbox and unchecks the Event Scheduled or Event Complete checkbox, if one is checked; the button is hidden after if it clicked, specifically, if the checkbox is checked; visible for Regional Reps and Super Admins) 
  * Event Complete (checkbox; defaults to unchecked; if checked, Event Status is set to Complete; validation error on the field if any of the rows in the Registration table are missing a selection for the "Attended?" column: "One or more of the registrants are missing attendance information."; validation error on the field if if the current date is before the Event Date: "This Event cannot be marked complete because the Event Date is still in the future.") 
  * Mark Complete (button; visible in the location of the Event Complete checkbox, if the checkbox is unchecked; clicking the button checks the corresponding checkbox and unchecks the Event Scheduled or Event Canceled checkbox, if one is checked; the button is hidden after if it clicked, specifically, if the checkbox is checked) 



  


  * Event Date (date field; defaults to blank; required if Event Status = Scheduled or Complete)
  * Event Time (time field; defaults to blank, showing a gray hint in Edit mode if blank: "e.g. 6:30 AM"; required if Event Status = Scheduled or Complete) 
  * Event Duration (visible if "Event Time" is not blank; includes two entry fields, and a non-zero entry is required in at least one of them if they are visible; the calendar event included with the emails is set to this length; the data entry fields are as follows: 
    * [  ] hours (number; no decimals; if a number with a decimal is entered, it automatically rounds to the nearest whole number; defaults to blank); 
    * [  ] minutes (drop list of "15", "30", "45", and blank; defaults to "0"; selecting the blank option sets it to "0"); 
    * note that when the record is out of edit mode, this displays as a time value, i.e. "4:00") 
  * Time Zone (required; drop list of all global time zones; filters down as you type; defaults to "(UTC-05:00) Eastern Time (US & Canada)", which displays as "Eastern") 
  * Event Format (required; drop list of Event Format list Items (In-Person / Virtual / Hybrid); defaults to blank) 
  * Registration Deadline (date field; defaults to blank; with the following validations:
    * if the "Always Requires Registration Deadline" checkbox is checked on the selected Event Type record: Required from creation of the Event record; 
    * otherwise: Required if Event Status = Scheduled) 
  * View My Registration (link; visible if the current logged-in user is registered for the Event; opens the corresponding Event Registration record) 
  * Event Registration Coordinator contact info (green text; displays a message, the top primary email, and/or primary phone number (the top non-Fax number first phone number) for the Contact selected in the "Registration Coordinator" field - see corresponding details; in the future we could add a "Register for Event" link/button to allow users to self-register) 
    * "For more info< or to register>:" (" or to register" only visible if there is no linked Registration record for the current user) 
    * "Email: <Registration Email>" (clickable link to open a new email) 
    * "Phone: <Registration Phone>" 
  * Event Description (optional; multi-line plain text field; used for entering a public description of the event)
  * Event Recording (optional; field for pasting in a recording link stored on another platform; for users who can edit the record, when out of Edit mode, this becomes a clickable link that opens the recording; for users who cannot edit the record, this displays as a clickable link)



  


Development Specification

Change Requests:

  * Tim Reitz 02/01/2025: [[[IN10958](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10960&)]] - ZSB - Events - Registration Record - "Event Type" Link
  * Tim Reitz 02/01/2025: [[[IN10960](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10962&)]] - ZSB - Events - Misc. Changes from 1/13/25 Client Walkthrough 
  * Tim Reitz 02/01/2025: [[[IN11085](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11087&)]] - ZSB - Events - Event Record - Add Duration Field


