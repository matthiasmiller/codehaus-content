9.6. Booking Summary Printout (Excel)

  


Requirements

Purpose: This is an Excel printout of data displayed on the Export Tallies Report for a selected Booking. It is sent to the Customer in the Booking Summary Email, and contains the following: 

  * Summary of load information for all Export Tallies for the Booking
  * Breakdown of the logs included in each Export Tally (here referred to also as a "load") 



This is a basic printout, based of a simple export and template, displaying all the details on a single tab in the Excel file. 

  


Printed From: 

  * The Bookings Report ("Excel" link)
  * The Booking Summary Email



  


File Format: 

  * Excel: "Booking Summary - <Customer Name> \- <Booking ID> \- <current date in the MM-DD-YYYY format>"



  


Fields to be Filled:

  


Page Heading: Includes hard-coded Eby's contact information (no filled fields) 

  


Loads Summary section/table: (table listing all Export Tallies for the Booking, with one row for each tally/load, unless there are multiple Species + Grade combinations for a Tally, in which case there is an additional row for each combination)

  * Section heading: "Loads Summary"
  * Table columns: 
    * Load ID
    * Species + Grade (displays the Species and Base Grade in "<Species abbreviation> \- <Base Grade>" format; includes a breakdown for each Species + Grade, if applicable 
      * Further explanation: If the Tally has more than one Species + Grade combination, include a row for each, displaying contents only for "Species + Grade", "Log Count", and "Net BF", in gray font, below the main row the Tally; the main row for the Tally includes "All" for this column, and Tally totals for all other columns)
    * Log Count (displays the total number of logs for each Tally; includes a breakdown for each Species + Grade, if applicable)
    * Net Board Feet (column header displays "Net BF"; displays the total Net BF for each Tally; includes a breakdown for each Species + Grade, if applicable) 
    * Container #
    * Heavy Weight
    * Light Weight
    * Seal #
    * Loaded Date
  * Grand Totals: 
    * Log Count (no label; below the Log Count column; displays the grand total of logs for all Tallies linked to the Booking in bold font) 
    * Net BF (no preceding label; below the Net Board Feet column; displays the grand total of Net BF for all Tallies linked to the Booking in bold font, in the following format: "<number> Logs") 



  


Logs for Load sections/tables: (one table for each Export Tally for the Booking, each with its corresponding heading; each table includes a row for each log on the tally)

  * Section headings: "Logs for Load <Export Tally ID>"
  * Table columns: 
    * Tag # 
    * Species
    * Base Grade
    * Length
    * Diameter
    * Gross BF
    * Net BF
  * Totals: 
    * Log Count (no label; below the Tag # column; displays the total number of logs for the Tally in bold font, with the following format: "<#> logs") 
    * Gross BF (no label; below the Gross BF column; displays the total Gross BF for the Tally in bold font) 
    * Net BF (no label; below the Net BF column; displays the total Net BF for the Tally in bold font)



  


Handling Multiple Pages: N/A (one continuous sheet in the Excel file) 

  


Other Notes: 

  * N/A



  


Development Specification

Change Requests:

  * Tim Reitz 10/01/2024: Added in [[[IN9588](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9590&)]] - ZET - Changes to Booking Summary PDF and Excel file
  * 


  


Tim Reitz 10/01/2024: Template: See mockup, with changes highlighted in yellow ([https://docs.google.com/spreadsheets/d/1Uwv6gi3wM1UEoPSerd4i915gDk7gazvQ/](https://docs.google.com/spreadsheets/d/1Uwv6gi3wM1UEoPSerd4i915gDk7gazvQ/))
