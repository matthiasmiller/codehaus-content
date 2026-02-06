10.1.10. Statements

  


Requirements

Clicking on the Statements menu option would generate statements for all customers who have one or more overdue invoices. These would be generated on one PDF that could then be downloaded and/or printed. Individual statements generated and printed or sent via Email/Fax from the Customer/Ads Page

  


The statement would have a Statement Date, which is the date the statement is generated. 

  


The statement would have a table similar to the table on invoices: 

The following would show on the table as separate line items:

  * Invoices 
  * Late Fees 
  * Payments 
  * Prepay credits applied



  


The table would have the following columns: 

  * Invoice # (the number associated with the rest of the line item)
  * Date (invoice date, fee assessed date, or payment date) 
  * Description (see notes below)
  * Amount (amount due, amount assessed, or amount paid)
  * Balance (running total of items in the Amount column)



  


The line items should be grouped by Invoice # and sorted by Date (oldest at the top). 

  


The Descriptions for the different item types should be as following: 

  * For invoices: Invoice #, "Due <Due Date>"
  * For payments: "Partial Payment"
  * For late fees: "Late Fee Assessed" 
  * For prepay credits: "Credit Applied" 



  


There would be a Total Balance Due below the table. 

  


At the bottom of the statement there would be a breakdown of the amounts due in various periods: 

  * Current
  * 1-30 Days Overdue 
  * 31-60 Days Overdue 
  * 61-90 Days Overdue 
  * 90+ Days Overdue



  


Note that the appearance of the statement may vary from what is shown in the mockups.

  


Development Specification

Tim Reitz 01/11/2021: Sample statement:  [https://www.mucr.com/content/client/cfdd857eb36cf4c16eb14b6481fb7a44/uploads/qbnewsletter/issue6/figure4.jpg](https://www.mucr.com/content/client/cfdd857eb36cf4c16eb14b6481fb7a44/uploads/qbnewsletter/issue6/figure4.jpg)

Create an index for invoices that tracks: 

  * invoice Date
  * Late Fee Dates
  * Payment Dates



  


Create a report that shows all unpaid invoices. It should be a repeat for list report. It should generate rows with a date, transaction  description, and amount. The report should sort by date. It should include a running sum.

  


Feel free to adjust the layout of the printout as needed. 

  


Tim Reitz 03/04/2021: Ellis - Would Statements become a standard feature?

If so, would AppHosting/CCI pay for part of it?

Also, what features would we want to include?
