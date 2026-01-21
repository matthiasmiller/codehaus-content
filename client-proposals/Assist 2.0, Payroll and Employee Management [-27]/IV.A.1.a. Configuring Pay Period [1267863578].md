4.1.1.1. Configuring Pay Period

  


Requirements

On the Configure Payroll child screen there is a section for Configure Pay Period. This section contains the following: 

  * Pay Period (optional drop list of blank, Weekly, Biweekly, Monthly)
  * Pay Period Start Date (date field; visible and required if Pay Period = Biweekly) 



  


Other Notes: 

  * Each company will be configured to have a weekly, biweekly, or monthly pay period. The biweekly pay period would require a start date to be specified.
  * Monthly pay periods are paid for full weeks and do not include any partial weeks. Because Assist treats pay periods from Sunday through Saturday, whereas the shops are closed on Sunday, the monthly pay period would start the week of the first Monday. It would continue until the start of the next month's pay period.
  * The pay period will only be used to generate the automatic submission to the accountant. Biweekly and monthly reports would include multiple weeks.



  


Development Specification

  * Investortools-owned list for PayPeriods with options for Weekly, Biweekly, Monthly.
  * Company: Add CompanyPayPeriod field with this list. Required.
  * Company: Add CompanyPayPeriod StartDate. It should be visible if PayPeriod = "2 weeks". Required if visible.



  


Bid: 2 hours
