2.5.2. Incidents: Child and Parent Incidents

Breaking Down Jobs/Using Child Incidents: The software uses AppHosting's standard child incidents feature, with the following additional notes: 

  


Misc Notes (Good's Ag): 

Each child incident should have its individual time estimate. The sum of the time estimates for the individual incidents would be the estimate for the whole project (would display as the Combined Estimate on the parent incident). 

The parent incident does not have its own Estimated Hours or Finished Date (these are derived from its child incidents). 

The parent incident's end date would need to take into account all the end dates for the child incidents (it cannot be set to an earlier date than the latest end date of the child incidents). The schedule should show the child jobs and their end dates, rather than the parent job, since no one would be scheduled to do work on main job. The total hours for all the child jobs would be combined on the main job for the total estimated hours and final estimated end date.

A parent incident will not show up on the schedule. 

The child incidents can be marked as completed individually, but they would not use "Ready to Bill" or "Billed". They would use "Complete" when they are done. 

The parent incident does not advance to Ready to Bill until all the child incidents are marked Complete. 

The child incidents can be assigned to different assignees or can all have the same assignee. 

The parent incident will have its assignee set separately from the child incidents. 

The child incidents should not be dependent on each other - multiple ones can be going simultaneously. 

At this point "grandchild" incidents are not needed.

If a job does not need child incidents, it will behave like the current incidents do. 

  


For the Parent Job:

Estimated Hours - read-only sum of all child jobs

Actual Hours - read-only sum of all child jobs

Finished Date - becomes a macro; stored date for child jobs; NA if any child jobs are unfinished; otherwise, the latest date of all child jobs

Finished - based on date

Billed (same field as already on detail screen)

Projected Start Date - earliest date of all child incidents.

Projected End Date - latest date of all child incidents.

  


For the Child Job:

Billed will never be shown, since it should never be billable.

  


Validation:

Do not allow selecting a parent incident if the job is billable.
