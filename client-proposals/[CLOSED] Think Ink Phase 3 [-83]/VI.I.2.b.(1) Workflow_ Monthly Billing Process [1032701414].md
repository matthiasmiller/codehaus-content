6.9.2.2.1. Workflow: Monthly Billing Process

Billing (invoicing) is normally done or or around the 10th of each month, following the following process:

  


Note that this all pertains to Phase 4, when invoicing and full page count collections are to be included.

  


Months of January, April, July, September (months when page counts are billed): Includes this additional process before the "Every Month" process:

1\. Collect page counts from the previous quarter 

  * For Devices with "Page Count Collection Type" = "Manual", the Page Count Request email is sent out one week before the last day of the quarter. 
  * For Devices with "Page Count Collection Type" = "Manual", if the page counts have not been received by Think Ink by a certain date, the Page Count Reminder email is sent out.
  * Collections  should happen on or around the last day of the previous quarter or the first day of the current quarter, and includes all pages printed since the last page count collection.
  * If page counts are missing for a device on an Agreement, that Agreement cannot be billed until the page counts are resolved (either via getting the page count or doing an estimation)



  


Every Month:

1\. On the billing date:  

  * Step 1: Review the Devices Needing Review Report to catch problems and devices that need extra attention.
    * Click the "Start Billing Review" menu option



TODO_IDD: menu option that opens a prompt screen with a Continue button; run background process to look for devices missing page counts and set the checkbox; open the report

TODO_EM: automatically or another button?

TODO_JM: which menu do you want this on?

  * Review the "Devices Needing Review" report and clean up Devices as able. 


  * Step 2: Review the Pre-Billing Review Report to review invoice details before the invoices are created.
    * Click the "Pre-Billing Review" button on the Devices Needing Review report
  * Step 3: Create Invoices / Statements:
    * Click the "Start Invoicing" button on the Pre-Billing Review report
      * This pulls together all uninvoiced fees for all Agreements that are ready for invoicing and create invoices. 
      * For Customers with multiple Agreements: Combine the multiple invoices (one for each Agreement) into a single Statement 



TODO_EM: Tim Reitz 08/17/2023: should we do like we do for ZWA and create statements for everyone even if they just have one invoice? 

  * Step 4: Print and Send invoices: 



TODO_EM: Tim Reitz 08/17/2023: Are you good with this? 

  * Email / Fax: Click a "Send Email / Fax Invoices" button that sends the Monthly Invoice Email with the PDF attachments to all customers who have "Preferred Invoiced Format" set to "Email" or "Fax" .
    * Details to be specced out in Phase 4. 
  * Print/mail: Click a "Generate Print Invoices" button that generates the PDF file for the user to print or download. This would include the statements/invoices for all customers who have "Preferred Invoiced Format" set to "Print". 
    * Details to be specced out in Phase 4 (using a #10 windowed envelope with the return address pre-printed)



2\. Receiving payment / marking paid: 

  * Details to be determined in Phase 4. 



3\. Handling overdue invoices:

  * Details to be determined in Phase 4.


