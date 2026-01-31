10.1.7. Invoices Report

  


Requirements

This report will show invoices, based on various criteria. This will be the standard AppHosting Invoices Report, with the addition of a Publication column and a Publication filter for Full Admin Users.

  


Left Pane: 

Views

  * Open Invoices (includes Draft and Invoiced statuses)
  * Closed Invoices (includes Paid and Canceled statuses)
  * All Invoices (includes all statuses)
  * By Publication Date (grouped by Publication Date; includes Status column))
  * Recent Invoices (grouped by standard report's date/date range; includes Status column)



  


Right Pane: 

Columns: 

  * Invoice Number (link to invoice page)
  * Invoice Date
  * Total Amount
  * Contact
  * Organization
  * Location (City, State)
  * Payment Date



  


Grouping/Sorting:

  * Grouped by Status (other than Recent Invoices and By Publication Date views)
  * Sorted by Invoice Date



  


Popping open this pane by itself gives the many filter invoices, including by Contact, Status, and Sales Item(s). 

  


  


Other Notes: 

There will be a "New Invoice" button at the top of this report to manually create an invoice (defaulting to blank).

  


Development Specification

Standard report customizations: Use custom macros to control a customized column (heading, contents, visibility) and custom macro for report subset (custom ask prompt).
