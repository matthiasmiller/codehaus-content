4.4.1. Customer Credit Information Report

  


Requirements

This is a report of credit additions and deductions for the customer. It is opened via the View Credit Information link on the Customer/Ads Page. 

  


It should have the following columns: 

  * Date (the Invoiced Date or the Paid Date, as applicable)
  * Invoice Number (link to the invoice detail)
  * Purchased Credit Amount
  * Applied Credit Amount
  * Credit Balance (running sum)



  


The lines should be sorted by Invoice Number.

  


Development Specification

Date Column: We can either implement this with two columns (which will cause strange sorting), or we can do this:

  * Repeat for List on Invoice Date (if there was any applied credit) and Payment Date (if there was any purchased credit). Remove duplicates.
  * If the RepeatListItem = InvoiceDate, show the Applied Credit. Otherwise, leave it blank.
  * If the RepeatListItem = PaymentDate, show the Purchased Credit. Otherwise, leave it blank.
  * Sort by RepeatListItem (as a date sort string)


