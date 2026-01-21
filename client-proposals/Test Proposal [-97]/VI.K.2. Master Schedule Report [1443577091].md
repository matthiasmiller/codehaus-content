6.11.2. Master Schedule Report

New / updated spec for the Schedule report (note that the existing report may be overhauled to match the changes noted in blue, or a new report may be coded to replace the existing one): 

  


This is an editable report of Incidents that meet all of the following criteria: 

  * Stage = Ready to Invoice, Quality Control, Assigned to Tech, or Work Schedule 
  * Are non-child incidents or are child incidents with a different Assignee or Shadow Assignee than their parent



  


If an incident (non-child or child) has both an Assignee and a Shadow Assignee, it will appear twice on the report, once for each of those techs. Rows for Shadow Assignees are displayed in gray text and may overlap with the tech's other scheduled jobs (since Shadow Assignee jobs do iaffect the tech's schedule).

  


If a tech is an Assignee for a child job (different from the Assignee for the parent job), that tech's schedule is affected by the amount of hours on the child job. The Assignee for the parent does not receive that child job's hours on their schedule

  


Accessed from: The various versions of this report are accessed from other menu options (see corresponding sections of the proposal).

  


Title: 

TODO_SG: Tim Reitz 04/11/2024: Do you want to include the changes for Location Categories? That would affect jobs & the schedule report.

  * If "Assignee" filter is blank and "Location Category" filter is blank: "Full Schedule"
  * If "Assignee" filter is blank and "Location Category" filter has a selection: "Full <Location Category> Schedule" 
  * If "Assignee" filter and "Location Category" filter both have selections: "<Location Category> Schedule for <Assignee>"
  * If "Assignee" filter has a selection and "Location Category" is blank: "Full Schedule for <Assignee>" 



  


Columns: 

TODO_VA: Tim Reitz 04/11/2024: Make sure we updated this to match the fields that they want / don't want.

  * Assignee / Shadow (displays the Assignee or Shadow Assignee for the incident or applicable child incident; not editable) 
  * Title (editable for all incidents; incident title; link to record) 
  * Machine on Site (editable for non-child incidents; if the corresponding checkbox on the record is checked, this displays "Yes" in white text with green background for easy visibility; if the checkbox is unchecked, this displays "No" in regular black text with white background; report cell changes from Yes/No to a checkbox for editing)
  * Service Location (editable for non-child incidents) 
  * Job Progress (editable for all incidents) 
  * Est Hours 
  * Actual Hours (simply changing the column title to be consistent with the detail screen)
  * Target Start Date (editable for non-child incidents to allow for easy rescheduling; date field; displays red text if in the past and no time has been tracked on the project, otherwise displays black text) 
  * Projected Start / Resume Date 
  * Actual Start Date 
  * Projected Finalization Date 



TODO_VA: Tim Reitz 04/11/2024: How much do we need to rework to remove Finalization Date?

  * Parent ID (if the incident is a child incident, this displays the ID of the parent; otherwise is blank)
  * Incident ID 
  * Due Date (editable for non-child incidents) 
  * QC Passed (editable for all incidents; displays "Yes" if the corresponding checkbox on the incident is checked; otherwise is blank; report cell changes from Yes/blank to a checkbox for editing) 
  * Status Summary (editable for all incidents) 



  


Grouped by: 

  * If "Location Category" filter = "Shop":
    * First by: Stage (Ready to Invoice, Quality Control, Assigned to Tech, Work Schedule) 
    * Second by: Assignee / Shadow (alphabetically) 
  * If "Location Category" filter = "Service Truck": 
    * First by: Stage (Ready to Invoice, Assigned to Tech, Work Schedule)
    * Second by: Assignee / Shadow (alphabetically) 
    * Third by: Service Location (alphabetically)
  * If "Location Category" filter = "All": 
    * First by: Stage (Ready to Invoice, Quality Control, Assigned to Tech, Work Schedule) 
    * Second by: Assignee / Shadow (alphabetically, excluding "Shop") 
    * Third by: Service Location ("Shop" at the top, then alphabetically)



  


Sorted by:  

  * First by: Target Start Date (with blank at the top, followed by earliest date, with furthest date into the future at the bottom) 
  * Second by: Remaining Estimated Hours ("Estimated Hours" for the incident minus "Actual Hours" for the incident), lowest value at the top
    * Note: This looks at the Estimated Hours and Actual Hours for each incident on the schedule, so for parent incidents it is the sum of the parent and all child incident; for child incidents assigned to a different Assignee than the parent, it is just the child job's hours. 
  * Third by: Incident ID (alphabetical / lowest at the top) 
  * Note that this is the same sequence used for calculations for jobs with the same Target Start Date, so changes to one should be considered in light of the other as well.  



  


Filters: 

  * Show jobs for next [    ] days (number field; looks at the Projected Finished Date; defaults to blank = all)
  * Location Category (required; drop list of Shop / Service Truck / blank = all; defaults to blank = all or based on menu option selection; see additional details on the Service Location record section of this proposal) 
  * Service Locations (multi-select drop list of Service locations; filtered based on the selection in the "Location Category" prompt; defaults to blank = all) 
  * Incident ID (drop list of Incident IDs for Incidents that are on the report; filters down as you type; defaults to blank = all) 
  * Incident Contact (drop list of Contact names; filters down as you type; defaults to blank = all) 
  * Assignee (drop list of Assignees and Shadow Assignees together; defaults to blank = all or based on menu option selection) 



  


Buttons: 

  * New Incident (opens a blank new incident record, with Type and Workflow both defaulted to "Work Order") 



  


Menu Visibility: All users

  


Save Type: Instant Save 

  


Other Notes: 

  * Includes the following behaviors (and the following notes at the bottom of the report screen):
    * Incidents for which a tech is the Shadow Assignee are shown in gray on this report. The start and end dates of such incidents do not affect the schedule of the shadow assignee.
    * When an incident is projected to end after the Due Date, the Due Date is shown in red color. 
    * Only the Calculated Finish Date is shown in red when the incident is projected to finish in the past.



TODO_VA: Tim Reitz 04/11/2024: I'm not seeing this column on the report spec...

  * Actual Hours and Projected Finished Date are shown in red when more hours than estimated have been tracked against the incident.



TODO_VA: Tim Reitz 04/11/2024: I'm not seeing this column on the report spec...

  * The Solution looks at the total available time when scheduling any job (Shop or non-Shop). There is not time specified separately for Shop or Service Truck jobs. 
  * Since sorting now going to happen by Target Start Date, there isn't a need to manually moving the jobs around on the Schedule. The rearrange / reschedule feature is to be removed.


