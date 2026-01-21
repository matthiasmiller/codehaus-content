2.1. Sales Rep Fields

Matthias Miller 07/27/2021: 

  


Add the following fields to the salesperson:

  * Pay Period
    * Weekly
    * Biweekly
    * Monthly
    * This follows the same list and logic as builder pay periods in the Payroll Module.
  * Override commission balance start date (checkbox with a required date if checked; date must be the start of a week). Normally, the commission balance will restart at the beginning of the year. If this is specified, it will start as of that date, and it will roll over from year to year
  * Commission RG
    * Effective Date (must start of week)
    * Compensation Type (informational only)
      * Hourly
      * Salaried
    * Commission Only
    * Straight Commission %
    * Over Goal Commission %



  


Dev Specs:

  * To enforce Start of Week, you can either add validation or a simple OnChange of StartOfWeek( DetailNewValue).


