7.2.2. Company Payroll Overview

  


Requirements

This section provides a payroll overview for the entire company.

  


The Production Payroll $ is calculated by the Employee Hourly Wages for time spent in production, taking into account overtime hours.

  


The Non-Production Payroll $ includes Salaried Employee Wages, as well as Employee Hourly Wages for time not spent in production.

  


Overview

The Company Payroll Overview would include general company information for the reporting period:

Company| Shed Time  
---|---  
Reporting Period|   
  
     Week #| 45  
     Dates| 11/1/2020 - 11/7/2020  
Production|   
  
     # of Completed Buildings| 30  
     Production Total $| $164,630.28  
     Production Hours (time card hours)| 380  
     Production Overtime-Adjusted Hours| 400  
Production Pool|   
  
     Pool %| 7.5%  
     Pool $ Subtotal | $12,347.27  
     Labor Intensive Building Adjustments     (Dog kennels, Cottages, and on-site)| $525.17  
     Pool $ Total| $12,872.44  
     Pool Surplus/Deficit(This is calculated by taking the total production bonus paid minus the production bonus pool. If money is left over from the pool, it's a surplus. Otherwise, it's a deficit. Show the number as an absolute value.)|   
  
Base Payroll $|   
  
     Production Payroll $| $7,723.89  
     Non-Production Payroll $| $2,391.55  
Bonuses|   
  
     Production Bonus     (Pool $ Total minus Base Wage $)| $5,148.55  
     General Bonus     (guaranteed wage)| $304.00  
     Discretionary Bonuses     (extra, transport, Christmas, general, etc)| $1,513.07  
     Total| $6,965.62  
Work Orders| $791.39  
     Hourly Adjustment| $1.98  
Gross Payroll| $16,289.67  
  
|   
  
Average Hourly Rates|   
  
     Avg Production Bonus / Production Hour     (calculated from Production Overtime-Adjusted Hours)| $12.87  
     Avg Production Wage / Production Hour     (calculated from Production Overtime-Adjusted Hours)| $32.18  
     Avg Non-production Payroll / Production Hour| $5.98  
  
  


Labor Intensive Building Adjustments

It will also include a section that shows all the buildings that adjust the pool amounts during the reporting date range:

Invoice #| Reason| Amount  
---|---|---  
123456| Dog Kennel| $275.17  
425124| On-Site| $250.00  
  
  


Discretionary Bonuses

It will also include a section that details the payroll bonuses by type:

Type| Amount  
---|---  
Thanksgiving Bonus| $1513.01  
  
  


General Bonuses

Name| Amount  
---|---  
Samuel| $304.00  
  
  


Work Orders

Invoice #| Reason| Amount  
---|---|---  
123456| Missing loft & window| $791.39  
  
  


  


Development Specification

NOTE: Since we will automatically create entries for transport bonuses on the time card (if it's enabled on the employee), the Transport Bonuses entry will always show up on this report, regardless of whether the employee received any bonus. (Thus, it will show up for the company if ANY of the employees have it enabled.) This creates consistency in reporting for the companies.

  


We need to make sure that Assist knows that the building is on-site. Check with Josh. Work with Jason on the Compass API to find out when it's an on-site building. We can maybe use line items to detect.

Nate Kilcrease 01/15/2021: Do we need to track this on the report itself? Does this belong in the Building Record?

Matthias Miller 01/15/2021: It should be on the building record, but I don't know whether we need to add a field or can look at imported line items from Compass. Defer without mockups.
