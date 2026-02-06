6.4.1. Event Registrations Report

  


Requirements

*Documented 

  


Add the following new report:

  


This is a two-pane editable report of Events and their corresponding Registration records with various filtering options, and includes the option to create another Registration. This is used as the master report for all Registration records, and various versions of it are used for Events of different Types.

  


This is accessed from: 

  * Admin | Event Management | All Event Registrations (bypasses the filter screen to open the report directly) 
  * Members Menu | Events | My Event Registrations (bypasses the filter screen to open the report directly)
  * "View/Manage Event Registrations" link in the Registration Details (Internal) section of the Event record



  


Title: 

  * If the Event filter has only one selection: "Registrations for <Event Name> (<Event Type>)" 
  * If the Event filter is blank: "Event Registrations" 



  


Left Pane: This pane displays one or more Event records, based on selected filters, with one row for each Event. 

Subpane title (within report): Events

Columns: 

  * Event (displays the Event Name; link to open the corresponding Event record)
  * Date (displays the Event Date)



  


Grouped by: Event Status (from top to bottom: Scheduled, Tentative, Complete, Canceled)

  


Sorted by: Event Date (greatest at the top)

  


Right Pane: This pane displays Event Registration records for the last-selected Event in the left pane, and based on selected filters, with one row for each Registration record.

Subpane title (within report): "Registrations for <Event Name> (<Event Type>)" 

Columns: 

  * Registration Record (visible to everyone who can see the Event record; link to open the Event Registration record; link text displays as "View Registration") 
  * Registrant Name (visible to everyone who can see the Event record; link to open the Contact record; displays the Registrant Name; total row shows sum of Registrants)
  * Registration Status (data visible to the Registrant and all uplines; editable for Regional Reps & Super Admins)
  * Attended (data visible to the Registrant and all uplines; Yes/No/blank; editable for Regional Reps & Super Admins)
  * Notes (visible to and editable for Regional Reps & Super Admins; editable; not very wide, to allow space for other columns) 
  * Lead Follow-up Completed (displays as Yes/No on rows for "Lead" Registrant Type, blank on rows for other Registrant Types; visible to and editable for Regional Reps & Super Admins if the "Event Type" filter = "Info Meeting" or blank) 
  * Registrant Phone (data visible to the Registrant and all uplines)
  * Registrant Email (data visible to the Registrant and all uplines)
  * Bringing Guest (visible to the Registrant and all uplines; Yes/No/blank; editable for Regional Reps & Super Admins)
  * Guest Name (visible to the Registrant and all uplines; editable for Regional Reps & Super Admins; total row shows sum of Guests)
  * Guest Type (visible to the Registrant and all uplines; editable for Regional Reps & Super Admins)
  * Registrant Attending M & G (visible to the Registrant and all uplines; visible if "Event Type" filter = "Annual Summit" or blank; editable for Regional Reps & Super Admins; displays Yes/No; total row shows sum)
  * Guest Attending M & G (visible to the Registrant and all uplines; visible if "Event Type" filter = "Annual Summit" or blank; editable for Regional Reps & Super Admins; displays Yes/No; total row shows sum) 



  


Grouped by: N/A 

  


Sorted by: 

  * Standard: Registrant Name (alphabetically); 
  * Special: If a selection is made in the "Registrant" filter, the selected Registrant's row is highlighted and displayed at the top of this pane, and the rest are sorted with the standard sort order above. 



  


Filters: 

  * Event Status (drop list of Event Statuses; defaults to blank = all; applies to the left pane)
  * Event Type (drop list of Event Types; defaults to blank = all; applies to the left pane)
  * Event (drop list of all Event IDs, sorted by "Event Date" with the latest date at the top; filters down as you type; defaults to blank = all; applies to both the left pane and the right pane)
  * Registrant (drop list of Lead, Member, and Other Individual-type Contacts; users can see their own name and any/all downlines; filters down as you type; defaults to blank = all; applies to the left right pane, filtering the left pane to Events for which the selected Registrant has a Registration record) 
  * Registration Status (drop list of Event Registration Status list items and blank = all; defaults to blank; applies to both the left pane and the right pane)
  * Attended (drop list of Yes / No / blank = all; defaults to blank; applies to the right pane)
  * Meet & Greet Registration Only (visible if Event Type = Annual Summit or blank; visible only to Regional Reps and Super Admins; checkbox; defaults to unchecked; applies to the right pane; if checked, only the following columns are displayed: 
    * Registration Record
    * Registrant Name
    * Guest Name
    * Registrant Attending M & G
    * Guest Attending M & G
  * Lead Follow-up Completed (visible if Event Type = Info Meeting or blank; visible only for Regional Reps and Super Admins; drop list of Yes / No / blank = all; defaults to blank; applies to the right pane; if set to "Yes" or "No", only the corresponding rows for "Lead" Registrant Type are displayed)



  


Buttons: 

  * Add Registrant (runs on the right pane; always visible; opens the "New Registration prompt screen", with "Event" defaulted)  
  * Mark All as Attended (runs on the right pane; always visible; sets the "Attended" field to "Yes" for all that are blank (does not change "No" to "Yes"); clicking this button immediately makes the change on all of the records that need it and saves them, without using an automatic process)
  * Mark All Follow-up Completed (runs on the right pane; visible if the "Event Type" filter = "Info Meeting"; sets the "Lead Follow-up Completed" checkbox to checked for all that are not checked; clicking this button immediately makes the change on all of the records that need it and saves them, without using an automatic process)



  


Menu Visibility: Based on the visibility of the menu itself.

  


Editability: All editable columns are editable for Regional Reps and Super Admins only. 

  


Save Type: Instant Save 

  


Other Notes:

  * Warnings and errors from the Event Registration record apply when changes are made on the report.
  * This design does not include columns for the Guest Organization and Guest contact info, since that would make the report too wide. This assumes that the user will open the Registration record if edits are needed for these fields. However, if desired at some point in the future, a more complex design could be considered to allow editing those fields via the report as well.



  


Development Specification

Mockup: N/A 

_CCI: Tim Reitz 05/28/2024: Please send us screenshots of the report once you have it coded so we can review it prior to testing. Thanks!

  


  


Change Requests:

  * Tim Reitz 01/20/2025: [[[IN10946](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10948&)]] - ZSB - Events - Improvements for Creating Registrations 
  * 


  


TODO_EM / TODO_CCI: Tim Reitz 07/04/2024: For the Meet & Greet registration report, is the current spec the best option (having the "Meet & Greet Registration Only" checkbox), or should we just split it out into a separate simple report? 

  


TODO_CCI: Tim Reitz 05/31/2024: Note that "Mark All as Attended" and "Mark All Follow-up Completed" are modify all buttons (not x30s).
