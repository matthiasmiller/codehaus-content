7.6. Changes to Customers Needing Check-In Report for Phase 3a

  


Requirements

This is an editable 3-pane editable report of customers needing check-in within a selected time period. These panes show customers needing a check-in, as detailed below. 

  


From this report a user can can schedule (create) Check-In incidents for customers who are due for a check-in but do not have one scheduled yet, and can edit various details for Check-In incidents that already have been created/scheduled.

  


This would be accessed from a "Customers Needing Check-In" menu option in the Contacts section of the Home Menu. 

  


Title: "Customers Needing Check-In for <selected Tag(s)> Tag(s)" (if no Tags or all Tags are selected this displays "... for All Tag(s)")

  


Left Pane: The left pane is a placeholder pane that contains the filters/ask prompts and passes them along to the other two panes. This allows the right pane to be displayed even if the middle pane is empty.

  


Center Pane: This pane shows all Customers who are are (1) linked to Regions that are scheduled for a check-in in the selected time period and (2) do not have an open Check-In incident with the Check-In Month in the selected time period. Note that this pane does not include any incidents that have been created - it only shows customers / check-ins that need an incident to be created. 

  


Title: 

  * If Sales Rep filter is blank: Customers Needing Check-In
  * If Sales Rep filter has a selection: Customers Needing Check-In for <Sales Rep> 



  


Grouping Label: Customers Needing Check-In Incidents 

  


Columns: (note that the sequence has been changed)

  * Customer Name (link to record) 
  * Contact Tags (editable if blank, with a single-select drop list; read-only if the customer has one or more Tags set; comma-separated list, with text wrapping; the report cell includes an ellipsis child screen button to make additional edits if desired: 
    * Ellipsis button: Opens a child screen with a multi-select drop list of Tags and a "Continue" button; clicking "Continue" applies any changes to the Tags for the corresponding customer Contact record; note that this only changes one record at a time) 
  * Last Check-In (from the contact record) 
  * Recent Check-In (displays "Yes" in red text if there is a Check-In for the Customer with a Closed Date within the past 2 weeks; this gives the user context and helps avoid overly-frequent check-ins) 
  * Next Check-In (from the contact record)
  * Check-In Schedule (from the contact record; with text wrapping)



  


Note: Remove the extra space from the right-hand side of this pane, so that there's more space for displaying the right pane on a laptop screen. 

  


Grouped by: 

  * First by: Next Check-In Month ("Overdue" at the top, displaying any open Check-Ins from previous months; followed by months in the "Month Year" format with the earliest month first) 
  * Second by: Region (in alphabetical order)



  


Sorted by: Customer Name (in alphabetical order)

  


Buttons: 

  * Create Check-In Incidents for Selected (opens a prompt that says, "Are you sure you want to create Check-In incidents for the selected Customers?"; clicking Continue runs a background process to create Check-In incidents for the selected Customers in the center pane, filling the Check-In Month and the Check-In Notes based on the info on the Contact record, and setting the Assignee to the current logged-in user; the page will auto-refresh after the process runs) 



  


Save Type: Instant Save (when an editable field is changed, the record is saved as soon as the user selects another row on the report) 

  


Right Pane: This pane is a live-updating report that shows all Check-In incidents that are scheduled for the selected time period. Incidents created from the center pane will appear immediately in the right pane, highlighted in green at the top of the report; refreshing the screen will place the new incidents in their correct groupings / sorting. Unless otherwise specified, this will only include incomplete Check-Ins. 

Note: It appears that this pane only shows results for customers with the "Scheduled Check-Ins" checkbox filled. If a Check-In is scheduled for a customer with that box unchecked, it does not appear on this report. This should be changed so that it matches the spec above: "This pane shows all Check-In incidents that are scheduled for the selected time period." The Check-In Frequency column would need to be blank (or display "N/A") for these check-ins.

  


Title: All Scheduled Check-Ins

  


Info Note at the Top: "Newly created incidents will be highlighted in green and displayed at the top of the report. Refresh the report (press F5) to show them in the correct grouping."

  


Grouping Label: All Scheduled Check-Ins

  


Columns: (note that the sequence has been changed)

  * Customer Name
  * Incident (displays only the Incident ID; link to record) 
  * Customer Address (displays the address in the standard 2-line format)
  * Google Maps (link; displays as "Open in Maps") 
  * Last Check-In Date (displays the Closed date of the last closed Check-In incident for the Customer)
  * Due Date (editable) 
  * Check-In Notes (editable; wrapped text; wide enough for 60 characters if space allows; shows 2 lines when editing and scrolls if there are more than 2 lines)
  * Contact Tags (comma-separated; wrap text if needed) 



Note: make this column more narrow -- let's say approximately 20 characters wide. 

  * Assignee (required; editable; drop list of Incident Assignees) 
  * Check-In Schedule (from the customer's Contact record; is blank if N/A for the Customer; with text wrapping)



  


Grouped by: 

  * First by: Scheduled Check-In Month ("Overdue" grouping at the top, displaying any open Check-Ins from past months; followed by months in the "Month Year" format with the current month first and showing all months with at least one open Check-In incident) 
    * Check-In incidents with a blank Check-In Month field are displayed at the top of the current month's grouping.
    * If the "Show Completed Check-Ins" filter checkbox is checked, completed/closed Check-Ins will be shown in gray in a special "Completed" group at the bottom of the right pane, with the same sub-grouping and sorting. Since closed Check-Ins have the Month set by the Closed Date, this includes closed Check-Ins in their corresponding Months.
  * Second by: Region (in alphabetical order)



  


Sorted by:

  * First by: Scheduled Check-In Month (blank at the top)
  * Second by: Customer Name (in alphabetical order)



  


Save Type: Instant Save (when an editable field is changed, the record is saved as soon as the user selects another row on the report) 

  


Live Updating Report: As mentioned, this pane/report automatically updates without a refresh as soon as a record is created that meets the criteria to display on the report. New items are included at the top of the report, highlighted in green. Refreshing the screen (selecting the browser's refresh button or hitting F5 or Ctrl+R) places the new items in their correct groupings / sorting. 

  


Filters: 

  * Contact Tag (applies to both panes; multi-select drop list of all Contact Tags and "(No Tag)"; default to blank = all)
  * Sales Rep (applies to both panes; drop list of all employee Contacts; default to blank = all)
  * Region (applies to both panes; drop list of Regions for the selected Sales Rep, or all Regions if Sales Rep is blank)
  * Filter By (applies to both panes; required; drop list of Month, Month Range; default to Month)
  * Month (applies to both panes; visible if Filter By = Month; multi-select drop list of months; options displayed as "<Month> <Year>"; starts with the current month and showing 1 full year into the future, e.g. starting with June 2022, and going through May 2023; defaults to blank = all 12 months; looks at the Next Check-In Month for center pane, Check-In Month for right pane)
  * Check-In Month Start (applies to both panes; visible if Filter By = Month Range; drop list of months; options displayed as "<Month> <Year>"; starts with the current month and showing 1 full year into the future, e.g. starting with June 2022, and going through May 2023; defaults to blank = all; looks at the Next Check-In Month for center pane, Check-In Month for right pane)
  * Check-In Month End (applies to both panes; visible if Filter By = Month Range; drop list of months; options displayed as "<Month> <Year>"; starts with the current month and showing 1 full year into the future, e.g. starting with June 2022, and going through May 2023; defaults to blank = all; looks at the Next Check-In Month for center pane, Check-In Month for right pane)
  * Show Completed Check-Ins (applies only to the right pane; checkbox; if filled, the report will include completed check-in incidents) 



  


Menu Visibility: All users can view and edit

  


Other Notes: 

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1962167649](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1962167649)

  


  


Tim Reitz 08/17/2023: Adapted from [[[IN8275](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8277&)]] - ZTK - Changes to Customers Needing Check-In Report.

  


TODO_CCI: Tim Reitz 10/19/2023: The client's live system has a problem with the months being listed out of order. Could you please confirm that this updated report has resolved that / handles the sort order correctly, and let me know via email? Here's a link to the incident where we documented the issue: [[[IN8501](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8503&)]] - ZTK - Customers Needing Check-In report out of monthly order . Thanks!
