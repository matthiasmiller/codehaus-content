4.1.1.7. Calculating Vacation Days

  


Requirements

Vacation days can be calculated with different methods for different companies. Josh will be able to configure vacation tracking as needed on a per-company basis.

  


As discussed, the ideal vacation policy would be to prorate vacation hours, making them available the following January. (For example, someone starting on June 1 would not get any immediate vacation days. They would receive 20 vacation hours on January 1 of the next year. They would receive 40 vacation hours on January 1 of the following year.)

  


While vacation hours do not roll over in this ideal policy, it would be possible to provide that if needed.

  


Development Specification

CCI will be adding the three fields, configuring Expression Field Requirements, and validation. They will not be specifying the expressions, so the details on calculations can be ignored.

  


Fields

The Company record will have three expressions to control vacation tracking. Each one can reference fields on the Contact record:

  


  * Total Vacation Days (CompanyContactTotalVacDaysExpr). It will accept a date and return the total number of vacation days available as of that date.



  


  * Vacation Year Start Date (CompanyContactYearStartDateExpr). It will accept a date, and return the beginning date of that vacation year. If not specified, it will default to the beginning of the calendar year.



  


  * Vacation Year End Date (CompanyContactEndDateExpr). It will accept a date, and return the ending date of that vacation year. If not specified, it will default to the end of the calendar year.



  


These are numeric expressions. Each has a vAsOfDate parameter. If one is specified, all 3 should be specified.

  


The Vacation Year Start/End Date will be used to determine the number of used vacation days. We will not require this to land on a start or end of week.

  


Design Notes

We do not need to have dated RGs for the vacation settings, since we can simply adjust the expression if needed.

  


We will allow the Vacation Year Start/End Date to be calculated for the middle of the week. This will allow supporting vacation time that's based on the calendar year.

  


If you do want to calculate the Vacation Year Start/End Date to fall on the start/end of a week, we propose:

  * Find the start of the week for the Hire Date anniversary for the previous year, requested year, and following year.
  * If the requested date falls between last year and this year, return the first date range.
  * Otherwise, return the second date range.



  


Bid: 4 hours

  


Tim Reitz 12/30/2020: Matthias - Thoughts on the additional features in the Calculating Vacation Days section of the Company Record (mockups)?

Matthias Miller 01/22/2021: Will review through the mockups
