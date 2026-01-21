10.1.9. Aging Invoices Report

  


Requirements

This would be AppHosting's standard Aging Invoices Report, with the addition of a Publication column and a Publication filter for Full Admin Users. 

  


This report would show current and overdue invoices. There would be columns for:

  * Invoice Number
  * Invoice Date
  * Invoice Due Date
  * Days Overdue
  * Contact 
  * Organization 
  * Due Amount 
  * Aging (showing Due Amount) 
    * Current
    * 1-30 Days
    * 31-60 Days
    * 61-90 Days
    * 90+ Days
  * Publication (Full Admin only)



  


The following columns would show a total sum:

  * Due Amount
  * Current
  * 1-30 Days
  * 31-60 Days
  * 61-90 Days
  * 90+ Days



  


The report would have the following filters:

  * Group By (list of Contact, Days Overdue, Organization)
  * Invoice date range ("from" and "through" dates)
  * Days Overdue (default to blank = all; multi-select list of Current, 1-30 Days, 31-60 Days, 61-90 Days, 90+ Days)
  * Contact(s) (default to blank = all; multi-select list of all Customers)
  * Organization(s) (default to blank = all; multi-select list of all Organizations)
  * Include draft invoices (checkbox; defaults to blank)
  * Publication (only for Full Admins; list of publications; default to blank = all)



  


Development Specification

Tim Reitz 12/21/2020: AppHosting Aging Invoices report: [https://demo.apphosting.zone/Reports/Standard/Std_Invoice_Aging?Asks=..](https://demo.apphosting.zone/Reports/Standard/Std_Invoice_Aging?Asks=..).

  


Standard report customizations: Use custom macros to control a customized column (heading, contents, visibility) and custom macro for report subset (custom ask prompt).
