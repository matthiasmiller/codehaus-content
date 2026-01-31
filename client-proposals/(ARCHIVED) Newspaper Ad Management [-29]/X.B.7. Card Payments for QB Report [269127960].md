10.2.7. Card Payments for QB Report

  


Requirements

This report would be used for tracking card payments received, and for entering them into QuickBooks. 

  


This would be an editable report. 

  


Columns

  * Invoice # (link; for reference purposes)
  * Customer 
  * Estimated Payout Date (the Payment Date + 2 days)
  * Payment Amount 
  * Merchant Fee 
  * Total Amount (difference of Payment Amount and Merchant Fee) 
  * Entered in QB (checkbox; default to cleared)
  * Publication (only for Full Admins)



  


Example: If the payment amount was $100.00 and the merchant fee was $3.00, the three amount columns would display the following:  

  * Payment Amount: 100.00 
  * Merchant Fees: 3.00 
  * Total Amount: 97.00 



  


There should be a Total row for the Payment Amount, Merchant Fees, and Total Amount columns, on a per-group basis. 

  


Filters

  * Date Range (for Estimated Payout Date; default to blank = all)
  * Show (list of Entered in QB, Not Entered in QB, All; default to All)
  * Publication (only for Full Admins; list of publications; default to blank = all)



  


Grouping/Sorting

  * Group by Estimated Payout Date
  * Sort by Payment Date (most recent at top)



  


When the user is ready to enter card transactions into QuickBooks, they would open this report. As they enter the transaction information into QB, they would check the "Entered in QB" checkbox and save the report by clicking the "Save Changes" button at the top.

  


Development Specification

Projected Settle Date: Have a System Switch "Settle Date Business Days" \- default to 2; have a macro that takes the Payment Date and increments it by 2 business days.
