9.2. Landowner % Payment Summary Printout

  


Requirements

Purpose/Overview: This is a PDF and Excel printout of the Landowner % Payments Summary report for a selected Payee + Tract. It includes the following:

  * Breakdown of the selected Payment (same information as the top right pane of the report)
  * Summary of all Payments (same information as the left pane of the report, except Payee)



  


Printed From: 

  * Landowner % Payments Due Report
  * Landowner % Payments Summary Report
  * Included in the Landowner Payment Summary Email



  


File Format/Name: 

  * PDF
    * File name: "Payment Summary - <Tract Name> \- <Payment Date in the MM-DD-YYYY format>"
  * Excel
    * File name: "Payment Summary - <Tract Name> \- <Payment Date in the MM-DD-YYYY format>"



  


Fields to be Filled

PDF: This is a customized printout with the Eby's letterhead: 

Filled fields in the letterhead / repeating header (displayed on all pages): 

  * Tract
  * Payee 



  


Payment Breakdown section/table (one row for each Yard Tally):

  * Section heading: Breakdown of Payment <ID>
  * Totals (table with the following columns; included if the "Show All Totals" filter checkbox is checked):
    * Total BF
    * Tally Amount Due
    * Pulpwood Load Tons
    * Pulpwood Load Amount Due
    * Down Payment Amount
    * Expense Withholding Amount



  


  * Yard Tally Breakdowns (table with the following columns; included if the "Show Yard Tally Breakdowns" filter checkbox is checked):
    * Yard Tally ID
    * Total BF
    * 1st Tier Board Footage (column heading displays the same as Tract record/Payments report) 
    * 1st Tier Log Value (column heading displays the same as Tract record/Payments report) 
    * 1st Tier Landowner Share (column heading displays the same as Tract record/Payments report)
    * 2nd Tier Board Footage (column heading displays the same as Tract record/Payments report) 
    * 2nd Tier Log Value (column heading displays the same as Tract record/Payments report)
    * 2nd Tier Landowner Share (column heading displays the same as Tract record/Payments report)
    * 3rd Tier Board Footage (column heading displays the same as Tract record/Payments report) 
    * 3rd Tier Log Value (column heading displays the same as Tract record/Payments report)
    * 3rd Tier Landowner Share (column heading displays the same as Tract record/Payments report)
    * 4th Tier Board Footage (column heading displays the same as Tract record/Payments report) 
    * 4th Tier Log Value (column heading displays the same as Tract record/Payments report)
    * 4th Tier Landowner Share (column heading displays the same as Tract record/Payments report)
    * 5th Tier Board Footage (column heading displays the same as Tract record/Payments report) 
    * 5th Tier Log Value (column heading displays the same as Tract record/Payments report)
    * 5th Tier Landowner Share (column heading displays the same as Tract record/Payments report)
    * Tally Amount Due



  


Payments Summaries section/table (one row for each Payment for this Payee + Tract):

  * Section heading: Summary of All Payments
  * Columns:
    * Payment ID
    * Payee
    * Tract Name
    * Amount Paid (displays the "Amount Paid" from the Payment for the row; total row at the bottom shows sum) 
    * Payment Total (total row at the bottom shows sum)
    * Check #
    * Notes
    * Payment Date



  


Excel: A basic export of the information is sufficient for this. This will be based off of a basic template, and the file will have three tabs with the following labels and details: 

  * "Totals" (same columns and data as the corresponding table on the PDF)
  * "Breakdown of Payment <ID>" (same columns and data as the Yard Tally Breakdowns table) 
  * "Summary of All Payments" (same columns and data as the corresponding section on the PDF)



  


Handling Multiple Pages (PDF): 

  * The letterhead is included on all pages. 
  * If the PDF generation allows, the page number is displayed in the top right corner of each page. 
  * If a page break is needed, split between the sections/table (not in the middle of a section/table). 



  


Other Notes: 

  * This printout can be in landscape orientation if that allows all the information to fit on the page better.



  


Development Specification

Change Requests: 

  * Tim Reitz 08/19/2024: [[[IN10016](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10018&)]] - ZET - Tract Record - Adding More Tiers 
  * Tim Reitz 08/31/2024: [[[IN10285](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10287&)]] - ZET - Landowner Payment Summary Printout - Re-Include Historical Payments
  * Ben Reitz 09/17/2025: [[[IN10641](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10643&)]] - ZET - Printouts - Consider Changing Date Format in File Name
  * Tim Reitz 10/04/2025: [[[IN11651](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11653&)]] - ZET - Landowner % Payments - Add Down Payment Info
  * Tim Reitz 10/04/2025: [[[IN12073](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12075&)]] - ZET - Landowner % Payment Printout - Add "Tract Name" and "Payee"
  * 


  


  


Mockup: 

  * PDF: [https://docs.google.com/document/d/1txvz-UEZ9hyyLGm9-KGA_71f-2pdAJpEXnstwLzJPNw/edit](https://docs.google.com/document/d/1txvz-UEZ9hyyLGm9-KGA_71f-2pdAJpEXnstwLzJPNw/edit) 
    * TODO_CCI: Tim Reitz 02/14/2023: Formatting for the headings in the actual printout should be done more nicely than here in the mockup (try to avoid splitting words on line breaks).
  * Excel: N/A (spec should be sufficient)



  


Data: This is the Yard Tally printout. See comments there.

  


See Client Proposal template as an example of different footers on different pages. 

  


PDF Export:

[ ] Basic template, but using letterhead heading.

[ ] First report is a version of the Master Payment report's right pane (Yard Tally) report for minor tweaks to visible columns.

[ ] Add a vAskTemplateMode ask prompt for these differences.

[ ] Second report is the Master Payment's left pane. We probably don't need to the ask prompt, but we can add it if needed.

[ ] Try to split between sections. 

4 DAYS

  


  


Excel Export: 

[ ] Simple export with two tabs,each with one #report#

1 DAY
