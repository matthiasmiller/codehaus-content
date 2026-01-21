5.9.1. Scheduled Processes

  


Requirements

Scheduled Processes: The Solution contains the following automatic processes that are initiated on a scheduled basis (also referred to as "Scheduled Tasks"). 

  


Note that errors from the background processes will be sent to designated users as standard email alerts (if outbound emails are configured). The designated users are set as part of the Scheduled Task setup.

  


  


1\. Activate New Membership: 

  * Description: Used to activate a new membership, for any Members who have the Activate Membership button visible.
  * Category: Membership Management
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated:
    * Daily at 2:30am ET (for all Contacts that have the "Activate Membership" button visible, to catch any that were missed).
    * Also when the "Activate Membership" button is clicked on an individual Contact record -- see "User-Initiated Processes" spec.
  * Should Wait On: N/A
  * Commands: 
    * import "MainDir::\Standard\Std Service Activate Membership.x30list"
  * Prompts: 
    * __



TODO_VA: Tim Reitz 06/04/2025: Ask Jonathan for details on prompts for all.

  * Actions:
    * Fill the Active Membership checkbox on the Contact record.
    * Activate the linked User Profile, if one is linked and inactive.
    * Create a new active User Profile and link it to the Contact if none is linked and "Online Member" is set to "Yes".
  * Other Notes:
    * Note that this does not set the Paid Membership Start date.
    * Note that this appends the Contact ID to the last name to avoid conflicts between Users with the same first and last name. 



  


2\. Annual Renewal Due:

  * Description: Used to prepare a Member's Contact and membership for renewal, for any members who have their Next Renewal Date set to the current month or the following month.
  * Category: Membership Management
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: The 1st of every month at 4:00am ET (to catch any Contacts with their Next Renewal Date set to the current month or the following month)
  * Should Wait On: N/A
  * Commands: 
    * import "MainDir::\Standard\Std Service Annual Renewal Due.x30"
  * Prompts: 
    * __
  * Action(s): 
    * Add a new row the the Membership History embedded spreadsheet.



  


  


3. Annual Renewal Notices Due:

  * Description: Used to send the email version of this User Notification on the 1st of every month.
  * Category: User Notifications
  * Notes: N/A
  * Initiated: Monthly on the first day of the month at 6:00am ET
  * Should Wait On: N/A
  * Commands: 
    * email "Standard\Std Email Notification - Annual Renewal Notices Due.r20" 
  * Prompts: 
    * __
  * Action(s): 
    * Checks Member-type Contact records, and sends the "Annual Renewal Notices Due" email notification to all Super Admin users for whom the Email version of the notification is enabled. 



  


  


4. Sync Contacts and User Profiles:

  * Description: Used to keep the Contact and User Profile in sync
  * Category: Membership Management
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: Daily at 3:00am ET
  * Should Wait On: N/A
  * Commands: 
    * import "MainDir::\Standard\Std Service Sync Contacts and Update User Profiles.x30list"
  * Prompts: 
    * __
  * Action(s): 
    * Update the User Profile to match any changes that were made to the corresponding Contact record (i.e., first or last name edited, email address edited). 
    * Activate the User Profile if it is inactive and the corresponding Contact's membership is active. 
    * Create and link a new User Profile if the Contact's "Active Membership" checkbox is filled, "Online Member" = Yes, and the Contact has no corresponding User Profile. 
    * Deactivate the User Profile if it is active and the corresponding Contact's membership is inactive.
    * Deactivate any User Profiles that are active and not linked to a Contact record.
      * Excludes User Profiles that match any of the following criteria:
        * User ID includes the "CCI_" prefix (disregarding case)
        * "Edit Super Admin fields" permission is set to true.
        * User ID is one of the following hard-coded system users: "SYSTEM", "Administrator", and "Default"



  


  


5\. Update Meeting Attendees:  

  * Description: Used to update the Attendance list for each Growth Ring Meeting with a Status of Tentative or Scheduled.
  * Category: Membership Management
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: Daily at 3:00am ET
  * Should Wait On: N/A
  * Commands: 
    * import "MainDir::\Standard\Std Service Update Meeting Attendees.x30"
  * Prompts: 
    * __
  * Action(s): 
    * Check the Growth Ring Group Members table on each Growth Ring Group record and update the Attendance table on any Scheduled Growth Ring Meeting record for that Group, adding or removing members as needed, based on group membership. 



  


  


6. Upcoming Growth Ring Meeting (used to send the email version of this User Notification 3 days and the day before a scheduled Growth Ring Meeting): 

  * Schedule: Every day at 5:00am ET. 
  * Actions:
    * Send the "Upcoming Growth Ring Meeting" email notification, which does the following: 
      * Checks all upcoming Growth Ring Meetings to see if there are any Meetings that are 3 calendar days or 1 calendar day from the current date;
      * Sends the corresponding version of the the "Upcoming Growth Ring Meeting" notification to the necessary Members
  * Scheduled Task Commands: 
    * email "Standard/Std Email Notification - Upcoming Growth Ring Meeting.r20"
    * email "Standard/Std Email Notification - Upcoming Growth Ring Meeting.r20" \--prompt.vAskNumDays=3



  


  


7\. Yesterday's Growth Ring Meeting:

  * Description: Used to send the email version of this User Notification the day after a scheduled or complete Growth Ring Meeting
  * Category: User Notifications
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: Daily at 5:00am
  * Should Wait On: N/A
  * Commands: 
    * email "Standard\Std Email Notification - Yesterday's Meeting.r20"
  * Prompts: 
    * __
  * Action(s): 
    * __



TODO_VA: Tim Reitz 06/04/2025: Ask Jonathan for details on this.

  


  


8\. Missing Payments / Confidentiality Agreements:

  * Description: Used to send the email version of this Email Notification every Monday
  * Category: User Notifications
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: Every Monday at 5:00am ET
  * Should Wait On: N/A
  * Commands: 
    * email "Standard\Std Email Notification - Missing Payments or Confidentiality Agreements.r20"
  * Prompts: 
    * __
  * Action(s): 
    * __



TODO_VA: Tim Reitz 06/04/2025: Ask Jonathan for details on this.

  


  


9\. Recently Ended Memberships:

  * Description: Used to send the email version of this User Notification on the first of every month
  * Category: User Notifications
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: Monthly on the first day of the month at 6:00am ET
  * Should Wait On: N/A
  * Commands: 
    * email "Standard\Std Email Notification - Recently Ended Memberships.r20"
  * Prompts: 
    * __
  * Action(s): 
    * __



TODO_VA: Tim Reitz 06/04/2025: Ask Jonathan for details on this.

  


  


10\. Approve New Resources:

  * Description: Used to send the email version of this User Notification on the 1st of each month.
  * Category: User Notifications
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: Monthly on the first day of the month at 5:00am ET
  * Should Wait On: N/A
  * Commands: 
    * email "Standard\Std Email Notification - Approve New Resources.r20"
  * Prompts: 
    * __
  * Actions:
    * Send the "Approve New Resources" email notification, which does the following: 
      * Check all Development Resource records to find any that have Status = "Submitted" 
      * If there are any, send the "Approve New Resources" email notification to all Contacts who have the email notification enabled. 



  


  


11\. Review / Update Annual Goals: 

  * Description: Used to send the reminder to the members.
  * Category: User Notifications
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: Daily at 3:00am ET
  * Should Wait On: N/A
  * Commands: 
    * email "MainDir::\Standard\Std Email Notification - Review and Update Annual Goals.r20"
  * Prompts: 
    * __
  * Action(s): 
    * Checks Member-type Contact records, and sends the "Review / Update Annual Goals" Email Notification to all members for whom the "Review Date" for the Annual Goal on the Contact record is the current date.



  


  


12\. Review / Update Annual Goals (Facilitator) (used to send the email version of the reminder to the Facilitator): 

  * Schedule: Daily at 3:00am ET. 
  * Actions: 
    * Checks Member-type Contact records, and send the Review / Update Annual Goals email notification to the Facilitators all members for whom the Review Date for the Annual Goal on the Contact record is the current date. Email is skipped/not sent if one of the following conditions are met: 
      * The Member is not part of a Growth Ring Group (and therefore does not have a Facilitator). 
      * The Facilitator does not have any email address specified on their Contact record. 
  * Scheduled Task Command: email "Standard\Std Email Notification - Review and Update Annual Goals (Facilitator).r20"



  


  


13\. Prepare Symbuzz Extra Posts:

  * Description: Used to send the reminder to the Meeting Secretary that they need to prepare the posts for the recent Growth Ring Meeting.
  * Category: User Notifications
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: Every day at 7:00am ET
  * Should Wait On: N/A
  * Commands: 
    * email "MainDir::\Standard\Std Email Notification - Prepare Symbuzz Extra Posts.r20"
  * Prompts: 
    * __
  * Action(s):
    * Runs the email merge to send the email version of the "Prepare Symbuzz Extra Posts" User Notification to the Meeting Secretary. Email is skipped/not sent for Members who do not have any email address specified on their Contact record. 



  


  


14\. Review Symbuzz Extra Posts:

  * Description: Used to send the weekly reminder to all users with the "Is Symbuzz Extra Post Reviewer" checkbox checked on their Contact record.
  * Category: User Notifications
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: Every Monday at 7:00am ET
  * Should Wait On: N/A
  * Commands: 
    * email "MainDir::\Standard\Std Email Notification - Review Symbuzz Extra Posts.r20"
  * Prompts: 
    * __
  * Action(s): 
    * __



TODO_VA: Tim Reitz 06/04/2025: Ask Jonathan for details on this.

  


  


15\. Symbuzz Extra (Weekly):

  * Description: Used to send the weekly edition of Symbuzz Extra to online members.
  * Category: User Notifications
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: Every Tuesday at 7:00am ET
  * Should Wait On: N/A
  * Commands: 
    *  email "MainDir::\Standard\Std Email Notification - Symbuzz Extra (Weekly).r20"
  * Prompts: 
    * __
  * Action(s): 
    * __



TODO_VA: Tim Reitz 06/04/2025: Ask Jonathan for details on this.

  


  


16\. Print Symbuzz Extra (Monthly):  

  * Description: Used to send the email to the person designated to prepare/send the monthly paper edition of Symbuzz Extra (any users with the "Receives Symbuzz Extra Monthly Reminder" checkbox checked on their Contact record).
  * Category: User Notifications
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: The 3rd Thursday of every month at 7:00am ET
  * Should Wait On: N/A
  * Commands: 
    * email "MainDir::\Standard\Std Email Notification - Print Symbuzz Extra (Monthly).r20"
  * Prompts: 
    * __
  * Action(s): 
    * __



TODO_VA: Tim Reitz 06/04/2025: Ask Jonathan for details on this.

  


  


17\. Send Info Meeting Follow-up Emails (Primary & Secondary):

  * Description: Used to automatically send the following User Notification emails:



\- Info Meeting Follow-up (Primary)

\- Info Meeting Follow-up (Secondary)

  * Category: User Notifications
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: Every day at 7:00 am ET
  * Should Wait On: N/A
  * Commands: 
    * Line 1: "< email "Standard\Std Email Notification - Info Meeting Follow-up (Primary).r20" >"
    * Line 2: "< email "Standard\Std Email Notification - Info Meeting Follow-up (Secondary).r20"" >"
  * Prompts: 
    * __
  * Action(s):
    * Checks Info Meeting-type Event records, and send the "Info Meeting Follow-up (Primary)" email notification for all records with a Status other than Canceled that have the Event Date 14 calendar days in the past. 
    * Checks Info Meeting-type Event records, and send the "Info Meeting Follow-up (Secondary)" email notification for all records with a Status other than Canceled that have the Event Date 3 weeks (21 calendar days) in the past, if there is at least one linked Event Registration record with the "Lead Follow-up Completed" checkbox not checked.



  


  


18\. Send Review Launch Meeting Registrations Email:

  * Description: Used to automatically send the "Review Launch Meeting Registrations" User Notification email
  * Category: User Notifications 
  * Notes: Contains the contents of the "Actions" point below.
  * Initiated: Every day at 7:00 am ET
  * Should Wait On: N/A
  * Commands: 
    * "< email "Standard\Std Email Notification - Review Launch Meeting Registrations.r20" >"
  * Prompts: 
    * __
  * Action(s): 
    * Checks Launch Meeting-type Event records, and send the "Review Launch Meeting Registrations" email notification for all records with a Status of Tentative or Scheduled that have the Event Date 14 days in the future.



  


Development Specification

TODO_VA: Tim Reitz 07/10/2025: This could be broken down into sub-sections, one for each process (remove the numbering). 

  


Change Requests:

  * Tim Reitz 06/04/2025: [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)
  * Ben Reitz 08/01/2025: [[[IN11164](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11166&)]] - ZSB - Notifications - Growth Ring Meeting in 3 Days


