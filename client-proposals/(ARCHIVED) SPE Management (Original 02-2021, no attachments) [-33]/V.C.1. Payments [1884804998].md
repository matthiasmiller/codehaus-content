5.3.1. Payments

  


Requirements

This report will show all payments for specific member agreements.

  


It will prompt for:

  * Member (blank = all)
  * SPE (blank = all)
  * Member Application Type (blank = all)
  * Member Application Date (start/end date; blank = all)
  * Tax Year (default to current tax year; blank = all)
  * Year (choice of Year 1 of 2 or Year 2 of 2; blank = all)
  * Accepted by SPE (choice of Yes or No; blank = all)
  * Admittance Status (blank = all)
  * Check Status (blank = all; multiple choice)
  * Deposit Date (start/end date; blank = all)



  


It will show one row per payment. It may include multiple rows for a single member application.

  


It will be grouped by SPE.

  


It will sort by Check Status, then by Deposit Date (if deposited), and finally by check date.

  


The columns should show:

  * Check Status
  * Deposit Date
  * Member (link to member application)
  * Approval
  * Check Amount
  * Check Number



  


It would include a total row for the check amount.

  


This will include a button called Schedule for Deposit. It will prompt for a date, then update all checks being "held" to being "Scheduled for Deposit" as of the entered date. (This will only update checks listed in the report.)

  


It will also include a button called Deposit Checks. It will prompt for a date (defaulting to today), then update all checks being "held" or "scheduled for deposit" to being "deposited" as of the entered date. (This will only update checks listed in the report.)

  


This report can be used to reconcile with QuickBooks by selecting the Check Status of Deposited.

  


Development Specification

Ellis Miller 02/09/2021: 

  


Member Application report, RepeatRG on Payments 

[ ] Lots of ask prompts for filtering

[ ] Simple columns

[ ] Schedule for Deposit and Deposit Checks: ModifyAll with a condition that status is held.

[ ] Use blank for shredded checks in total column.

  


Target: 1.5 days
