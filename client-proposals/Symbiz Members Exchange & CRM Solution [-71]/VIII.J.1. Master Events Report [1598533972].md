8.10.1. Master Events Report

  


Requirements

Overview: This is a report of Event records with various filtering options, and includes the option to set up a new Event. This is used as the master report for all Event records, and various versions of it are used for the different Event Types.

  


Accessed from: 

  * Admin | Event Management | All Events (bypasses the filter screen to open the report directly) 
  * Members Menu | Events | All Events (bypasses the filter screen to open the report directly)
  * Various other menu options (see other sections of the proposal)



  


Title:

  * If "Event Type" filter = blank: "All Events"
  * If "Event Type" filter= "Annual Summit": "Annual Summits"
  * If "Event Type" filter = "Industry Forum": "Industry Forums"
  * If "Event Type" filter = "Info Meeting": "Info Meetings"
  * If "Event Type" filter = "Launch Meeting": "Launch Meetings"



  


Columns:

  * Event Status
  * Event Type
  * Execution Status (column visible only to Regional Reps and Super Admins)
  * Event Name (link to record) 
  * Date 
  * Time
  * Time Zone
  * Industries (column visible if Event Type filter = Industry Forum or blank; comma-separated with text wrapping, if multiple)
  * Description (displays the text from the Event Description field, with text wrapping)
  * Virtual Event (Yes / No)
  * In-Person Event (Yes / No)
  * Venue (column visible if Event Format filter = In-Person, Hybrid, or All)
  * Address (column visible if Event Format filter = In-Person, Hybrid, or All; displays the full address in the standard 2-line address format)
  * Registration Count (column visible only to Regional Reps and Super Admins; displays the "Total" Registrants)
  * Registration List (link to open the right pane of the Registrations report, filtered to the corresponding Event; link text displays as "View Report"; column visible only to Regional Reps and Super Admins)
  * Attendance Count (column visible only to Regional Reps and Super Admins; displays the "Total" Attendees)
  * Symbiz Presenter (column visible only to Regional Reps and Super Admins; visible if Event Type = Industry Forum, Info Meeting, or Launch Meeting)
  * Event Host (column visible only to Regional Reps and Super Admins; visible if Event Type = Industry Forum, Info Meeting, or Launch Meeting)



  


Grouped by: the selection in the "Group By" filter:  

  * if Group By = Event Type: display the Type in the group headings and list the groupings in alphabetical order.
  * if Group By = "Month": display the group headings in the format of "<Month> <Year>" and show the greatest month + year at the top.
  * if Group By = Status: display the Status in the group headings and list them in the list sequence.
  * if Group By = blank: display no groupings and follow the specced sort order.



  


Sorted by: 

  * First by Event Date (greatest date at the top) 
  * Second by Event Time (greatest at the top) 



  


Filters: 

  * Event (drop list of all Event IDs; filters down as you type; defaults to blank = all; allows the report to be run for a single Event record)
  * Event Type (drop list of Event Type list items and blank = all; defaults to blank = all or the selection passed through from the menu option)
  * Industry (visible if "Event Type" filter = "Industry Forum" or blank; multi-select drop list of all Industries; defaults to blank = all)
  * Symbiz Presenter (visible to Regional Reps and Super Admins; visible if "Event Type" = "Industry Forum", "Info Meeting", or "Launch Meeting"; drop list of Contacts that are selected as "Symbiz Presenter" on at least one Event; defaults to blank = all) 
  * Event Host (visible to Regional Reps and Super Admins; visible if "Event Type" = "Industry Forum", "Info Meeting", or "Launch Meeting"; drop list of Contacts that are selected as "Event Host" on at least one Event; defaults to blank = all) 
  * Format (drop list of "Virtual", "In-Person", "Hybrid", "All"; defaults to "All")
  * State/Province (visible if "Format" filter = "In-Person", "Hybrid", or "All"; drop list of US states & Canadian provinces; looks at the state or province in the Event Address; defaults to blank = all) 
  * Event Date Start (date field; blank = all; defaults to 6 months before the current date; looks at the Event Date) 
  * End (date field; defaults to blank = all; looks at the Event Date)
  * Group By (drop list of "Event Type", "Month", "Status", and blank = N/A; defaults to "Status")



  


Buttons: 

  * New Annual Summit (Visible only to regional rep or super admin; visible if "Event Type" filter = "Annual Summit" or blank; opens a new Event record with "Type" = "Annual Summit")
  * New Industry Forum (Visible only to regional rep or super admin; visible if "Event Type" filter = "Industry Forum" or blank; opens a new Event record with "Type" = "Industry Forum")
  * New Info Meeting (Visible only to regional rep or super admin; visible if "Event Type" filter = "Info Meeting" or blank; opens a new Event record with "Type" = "Info Meeting")
  * New Launch Meeting (Visible only to regional rep or super admin; visible if Event Type filter = Launch Meeting or blank; opens a new Event record with Type = Launch Meeting)



  


Menu Visibility: 

  * Items on the Admin Menu: Regional Reps and Super Admins (by virtue of the Admin Menu being restricted)
  * Item(s) on the Members Menu: All users



  


Other Notes:

  * N/A



  


Development Specification

Change Requests:

  * Tim Reitz 07/10/2025: : Added in [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)


