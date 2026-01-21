7.4. Growth Ring Meeting Record

  


Requirements

Overview: The Growth Ring Meeting record stores information for a monthly meeting of a Growth Ring Group. More details can be seen in the Workflow for Growth Ring Meetings section.

  


Accessed via:

  * Growth Ring Meetings Report
  * Growth Ring Record
  * Members Menu | My Next Meeting Details | My Next Growth Ring Meeting 
  * etc.



  


Sections and Fields: 

  


  * Growth Ring Meeting Details section:
    * Meeting Status (read-only; displays in the section header; options are Tentative, Scheduled, Complete, Canceled:)
      * Tentative: default status for new records; if none of the following checkboxes are filled: Scheduled, Complete, Canceled; requires only the Growth Ring Group and Meeting Date to be specified. 
      * Scheduled: if the Meeting Scheduled checkbox is filled.
      * Complete: if the Meeting Complete checkbox is filled.
      * Canceled: if the Meeting Canceled checkbox is filled.
    * System ID (hidden; auto-set ID; unique identifier for the record) 
    * Growth Ring Meeting ID (auto-set and read-only; in the following format: "<Growth Ring Group ID> \- <Meeting Date>"; if the Meeting Status = Canceled, this ID also includes the following suffix: "Canceled"; used to display the Meeting on a report or a drop list)
    * Growth Ring Group (required; drop list of active Growth Ring Groups that the user has permission to edit; displays the Growth Ring Group Descriptions; editable in the detail screen for new records)
    * View/Edit Group (link to open the corresponding Group record; visible to the right of the Group drop list if a Group is selected) 
    * Meeting Date (required; date; defaults to blank; validate against duplicate dates for the same Group - error message on Save: "This Growth Ring Group already has a Meeting for the same date."; validate against dates more than 90 days in the future - error message on Save: "The Meeting Date cannot be more than 90 days in the future."; warning on Save for Tentative and Scheduled if the date is in the past: "The Meeting Date is in the past."; label displays as "Tentative Meeting Date" if Status = Tentative)
    * Meeting Time (required if "Meeting Status" = "Scheduled"; time field; defaults to blank, showing a gray hint in edit mode if blank: "e.g. 6:30 AM") 
    * Meeting Duration (visible if "Meeting Time" is not blank; includes two entry fields, and a non-zero entry is required for at least one of them if they are visible; the calendar event included with the emails is set to this length; the data entry fields are as follows: 
      * [  ] hours (number; no decimals; if a number with a decimal is entered, it automatically rounds to the nearest whole number; defaults to "2"); 
      * [  ] minutes (drop list of "15", "30", "45", and blank; defaults to "0"; selecting the blank option sets it to "0"); 
      * note that when the record is out of edit mode, this displays as a time value, i.e. "2:00") 
    * Time Zone (required; drop list of all global time zones; defaults to the selected Time Zone on the linked Growth Ring Group record) 
    * Meeting Scheduled (checkbox; defaults to cleared; to be checked via the "Schedule Meeting" button when the meeting date is confirmed; on the first Save after it is checked, the "Create Tentative Growth Ring Meeting" runs to create a new Tentative Meeting for the same Growth Ring Group, if needed; unchecking the checkbox makes the Schedule Meeting button visible; visible to Attendees and uplines) 
    * Schedule Meeting (button; visible in the location of the Meeting Scheduled checkbox, if the checkbox is unchecked; clicking the button checks the corresponding checkbox and unchecks the Meeting Canceled or Meeting Complete checkbox, if one is checked; the button is hidden after if it clicked, specifically, if the checkbox is checked) 
    * Meeting Canceled (checkbox; defaults to unchecked; if checked, Meeting Status is set to Canceled; note that fields on the record will still be editable; if the checkbox is checked, warning on save if there is not a Tentative or Scheduled Meeting with a Meeting Date after this Meeting's date for the same Growth Ring: "You have not scheduled next month's Meeting yet. Click "Schedule Next Meeting" after you save."; visible to Attendees and uplines)
    * Cancel Meeting (button; visible in the location of the Meeting Canceled checkbox, if the checkbox is unchecked; clicking the button checks the corresponding checkbox and unchecks the Meeting Scheduled or Meeting Complete checkbox, if one is checked; the button is hidden after if it clicked, specifically, if the checkbox is checked) 
    * Meeting Complete (checkbox; defaults to unchecked; if checked, Meeting Status is set to Complete; automatically checked if any row in the "Attended" column of the "Attendance" table is set to "Yes"; validation error on the field if if the current date is before the Meeting Date: "This meeting cannot be marked complete because the Meeting Date is still in the future."; if checkbox is checked, warning on save if there is not a Scheduled Meeting with a Meeting Date after this Meeting's date: "You have not scheduled next month's Meeting yet. Click "Schedule Next Meeting" after you save."; visible to Attendees and uplines) 
    * Mark Complete (button; visible in the location of the Meeting Complete checkbox, if the checkbox is unchecked; clicking the button checks the corresponding checkbox and unchecks the Meeting Scheduled or Meeting Canceled checkbox, if one is checked; the button is hidden after it is clicked, specifically, if the checkbox is checked) 
    * Schedule Next Meeting (link; visible to Facilitator and uplines if the current date is on or after the "Meeting Date" for this Meeting and there is not a Scheduled Meeting with a "Meeting Date" after this Meeting; opens the future Tentative Meeting if there is one; otherwise creates and opens a new Meeting record with Growth Ring Group defaulted) 



  


  * Host (required if "Meeting Status" = "Scheduled" or "Complete"; drop list of names of the members in the Group and an option for "Other"; visible to Attendees and uplines)
  * Other Host Details (visible and required if Host = "Other"; plain text field; visible to Attendees and uplines)
  * Meeting Location (required if "Meeting Status" = "Scheduled" or "Complete"; drop list of "Host Address", "Virtual", and "Other"; default to blank; visible to Attendees and uplines)
  * Host Address (visible if "Meeting Location" = "Host Address"; auto-set and read-only; displays the Primary address of the selected Host; note that if Host = "Other", this will be blank; visible to Attendees and uplines)
  * Virtual Meeting Link (visible and required if "Meeting Location" = "Virtual"; field for pasting in a link; for users with editability, the link will be displayed beside or below the field for easy opening; visible to Attendees and uplines)
  * Other Address (label & fields visible and required if "Meeting Location" = "Other"; all visible to Attendees and uplines:)
    * Street (plain text)
    * City (plain text)
    * State (drop list of state & province abbreviations)
    * Zip (plain text field)
  * Development Resource (required if "Meeting Status" = "Scheduled" or "Complete"; drop list of all Development Resources, grouped by Status and sorted by full description; full description displays in the format of "<Title>, <Author / Creator> (<Resource Status>)"; list filters down as you type; if a Resource record is edited, the full description will be updated here; for standard members this will appear as a link that opens the corresponding record)
  * Add New Resource (link; visible if no Resource is selected; opens a blank new Development Resource record; after saving the new record, it will appear on the Development Resource list; visible to Attendees and uplines) 
  * View Resource (link; in the same location as the "Add New Resource" link; visible if a Resource is selected, visible if in edit mode; note that the drop list item already turns into a link when out of edit mode)
  * View Group Members' Reviews (link; visible if there is a Development Resource selected; opens the Development Resource Reviews report, filtered to the selected Development Resource and the current Meeting; visible to Attendees and uplines)
  * View Growth Ring Meeting Goals (link; opens the Growth Ring Goals report, filtered to the corresponding Growth Ring Group and corresponding Meeting; visible to Attendees and uplines)
  * Meeting Secretary (required if Status is Scheduled or Complete; defaults to the Group's Facilitator; drop list of meeting attendees; this assignee gets the Prepare Symbuzz Extra Posts notification) 
  * New Lead (link; visible to Regional Reps and Super Admins; opens a new Contact record with Type = Lead) Internal Meeting Notes (memo with formatting options; can be used to document notes about the meeting, guests, additional resources, etc.; visible to Attendees and uplines) 



  


  * My Meeting Items section (section and fields visible to Attendees and uplines)
    * Print Book/Resource Impact Worksheet (link; opens the PDF saved in the "Book/Resource Impact Worksheet" field on the Silverloom Settings page; opens in a new tab if the Meeting page is in edit mode) 
    * My Goals for This Meeting (link; opens the Growth Ring Goals page linked to this Meeting for the current logged-in user, or creates the new Growth Ring Goals page if none exists; opens in a new tab if the Meeting page is in edit mode) 
    * Print Meeting Goals Worksheet (link; opens the "Print Meeting Goals Worksheet" prompt screen - see corresponding spec)
    * My Resource Review & Takeaways (link; visible if there is a Development Resource selected for the Meeting; opens the Development Resource Review page for the selected Resource for the current logged-in user, or creates the new Review page if no review exists; opens in a new tab if the Meeting page is in edit mode) 
    * "My Resource Review & Takeaways - No Resource Selected Yet" (message in gray text, in the location of the corresponding link; visible if there is no Development Resource selected for the Meeting; informational only, to let the user know why the link is not visible) 



  


  * Attendance (embedded spreadsheet with the following:) 
    * Columns: 
      * Member (required; drop list of current Members of the Growth Ring Group; when the meeting record is created, the table is pre-filled with a row for each current member of the Growth Ring Group; list is updated nightly) 
      * Facilitator (checkbox; automatic based on the Growth Ring Group; read-only)
      * Attended (required if Status = Complete; drop list of blank/Yes/No; defaults to blank; when any row is set to "Yes", checks the "Meeting Complete" checkbox; validation error message on Save if Status = Complete and one or more members are missing attendance information) 
      * View Goals (displays as "Link" if the Member has a Goals record linked to the Meeting; opens the corresponding Goals record) 
      * Goals Set (number field with no decimals; used to track how many goals each Member set to be completed for the Meeting; with the following special behaviors: 
        * if a Goals record exists for the corresponding Member and Meeting: auto-set and read-only; dynamically displays the number of rows on the "Goals" embedded spreadsheet that have an entry in "Description"; 
        * if no Goals record exists for the corresponding Member and Meeting: editable and optional)  
      * Goals Achieved (number with no decimals; used to track how many set goals each Member achieved; with the following special behaviors:
        * if a Goals record exists for the corresponding Member and Meeting: auto-set and read-only; dynamically displays the number of rows on the "Goals" embedded spreadsheet that have an entry in "Description" and have "Achieved" set to "Yes"; 
        * if no Goals record exists for the corresponding Member and Meeting: editable and optional; validate that this number is not greater than the "Goals Set" for the same member - error on the field: "Goals Completed is greater than Goals Set for this member.")  
      * Meeting Rating (optional; drop list of 1-5, with 5 being the best; used to track each member's overall general rating of the meeting) 
    * Automatically sorted by: Same as the Growth Ring Group Members Details table on the Group record
    * Buttons to add/remove rows ("Add"/"Delete") 
    * Show 14 rows without scrolling
    * There is a nightly background process that runs to update the Attendance list for each Growth Ring Meeting with a Status of Tentative or Scheduled. This process checks the Growth Ring Group Members table on the Growth Ring Group record and updates the Attendance table on any Scheduled Growth Ring Meeting record for that Group, adding or removing members as needed.



  


  * Growth Ring Health Report section (section and fields visible to Attendees and uplines): 
    * Total Group Members (optional; number with no decimals; defaults to blank when the record is created; when the Meeting Status is set to Scheduled, auto-sets to the current number of Members on the "Attendance" embedded spreadsheet; remains editable to allow overriding it; at some point this can be used to set up an alert if the number of reported group members is different from the number of Member-type Contacts linked to the Group record) 
    * New Groups Started (optional; number with no decimals; defaults to blank) 
    * Symbiz Core Value Stories (optional; number with no decimals; defaults to blank; used to track the number of reported incidents of exemplifying Symbiz values) 
    * Members Added to Group (optional; number field with no decimals; defaults to blank) 
    * Members w/ Symbiz Vision Memorized (optional; number with no decimals; defaults to blank) 
    * Book Impact Completed / Application Made (optional; number with no decimals; defaults to blank)
    * Total Goals Set (number with no decimals; auto-set and read-only; displays the sum of "Goals Set" from the Attendance embedded spreadsheet) 
    * Total Goals Achieved (number with no decimals; auto-set and read-only; displays the sum of "Goals Completed" from the Attendance embedded spreadsheet) 
    * Average Meeting Rating (number rounded to 1 decimal place; auto-set and read-only; displays the average of "Meeting Rating" selections from the Attendance embedded spreadsheet)



  


  * Symbuzz Extra Posts section: 
    * Post Entry Date (date field; auto-set and read-only; displays the date that the first entry was saved in one of the Post fields)
    * Reviewed (checkbox; visible to Attendees and uplines; editable for all Super Admins; defaults to unchecked; designates all three posts as reviewed and approved, but posts are included in Symbuzz Extra even if the checkbox is not checked) 
    * Growth Ring News Post (multi-line plain text field; editable for the Meeting Secretary, Facilitator, and all uplines) 
    * Prayer Requests Post (multi-line plain text field; editable for the Meeting Secretary, Facilitator, and all uplines) 
    * Networking Requests Post (multi-line plain text field; editable for the Meeting Secretary, Facilitator, and all uplines) 
    * Print Growth Ring Health Report (blank) (link; opens the PDF from the "Growth Ring Health Report" memo on the Silverloom Settings page, so that it can be printed for an offline Secretary to write out their posts)



  


  * Additional Validations: 
    * Warning on Save when Meeting Status = Complete if there is one or more Meetings for the same Group with Meeting Date set to a date in the past and Meeting Status = Tentative or Scheduled: "There is one or more past Growth Ring Meeting(s) that need to be marked as Complete or Canceled: <date>, <date>, and <date>."



  


Data Access: See the Data Access Controls section of the proposal, and specific fields & sections on this record, for details.

  * High-level overview of visibility: 
    * Group Members: Full record 
    * Non-Group Members: Details specific to and relevant to Symbuzz Extra. 
  * High-level overview of editability: 
    * Secretary: Only the Post memos
    * Facilitator and corresponding Regional Rep: Everything except the Reviewed checkbox
    * Super Admins: Everything 



  


Special Considerations:

  * Copy Record: Clear the Meeting Date
  * Delete Record: Prevent deletion if Status is not Canceled (error message: "This Growth Ring Meeting record cannot be deleted because its Status is not Canceled.")
  * Merge Record: Only can be merged by Super Admins. All other users would get a message to contact an Admin to resolve a duplicate.



  


Other Notes:

  * A standard member can only see Growth Ring Meetings for which their name appears in the Attendance table (whether or not they actually were in attendance). This means that if a member changes to another group, he can still view meetings for his previous group, but only ones in which he is listed in the Attendance table.
  * Facilitators can view and edit Meetings for Groups of which they are marked as the Facilitator. This means that technically they can edit any Meetings on which they are set as the Facilitator, even if they are no longer Facilitator for that Group or a Member of that Group.
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

TODO_VA: Tim Reitz 07/10/2025: Let's break this one out into separate sub-sections for the detail screen sections (like we did for the event record, etc.). 

  


  


Change Requests: 

  * Tim Reitz 03/07/2024: [[[IN9076](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9078&)]] - ZSB - Growth Ring Meeting Record - Misc Items
  * Tim Reitz 03/29/2024: [[[IN9471](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9473&)]] - ZSB - Growth Ring Meeting - Add Meeting Time
  * Tim Reitz 04/03/2024: [[[IN9217](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9219&)]] - ZSB - Growth Ring Meetings - Changes to Meeting Scheduling
  * Tim Reitz 04/08/2024: [[[IN9775](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9777&)]] - ZSB - Growth Ring Meeting - Fix "Group" Drop List
  * Tim Reitz 04/08/2024: [[[IN9637](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9639&)]] - ZSB - Improve User Workflow for Growth Ring Meetings (prev. Add links to Members Menu and...)
  * Tim Reitz 04/11/2024: [[[IN8960](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8962&)]] - ZSB - Add Features for Symbuzz Extra (prev. called Cross Network Forum)
  * Tim Reitz 04/11/2024: [[[IN9417](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9419&)]] - ZSB - Symbuzz Extra - Revisions (#1)
  * Tim Reitz 06/10/2024: [[[IN9847](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9849&)]] - ZSB - Growth Ring Meeting Record - Various Changes April/May 2024
  * Tim Reitz 07/19/2024: [[[IN10048](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10050&)]] - ZSB - Growth Ring Meeting Record - Duplicate Meeting Date bug
  * Tim Reitz 07/19/2024: [[[IN9997](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9999&)]] - ZSB - Fix Growth Ring Meeting visibility error
  * Tim Reitz 07/20/2024: [[[IN9853](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9855&)]] - ZSB - Growth Ring Meeting Record - Add Growth Ring Health Report Feature
  * Tim Reitz 09/03/2024: [[[IN9889](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9891&)]] - ZSB - Add Time Zone Feature (for Groups & GR Meetings)
  * Tim Reitz 09/03/2024: Tim Reitz 09/03/2024: (added in) Tim Reitz 09/03/2024: [[[IN9858](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9860&)]] - ZSB - User Notifications - Add .ics Calendar Invites with New GR Meeting Notification 
  * Ben Reitz 05/01/2025: [[[IN10854](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10856&)]] - ZSB - Growth Ring Meeting record - Add / change fields
  * Ben Reitz 08/01/2025: [[[IN10720](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10722&)]] - ZSB - Clarify Terminology on Field Names / Links / Printouts
  * Ben Reitz 09/17/2025: [[[IN11622](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11624&)]] - ZSB - Growth Ring Meeting record - Change "Dev. Resource / Impact Submitted" field
  * Ben Reitz 09/17/2025: [[[IN10074](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10076&)]] - ZSB - Growth Ring Goals - Add "Meeting Goals Worksheet" printout (prev. Add "Print Goals" button)
  * Ben Reitz 11/26/2025: [[[IN12104](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12106&)]] - ZSB - Meeting record - Automatically mark Meetings as "Complete" (prev. Add warning if not marked as Complete or Canceled)
  * Ben Reitz 11/26/2025: [[[IN10169](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10171&)]] - ZSB - Growth Ring Meeting Record: Never Allow Duplicate Dates for Same Group
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=751445068](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=751445068)

  


  


Tim Reitz 05/09/2023: Per Matthias, for "Meeting Complete" and "Meeting Canceled", we should spec this out as an editable macro with Status as the source of truth. Checkboxes toggle.
