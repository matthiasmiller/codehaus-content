1.3.1. Tracking Service Runs

  


Requirements

Overview: When doing a Service Run, several jobs/incidents with service locations in the same general area are grouped together and assigned to the tech doing the run. Driving time will be tracked on a "Travel Time"-type incident and then automatically divided evenly between the jobs on that Service Run. 

  


General Workflow: 

  * A tech on a Service Run tracks driving time on a "Travel Time"-type incident. 
  * A Service Run number for the current day is stored on the Time Card for Travel Time incidents and non-Shop incidents, to divide time properly for service runs. 
  * The Daily Service Run numbers will be non-editable numbers 1 - 9. These will be reset every day.
  * When a tech starts tracking time on the Travel Time or non-Shop incidents, the "Svc Run" number is intelligently defaulted to the most recently used Service Run for that tech for the current day (or to "1" for the first Service Run of the day). If the tech starts a subsequent / separate Service Run for the same day, they can change the "Svc Run" number when starting/switching time tracking from an incident (or on the Time Card itself). 
  * When calculating the time for an incident, the Solution will look at all incidents with the same Svc. Run number for the day and split the tracked travel time equally between all of the Work Order incidents.  



  


Here are some examples of how to use the Service Runs feature:

  * Example 1: A tech has two jobs, one in Town A and one in Town B, and includes it all on one Service Run: 
    * When he drives from the shop to Town A, he tracks that time on "Travel Time" and sets Svc. Run to #1.
    * When he gets to Town A, he changes his time tracking to that job and again sets the Svc. Run to #1.
    * After finishing that job, he again switches to "Travel Time" with Svc. Run #1 while he drives to Town B.
    * When he gets to Town B, he again switches to track time for that job and again sets the Svc. Run to #1.
    * After finishing that job, he tracks time on "Travel Time" while driving back to the shop, with the Svc. Run set to #1.
    * The system then looks at all of those #1's and splits the Travel Time evenly between the Town A job and the Town B job.
  * Example 2: Same Town A and Town B scenario, but splitting it into 2 separate service runs: 
    * When he drives from the shop to Town A, he tracks that time on "Travel Time" and sets Svc. Run to #1.
    * When he gets to Town A, he changes his time tracking to that job and again sets the Svc. Run to #1.
    * After finishing that job, he switches to "Travel Time" but sets Svc. Run to #2.
    * When he gets to Town B, he switches to that job and sets Svc. Run to #2.
    * While driving back to the Shop, he tracks time on "Travel Time" and sets Svc. Run to either #1 or #2.
    * The system then looks at those #1's and #2's and splits the travel time accordingly between the Town A and Town B jobs.



  


Development Specification

Mockup: N/A

  


Ellis Miller 11/01/2023:

[ ] Add a new Incident Type of "Travel Time", but no special behaviors.

[ ] Maybe hide a few custom fields on the incident screen.

[ ] defaulting time card fields and calculating time is handled in "Changes to the Time Card"

  


4 Hours.

  


Prompts for Service Run

[ ] Add a new x30 "cStd Time Card - Incident Start.x30"

[ ] Takes a hidden ask checkbox "Show Svc Run"

[ ] Takes a hidden Incident ID

[ ] Conditionally shows a Svc Run drop list based on vAskShowSvcRun

  


[ ] Add a new x30 "cStd Time Card - Incident Switch.x30"

[ ] Uses vAskCategory list like "Std Time Card Clock In.x30" 

[ ] Conditionally shows a Svc Run drop list based on which incident is selected (IncidentUsesSvcRun)

[ ] The Service Run drop list default value will default to the current service run from the time card. 

  


[ ] Create macros (e.g. CustomIncident_TimeCardStartPath and CustomIncident_TimeCardSwitchPath) that are overridden in ZGA to point to the new x30's. 

[ ] For the StartPath, If we are on an incident that uses Service Runs, we need to pass in |? to force a prompt. If we are on another incident, we should just use |.

Bid 2 Days
