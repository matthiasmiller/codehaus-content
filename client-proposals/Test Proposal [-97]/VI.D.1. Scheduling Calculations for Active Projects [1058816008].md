6.4.1. Scheduling Calculations for Active Projects

Scheduling calculations for active projects (incidents in the "Assigned to Tech", "Quality Control", and "Ready to Invoice" stages): 

  


Overview: Calculations for scheduling projects in these stages will be done based on the "Weekly Shop Schedule" and "Shop Schedule Override" sections on the employees' Contact records (this is similar to how the scheduling calculations are currently being done).

  


Calculating the Projected Start Date field: Determine the next date on the Assignee's schedule that the Assignee has availability to start a new non-child incident (child incidents simply display the Projected Start Date from their parent):

  * Distinguish between "Schedule Rows" and "Shadow Rows" (Schedule Rows are rows for jobs with the Scheduled checkbox checked, even if there is no Assignee. Shadow Rows are rows for Shadow Assignees. Note that the same incident may show up on the Schedule report as a Schedule Job for the Assignee and a Shadow Job for the Shadow Assignee). Shadow rows/assignments do not affect schedules in any way.
  * Determine the sequence in which the jobs should be scheduled (based on Target Start Date, then Estimated Hours, then Incident ID). Note that this means that started and non-started jobs may be interspersed on the schedule.
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


