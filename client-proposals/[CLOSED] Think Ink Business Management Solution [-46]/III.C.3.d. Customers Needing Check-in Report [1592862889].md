3.3.3.4. Customers Needing Check-in Report

  


Requirements

This is an editable 3-pane editable report of customers needing check-in within a selected time period. These panes show customers needing a check-in, as detailed below. 

  


From this report a user can can schedule (create) Check-In incidents for customers who are due for a check-in but do not have one scheduled yet, and can edit the Check-In Date and Check-In Notes for Check-In incidents that already have been created/scheduled.

  


This would be accessed from a "Customers Needing Check-In" menu option in the Contacts section of the Home Menu. 

  


Title: Customers Needing Check-In

  


Left Pane: The left pane is a placeholder pane that contains the filters/ask prompts and passes them along to the other two panes. This allows the right pane to be displayed even if the middle pane is empty.

  


Center Pane: This pane shows all customers who are are scheduled for check-ins in the selected time period but do not have an open Check-In incident. Note that this pane does not include any incidents that have been created - it only shows customers/check-ins that need an incident to be created. 

  


Title: Customers Needing Check-in Incidents

  


Grouping Label: Customers Needing Check-in Incidents 

  


Columns: 

  * Customer Name (link to record) 
  * Contact Tags (comma-separated)
  * Last Check-In Date (from the contact record) 
  * Check-In Frequency (from the contact record)
  * Next Check-In Date (from the contact record)



  


Grouped by: Next Check-In Month (current month at the top; in the "June 2022" format) 

  


Sub-grouped by: Next Check-In Week (current week at the top; in the "Week of mm/dd/yyyy" format, where "mm/dd/yyyy" is Sunday of the week)

  


Sorted by: Next Check-In Date (earliest date at the top)

  


Buttons: 

  * Create Check-In Incidents for Selected (opens a prompt that says, "Are you sure you want to create Check-In incidents for the selected Customers?"; clicking Continue runs a background process to create Check-In incidents for the selected Customers in the center pane, filling the Check-In Date and the Check-In Notes; the page will auto-refresh after the process runs) 



  


Right Pane: This pane shows all Check-In incidents that are scheduled for the selected time period. Incidents created from the center pane for the selected time period will appear in the right pane. Unless specified, this will only include incomplete Check-Ins. 

  


Title: All Scheduled Check-Ins

  


Grouping Label: All Scheduled Check-Ins

  


Columns: 

  * Incident (ID; link to record) 
  * Customer Name 
  * Contact Tags (comma-separated)
  * Last Check-In Date (from last closed Check-In incident)
  * Check-In Frequency (from the customer's contact record)
  * Check-In Date (editable) 
  * Check-In Notes (editable)
    * For the Check-In Notes column, allow text to wrap and make the field larger so that there can be 2 entry lines visible at a time (more lines visible with scrolling).



  


Grouped by: 

  * Check-In Month (current month at the top; in the "June 2022" format) 
  * If "Show Completed Check-Ins" is selected, these will be shown in gray in a special "Completed" group at the bottom of the right pane, with the same sub-grouping



  


Sub-grouped by: Check-In Week (current week at the top; in the "Week of mm/dd/yyyy" format, where "mm/dd/yyyy" is Sunday of the week) 

  


Sorted by: Check-In Date (earliest date at the top)

  


Save Type: Instant Save (when an editable field is changed, the record is saved as soon as the user selects another row on the report) 

  


Filters: 

  * Contact Tag (applies to both panes; multi-select drop list of all Contact Tags; default to blank = all)
  * Sales Rep (applies to both panes; drop list of Sales Reps; default to blank = all)
  * Filter By (applies to both panes; required; drop list of Month, Date Range; default to Month)
  * Month (applies to both panes; visible if Filter By = Month; multi-select drop list of months; options displayed as "<Month> <Year>"; starts with the current month and showing 1 full year into the future, e.g. starting with June 2022, and going through May 2023; defaults to blank = all 12 months; looks at the Next Check-In Date for center pane, Check-In Date for right pane)
  * Check-In Date Start (applies to both panes; visible if Filter By = Date Range; date field; default to 30 days prior to today; blank = all; looks at the Next Check-In Date for center pane, Check-In Date for right pane)
  * Check-In Date End (applies to both panes; visible if Filter By = Date Range; date field; default to blank = all; looks at the Next Check-In Date for center pane, Check-In Date for right pane)
  * Show Completed Check-Ins (applies only to the right pane; checkbox; if filled, the report will include completed check-in incidents, looks at Check-In Date) 



  


Menu Visibility: All users can view and edit

  


Other Notes: 

  * Any uncompleted/overdue check-ins from previous months or weeks will be listed in the current month and week. This applies both to customers needing checkins in the center pane (customers who are overdue for a check-in but don't have an incident should be listed in the current month and week) and to incidents in the right pane (check-in incidents that are overdue should be listed in the current month and week).



  


Dev Spec

Make Month a multi-select drop list.

  


The report sort should be ReplaceNA(NextCheckInDate, ProposedNextDate)

  


Check-ins will be placed in the calculated month based on the last check-in date + Check-in frequency.

  


Development Specification

Austin Priest 01/20/2023: [[[IN7191](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-7193&)]] - ZTK - Customers Needing Check-In Report Bug (platform limitation)

Austin Priest 05/17/2023: [[[IN7294](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-7296&)]] - ZTK - Check-In Notes on the Customers Needing Check-In Report

  


  


  


Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1962167649](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1962167649)

  


Make Month a multi-select drop list.

  


CCI: This is a New Records spreadsheet that shows any existing check-in incidents that match filters (typically only open incidents, but if "Show completed" is checked then also closed incidents). It will also add new blank check-in incidents for any clients that don't have an open check-in incident.

  


The Button can just be a Modify button that sets the incident's check-in date.

  


The report sort should be ReplaceNA(NextCheckInDate, ProposedNextDate)

  


Check-ins will be placed in the calculated month based on the last check-in date + Check-in frequency.

Tim Reitz 06/21/2022: I think this refers to checkins that still need to be created? 

  


DONE_CCI: Tim Reitz 06/21/2022: How would we normally handle partial weeks (i.e. week of June 26-July 22)?

Matthias Miller 06/21/2022: This sounds fine. CCI can confirm. See mockups as well

Tim Reitz 06/22/2022: Ellis said new design looks fine and doesn't change spec. 

  


DONE_CCI: Tim Reitz 06/21/2022: See the following updates:

  * Option 3 for scheduling new check-ins (
  * Adding column for Check-In Frequency (to give the user an easy reference for setting the Next Check-In Date)
  * Adding subgrouping for Week (client mentioned wanting this on today's call)
  * Added note to the button description: "if a row is included that already has a Check-In Date, that row will be skipped"



Mentioning this in case it changes any of the pricing or Dev Specs.

Tim Reitz 06/22/2022: Ellis said new design looks fine and doesn't change spec.
