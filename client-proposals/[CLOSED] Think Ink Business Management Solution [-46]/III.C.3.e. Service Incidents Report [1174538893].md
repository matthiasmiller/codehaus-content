3.3.3.5. Service Incidents Report

  


Requirements

This is a custom multi-pane report of Service Incidents.

  


This is accessed from a Service Incidents menu option in the Incidents section of the Home Menu. 

  


Left Pane: This pane shows Service-type incidents, always showing incidents without a Due Date regardless of whether the filters specify dates

Title: Service Incidents

  


Columns: 

  * ID
  * Title (link to record)
  * Contact
  * Workflow
  * Assignee
  * Origination Date
  * Due Date



  


Grouped by: A "Due date unspecified" group at the top, then by Week in ascending order (oldest at the bottom), in the "Week of 1/1/2022" format.

  


Sorted by: Due Date

  


Filters: 

  * Workflow (drop list; default to blank = all)
  * Assignee (drop list; default to blank = all)
  * Due Date Start (date field; default to 30 days prior to today; blank = all) 
  * Due Date End (date field; default to blank = all) 



  


Buttons: 

  * New Service Incident (opens a new incident with Type defaulted)



  


Right Pane: This pane shows information from certain fields of the selected incident in the left pane:

Title: Service Incident Details 

  


This would show a text version of the the following fields from the incident, in a format like the following: 

Contact Tags:| Tag 1, Tag 2  
---|---  
Primary Address:| 123 Some StreetSometown, OH 11111  
Device:| My Device ID  
*Serial #:| *352345423523  
Notes:| Multi-line Note field with comments  
  
* Note that the Serial # would not be included in Phase 1; it would be added when Device records are added.

  


Grouped by: N/A

  


Sorted by: N/A

  


Filters: N/A

  


Buttons: N/A

  


Menu Visibility: All users

  


Other Notes:

  * The right pane is will show details for one incident at a time.



  


Development Specification

Austin Priest 05/18/2023: [[[IN7945](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-7947&)]] - [[PC0153561]] - ZTK - Service Incidents Report - Filter Bug

  


  


Mockups: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=802012883](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=802012883)

  


  


BID: 1 day
