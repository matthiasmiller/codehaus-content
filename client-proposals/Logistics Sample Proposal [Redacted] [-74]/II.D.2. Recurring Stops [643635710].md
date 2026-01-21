2.4.2. Recurring Stops

  


Requirements

We need to support recurring stops. These are used primarily for lunch breaks and some weekly repeating stops.

  


Recurring stops will be defined on the Route. It will be configured through an embedded spreadsheet such as:

  


Schedule| Weekday| Contact| Stop Type| Instructions  
---|---|---|---|---  
(choice of Daily or Weekly)| (if Weekly schedule)|   
|   
|   
  
  
  


  


Development Specification

Hidden Fields

[ ] Add a hidden RoutesRecurringStopID list field to the RG. Initialize it to a somewhat lengthy random character string (see where do this elsewhere).

[ ] Add a hidden RouteStopRecurringStopID list field to the stop.

[ ] Validate that the Weekday selected in the recurring stops is also in the routes schedule.

[ ] Add a RoutesRecurringSchedules list of "Daily" and "Weekly".

  


  


Matthias Miller 09/23/2020: Tim, consider an MRG for this.
