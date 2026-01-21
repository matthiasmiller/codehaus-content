1.3.2. Scheduling Logic

  


Requirements

Project Finalization Date overview: Every project has a "Projected Finalization Date" field on the non-child incident and a corresponding column on the Schedule report. This date is calculated by adding extra time after the Calculated Finish Date to account for time spent waiting on other things (i.e. waiting on parts to arrive). 

  


Additional notes: 

  * This date is used only for reference purposes and does not affect schedule calculations in any way. 
  * This date updates as the Calculated Finish Date changes throughout the duration of the project. 
  * For a project with 0-40 Estimated Hours, there should be 8 hours added to it. For every additional 40 hours, another 8 hours of waiting time should be added. For example:
    * 0-40 Estimated Hours = 8 hours added
    * 41-80 Estimated Hours = 16 hours added
    * 81-120 Estimated Hours = 24 hours added
    * 121-160 Estimated Hours = 32 hours added  
  * Example calculations: 
    * 10 Estimated Hours for the project + 8 waiting hours = 18 hours from the Projected Start Date / time until the Projected Finalization Date
    * 45 Estimated Hours for the project + 16 waiting hours = 61 hours from the Projected Start Date / time until the Projected Finalization Date
    * 85 Estimated Hours for the project + 24 waiting hours = 109 hours from the Projected Start Date / time until the Projected Finalization Date
  * The waiting hours are added to / based on the total number of Estimated Hours for a project, even if there are multiple techs assigned to jobs in the project. 



  


Scheduling example(s): 

  * One tech: 
    * Project assigned to a tech with 15 total Estimated Hours for the project (sum of all child incidents' Estimated Hours or the Estimated Hours for an independent incident). 
    * Project Finalization Date is 15 + 8 = 23 hours after the Projected Start Date / time. 
  * Multiple techs: 
    * Project assigned to Tech A with 42 Estimated Hours for the project; 12 hour child incident assigned to Tech B. 
    * Projected Finalization Date is 42 + 16 = 58 hours after the Projected Start Date / time. 
    * Tech A's schedule accounts for 30 hours of the project (not the 12 hours for Tech B) and Tech B's schedule accounts for the 12 hours from his assigned child incident. 
    * Both Tech A and Tech B's schedules have the job scheduled to start on the Target Start Date. 
    * Tech A's schedule shows the parent job for the project, and Tech B's schedule shows the child job to which they are assigned. 



  


Other Notes: 

  * Note that projects in the "Pending" and "Complete" stages do not have any scheduling calculations applied to them.



  


Development Specification

Mockup: N/A

  


Tim Reitz 10/10/2023: Here is a macro that is currently being used: JobScheduler_CalcMatrix

  


Tim Reitz 10/21/2023: Here's a list of ZGA jobs with "Schedul" in the title: [https://docs.google.com/spreadsheets/d/1JzOE8XR-RJ8XoYoiw8Rzz2nlKHzCpQzf/edit#gid=1569620913](https://docs.google.com/spreadsheets/d/1JzOE8XR-RJ8XoYoiw8Rzz2nlKHzCpQzf/edit#gid=1569620913)
