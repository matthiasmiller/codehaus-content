11.0.0.1. Haul Request Calendar

  


Requirements

TODO_TR: Poke holes in this?

  


Haul Requests and Service Jobs will be scheduled through Google Calendar.

  


Any assignees would have the following Event configuration settings:

  * Google Calendar Start Time
  * Google Calendar End Time



  


The Google Calendar colors would be defined as:

  * Name (i.e. "Cave City (Dark Blue)", "Other Lot (Light Blue)", etc)
  * Color ID (number corresponding to Google's color scheme.



  


For example:

  * Default color is dark blue (default color for a building that's on the Cave City lot or customer building that's to be sold)
  * Lighter blue (means that the building is on a sales lot - not Cave City; driver needs to open the event to see more information)
  * Purple (are for move jobs - moving an existing building for a customer from one location to another)
  * Orange (are for escorts and service jobs)
  * Red (site inspection)
  * ___ (lot buildings going from the factory to the lot) 



  


A Haul Request or Service Job work order would require:

  * Schedule Date
  * Assignee
  * Event Color



Then would automatically generate the event. The Haul Request / Service Job would have a link to view/edit the event.

  


After the event is created, these fields would become read-only and could only be edited on the event itself. When the event date or time is changed, it would update the date and assignee of the work order. If the time is outside of a recognized time period, the assignee would be cleared.

  


The Google calendar event would be defaulted as follows:

  * Date - scheduled date
  * Time - next available 1-hour interval between the assignee's start and end time; if there are no open time slots, it would be scheduled at the last hour
  * Title: "City / Building Style / Customer Name / Customer Phone" 
  * Notes:
    * Last 4 of serial #: [xxxx]
    *     * Building: [link to building]
    * Work Order: [link to work order]
  * Location: Address OR coordinates
  * Color: as determined by the Haul Request or Service Job



  


Development Specification

The Calendar Event would be a hidden record type used for syncing. 

  * ID (from Google Calendar)
  * Title
  * Notes
  * Start Date
  * Start Time
  * Location
  * Color ID



  


The events for work orders would use a special format:

["beb"][WorkOrderID]["beb"][Random Hex String]

  


This would trigger an x30list that would update the underlying record. We would extend that to also update the sales order. We would pull the work order ID from the event ID.

  


We'd have a trigger for new sales orders that would run an X30 to create the event.
