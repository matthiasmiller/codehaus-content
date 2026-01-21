7.3. Growth Ring Group Record

  


Requirements

Overview: A Growth Ring Group is a group of members who meet together monthly for accountability, discussion, and growth. The size of the growth ring group is not limited, but 8 members is a healthy size. Group information is stored on the Growth Ring Group Record. When a group becomes large enough, it may divide to form a second group. 

  


Accessed via:

  * Growth Ring Groups Report
  * My Growth Ring Group menu option
  * etc.



  


Sections and Fields: 

  * Growth Ring Group Details section:
    * Active (checkbox; defaults to filled; validate against deactivation if there are any Members in the group - error message on the field: "This Group cannot be deactivated because there are still Members in it."; validate against deactivation if it has any meetings with a status of Scheduled - error message on the field: "This Group cannot be deactivated because it has one or more scheduled Meetings."; editable only for Super Admin users) 
    * Growth Ring Group Description (auto-set and read-only; displays the Group ID and Group Name in the following format: "<ID> \- <Name>";  note that if a Name is specified it will be displayed with the Group ID throughout the Solution in this format; if no Name is specified, the Description will display only the ID)
    * Growth Ring Group ID (required; editable only for Super Admin users; number with no decimals; used as the unique identifier; validate against duplicate IDs - error message on the field: "This ID is already being used by another Growth Ring Group.") 
    * Growth Ring Group Name (optional; plain text field; used to give the group the ability to set a name/nickname that is separate from the numeric ID) 
    * Facilitator's State/Province (automatic and read-only; pulls the State/Province from the Primary address of the Group's Facilitator) 
    * Time Zone (required; drop list of all global time zones with extended names; defaults to blank) 
    * Region (required; drop list of active Regions; editable only for Super Admins) 
    * Regional Rep (auto-set and read-only; displays the Regional Rep for the selected Region) 
    * Last Rep Visit (date; defaults to blank; editable for the Regional Rep and their uplines)
    * Next Rep Visit (date; defaults to blank; editable for the Regional Rep and their uplines)
    * "Rep Visit expected on <"Next Rep Visit" date>." (label in red text; displays to the right of the field if the "Next Rep Visit" date is less than 30 days in the future or is in the past) 
    * Group Type (optional; drop list of Group Types with no option to add a new item; defaults to blank; editable only for the group's Regional Rep and all Super Admins; currently used only for reference)
    * Growth Ring Meetings (link; opens the Growth Ring Group Meetings report, filtered to the current Group)
    * Schedule New Meeting (link; visible if there are no Growth Ring Meetings linked to the Group; opens a new blank Growth Ring Meeting record with Group defaulted; visible only for Group members and uplines) 
    * Last Facilitator Change (date; defaults to blank; when a date is entered, sets the "Next Facilitator Change" date to 12 months from this date; if the "Facilitator" checkbox is checked for a new Member, auto-updates to the current date; editable for Facilitators and uplines)
    * Next Facilitator Change (date; defaults to blank; auto-updates to 12 months after the date in the "Last Facilitator Change" field; editable for Facilitators and uplines)
    * "Facilitator change due by <"Next Facilitator Change" date>." (label in red text; displays to the right of the field if the "Next Facilitator Change" date is less than 30 days in the future or is in the past) 
    * Credit Group? (required; drop list of Yes/No; editable only for Regional Reps and Super Admins)
    * Credited Group (visible if Credit Group = Yes; drop list of all Groups; editable only for Regional Reps and Super Admins)
    * Credit as of (visible if Credit Group = Yes; date field; defaults to today; editable only for Regional Reps and Super Admins)



  


  * Group Members section:
    * Growth Ring Group Members (embedded spreadsheet of:)Columns: 
      * Name (required; editable only for the group's Regional Rep and all Super Admins; drop list of all Member-type Contacts with an active membership, filters down as you type; includes the following validations: 
        * Validate against having the same member in the same group more than once -- error message on the field: "This Member is already part of this Group."
        * Validate against having a member in a group if the member does not have an active membership -- warning on Save if any of the Names do not have an active membership: "<Member Name> does not have an active membership. Their membership should be reactivated or they should be removed from the Group."
      * Open (displays as "Link"; opens the Contact record page) 
      * Facilitator (checkbox; when checked, the corresponding Member is labeled as the Facilitator for the Group; when checked in a new row, sets the "Last Facilitator Change" date to the current date and sets the "Next Facilitator Change" date to 12 months from this date; validate that there is a Facilitator for each group - error message on Save if there is none: "This Group does not have a Facilitator set."; validate that there is only one Facilitator per Group - error message on the field if a second checkbox is checked: "This Group already has a Facilitator set.")
      * Group Member Since (required; date; editable only for the group's Regional Rep and all Super Admins; default to the current date when adding a new row)
      * Phone Number (automatic and read-only; displays the top phone number listed on the Contact record)
      * Email (automatic and read-only; displays all Primary email address listed on the Contact record; separated by commas)
      * Address (automatic and read-only; displays the Primary address from the Contact record)
      * Account Name (auto-set and read-only; displays the Account Name from the Contact record; visible only for the Facilitator and uplines) 
    * Automatically sorted by: The Facilitator first, then by Group Member Since date (oldest date at the top)
    * Buttons to add/remove rows:
      * Add Member (button; visible and editable only for the group's Regional Rep and all Super Admins; opens the Add Member Child Screen; see details below) 
      * "Remove Member" (visible and editable only for the group's Regional Rep and all Super Admins; opens a prompt to confirm removal) 
    * Show 14 rows without scrolling 



  


  * Group Bylaws section (visible only for Group members and uplines): 
    * Group Bylaws (memo) 



  


  


  * Add Member Child Screen
    * Group (auto-set and read-only; defaults to the Group from which the child screen was opened) 
    * New Member (required; drop list of all Member-type Contacts with an active membership who are not already part of the selected Group, filters down as you type) 
    * Continue (button; when clicked, the following happen: 
      * The screen prompts the user to save to record. 
      * The Add Member to Growth Ring Group background process is run (to add the selected Member to the selected Group). 
      * The Service Contact Set Membership Start Date background process is run (to fill in the Paid Membership Start date if needed). 



  


  


Data Access: See the Data Access Controls section of the proposal for details.

  


Special Considerations:

  * Copy Record: Clear the Group ID and Group Name
  * Delete Record: Cannot delete if Active (Error message: "This Growth Ring Group record cannot be deleted because it is still active.")
  * Merge Record: N/A



  


Other Notes:

  * A Member can see details for his group only while he is a member of the group. For example, he cannot see Growth Ring Meeting records from prior to his Group Member Since date or from after he leaves the group. However, even after leaving a group, he can see meeting records from the time that he was a member of the Group. This is managed on the Growth Ring Meeting record (see further details in the corresponding section of the proposal). 
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Change Requests:

  * Tim Reitz 03/06/2024: [[[IN8836](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8838&)]] - ZSB - Growth Ring Meetings - Add a way to create the initial meeting for a Group
  * Tim Reitz 04/09/2024: [[[IN9045](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9047&)]] - ZSB - Growth Ring Group - Changes to Group Members RG
  * Tim Reitz 04/09/2024: [[[IN8696](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8698&)]] - ZSB - Growth Ring Group - Change behavior for adding a new member 
  * Tim Reitz 07/20/2024: [[[IN9841](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9843&)]] - ZSB - Growth Ring Group Record - Improve Visibility for Members of Other Groups
  * Tim Reitz 09/03/2024: [[[IN9889](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9891&)]] - ZSB - Add Time Zone Feature (for Groups & GR Meetings)
  * Ben Reitz 05/01/2025: [[[IN10837](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10839&)]] - ZSB - Growth Ring Group record - Add "Credit" field
  * Tim Reitz 06/04/2025: [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.) 
  * Ben Reitz 10/08/2025: [[[IN10718](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10720&)]] - ZSB - Group Record - Add Fielding for Facilitator Change & Rep Visit Dates
  * 


  


Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1698763411](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1698763411)

  


Wireframe mockups by Rubico: 

  * For Members: [https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=170%3A1536&scaling=min-zoom&starting-point-node-id=9%3A3](https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=170%3A1536&scaling=min-zoom&starting-point-node-id=9%3A3)
  * For Super Admins: [https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=795%3A4797&node-id=943%3A11644&viewport=-1359%2C-478%2C0.26&scaling=min-zoom&starting-point-node-id=806%3A4917](https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=795%3A4797&node-id=943%3A11644&viewport=-1359%2C-478%2C0.26&scaling=min-zoom&starting-point-node-id=806%3A4917)


