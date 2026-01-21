9.5. Booking Summary Printout (PDF)

  


Requirements

Purpose: This is a PDF printout of data displayed on the Export Tallies Report for a selected Booking. It is sent to the Customer in the Booking Summary Email, and contains the following: 

  * Summary of load information for all Export Tallies for the Booking
  * Breakdown of the logs included in each Export Tally (here referred to also as a "load"), in the form of the Export Tally Summary printout for each load.  



  


Printed From: 

  * The Bookings Report ("PDF" link)
  * Included in the Booking Summary Email



  


File Format: 

  * PDF (custom template that embeds data from both sides of the Export Tallies Report): "Booking Summary - <Customer Name> \- <Booking ID> \- <current date in the MM-DD-YYYY format>"



  


Fields to be Filled: This is a customized printout with the Eby's letterhead: 

  


  * First page: The first page includes a summary of the Booking details and a summary of all loads/Tallies linked to the Booking. 
    * Letterhead / page heading: 
      * Customer: <displays the corresponding Customer Name> 
      * Booking ID: <displays the corresponding Booking ID; note that this is visible on all pages, including the Export Tallies> 



  


  * Booking Info section: (fields filled with details from the Booking record)
    * Section heading: N/A (none) 
    * Field(s):
      * Description: 



  


  * Loads Summary section/table: (table listing all Export Tallies for the Booking, with one row for each tally/load, unless there are multiple Species + Grade combinations for a Tally, in which case there is an additional row for each combination)
    * Section heading: "Loads Summary"
    * Table columns: 
      * Load ID
      * Species + Grade (displays the Species and Base Grade in "<Species abbreviation> \- <Base Grade>" format; includes a breakdown for each Species + Grade, if applicable 
        * Further explanation: If the Tally has more than one Species + Grade combination, include a row for each, displaying contents only for "Species + Grade", "Log Count", and "Net BF", below the main row the Tally; the main row for the Tally includes "All" for this column, and Tally totals for all other columns) 
      * Log Count (displays the total number of logs for each Tally; includes a breakdown for each Species + Grade, if applicable)
      * Net Board Feet (column header displays "Net BF"; displays the total Net BF for each Tally; includes a breakdown for each Species + Grade, if applicable) 
      * Container #
      * Heavy Weight
      * Light Weight
      * Seal #
      * Loaded Date
    * Grand Totals: 
      * Log Count (no label; below the Log Count column; displays the grand total of logs for all Tallies linked to the Booking in bold font) 
      * Net BF (no label; below the Net Board Feet column; displays the grand total of Net BF for all Tallies linked to the Booking in bold font) 



  


  * Subsequent pages: "Export Tally Summary sections": The Export Tally Summary printouts for all Export Tallies linked to the Booking are included below the first page. See the spec for the Export Tally Summary Printout for details about those printouts. 



  


Template: See mockup ([https://drive.google.com/file/d/12-qyUzCdi25zuvAhtDaWrDksV_MLv1F_/view](https://drive.google.com/file/d/12-qyUzCdi25zuvAhtDaWrDksV_MLv1F_/view)) 

  


Handling Multiple Pages:

  * The letterhead is included on all pages.
  * There are no page numbers on this printout, due to the complexity of incorporating the Export Tally Summaries. 
  * The printout should split after the Loads Summary section (keeping the Booking Info and Loads Summary together on the same page) and after each Export Tally Summary. Additional page breaks may be done in the middle of tables if needed. 



  


Other Notes: 

  * Note that while this printout includes all Export Tallies for a Booking, regardless of Tally Status, Eby's usually prints this after all Tallies are loaded, meaning that it normally would only include Tallies with Status = "Loaded".



  


Development Specification

Change Requests: 

  * Tim Reitz 10/01/2024: (multiple changes, adding Export Tally Summaries and splitting off the Excel file into a separately-specced printout) [[[IN9588](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9590&)]] - ZET - Changes to Booking Summary PDF and Excel file
  * 


  


Mockup:

  * PDF: [https://docs.google.com/document/d/1Be_oeckm6zUEKW9Sqnw_uRkQW_20-DV_QiG2r4WfVSE/edit](https://docs.google.com/document/d/1Be_oeckm6zUEKW9Sqnw_uRkQW_20-DV_QiG2r4WfVSE/edit) 
  * Excel: N/A (spec should be sufficient)



  


Data: Multiple Export Tallies; Run merge report with an "Export Tally" template for all export tallies in a booking. The first export tally will also export the summary

  


\------------------

  


Ellis Miller 12/28/2022: This is actually a Export Tally level merge but appears to be a Booking Summary level merge. Prompt for one or more Booking ID's. Output file names should reference booking ID. 

  


PDF:

[ ] Parent Merge report takes a Booking ID and finds Export Tallies for that booking.

[ ] Use two sections on separate pages -- one for summary and one for each Export Tally. DeleteSectionIf we aren't the first section. Use a model to determine whether we are the first tally in the booking summary. Similar to what happens below.

[ ] Create simple reports for the contents.

[ ] Don't worry about the "split" comments in the "Handling Multiple Pages". This will automatically happen with the pages.

BID: 4 DAYS

  


Excel: One tab for all the summaries combined and one separate tab for each Export Tally breakdown. 

To do this:

* Create an Excel merge that includes all the tallies

* Include a column that indicates whether this is the first tally

* Have the Excel template include the summary page, as well as the tally breakdown

* Use DeleteSheetIf to delete the summary page for all but the first tally

BID: 1 DAY
