10.1.5. Ads Ready for Invoicing Report

  


Requirements

Clicking on "Ads Ready for Invoicing" on the menu with open a two-pane report displaying customers and uninvoiced ads. This will normally only show ads for the current Publication Date since the Publication Date cannot be advanced if there are any uninvoiced ads.

  


Note that this report will include uninvoiced prepaid ads with their full Ad Price and their Prepay Discount amount, but not showing the discounted price. 

  


There will be an "Invoice All Ads" button at the top of this page. Clicking this button will create invoices for all the ads and customers on this report (it will not create invoices for ads that have already been invoiced). The user then goes to the Print/Send Invoices menu option when ready to print and send the invoices (see details in that part of this proposal).

  


Left Pane: This pane will show the customers:

Columns: 

  * Contact (link to the Customer/Ads Page)
  * # of Ads (the number of uninvoiced ads for that customer contact)



  


Beside each customer name will be a small "+" button with an option to "Invoice This Customer". This can be used to create an invoice for all ads of just that customer.

  


Filter: 

  * Publication (only for Full Admins; list of publications; default to blank = all)



  


Grouping/Sorting:

  * Group by Publication (only for Full Admin) 
  * Sort by Contact Name



  


Right Pane: This pane will show the uninvoiced ads for the selected customer:

Columns: 

  * Publication Date
  * Ad Title
  * Ad Size
  * Ad Color
  * Ad Price
  * Discount 
  * Special Placement Location & Page # (Location and Page Number separated by a comma)
  * Special Placement Charge
  * Ad Subtotal (total amount for each ad; show a Grand Total row at the bottom of this column)
  * Prepaid? (checkboxes)



  


Grouping/Sorting:

  * No grouping  (except for Full Admin - group by Publication --instead of Publication column)
  * Sort by Publication Date



  


Note about Invoicing with "Auto-Pay Ads" and "Pay with Credit Ads": 

Any time an auto-pay ad is invoiced (from the Customer/Ads Page, or via the "Invoice All Ads" button or  the "Invoice This Customer" button on the Ads Ready for Invoicing report), there will be a child screen that pops up with a warning such as, "This will automatically charge all customers with an Auto-pay Card selected".  

  


Clicking Continue closes the child screen and initiates the transaction(s) on the selected card(s), paying for the auto-pay ad(s).

  


"Print/Send Invoices" Button:

Once all ads for the selected publication date have been invoiced, a "Print/Send Invoices" button will appear at the top of this report. Clicking it will open a page prompting for the following:

  * Publication Date (list of Publication Dates; default to current)
  * Action (below list of actions; default to blank)
    * Print all Print Invoices
    * Send All Email/Fax Invoices & Ad Images
    * Print All Invoices
  * Publication (only for Full Admins; list of publications; default to blank = all)



  


Selecting an action and clicking "Continue" would open a report with the behavior described in the Print/Send Invoices section of this proposal. See that section for further details about the printing/sending process.

  


Development Specification

This is a customized report, similar to ZLC's Orders Ready for Invoicing report.
