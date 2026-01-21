6.1.3. Entering Building Time by Employee

  


Requirements

When tracking labor costs by employee, this will generally be entered after the shed has been completed, since the paper accompanies the shed's printed invoice. Each week, the company will be responsible for submitting all of their partially-completed time sheets to allow weekly profitability and payroll numbers.

  


If the selected company tracks building costs by employee, prompt for one or more invoice numbers on the right, then show the following spreadsheet with three rows per employee:

  


Employee| Prev Work Dates| Prev Hours| Date| Start Time| End Time| Hours Worked  
---|---|---|---|---|---|---  
(Invoice 1)|   
|   
|   
|   
|   
|   
  
(Employee 1)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 1)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 1)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 2)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 2)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 2)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 3)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 3)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 3)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 4)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 4)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 4)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 5)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 5)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 5)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 6)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 6)| (auto)| (auto)|   
|   
|   
| (auto)  
(Employee 6)| (auto)| (auto)|   
|   
|   
| (auto)  
  
|   
|   
|   
|   
|   
|   
  
(Invoice 2)|   
|   
|   
|   
|   
|   
  
Etc|   
|   
|   
|   
|   
|   
  
  
|   
|   
|   
|   
|   
|   
  
  
  


The employees would be auto-filled from the Company record. It would include all employees/owners that spend time in production (see Configuring Employee Compensation), with the option to manually enter additional employees if needed.

  


The Start Time would be auto-filled to 0:00. To keep things simple for the employees, the companies only track Duration when using employee time tracking. However, Assist will support both methods, allowing the End Time to be entered as the duration.

  


The Hours Worked will automatically exclude production break times, if specified.

  


The Previous Hours and Previous Work Dates would show the last time that the building was worked on. This would help to ensure that information doesn't get double-entered.

  


Assist will warn if the building had already been built as of the specified date.

  


NOTE: Burkholder Management is responsible to ensure the blank paper versions of the tracking include columns for the start and end time, if desired. They are also responsible to ensure the paper versions sort the employees by "LastName, FirstName" to be consistent with Assist.

  


Development Specification

Nate Kilcrease 01/15/2021: How do you think we should display the prompt (checkboxes, drop-down, multiple-choice, text box entry, etc.)?  Matthias Miller 01/15/2021: multi-line text box, one invoice per line

Nate Kilcrease 01/15/2021: Would this add an employee to all invoices or just one at a time? If just one at a time, we'd need a way to select just one invoice. Matthias Miller 01/15/2021: See above

Nate Kilcrease 01/15/2021: Should there be separate RGs per invoice? That would make adding employees manually easier.

  


We can use a repeat RG editable report with an init expression to add blank rows for all employees, with extra rows on the end.
