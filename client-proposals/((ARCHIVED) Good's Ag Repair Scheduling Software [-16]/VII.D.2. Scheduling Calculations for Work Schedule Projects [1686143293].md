7.4.2. Scheduling Calculations for Work Schedule Projects

Scheduling calculations for projects in the "Work Schedule" stage: 

  


Overview: The "Work Schedule" stage is used for projects that have not been assigned to a tech. Special calculations are used to project the next available Start Date based on the Estimated Hours on the incidents in this stage against the number of unassigned hours for all techs (looking at incidents that are assigned to the techs and at the "Weekly Shop Schedule" and "Shop Schedule Override" fields on the employees' Contact record). Jobs are held in "Work Schedule" and then assigned to the techs on a daily (or even hour-to-hour) basis. 

  


The goal is to have moderately accurate Projected Start and Calculated Finish Dates for individual jobs while also providing the next combined available Projected Start Date. This would involve doing hidden/background assignments based on individual techs' availability. For example, if there are 48 hours available in a day (8 hours each for 6 techs), the software could break that into 8-hour blocks, and spread those blocks across the scheduled jobs. Thus a 40-hour job would get assigned 5 days' worth of 8-hour blocks to arrive at the calculated finish date for that individual job, as if it were actually assigned to a tech. 

  


Calculating the Projected Start Date field (Work Schedule): Determine the next date on the "Work Schedule" that the shop has availability to start a new non-child incident (child incidents display the date from their parent):

  * Look at the Calculated Finish Date for the bottom-most incident in the Work Schedule grouping.
    * If there are no incidents in the grouping, look at the current date.
  * Determine how many hours are allotted to that bottom-most incident for that date.
  * Look at the Daily Shop Hours on the AppHosting.Zone Settings page to determine how much total time the shop has available on that date.
    * If there is unallocated time on that date, set the Projected Start Date to that date.
    * If there is no unallocated time on that date, look at the Daily Shop Hours again and set the Projected Start Date to the next date that has availability.



  


Calculating the Estimated Hours field (Work Schedule): Same as for active projects.

  


Calculating the Calculated Finish Date field (Work Schedule): Determine the date that the project should be finished (child incidents display the date from their parent):

  * Look at the Projected Start Date on the incident.
  * Look at the Estimated Hours on the incident.
  * Look at the Daily Shop Hours on the AppHosting Settings page.
  * Allocate hours on the Work Schedule based on availability until all of the Estimated Hours have been allocated.
  * The date on which the last allocated time falls is the Calculated Finish Date.  



  


Calculating the Projected Finalization Date field (Work Schedule): Same as for active projects.
