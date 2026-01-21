3.3. Commissions

We need to add a Commissions report.

  


  


Prompt for:

  * End of Pay Period (can be any day of week; default to the last day of the prior week; required)



  


Columns:

  * Sales Rep
  * Compensation Type
  * Start of Week
  * Straight Commission $
  * Over Goal Commission $



  


NOTES:

  * Commissions need to handle both a purchase and a cancellation to prevent numbers from changing because of a cancellation. In other words, we should add commission the week it was accepted, and should subtract it the week it was cancelled.
  * Straight commissions is a simple % calculation.
  * Over Goal sums all the sales from the starting date (as configured on the contact record), looking at the difference of the sum of all goals, and paying a % on the difference if its >0.
  * We should have multiple rows, one for each week in the pay period. These are split the same way as for the payroll module.


