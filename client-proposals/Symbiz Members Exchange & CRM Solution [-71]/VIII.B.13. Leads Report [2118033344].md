8.2.13. Leads Report

  


Requirements

Overview: This is a report of all Lead-type contacts, with various filtering options.

  


Accessed from: 

  * Admin | Lead Management | View Leads (bypasses the filter screen to open the report directly). 
  * Admin | Lead Management | Leads by Info Meeting (opens a page with the report filters, for the user to search for a specific Info Meeting) 



  


Title: 

  * If the Info Meeting filter is blank: Leads
  * If the Info Meeting has a selection: Leads for <Event ID> Info Meeting



  


Columns: 

  * Name (name of Contact; link to open record)
  * Phone 
  * Lead Status 
  * Source
  * Industry (if there are multiple, comma-separated, with wrapping text) 
  * Church Affiliation
  * Info Meeting (displays the contents of the corresponding field/macro on the Contact record; if the Lead has Registration records for multiple Info Meetings, they display as a comma-separated list, with wrapping text)
  * Follow-up Completed (Yes/No according to the read-only checkbox on the Contact record; if checkbox is checked, displays as "Yes"; if checkbox is unchecked, displays as "No"; if "Info Meeting" filter is blank = all and there are multiple Registrations for a Contact, this column displays the information only for the Registration record for the most recent non-Canceled Info Meeting for which the Contact has a Registration) 



  


Grouped by: Based on the selection on the "Group by..." filter checkboxes:

  * If only "Group by Info Meeting" is checked: Grouped by Info Meeting, with a "No Info Meeting" grouping at the top for Leads not connected to an Info Meeting 
    * Note that if a Lead has Registration records for multiple Info Meetings, only one row is included, for the latest non-Canceled Event. 
  * If only "Group by Lead Status" is checked: Grouped by Lead Status. 
  * If both of these checkboxes are checked: Grouped first by Info Meeting, and second by Lead Status, with the same details as the individual grouping notes above. 



  


Sorted by: Name (alphabetically) 

  


Filters: 

  * Info Meeting (drop list of Event IDs for all Info Meeting-type Event records; default is blank = all; if one is selected, the report displays only current Leads that have a Registration record for that Event - note that this will not show leads that have since become members - that can be viewed via the Info Meetings by Contact report) 
  * Follow-up Completed (Required; drop list of Yes/No/All; defaults to "All"; if set to "Yes", report shows only Registrations that have the "Event Follow-up Completed" checkbox checked; if set to "No", report shows only Registrations that have the checkbox not checked) 
  * Lead Status (drop list of Lead Status items; default to blank = all)
  * Source (drop list of all Lead Source items; default to blank = all)
  * Industry (drop list of all Industry items; default to blank = all)
  * Church Affiliation (drop list of all Church Affiliation items; default to blank = all)
  * Group by Info Meeting (checkbox; defaults to not checked; see grouping details under "Grouped by" above)
  * Group by Lead Status (checkbox; defaults to checked; see grouping details under "Grouped by" above)



  


Buttons: 

  * New Lead (opens a blank new Lead-type Contact record)



  


Menu Visibility: Regional Reps and Super Admins (by virtue of the Admin Menu being restricted)

  


Other Notes:

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1032846230](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1032846230)

  


  


  


Change Requests:

  * Tim Reitz 07/01/2025: [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)


