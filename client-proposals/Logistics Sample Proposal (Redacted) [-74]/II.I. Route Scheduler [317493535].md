2.9. Route Scheduler

  


Requirements

The Route Scheduler would function similarly to how it works in the current system. The "Schedule Stops" link would open a blank page with a menu bar along the top listing all the current days of the week.

  


Clicking on a day of the week would show columns for the all routes on that weekday. It would show this for the current week, the week with the last scheduled stop for that weekday, and all weeks in between. It would always include a blank week at the very end.

  


Stops can be dragged in different orders on the current day, or dragged to another day.

  


This will closely reflect the Route Scheduler for the current system.

  


Development Specification

[ ] Add a SelectStopsByRouteSchedule subset that takes route and date ask prompts (required). This is returning the STOP record, not the SCHEDULE record.

  


FOR MATTHIAS:

Tim Reitz 09/14/2020: This is probably an important one to have screenshots or old system access.

[ ] The days of the week on the menu should include all available days on the schedule, as well as the weekdays for all upcoming stops.

[ ] Matthias needs to handle if any of the required settings are missing on the daily schedule
