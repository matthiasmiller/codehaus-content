2.5.3. Incidents: Scheduling Information

Incidents - Schedule

  * Total Estimated Hours. This could be filled in at any time, but would be required if it's being scheduled
  * Optional Deadline. If specified, the project must be completed by the end of day of the specified date.
  * Scheduled checkbox. Checking this would put it on the schedule for the current assignee.
  * Projected Start Date (automatic). This would calculated automatically based on the previous incidents' completion date.
  * Actual Start Date (automatic). This would be calculated automatically based on first date/time on the time card.
  * Projected Finish Date (automatic). This would be calculated based on the actual or projected start time, using the assignee's schedule and the total estimated hours.
  * Finished checkbox. Because the incident needs to go through billing, we'd have a separate finished checkbox. We would require this to be scheduled in order to close out the incident. At this point, the incident would get assigned to Stephen.
  * Actual Finish Date/Time (automatic). This would be the date and time that the Finished checkbox was checked.
  * Billed date/time. This would be a checkbox to indicate that the project had been billed. We would show a warning if the incident has tracked hours, but has been closed out without being billed.



  


We would also show an automatic stage:

  * Scheduled
  * Started
  * Completed
  * Billed



  


When an incident is scheduled, it would be put into the list of scheduled jobs. By default, it would go after all the assignee's currently scheduled items. However, you could use the Scheduling View to move it around.

  


In addition, if you change the assignee, it would automatically be scheduled after the assignee's current items, but you could use the Scheduling View to move it around.

  


The incident would show a warning on save if the projected finish time is after the deadline.
