3.6. Route Scheduler - Lock Schedule

  


Requirements

The Route Scheduler screen would have an option to lock a route's schedule for a specific date. This would prevent additional stops from being entered, and it would prevent stops from being reordered or optimized.

  


If a route is locked, canceled stops would stay in visible in the schedule (perhaps with a red notification/flag) until the route is unlocked.

  


It would also send a text message to a set of contacts defined in the AppHosting.zone Settings. (When choosing these contacts, we will require them to have a mobile number specified.)

  


The message should be something like: "[RouteName] has been locked for [____]." It would include a date such as "Friday, September 11". It would send a similar message when the route is unlocked.

  


These notification contacts will be defined on the Routes detail screen with an embedded spreadsheet called "Locked Route Notifications". It will show two columns:

  * Contact
  * Weekday (blank = all)



  


If individuals need notifications for multiple weekdays, they will need multiple entries. The spreadsheet should be sorted first by name, then by weekday.

  


Development Specification

Matthias Miller 08/27/2020: 

[ ] Create an x30list to do this. One x30 for the text messages. The other one to actually update the status.
