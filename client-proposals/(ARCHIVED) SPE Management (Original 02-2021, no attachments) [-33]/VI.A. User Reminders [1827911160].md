6.1. User Reminders

  


Requirements

AppHosting will support user reminders. It will be a record definition that shows:

  * Summary
  * Contact (default to current user)
  * Remind On (required date)
  * Repeat Next Year (checkbox)
  * Notes
  * Complete (checkbox)



  


If the Repeat Annually checkbox is checked, the entire reminder will be duplicated when it's completed, but with a Remind On date exactly a year later.

  


Development Specification

Ellis Miller 02/10/2021: TODO_CH: Instead of putting this on the contact, let's put it on the menu with All Reminders / My Reminders report links and a "New Reminder" link that creates a User Reminder. These need mockups at some point, but may not need for the proposal.

  


  


Long-term goal -- be able to link to Incidents as well.

  


I think we should have a Contacts setting to indicate whether reminders can be assigned to the user.

  


For the Repeat Next Year, I think we have a daily x30list that duplicates it, updates the year, and clears the repeat on the prior one.

  


Ellis Miller 02/09/2021: 

  


[ ] Create simple User Reminder record. 

[ ] Filtering by member names that can be assignees

[ ] Requires adding a "Can be Reminder Assignee" field 

Target: 1 day

  


[ ] x30list to auto-create reminders.

[ ] Report alert if we aren't correctly creating new items?

Target: 1 day.

  


[ ] Have an All Reminders / My Reminders report links.

[ ] Have a "New Reminder" link.

Target: 2 Days. CH will mock up before we code.
