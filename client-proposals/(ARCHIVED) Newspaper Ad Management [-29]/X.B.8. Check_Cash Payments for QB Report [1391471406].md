10.2.8. Check/Cash Payments for QB Report

This report would be used for tracking check and cash payments received, and for entering them into QuickBooks. These would be entered as lump sum entries into QuickBooks.

  


This would be an editable report. 

  


Columns

  * Invoice # (link; for reference purposes)
  * Customer 
  * Payment Date 
  * Payment Amount 
  * Deposited (checkbox) 
  * Publication (only for Full Admins)



  


There should be a Total row for the Payment Amount column, on a per-group basis. 

  


Filters

  * Date Range (for Payment Date; default to blank = all)
  * Show (Deposited, Undeposited, All; default to All)
  * Publication (only for Full Admins; list of publications; default to blank = all)



  


Grouping/Sorting

  * Group by Deposit Date, Ueposited at the top
  * Sort by Payment Date (most recent at top)



  


When the user is ready to enter check/cash transactions into QuickBooks, they would open this report. They would check the "Deposited" checkbox of the payments in the Undeposited group that they want to deposit and enter into QB, then save the report. The report would automatically re-run and group the selected lines together with the current date as the Desposit Date, with a total row for that group. The user could then use that total amount to enter the lump sum amount into QB.
