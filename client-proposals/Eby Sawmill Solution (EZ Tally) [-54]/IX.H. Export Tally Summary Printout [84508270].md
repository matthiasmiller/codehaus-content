9.8. Export Tally Summary Printout

  


Requirements

Purpose/Overview: This is a customized PDF printout of an individual Export Tally, with three sections:

  * Basic tally details
  * List of all logs in the tally, in the order in which they were scaled
  * Summary of the logs in the tally, grouped by Species and Grade



  


Printed From: 

  * Export Tally Record (single tally) 
  * Right pane of the Bookings report (single tally) 
  * PDF included as an attachment in the Export Yard Tally Summary Email (single tally) 
  * Booking Record (all tallies for the Booking) 



  


File Format/Name: 

  * PDF for single Export Tally: "<Tally ID> \- <Customer Name>" 
  * PDF for all tallies for a Booking record: "Export Tally Summaries - Booking <ID>" 



  


Fields to be Filled: 

  * Page Heading: 
    * Export Tally ID: <Export Tally ID>
    * Customer: <Customer Name> 
    * Booking ID: <displays the corresponding Booking ID> (visible when the Printout is included on a Booking Summary Printout) 



  


  * Export Tally Summary section: 
    * Section heading: "Export Tally Summary" (bold font) 
    * Container #: <Container #> 
    * Loaded Date: <mm/dd/yyyy> 
    * Seal #: <Seal #> 
    * Heavy Weight: <Heavy Weight> 
    * Light Weight: Light Weight> 
    * Booking #: <Booking #> 
    * Early Return Date: <mm/dd/yyyy> 
    * Cutoff Date: <mm/dd/yyyy> 



  


  * Logs Breakdown section (table with all logs in the tally, in the order they were entered; two tables side-by-side, like the Yard Tally Summary printout, to maximize use of page space):
    * Section heading: "Logs:" (bold font) 
    * Columns:
      * Tag # 
      * Species (column displays abbreviation; column heading displays "Spec.")
      * Grade (column displays Base Grade only) 
      * Length 
      * Diameter (column heading displays "Diam.")
      * Gross Board Feet (column heading displays "Gross")
      * Net Board Feet (column heading displays "Net")
    * Other Notes: 
      * The number of logs in this section generally ranges from 50 to 60 logs, but could be up to around 140 logs (if the logs are small). 



  


  * Tally Summary section (table showing a summary of the logs in the tally, grouped by Species and Grade):
    * Section heading: "Summary:" (bold font)  
    * Tally Summary Table: 
      * Columns: 
        * Species + Grade (displays in the following format: "<Species abbreviation> \- <Base Grade>") 
        * Quantity of Logs (displays the quantity of logs of that Species + Grade; column heading displays "Qty.")
        * Gross Board Feet (total for that Species + Grade; column heading displays "Gross")
        * Net Board Feet (total for that Species + Grade; column heading displays "Net")
        * % of Total Board Feet (rounded to the nearest whole number; column heading displays "% of Total")
        * Average Length (column heading displays "Av. Length")
        * Average Diameter (column heading displays "Av. Diam.")
        * Average Net Board Feet (column heading displays "Av. Net BF"; displays the average Net Board Feet values)
      * Grouped by: Species + Grade (technically Base Grade; lowest at the top)
      * Totals: The following columns have a grand total row, displaying either a sum or average: 
        * Quantity of Logs (sum) 
        * Gross Board Feet (sum)
        * Net Board Feet (sum)
        * % of Total Board Feet (sum of non-rounded percentages, should always equal 100) 
        * Average Length (average of non-rounded average lengths) 
        * Average Diameter (average of non-rounded average diameters) 
        * Average Board Feet (average of non-rounded average board feet values) 
    * Other Notes: 
      * This section usually is very small for Export Tallies (often only one data row). 



  


Handling Multiple Pages:

  * The letterhead is included on all pages. 
  * Due to technical limitations in the PDF generation process, this printout does not contain page numbers. 
  * The printout can split wherever a page break lands (including in the middle of a table).



  


Other Notes:

  * Note that a load (Export Tally) usually has between 30 and 70 logs, but may include up to 150 logs.



  


Development Specification

Change Requests: 

  * Tim Reitz 08/31/2024: (added in) [[[IN10233](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10235&)]] - ZET - Add Export Tally Summary Printout 
  * Tim Reitz 10/01/2024: [[[IN9588](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9590&)]] - ZET - Changes to Booking Summary PDF and Excel file


