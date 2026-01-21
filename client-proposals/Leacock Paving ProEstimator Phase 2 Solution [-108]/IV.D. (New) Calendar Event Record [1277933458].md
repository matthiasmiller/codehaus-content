4.4. (New) Calendar Event Record

  


Requirements

This is the core scheduling record that ties a job to a specific crew, date range, and the crew members, trucks, and trailers assigned for each day.

  


  * Calendar Event section: 
    * Event Type (required; drop list of "Calendar Event Types")
    * Start Date (date; required) 
    * Multiday (checkbox) 
    * End Date (editable & required if "Multiday" is checked and "Start Date" is specified; otherwise, read-only and equal to the "Start Date")



  


Includes the following conditionally-visible fields, based on "Event Type": 

  * For "Time Off"-type Events
    * Employee (required; drop list of active Employees)



  


  * For "Job"-type Events:
    * Job ID (link to view the linked Proposal)
    * Groups (multi-select list of Groups; defaults to all "Awarded" Groups for the linked Proposal)
      * Hidden embedded spreadsheet of Groups from the Proposal
    * Crew Type (drop list of "Crew Types" list items; required)
    * Crew (drop list of active Crews for the selected "Crew Type"; required)
    * Crew Members - This is the day-by-day roster showing who's on the job, who's the foreman, and what resources they're taking - the digital version of your current manpower Excel sheet. (embedded spreadsheet with the following: 
      * Columns: 
        * Date (required)
        * Employee (required; drop list of active Employees)
        * Foreman (checkbox; only allow 1 / day; require 1/day; checking this checkbox sorts the corresponding employee to the top of the list; this is defaulted based on the "Crew Foreman" checkbox on the Employee's Contact record)
        * Truck (drop list of active Trucks)
        * Trailer (drop list of active Trailers)
        * Equipment (drop list of active Equipment) 
    * # of Hired Haulers (number; 0 decimals)



  


  * Job Downtime - This tracks unproductive time on the job site (waiting on material, weather delays, customer not ready) with start and end times and a reason code, so you have visibility into where time actually goes. (embedded spreadsheet of the following; used for tracking non-work time spent on the job:
    * Date (required)
    * Start Time (required; time field) 
    * End Time (required; time field)
    * Reason (required; drop list of "Downtime Reasons")
    * Notes (plain text) 



  


  * For "Other"-type Events
    * Title (required; plain text) 



  


  * Additional validations:
    * Warn when scheduling a prevailing wage job on a Friday.
    * Disallow having the same Job ID + Crew for the same day



  


Development Specification

Mockups: 

  * Job: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1718071714#gid=1718071714](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1718071714#gid=1718071714)
  * Time Off: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1988056554#gid=1988056554](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1988056554#gid=1988056554)
  * Other: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=976591927#gid=976591927](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=976591927#gid=976591927)



  


  


  


TODO_IDD: Tim Reitz 12/03/2025: What would be the unique ID for this record?

  


  * Job Downtime



_HLD: Tim Reitz 12/03/2025: I'm thinking this RG belongs on the Calendar Event / "Job" record, since it's event/phase-specific. Then maybe a virtual RG on the Proposal record that show all?  

Matthias Miller 12/03/2025: Don't care. I updated downtime as an amount of time shown on the RG. 

Matthias Miller 12/03/2025: This means you can't reschedule anything that has downtime attached.

TODO_IDD: Tim Reitz 12/04/2025: Work on this.
