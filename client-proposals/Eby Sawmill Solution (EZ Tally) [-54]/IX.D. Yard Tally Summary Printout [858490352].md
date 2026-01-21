9.4. Yard Tally Summary Printout

  


Requirements

Purpose/Overview: This is a customized PDF printout of an individual Yard Tally, with three sections:

  * Basic tally details
  * List of all logs in the tally, in the order in which they were scaled
  * Summary of the logs in the tally, grouped by Species and Grade



  


Printed From: 

  * Yard Tally Record (single yard tally; for either Vendor or Tract-sourced tallies) 
  * Included in the Vendor Yard Tally Summary Email (single yard tally) 
  * Vendor Payments Due Report (all yard tallies linked to one or more Payment records, grouped together in one PDF, sorted by Payee then Yard Tally ID)
  * Vendor Payments Summary Report (all yard tallies linked to selected Payment records, grouped together in one PDF; sorted by Payment ID then by Tally ID)
    * Example (for 2 Payment rows selected): 
      * Yard Tally 1 for Payment 1
      * Yard Tally 2 for Payment 1
      * Yard Tally 3 for Payment 1
      * Yard Tally 1 for Payment 2
      * Yard Tally 2 for Payment 2



  


File Format/Name: 

  * PDF, single yard tally: 
    * If Source = Vendor: "<Tally ID> \- <Vendor Name> \- <Confirmed Date in the MM-DD-YYYY format>" 
    * If Source = Tract: "<Tally ID> \- <Tract Name> \- <Confirmed Date in the MM-DD-YYYY format>" 
  * PDF, all yard tallies for a Payment record: "Yard Tally Summaries - Payment <ID>" 
  * PDF, all yard tallies for multiple Payment records: "Yard Tally Summaries - Unpaid Payments <mm-dd-yyyy>" 



  


Fields to be Filled: 

  * UNCONFIRMED TALLY (message, visible only if the Tally is not marked Confirmed; displays in bolded red text; located above the Yard Tally Summary section)
  * Yard Tally ID: <Yard Tally ID>
  * Vendor: <Vendor Name> (visible only if the Tally's Source = Vendor)
  * Tract: <Tract Name> (visible only if the Tally's Source = Tract) 
  * Tally Date/Time (no label): <mm/dd/yyyy, h:mm> (this shows the Created date and time)
  * "Eby Freight" (visible only if the Tally's Source = Vendor and if Eby Freight = "Yes" on the Tally)



  


Tally Details section (basic tally details):

  * Section heading: N/A
  * Fields:
    * Load Comments:
      * <Load Comments from the Tally>
      * "Scaled using the Doyle scale"



  


Logs Breakdown section (table with all logs in the tally, in the order they were entered; ideally this will be two tables side-by-side, to maximize use of page space):

  * Section heading: Logs
  * Columns:
    * Species (column displays abbreviation; column heading displays "Spec.")
    * Grade
    * Length 
    * Cutback (column heading displays "Cut.")
    * Diameter (column heading displays "Diam.")
    * Gross Board Feet (column heading displays "Gross")
    * Net Board Feet (column heading displays "Net")
    * Condition/Comment (column displays the Log Condition if one is entered; if the "Other" Condition is entered, also displays the corresponding Comment in the following format: "<Condition>: <Comment>")
    * Price
    * Value
  * Other Notes: 
    * The number of logs in this section can range from fewer than 5 to 300 or more



  


Tally Summary section (table showing a summary of the logs in the tally, grouped by Species and Grade):

  * Section heading: Summary 
  * Tally Summary Table: 
    * Note that this is the Yard Tally Summary report (the bottom right pane of the Yard Tallies Report) for the selected Yard Tally. 
    * Columns: 
      * Species + Grade
      * Quantity of Logs (displays the quantity of logs of that Species + Grade; column heading displays "Qty.")
      * Gross Board Feet (total for that Species + Grade; column heading displays "Gross")
      * Net Board Feet (total for that Species + Grade; column heading displays "Net")
      * % of Total Board Feet (rounded to the nearest whole number; column heading displays "% of Total")
      * Average Length (column heading displays "Av. Length")
      * Average Diameter (column heading displays "Av. Diam.")
      * Average Board Feet (column heading displays "Av. BF")
      * Price (column heading displays "Av. $MBF")
      * Total Value
    * Grouped by: Species
    * Sorted by: Grade (lowest at the top)
    * Totals: Subtotaled by species, grand total at the bottom
  * Summary Totals (note that this is larger (duplicate) fielding for "Net" total and "Total Value" totals. For better visibility, this uses slightly larger font than the font size in the table): 
    * UNCONFIRMED (message, visible only if the Tally is not marked Confirmed; displays in bolded red text; located to the left of Net)
    * Net: <displays the total from the Net column> 
    * Total ($): Total: $ <displays the total from the Total Value column>
  * Other Notes: 
    * This section could fill a full page or more



  


Handling Multiple Pages:

  * The letterhead is included on all pages. 
  * Due to technical limitations in the PDF generation process, this printout does not contain page numbers. 
  * The printout can split wherever a page break lands (including in the middle of a table).



  


Other Notes:

  * Note in the Letterhead section of the living spec that the standard letterhead is not being used for this printout. We've effectively created a secondary letterhead just for this printout.This printout was formerly called the "Scale Slip Summary".



  


Development Specification

Change Requests: 

  * Austin Priest 08/30/2023: [[[IN8537](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8539&)]] - ZET - Yard Tally Summary Printout - Adjustments for Tract-Source Tallies
  * Tim Reitz 02/03/2024: [[[IN9374](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9376&)]] - ZET - Deployment - Client Feedback on Yard Tally Summary Printout and [[[IN9418](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9420&)]] - ZET - Deployment - Round 2: Client Feedback on Yard Tally Summary Printout
  * Tim Reitz 08/06/2024: [[[IN10072](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10074&)]] - ZET - Yard Tally Summary Printout - Add warning when printing or downloading
  * Ben Reitz 09/17/2025: [[[IN10641](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10643&)]] - ZET - Printouts - Consider Changing Date Format in File Name
  * 


  


  


Mockup (out of date):

  * PDF: [https://docs.google.com/document/d/1eVcbQcv8QXRTqG_rJ0hIxrD4hK5nkwL0gB8vTPNsr00/edit](https://docs.google.com/document/d/1eVcbQcv8QXRTqG_rJ0hIxrD4hK5nkwL0gB8vTPNsr00/edit) 
  * Secondary mockup to show layout for printing for multiple Payments: [https://docs.google.com/document/d/1WJhDFD_CCEKNJPNdtzbNk0duKIEYfHIL9w76Xse7VJw/edit#](https://docs.google.com/document/d/1WJhDFD_CCEKNJPNdtzbNk0duKIEYfHIL9w76Xse7VJw/edit#) 



  


Data: Multiple Yard Tally records (with reports from other records). If run in Payment Mode, will be grouped by Payment ID's and include Payment Summary pages. If run in Yard Tally mode the Payment Summary sheets are deleted. 

  


Ellis Miller 12/28/2022: 

  * Create a helper report for the middle section (logs). It should have an ask prompt for first half vs. second half. Use CurrentRGNum and Ceiling(CountRG(...) / 2, 0) to determine halves. (If there's an odd number of rows, show the odd number in the first half, not the second half. Use similar #Report()# expressions in the template to show both halves. 4 HOURS



  


Things I'm worried about:

  * Large, complex repeating headers
  * Tight columns
  * Lots of data



5 DAYS

  


Link to sample (not all things on the sample are needed): [https://drive.google.com/file/d/1kaBVPCCtYdexOIxPjFBe4gp1MOQu2Y-r/view](https://drive.google.com/file/d/1kaBVPCCtYdexOIxPjFBe4gp1MOQu2Y-r/view)
