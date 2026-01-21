4.1.1.8. Break Times

  


Requirements

Each company will be able to configure break times. These break times can be automatically excluded from labor amounts (whether tracking by station or by employee) or from time cards (or both).

  


Each company will include an editable daily break schedule to cover all breaks, including lunch breaks. For example:

Start Time| End Time| Production Break| Payroll Break  
---|---|---|---  
9:00| 9:15| [ ] | [ ]   
11:00| 12:00| [ ] | [ ]   
15:00| 15:30| [ ] | [ ]   
  
  


This numbers will be used for profitability tracking and payroll. Each weekday will follow the same schedule. If the actual break times are adjusted for a specific date, simply adjust the times that are entered into Assist.

  


If the company uses employee-specific tracking, the station tracking will include durations only. None of the breaks should be flagged as production breaks.

  


If the company's time clocks do not include start/end times, the time cards will be entered based on the total duration worked. (For example, when working 8.5 hours, the time card should show a starting time of 0:00 and an ending time of 8:30.) Because these time slots reflect the total hours worked, not the actual times, no breaks should be entered.

  


Development Specification

If we need to adjust the schedule on a per-weekday or per-date basis, we can do that in the future.

  


Add fields: CompanyProdBreakStartTimeVal and CompanyProdBreakEndTimeVal

Add macros: CompanyProdBreakStartTimeStr and CompanyProdBreakEndTimeStr

  


The RG shows the Str versions. These are both required. 

  


Sort the RG by Start Time.

  


Use our standard parse and validate time macros.

  


Bid: 4 hours
