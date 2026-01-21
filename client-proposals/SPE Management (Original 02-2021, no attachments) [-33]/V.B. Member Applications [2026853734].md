5.2. Member Applications

  


Requirements

This report will show member applications.

  


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



  


It will group first by admittance status, then by SPE Application (which includes SPE name).

  


It will show the following columns:

  * Member
  * Application Type
  * Application Date
  * Tax Year
  * Year # (Year 1 of 2 or Year 2 of 2)  
  * Total Amount
  * Amount Received
  * Accepted by SPE
  * Admittance Status
  * Payment Due Date (red if within warning period)
  * # of Prior Admitted Applications



  


It will include a total row for Total Amount.

  


The Amount Received would be calculated by adding all Held and Deposited payments.

  


The # of Prior Admitted Applications would show the total number of admitted applications across all SPEs. Count the number of applications with an Admittance Date before this application's admittance date (if specified) or application date (if not admitted).

  


It will have a button called "Accept Members". This will mark any selected members as Accepted by SPE. (Note that this may not update the admittance status if the application has not yet been completed by the member. If no payment has been received, the status will update to Waiting for Payment. This is handled automatically, as described in the Entering Information section.)

  


Development Specification

Ellis Miller 02/08/2021: 

  


[ ] Ask prompts: 4 hours

[ ] Basic Report: 4 hours

[ ] Prior admitted Applications. 4 Hours.

[ ] "Accept Members" button: 4 hours.
