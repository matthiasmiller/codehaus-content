3.1.1. Configure Holidays

  


Requirements

Assist will allow entering holiday dates that apply to all companies. These MUST be universal to all companies. If a certain company is not closed for a specific holiday, that holiday date must be entered for each of the other companies.

  


This will be an embedded spreadsheet of:

Start Date| End Date| Reason| Paid Time Off  
---|---|---|---  
12/24/2020| 01/01/2021| Christmas| [X]   
07/04/2021| 07/04/2021| July 4| [ ]   
  
  


For now, these dates will be entered manually for each year.

  


If a date is selected as Paid Time Off, it will only include individual employees who are configured to receive paid time off (see Entering Employee Information). This way, paid time off can be entered universally, even if certain companies do not provide paid time off to their employees.

  


Assist will stop using the New York Stock Exchange holidays list. Instead, these dates (and the ones specified on a per-company basis) will be automatically excluded from lead times.

  


Development Specification

This goes on AppHosting.zone Settings

  


Let's use this instead of the business day logic. Talk to Josh about how this should work with lead times.

  


Ellis Miller 06/08/2021: 

[ ] Start / End / Reason are required.

[ ] Validate that start date is <= end date. 

[ ] Validate that end date is within 14 days of Start.

  


Estimate: 2 hours
