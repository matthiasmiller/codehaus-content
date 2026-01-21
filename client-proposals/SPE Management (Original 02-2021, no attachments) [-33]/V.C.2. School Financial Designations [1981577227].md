5.3.2. School Financial Designations

  


Requirements

This report would show all designations by school. This is an internal report, not to be shared with the schools because it includes member names that should be anonymized.

  


It will prompt for:

  * Application Type (default to Completed by Member; blank = all)
  * School (blank = all)
  * SPE (blank = all)
  * SPE Application (blank = all)
  * Tax Year (default to current tax year; blank = all)
  * Member Application Status (multiple selection; blank = all; default to Admitted)



  


It should show:

  * School
  * Member
  * Address (member address & contact info)
  * City
  * State
  * Zip
  * County
  * Application Status
  * Payment Status
  * Deposit Date
  * School Net Amount
  * School Gross Amount



  


The School Net Amount should be 95% of the total.

  


It should be grouped first by School, then by SPE Application. 

  


It should be sorted by member name.

  


It should include a total amount.

  


This report can be used when a school representative wants to know their total designations for the school. It can be filtered to include all pending or admitted applications, regardless of whether the payment has been received.

  


AppHosting will include a version of this report that only shows the school names and school gross amounts. This will be provided through a "Show member detail" checkbox or through a completely separate (but similar) report.

  


Development Specification

The 95% should be a hidden, unchangeable system switch.

  


 Tim Reitz 01/26/2021: Has it been determined which [Show member detail or other report] it will be? Matthias Miller 01/27/2021: Ellis and team will do whatever they choose.

  


Ellis Miller 02/09/2021: 

[ ] Member Application Detail with RepeatRG on Designations.

[ ] Use Conditional Totals based on: NOT vAskShowMemberDetail. Some columns should have visibility of vAskShowMemberDetail. 

  


Target: 1 day
