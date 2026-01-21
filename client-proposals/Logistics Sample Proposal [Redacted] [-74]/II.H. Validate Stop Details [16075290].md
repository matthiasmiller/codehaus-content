2.8. Validate Stop Details

  


Requirements

We need to add validation for stops.

  


When you schedule a stop, we will warn if:

  * The route settings does not include any settings for that weekday.
  * The date is a holiday for that route.



  


The Stop Length must be greater than or equal to 1 minute.

  


The Stop Date/Time is required if the status is Attempted or Fulfilled (not Unfulfilled or Canceled).

  


NOTE: The current system is validating the number of stops for any given day. We will NOT be doing that.

  


Development Specification

Matthias Miller 09/23/2020: 

[ ] Add a ValidateRouteForDate that returns an error message if it's invalid. Otherwise returns "".

[ ] Add the remaining validation mentioned above.

  


Matthias Miller 09/04/2020: Tim, when testing, make sure that we can schedule a stop of a weekday that does not have a route, and that the Mobile Routes works as expected.
