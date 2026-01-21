18.0.3.1. Payments

  


Requirements

This report will show all payments for member applications with a check date.

  


Accessed from: Accessed from: Faith Builders SPE | Financial Reports | Payments

  


Title: Payments

  


Columns:

  * Check Status
  * Deposit Date
  * Member (link to member application)
  * Approval
  * Check Amount (total type = sum)
  * Check Number



  


Filters:

  * Member (blank = all) (drop-list of contacts marked Eligible for SPE)
  * SPE (blank = all) (drop-list of SPEs)
  * Application Type (blank = all) (drop-list of Prefilled by SPE, Completed by Member)
  * Tax Year (blank = all) (default to the current tax year)
  * Member Application Start Date (blank = all)
  * Member Application End Date (blank = all)
  * Admittance Status (blank = all) (drop-list of admittance statuses)
  * Accepted by SPE (blank = all) (drop-list of Yes or No)
  * Deposit Start Date (blank = all) 
  * Deposit End Date (blank = all)
  * Check Status (blank = all) (multi-select drop-list of check statuses)
  * Year Number(blank = all) (drop-list of Year 1 of 2, Year 2 of 2)



  


Grouped by:

  * SPE, if SPE is not entered, admittance status.



  


Sorted by:

  * Check Status, then by Deposit Date (if deposited), and finally by Check Date.



  


Buttons:

  * Schedule for Deposit: prompts for a date, then updates all checks with a status of "Held" to "Scheduled for Deposit" as of the entered date. (This will only update checks listed in the report.)
  * Deposit Checks. Prompts for a date (defaulting to today), then updates all checks with a status of "Held" or "Scheduled for Deposit" to "Deposited" as of the entered date. (This will only update checks listed in the report.)



  


Additional notes:

  * This report can be used to reconcile with QuickBooks by selecting the Check Status of Deposited.



  


Development Specification

Ellis Miller 02/09/2021: 

  


Member Application report, RepeatRG on Payments 

[ ] Lots of ask prompts for filtering

[ ] Simple columns

[ ] Schedule for Deposit and Deposit Checks: ModifyAll with a condition that status is held.

[ ] Use blank for shredded checks in total column.

  


Target: 1.5 days
