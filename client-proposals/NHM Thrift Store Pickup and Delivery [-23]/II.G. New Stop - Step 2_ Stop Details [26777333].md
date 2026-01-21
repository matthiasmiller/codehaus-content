2.7. New Stop - Step 2: Stop Details

  


Requirements

Once we've selected a Guest in Step 1, we will open a new Stop screen. It will default the new stop's Guest field.

  


The Stop should define:

  * Contact (Contacts list; required)
  * Stop Type (required; all options from Stop Types)
  * Pickup Reason (required; only visible if the Stop Type is a pickup): choice of:
    * Downsizing
    * Moving
  * Route (Routes list; required)
  * Requested Date (date; required)
  * Creator (read-only; populated based on current user Contact)
  * Items (multi-line text field; hidden for Breaks)
  * Donation Receipt; required choice of (hidden for Breaks):
    * Print
    * None
  * Instructions (multi-line text field)
  * Employee Initial (string field)
  * Stop Length (in minutes) -- number
  * Status (list; default to unfulfilled; updated by the Mobile Routes; can be manually edited):
    * Unfulfilled
    * Attempted
    * Fulfilled
    * Canceled
  * Status Date/Time (cleared when status is Unfulfilled; otherwise automatically set to current date/time; can be manually edited)
  * Route Schedule Order (hidden; import only; number; no decimals)
  * Repeat Weekly (checkbox)



  


When saving a stop, the stop's Order will be updated to be the last stop in the schedule for that day whenever the Stop is created, the Route is changed, or the Requested Date is changed. (This does not apply when dragging/dropping the stop via the Route Scheduler.)

  


NOTE: Saving a new stop would no longer create a Receipt / Sold Tag. We will no longer have the Requested Times.

  


Development Specification

Route Stop

[ ] Update detail screen to match specification. The following fields are ZNH-specific:

  * Pickup Reason
  * Items
  * Donation Receipt
  * Employee Initial



  


Route Schedule

This is a hidden detail screen (Custom Level). We should have the report for it be visible if UserIsAppHostingSupport. It should be editable NOT InDetailScreen OR TestEnvironment

  * Route (list field of routes; require)
  * Date (date field; required)
  * Start Time (optional)
  * Start Location (optional)
  * End Location (optional)
  * RG of:
    * Stop #
    * Order
    * Sort by Order



[ ] Validate against duplicate schedules for the same route and date.

[ ] Add field change expressions to initialize the Start Time to the default value as specified by the route for the date, as long as the field is blank.

[ ] Do the same for Start Location and End Location.

  


[ ] Add a subset for SelectRouteSchedule that w/ required ask prompts for Route and Date. This will be used by integrations.

  


Matthias Miller 09/04/2020: Tim, when testing, make sure that we can schedule a stop of a weekday that does not have a route, and that the Mobile Routes works as expected.
