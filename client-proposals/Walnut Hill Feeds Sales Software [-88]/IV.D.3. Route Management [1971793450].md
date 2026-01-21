4.4.3. Route Management

  


Requirements

There are two main approaches to Route Management: 

1\. Use a report to list the customers due for check-ins, looking at the location of the salesperson and roughly estimates the customers that are closest and gives a general route suggestion on a report. This is the simplest/cheapest option.

2\. Use an integration with an additional piece of software to provide a map and grouping of customers by which days they should be visited. This is much more expensive, but also a powerful tool. See "Phase 2 - Route Management by Map" for more details.

  


Summary for option 1: This is a multi-pane Report used for managing routes. This is used for salespeople, to help make routes as efficient as possible. This uses information on the salesperson's Contact record and the customer's Contact record (address/location), and from the Check-In Incident record (when a customer is due for a check-in). 

  


Left Pane - Upcoming scheduled check-Ins

  * Columns:
    * Name
    * Address
    * Scheduled Check-In Date
  * Group By
    * Missing GPS Coordinates (if missing)
    * Scheduled Check-In Date 
  * Sorted By
    * Scheduled Check-In Date



  


Right Pane - All upcoming check-ins, sorted by straight-line distances (via GPS coordinates).

  


Distance Approaches:

  * Based on Address Location - requires clicking a link and waiting for the process to complete on all updated addresses
  * Based on Zip Code Location - can simply be calculated using the zip code



  


Button:

  * Calculate GPS Coordinates (applies to the left pane; opens link to Geocoder)
  * Reschedule Selected Check-Ins (applies to the right pane; reschedules the selected check-in, defaulting to the date in the left pane and marks it as scheduled)



  


Development Specification

  * If we use geocoding, we need to have an OnChange that clears out the latitude and longitude


