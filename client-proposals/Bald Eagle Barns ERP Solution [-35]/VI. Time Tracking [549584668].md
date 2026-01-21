6\. Time Tracking

  


Requirements

A custom feature would be included for tracking time, PTO, mileage reimbursement, and completed Tasks. This would be done using a custom record type called "Weekly Time Sheets" and related reporting.

  


The Main Menu would have a "Time Tracking" section with link options, including: 

  * My Time Sheet (opens the Time Sheet for the current user and current Work Week) 
  * View All Time Sheets (opens the Time Sheets report) 



  


BEB members track time in one of two ways: by the hour and by the day.

  


BEB's pay periods are 2 weeks, starting on Thursday and ending on Wednesday. The Weekly Time Sheets (both hourly and daily) would reflect the Thursday-Wednesday work week.

  


Overtime tracking looks at the hours worked in the work week (Thursday-Wednesday) and will not regard PTO time. A standard day is considered to be 8 hours, so overtime begins when the Total Worked Hours exceeds 40.0 hours for a work week. Note that Daily/Salary members do not get paid overtime. 

  


Note that for paid days off where a member also works (gets paid double), the Weekly Time Sheet will allow for tracking double time for that day in the Hours section (for Hours) and the Summary section (for Hours and Worked Days). For example, Worked Days will still show "1" for the Partial Day and "1" show in the PTO row below, and have both show in the Summary.

  


The Member Labor Report would be used as a "payroll report" to view payment due to members (see corresponding section of this proposal).

  


  


*Done.

  


Development Specification

For Hourly: Hardcode the standard workday length to 8 hours and the overtime threshold to 40.0 hours.
