6.1. Reminder Detail

  


Requirements

The Reminder Detail would have fields for: 

  * Reminder Title (required; text field)
  * Associated Task (auto-fill and read-only)
  * View Customer/Ads Page (automatic; link to the page for the associated Task)
  * Notes (optional; memo field)
  * Send To (required; list of all Full Admin Users, and all Users assigned to the current publication; default to the Assignee for the associated Task; editable) 
  * Due Date (required; date picker)
  * Due Time (required; time entry field; round to the nearest 15-minute increment)
  * Reminder Lead Time (required; hours and minutes fields; available in 15-minute increments up to 24 hours and 0 minutes; defaults to a configured amount of time - start with 30 minutes)
  * Status (auto-fill and read-only; Overdue, Sent Notification, Scheduled, Dismissed)
  * Dismissed (checkbox; defaults to unchecked; checking this dismisses the Reminder)



  


On Save, the Reminder would be set. At the designated time, it would be sent to the "Send To" User in two ways: 

  * via email to the Send To User's set email address
  * via System Notification in the software on the Send To User's account 



  


The system would send an individual email for each Reminder rather than including multiple Reminders in one email. Each email would show:

  * Reminder Title
  * Associated Task
  * Send To name
  * Notes
  * Due Date and Time
  * Link to the Reminder detail



  


The System Notification would open the Reminder detail if there is only one due Reminder, or the Reminders Report for the current User if there are more than one due Reminders.

  


If a Reminder is not dismissed by the Due Date/Time, the system will send another alert at the Due Time. 

  


If the Reminder is not dismissed by the time that the next Overdue Reminders Alert goes out, the Reminder would be added to that and remain there until the Reminder is dismissed. See the corresponding section in this proposal for more details on this.

  


Development Specification

Tim Reitz 02/01/2021: New record type for Reminders

  


Data Restrictions:

  * Full Admins: Full access
  * Publication Admins: Full access for assigned publication
  * Standard Users: Full access for assigned publication


