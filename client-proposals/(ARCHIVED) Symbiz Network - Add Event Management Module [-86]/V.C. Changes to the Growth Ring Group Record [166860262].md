5.3. Changes to the Growth Ring Group Record

  


Requirements

*Documented 

  


Make the following changes to the Growth Ring Group record (changes indicated with blue / strike-through):

  


  * Growth Ring Group Details section:
    * Active (checkbox; defaults to filled; validate against deactivation if there are any Members in the group - error message on the field: "This Group cannot be deactivated because there are still Members in it."; validate against deactivation if it has any Growth Ring Meetings with a status of Scheduled - error message on the field: "This Group cannot be deactivated because it has one or more scheduled Meetings.") 
    * Growth Ring Group Description (auto-set and read-only; displays the Group ID and Group Name in the following format: "<ID> \- <Name>";  note that if a Name is specified it will be displayed with the Group ID throughout the Solution in this format; if no Name is specified, the Description will display only the ID)
    * Growth Ring Group ID (required; editable only for Super Admin users; number with no decimals; used as the unique identifier; validate against duplicate IDs - error message on the field: "This ID is already being used by another Growth Ring Group.") 
    * Growth Ring Group Name (optional; plain text field; used to give the group the ability to set a name/nickname that is separate from the numeric ID) 
    * Facilitator's State/Province (automatic and read-only; pulls the State/Province from the Primary address of the Group's Facilitator) 
    * Region (required; drop list of active Regions; editable only for Super Admins) 
    * Regional Rep (auto-set and read-only; displays the Regional Rep for the selected Region)  
    * Group Type (optional; drop list of Group Types with no option to add a new item; defaults to blank; editable only for the group's Regional Rep and all Super Admins; currently used only for reference)
    * Info Meeting (optional; drop list of all non-canceled Info Meeting-type Event IDs, with the latest one at the top; includes an ellipsis button beside the field to open the corresponding record; used to link a Group to the Info Meeting from which it was formed; visible and editable for Regional Reps & Super Admins; visible and read-only for Group members and uplines if an Info Meeting is selected) 
    * Growth Ring Meetings (link; opens the Growth Ring Meetings report, filtered to the current Group)



  


Development Specification

Mockup: Not needed.

  


Ellis Miller 06/20/2024:

Info Meeting: Events drop list with a helper list of Info Meeting types.

[ ] SortedEventsList(vEventIDs) that takes a list of EventIDs and sorts them. Since the event ID's include the date as M/d/YY, we can do one ListSubstitute to prefix them with the same date using YYYYMMDD (If the Event date is "Unscheduled", treat it as "99999999"), Sort the list, and then another ListSubstitute to strip off the sorting key.

  


2 Hours
