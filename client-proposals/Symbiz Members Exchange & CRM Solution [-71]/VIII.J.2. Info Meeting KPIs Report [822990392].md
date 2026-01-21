8.10.2. Info Meeting KPIs Report

  


Requirements

Overview: This is a custom report of KPIs for Events with Event Type = Info Meeting. 

  


Accessed from: Admin | Reporting | Info Meeting KPIs (bypasses the filters to open the report directly)  

  


Title: Info Meeting KPIs

  


Columns: 

  * Info Meeting (displays the Event ID; link to record; total row shows the number of Events) 
  * State / Province (displays the State or Province from the "Venue" address of In-Person and Hybrid Events) 
  * Event Status 
  * Symbiz Presenter 
  * Leads Registered (total row shows sum)
  * Lead Attended (total row shows sum) 
  * Attendance Rate (%) (total row shows overall percentage, i.e. <Leads Attended total> / <Leads Registered total> * 100; rounded to the nearest 1 decimal place) 
  * Leads Converted (total row shows sum)
  * Conversion Rate (%) (total row shows overall percentage, like Attendance Rate (%); rounded to the nearest 1 decimal place) 



  


Grouped by: 

  * If Group By = Event Status: Standard sequence.
  * If Group By = Symbiz Presenter: Alphabetically by Presenter name. 
  * If Group By = None: No grouping; all Info Meetings listed together. 



  


Sorted by: Event ID (alphabetical) 

  


Filters: 

  * Event Status (drop list of Event Statuses; defaults to blank = all) 
  * Execution Status (drop list of Execution Statuses; defaults to blank = all) 
  * Symbiz Presenter (drop list of Info Meeting Presenters; defaults to blank = all) 
  * State / Province (drop list of states and provinces selected on Info Meetings; defaults to blank = all) 
  * Group By (drop list of Event Status / Symbiz Presenter / None; defaults to Event Status) 



  


Buttons: 

  * N/A 



  


Menu Visibility: Regional Reps and Super Admins only (by virtue of it being on the Admin menu) 

  


Other Notes: 

  * If desired, this report could be changed to exclude canceled Info Meetings (or a filter could be added to choose which Event Statuses to include).



  


Development Specification

Change Requests:

  * Tim Reitz 07/10/2025: : Added in [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)


