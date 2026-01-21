9.3. Logger Payment Summary Printout

  


Requirements

Purpose/Overview: This is a PDF and Excel printout of the most recent Payment for a selected Logger Payee + Tract. This includes the same details as the left and right panes of the Logger Payment Summary report for one selected Payment. 

  


Printed From: 

  * Logger Payments Due Report
  * Logger Payments Summary Report
  * Included in the Logger Payment Summary Email



  


File Format/Name: 

  * PDF
    * File name: "Payment Summary - <Logger Name> \- <Payment Date in the MM-DD-YYYY format>"
  * Excel
    * File name: "Payment Summary - <Logger Name> \- <Payment Date in the MM-DD-YYYY format>"



  


Fields to be Filled: 

PDF: This is a customized printout with the Eby's letterhead:

Payment Summary section/table (one row, since this would only be for one Payment at a time):

  * Section heading: Payment Summary (not displayed) 
  * Columns:
    * Payment ID
    * Payee
    * Payment Date
    * Tract Name
    * Payment Total
    * Check #
    * Notes



  


Yard Tallies section/table (one row for each tally; same as the sub pane from Logger Payments Summary report): 

  * Section heading: Yard Tallies
  * Columns: 
    * Yard Tally ID
    * Confirmed Date
    * Total Board Feet (with total row)
    * Amount Due (with total row)



  


Pulpwood Loads section/table (one row for each Pulpwood Load included linked to the Payment): 

  * Section heading: Pulpwood 
  * Columns: 
    * Tons
    * Date 
    * Location
    * Amount Due (displays the Logger Amount from the Pulpwood Load record; calculated as <Tract Logger Pulpwood Rate> * <Pulpwood Load Tons>) 



  


Excel: A basic export of the information is sufficient for this. This will be based off of a basic template, and the file will have three tabs (one for each of the sections in the PDF above) with the following labels and details: 

  * "Payment Summaries" (same columns and data as the corresponding section on the PDF)
  * "Yard Tallies" (same columns and data as the corresponding section on the PDF)
  * "Pulpwood Loads" (same columns and data as the corresponding section on the PDF)



  


Handling Multiple Pages (PDF): 

  * N/A (this should always fit on one page, so no need for page breaks or page numbers.)



  


Other Notes: 

  * There normally would not be more than 8-10 tallies and 6-8 pulpwood loads on a Logger Payment. The printout should allow for at least 10 tally rows and at least 8 pulpwood load rows on the one page.



  


Development Specification

Change Requests: 

  * Tim Reitz 06/20/2024: [[[IN10017](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10019&)]] - ZET - Logger Payment Summary Printout - Incorrect Logger Amount Due Pulpwood calculations
  * Ben Reitz 09/17/2025: [[[IN10641](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10643&)]] - ZET - Printouts - Consider Changing Date Format in File Name
  * 


  


Mockup: 

  * PDF: [https://docs.google.com/document/d/1KI_WgrD6915usgemEkBfwgtvfJiCnj3ZoO1JyNOwwSY/edit](https://docs.google.com/document/d/1KI_WgrD6915usgemEkBfwgtvfJiCnj3ZoO1JyNOwwSY/edit) 
  * Excel: N/A (spec should be sufficient)



  


Data: This is the Yard Tally printout. See comments there. 

  


Because the PDF version will need a full Yard tally export for every included Yard Tally record, we will actually make this a Yard Tally level export, grouped by Payment ID and include summary Yard Tally information for the first Yard Tally in each payment group.

  


Ellis Miller 12/28/2022:

[ ] Initial report at the top is the Master Payments Left Pane with a single Payment ID passed in.

[ ] Yard Tallies is the Right Pane (note that if vAskTemplateMode and we are showing for Logger, we don't include Logger columns since those are a separate report.

[ ] Pulpwood will be a separate export. Perhaps "Std Loggers Payments Export - Pulpwood.r20"

 BID: 2 DAYS
