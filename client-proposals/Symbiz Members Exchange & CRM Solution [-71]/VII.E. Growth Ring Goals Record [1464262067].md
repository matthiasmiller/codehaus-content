7.5. Growth Ring Goals Record

  


Requirements

Overview: This record tracks a individual member's goals for a specific Growth Ring Meeting. Goals must be set after a meeting for the next meeting; for example, goals for the June meeting need to be set right after the May meeting. However, a user can also set up goals for any meeting in the future for which there is a Meeting record created.

  


These are set up in the Solution by members with online access. For members without online access, the member fills out a paper sheet (the Growth Ring Worksheet Printout - see the corresponding section of the proposal), and the Facilitator fills out the record for them.

  


Accessed via:

  * All Growth Ring Goals Report
  * My Growth Ring Goals Report
  * View Growth Ring Goals link on the Growth Ring Meeting record
  * etc.



  


Sections and Fields: 

  * Previous Meeting's Goals (link; visible if a Meeting record exists for a meeting before the one selected on this Goals record; opens the Goals record from the previous meeting for the selected Member and Group; if there is no Goals record for the next meeting, this opens a blank new Goals record with Group, Member, and Meeting defaulted; if there is not another previous Meeting before the current Goals' Meeting, the link is replaced with the following message in gray text: "No previous meetings.") 
  * My Goals History (link; opens the My Growth Ring Goals report for the selected Member) 
  * Next Meeting's Goals (link; visible if a Meeting record exists for a meeting after the one selected on this Goals record; opens the Goals record from the following meeting for the selected Member and Group; if there is no Goals record for the next meeting, this opens a blank new Goals record with Group, Member, and Meeting defaulted; if there is not another Meeting scheduled after the current Goals' Meeting, the link is replaced with the following message in red text: "No future meetings.") 



  


  * Growth Ring Goals Overview section:
    * Growth Ring Goal ID (auto-numbered and read-only; unique identifier for the record)
    * Status (auto-set and read-only; Upcoming / In Progress / Overdue / Complete; according to the following:)
      * Upcoming: on or before the Meeting Date of the previous Meeting.
      * In Progress: after the Meeting Date of the previous Meeting has passed, if the "Complete" checkbox has not been filled.
      * Overdue: on or after the Meeting Date for the linked Meeting, if the "Complete" checkbox has not been filled.
      * Complete: if the "Complete" checkbox has been filled.
    * Complete (checkbox; defaults to read-only, and becomes editable 1 week before the Meeting Date; defaults to not checked; error on the field if any of the "Achieved" fields on the Goals embedded spreadsheet are blank - "One or more goals are lacking achievement information."; sets the status to Complete; warning on Save ("You have not set goals for the next meeting. Click "Next Meeting's Goals" after you save this page.") if this checkbox is checked and all of the following conditions are true:
      * the Status of this Goals record is Complete, 
      * the Status of the Meeting linked to this record is Scheduled or Complete, 
      * there is a Meeting record for the same Group with a Meeting Date in the future, 
      * there is no Growth Ring Goals record for the next Meeting for the Group)
    * Member (has the following behaviors:
      * if the current user is a standard Member, this is auto-set and becomes read-only after the initial save, defaulting to the current user.
      * if the current user is a Facilitator or an upline, this is editable and required, drop list of all downlines of the current user with active memberships; defaults to blank unless created from somewhere where this is auto-filled, like a Contact record or the Growth Ring Goals report.)
    * Growth Ring Group (hidden if Member is blank; visible if a Member is selected; drop list of Descriptions of the Growth Ring Groups of which the selected Member is a member; auto-set and read-only if there is only one Group; editable and required if there is more than one Group)
    * Open Group (link to open record; visible if a Group is selected; displayed to the right of the Growth Ring Group field) 
    * Growth Ring Meeting (required; drop list of all Meetings for the selected Growth Ring Group, with the earliest Meeting date at the bottom; designates the Meeting for which these goals should be completed; validate against duplicate Goals records for the same Meeting - error message on the field: "You already have set goals for this meeting. Select a different meeting, or open the corresponding goals page.") 
    * View Meeting Details (link; visible if a Meeting is selected; displayed to the right of the Growth Ring Meeting field; opens the corresponding Meeting record)
    * This Meeting's Development Resource (link; visible if a Meeting is selected; opens the Development Resource for the corresponding Meeting) 



  


  * Goals section: 
    * Copy Last Meeting's Goals (button; visible on creation of the new Goals record if the Member has a Goals record for a previous Meeting; visible in edit mode for users who can can edit the Goals record until this or the "Set All New Goals" button is clicked; if this button is clicked, the Goals embedded spreadsheet appears, with fields filled as noted below)
    * Set All New Goals (button; visible on creation of the new Goals record if the Member has a Goals record for a previous Meeting; visible in edit mode for users who can can edit the Goals record until this or the "Copy Last Meeting's Goals" button is clicked; if this button is clicked, the Goals embedded spreadsheet appears, with all fields blank as noted below)
    * Print Meeting Goals Worksheet (link; visible only to the selected Member in the "Member" drop list and their uplines; opens the "Print Meeting Goals Worksheet" prompt screen - see corresponding spec)
    * Goals (embedded spreadsheet of the following; hidden until one of the buttons is clicked:)
      * Columns: 
        * Life Branch (read-only; automatically generates one row for each Life Branch, including "Other", in the standard sequence)
        * Description (optional; multi-line plain text field; normally edited in the field below; 
          * if the "Copy Last Meeting's Goals" button is clicked: defaults to match the data in the corresponding fields of the Goals record for the most recent Meeting for the same Member + Group; 
          * if the "Set All New Goals" button is clicked: defaults to blank)
        * Make Up Option (optional; multi-line plain text field; normally edited in the field below; 
          * if the "Copy Last Meeting's Goals" button is clicked: defaults to match the data in the corresponding fields of the Goals record for the most recent Meeting  for the same Member + Group; 
          * if the "Set All New Goals" button is clicked: defaults to blank)
        * Achieved (drop list of blank / Yes / MUO / No / No Goal; defaults to blank; should be completed prior to the Meeting Date; required to mark the Goals record as Complete) 
        * Penalty $ (optional; number with no decimals; 
          * if the "Copy Last Meeting's Goals" button is clicked: defaults to match the data in the corresponding fields of the Goals record for the most recent Meeting for the same Member + Group; 
          * if the "Set All New Goals" button is clicked: defaults to blank)
      * Automatically sorted by: N/A
      * No option to insert/append/remove rows
      * Show 6 rows without scrolling
    * Life Branch (automatic and read-only; displays the contents of the Life Branch field of the selected row of the embedded spreadsheet; hidden if embedded spreadsheet is hidden) 
    * Description (required; multi-line plain text field; displays the contents of the Description field of the selected row of the embedded spreadsheet; edits made here are reflected there; hidden if embedded spreadsheet is hidden)
    * Make Up Option (required; multi-line plain text field; displays the contents of the Make Up Option field of the selected row of the embedded spreadsheet; edits made here are reflected there; hidden if embedded spreadsheet is hidden)
    * Total Penalty $ (auto-calculated and read-only; sum of all Penalties for all Goals for which "Achieved" = "No" or "No Goal"; note that this is only for the current month, as penalties are not carried over from previous months; hidden if embedded spreadsheet is hidden)



  


Data Access: See the Data Access Controls section of the proposal for details. 

  


Special Considerations:

  * Copy Record: Clear the Goal ID and the Meeting
  * Delete Record: Prevent deletion if the Status is Complete (error message: "This Goal record cannot be deleted because its Status is Complete.")
  * Merge Record: N/A



  


Other Notes:

  * Example of how the Status works: 
    * Today is 5/18/23
    * Linked Meeting Date for the Goals record is 5/22/23 (within 7 days of today)
    * April meeting was 4/24/23
    * Status on 4/23/23 and 4/24/23 (day before and day of the April meeting): Upcoming
    * Status on 4/25/23 (day after the April meeting): In Progress
    * Status on 5/12/23 (more than 7 days before the linked Meeting Date: In Progress 
    * Status today:
      * In Progress if the "Complete" checkbox is not filled
      * Complete if the "Complete" checkbox is filled
    * Status on 5/22/23 and after (the day of the meeting and after):
      * Overdue if the "Complete" checkbox is not filled
      * Complete if the "Complete" checkbox is filled
  * Note that this design removes the option for a "Lump Sum" penalty system.
  * Visibility & editability overview: 
    * Standard members can always view their own Goals, even including past ones from Groups of which they are no longer a member. 
    * A standard member can only see goals for other members in their group that correspond to meetings where the member is listed in the Attendance table. They cannot see historical goals for other members (i.e. Goals that were set prior to either member joining the Group).
    * Facilitators can view and edit all Goals (including historical) for members of the Groups(s) of which they are currently Facilitator. Once they are no longer Facilitator for a Group, they have standard visibility and editability like the other standard members.
    * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1530880492](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1530880492)

  


For reference, view: [https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=166%3A204&scaling=min-zoom&starting-point-node-id=9%3A3](https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=166%3A204&scaling=min-zoom&starting-point-node-id=9%3A3)

  


  


Change Requests: 

  * Tim Reitz 03/06/2024: [[[IN8953](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8955&)]] - ZSB - GR Goals Report - Changes to Behavior/Validations on "New Goals" Button
  * Tim Reitz 03/07/2024: [[[IN9262](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9264&)]] - ZSB - Growth Ring Goals - Clarifications / Tweaks
  * Tim Reitz 06/03/2024: [[[IN9846](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9848&)]] - ZSB - Growth Ring Goals Record - Various Changes April/May 2024
  * [[[IN9791](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9793&)]] - ZSB - Growth Ring Goals - Add Feature to Copy Goals
  * Ben Reitz 09/17/2025: [[[IN10074](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10076&)]] - ZSB - Growth Ring Goals - Add "Meeting Goals Worksheet" printout (prev. Add "Print Goals" button)


