10.1.6. Print/Send Invoices

  


Requirements

The batch printing/sending of invoices can happen after the following criteria have been met:

  * All ads for the current publication date have been invoiced
  * Credit has been applied to "Pay with Credit" ads
  * Auto-Pay ads have been paid or failed (if failed, they will remain as Invoiced)



  


Note that individual invoices can be printed or sent as soon as they are created (or paid, in the case of Pay with Credit/Auto-Pay ads).

  


Menu Options: 

The menu will have the following options for batch printing invoices and batch sending invoices & ad images:

  * Print All Print Invoices
  * Send All Email/Fax Invoices & Ad Images
  * Print All Invoices



  


Print/Send Process: 

To do the batch printing and sending, the user goes to the appropriate Print or Send menu option. Opening the menu option will open a prompt page with the following filter prompts and behaviors:

  


  * Publication Date (list of Publication Dates; default to current)
  * Action (below list of actions; default to match the menu option that was clicked)
    * Print all Print Invoices
    * Send All Email/Fax Invoices & Ad Images
    * Print All Invoices
  * Publication (only for Full Admins; list of publications; default to blank = all)



  


Clicking Continue would open a report with the following behavior:

  * If there are still ads for the current publication date that have not been invoiced, this will show a blank report with a message such as "There are ads for this publication date that have not been invoiced - please complete the invoicing process and try again."
  * If there is one or more outstanding transactions, this will show a blank report with a message such as "Waiting for 5 card transactions to complete - please rerun this report."
  * If all ads have been invoiced and all Auto-pay card transactions have cleared, this will open the report showing invoices as selected on the prompt and a button at the top to complete the action:
    * For "Print All Print Invoices"
      * Columns:
        * Customer
        * Invoice #
        * Invoice Date
        * Total Amount
        * Publication (only for Full Admins)
      * Sorting/Grouping:
        * Sort by Customer 
        * No grouping
      * Button at the top to "Print All Print Invoices". This would generate and open the PDF, with the invoices sorted the same way as the report. 
      * All invoices for for the selected Publication Date customers with "Print" set as their Invoice Preference would be generated on one PDF that could be downloaded and/or printed. Note that this would include any invoices that were already sent out.
    * For "Send All Email/Fax Invoices & Ad Images"
      * Columns:
        * Customer
        * Invoice #
        * Invoice Date
        * Total Amount
        * Publication (only for Full Admins)
      * Sorting/Grouping:
        * Sort by Customer  
        * No grouping
      * Button at the top to "Send All Email/Fax Invoices & Images". This would generate the email drafts with the invoice PDF and the ad image(s) (in PDF format) attached, and open the the email preview with the emails sorted the same way as the report. If a customer has more than one invoice, they would be grouped together on one email.
      * All invoices for the selected Publication Date for customers with "Email" or "Fax" set as their Invoice Preference would be generated on separate PDFs and emails would be generated. Each email would include the PDF invoice for the customer and PDF images of the ad(s) referenced in the invoice. These images would be the same image that shows up in the Image Preview on the Invoice Detail. For further details, see the Email/Fax Invoices & Ad Images section in this proposal.
    * For "Print All Invoices"  
      * Same columns and grouping/sorting as the "Print All Print Invoices" report
      * Button at the top to "Print All Invoices". This would generate and open the PDF with the invoices sorted the same way as the report. 
      * All invoices for the selected Publication Date would be generated on the PDF, regardless of the customer Invoice Preference.



  


Development Specification

Have an auto-run report that prompts for email vs print. If there are any pending charges, it shows something like "Waiting for 5 card transactions to complete. Please refresh this report." This can be an empty report expression. If there are no pending transactions, redirect to the appropriate merge.
