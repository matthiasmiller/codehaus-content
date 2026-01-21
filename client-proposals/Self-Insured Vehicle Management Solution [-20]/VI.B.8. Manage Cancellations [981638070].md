6.2.8. Manage Cancellations

  


Requirements

TODO_VA: standardize per current "reports" snippet

  


This is a report of clients who are inactive or who have no active vehicles.

  


This is accessed from Admin | Cancellations | Manage Cancellations. 

  


Title: Manage Cancellations

  


Columns: 

  * Name
  * Agent
  * Client Deactivation Reason
  * Reportable



  


Total Rows: total rows for number of vehicles in the Name column, at the bottom of each grouping, and a grand total at the very bottom of the report. The new spec would read as follows: 

Name (link to open record; total rows and grand total row show sum in the following format: "<sum> Vehicles") 

  


Grouped by: Active with No Active Vehicles, Snoozed, Inactive

  


Sorted by: Name

  


Filters: 

  * Start Date
  * End Date (defaults to the current date)
  * Agent (Blank = All) (drop-list of active in-state agents with a fund)
  * Include Inactive (checkbox; defaults to unchecked; if checked, the "Inactive" group and all corresponding Inactive vehicles are included at the bottom of the report)



  


Buttons: 

  * Deactivate Selected Clients (prompts for Effective Date, then deactivates the selected clients)
  * Snooze Selected Clients (prompts for Effective Date, then snoozes the selected clients)
  * State Report (opens the Cancellations of Clients State Report)



  


Menu Visibility: Admin

  


Development Specification

Change Requests: 

  * Austin Priest 09/19/2023: [[[IN8639](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8641&)]] - [[PC0158491]] - ZWA - Changes to Manage Cancellations Report (T&M)


