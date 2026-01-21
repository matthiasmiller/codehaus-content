2.7. Scheduled Incidents Report

  


Requirements

This is a report of all Scheduled Incidents.

  


This is accessed from:

  * Good's Ag Repair | Scheduling | Schedule



  


Title: Scheduled Incidents

  


Columns: 

  * Assignee (no column name)
  * Title
  * Service Location
  * Stage
  * Est Hours
  * Worked Hours
  * Projected Start / Resume Date
  * Actual Start Date
  * Projected Finish Date
  * Due Date
  * Incident ID
  * Time Calculations (hidden unless Show Diagnostic Columns checkbox is checked)
  * Specified Sort Order (hidden unless Show Diagnostic Columns checkbox is checked)
  *  Date Scheduled (hidden unless Show Diagnostic Columns checkbox is checked)
  * Time Scheduled (hidden unless Show Diagnostic Columns checkbox is checked)



  


Grouped by: Assignee

  


Sorted by: Projected Start / Resume Date (oldest at the top)

  


Filters: 

  * Show jobs for next ___ days (number field)
  * Service Locations (list of all Service Locations; blank = all)
  * Show Diagnostic Columns (checkbox; defaults to unchecked)



  


Buttons: 

  * Reschedule (appears when hovering over a "+" sign below the Assignee's name; reschedules the selected incident)
  * Move to Last (appears when hovering over a "+" sign below the Assignee's name; moves the selected incident to the bottom of the Assignee's schedule)



  


Menu Visibility: All Users

  


Other Notes:

  * If an individual is a shadow for a project, that project will show in gray.
  * If any job has a projected finish date after the deadline, it will show in red.
  * Displays the follow messages at the bottom:
    * *Incidents where the assignee is shadowing are shown in grey. The start and end dates of such incidents do not affect the schedule of the shadow assignee.
    * *When an incident is projected to end after the due date, the due date is shown in red color.
    * *Only the projected date is shown in red when the incident is projected to finish in the past.
    * *Worked hours and projected date are shown in red when more hours than estimated have been tracked against the incident.



  


Development Specification

Technical Details

  * We would store an internal numeric Schedule Order for a job. It would default to Assignee's Latest Schedule Order + 1.
  * We would use a tie-breaker for schedule order such as IncidentID as a tie-breaker so we don't have to populate these fields
  * If you want to reorder an incident, you would code an x30 or modify button that would find the two adjacent incidents and average their Schedule Order values.


