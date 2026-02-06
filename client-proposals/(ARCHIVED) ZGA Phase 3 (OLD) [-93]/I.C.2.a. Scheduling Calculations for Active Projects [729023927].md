1.3.2.1. Scheduling Calculations for Active Projects

  


Requirements

Scheduling calculations for active projects (incidents in the "Assigned to Tech", "Quality Control", and "Ready to Invoice" stages): 

  


Overview: Calculations for scheduling projects in these stages will be done based on the "Weekly Shop Schedule" and "Shop Schedule Override" sections on the employees' Contact records (this is similar to how the scheduling calculations are currently being done).

  


Calculating the Projected Start Date field: Determine the next date on the Assignee's schedule that the Assignee has availability to start a new non-child incident (child incidents simply display the Projected Start Date from their parent):

  * Distinguish between "Schedule Rows" and "Shadow Rows" (Schedule Rows are rows for jobs with the Scheduled checkbox checked, even if there is no Assignee. Shadow Rows are rows for Shadow Assignees. Note that the same incident may show up on the Schedule report as a Schedule Job for the Assignee and a Shadow Job for the Shadow Assignee). Shadow rows/assignments do not affect schedules in any way.
  * Determine the sequence in which the jobs should be scheduled (based on Target Start Date, then Estimated Hours, then Incident ID). Note that this means that started and unstarted jobs may be interspersed on the schedule.
  * Look at the Calculated Finish Date for the bottom-most incident on the Assignee's schedule.
    * If there are no incidents scheduled for the Assignee, take the current date.
  * Determine how many hours are allotted to that bottom-most incident for that date.
  * Look at the Weekly Shop Schedule and the Shop Schedule Override on the Assignee's Contact record to determine how much total time the Assignee has available on that date.
    * If the Assignee has unallocated time on that date, set the Projected Start Date to that date.
    * If the Assignee does not have any unallocated time on that date, look at the Weekly Shop Schedule and the Shop Schedule Override again and set the Projected Start Date to the next date that the Assignee is available. 



  


Calculating the Estimated Hours field: 

  * For an independent incident, or for a child incident, this is editable and manually set (no calculations needed)
  * For a parent incident, this dynamically displays the sum of all Estimated Hours fields on the child incidents.



  


Calculating the Calculated Finish Date field: Determine the date that the project should be finished (child incidents simply display the date from their parent):

  * Look at the Projected Start Date on the incident.
  * Look at the Estimated Hours on the incident.
  * Look at the Weekly Shop Schedule and the Shop Schedule Override on the Assignee's Contact record.
  * Allocate hours on the Assignee's schedule based on their availability until all of the Estimated Hours have been allocated.
  * The date on which the last allocated time falls is the Calculated Finish Date.



  


Calculating the Projected Finalization Date field: Determine the date on which the project should be finalized, accounting for time anticipated to be spent waiting on parts to arrive, etc.:

  * Look at the Estimated Hours for the project.
  * For every 40 hours of Estimated Hours, allot 8 additional "waiting" hours (i.e. 1 "waiting" day) .
  * Look at the Calculated Finish Date for the incident and add the "waiting" day(s) after the Calculated Finish Date (looking at business days only).
  * The date on which the last "waiting" day falls is the Project Finalization Date.



  


Development Specification

Mockup: N/A

  


  


Ellis Miller 11/07/2023: Dev Spec:

  


Make this Unit Testable:

Pass One pulls all date into a Data Table including separate rows for all child jobs. This is what we use for Unit Test inputs.

Find All Scheduled, non-completed jobs (using some Aggressive Ndx with lots of info in the key). Expand out all child jobs:

Job Assignee<tab>DateSortSTring(TargetStartDate)<tab>Pad(ThisJobEstimatedHours)<tab>JobIncidentID<tab>JobHoursWorked<tab>ProjectIncidentID

  


Pass 2 combines these into "Scheduled Jobs" merging child jobs with the same assignee into the parent row.

  


Sort these by the row to get them in the right order.

  


Consider Ndx subsetted to scheduled, incomplete by:

ListNum(JobAssignee) + TargetStartDate + ProjectIncidentID\+ ??

  


Sort these as a pipe list to get them in allocation order

Complex while loop to add Calculated Assignee Finish Date to the table.

  


This gives us the ScheduleMatrix (ignoring the unscheduled jobs)

  


To determine the ProjectFinishDate, just do a ListSubstitute looking for the Max Date based on ProjectIncidentID.

  


Projected Finalization Date is a (almost) simple calculation from Project Finish Date, we just need to skip weekend days.

  


BID: 7 Days including Ellis's Time
