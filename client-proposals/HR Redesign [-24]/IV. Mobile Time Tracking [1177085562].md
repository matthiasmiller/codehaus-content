4\. Mobile Time Tracking

  


Requirements

This includes two changes:

  * Time tracking will be expanded to allow mobile access.
  * Time tracking will support categorizing time slots.



  


These will be specified on a per-role basis. It will be optimized for no more than 15 categories per role.

  


Logging In

The user would have a special site they would bookmark on their mobile phone. They would log in using the same email address as the main AppHosting.zone system.

  


They would stay logged in for an extended period of time (exact duration to be determined).

  


User Interface

If the user is not clocked in, show a list of time slot categories. Clicking the category would clock in using that time slot category.

  


If the user is clocked in, show the same list of time slot categories. Clicking the category would switch to that time slot category. Have a button at the top to clock out.

  


The time card could only be edited through the Time Card screen in the main AppHosting.zone system.

  


Matthias Miller 08/11/2020: Should we have an option to clock in without any category?

  


Defining Time Slot Categories

Each Organization Role would have a checkbox that's called "Enable mobile time tracking". When checked, it would show a link on the user's menu to the mobile time tracking, as well as instructions to add it to their home screen.

  


It would also have a checkbox that says "Enable time card categories". When checked, it would allow entering multiple categories specific to the role.

  


Renaming a time slot category in the Organization Role would not update existing time cards.

  


Reporting

Show a report that prompts for:

  * Employee
  * Start Date
  * End Date



  


Columns:

  * Category
  * Hours
  * % of Time



  


Matthias Miller 08/11/2020: Would they want a graph for this?

  


Setup Instructions

Provide users with setup instructions for adding this to their home screen.

  


Development Specification

Josh is proposing a WSGI with OAuth. We would validate using the database emails, with persistent sessions. Use a WSGI to make this simple.

  


Josh would provide a report to query for categories.

  


He'd be willing to half-off as part of the time tracking ecosystem.
