5\. Production Schedule Printout

  


Requirements

This printout would be generated from the Production Schedule Report, and would be similar to their existing printout. 

  


Details: 

  * PDF format 
  * Include the Triple D logo at the top (Note: this logo will display on printouts generated from any reports in the system) 
  * Include one week per printout (only print one week at a time) 
  * Use alternating row colors (instead of gridlines)
  * Display "Week of MMMM DD-DD, YYYY" at the top (DD-DD should be the dates for Monday-Friday) 
  * Dates auto-filled for the days along the left side of the printout
  * Each date/day section should show the deliveries scheduled for that day 
  * Show a minimum of six rows per day, but add rows as needed to match the number of deliveries for the day if there are more than six deliveries 
  * Roll over to an additional page if needed
    * Keep the same heading of logo and week dates
    * Do not split days on a page split - carry over a full day to the next page  
  * Columns: 
    * Customer (auto-filled) 
    * Item (auto-filled) 
    * Board Feet (auto-filled) 
    * Job Name (auto-filled) 
    * Cut (blank checkbox or blank cell; this would not be used or filled in the database) 
    * Made (checkbox or cell; auto-fill from the record - filled if made, blank if not made)  



  


  


Prompt for:

  * Week Of (date; required; defaulting to today)
  * Title of "Week of MMMM DD-DD, YYYY"



  


Development Specification

Dev Specs: 

  * Repeat for List to force a minimum of 6 rows.
  * Use "Page Break Between Groups" to keep days together
  * Use HeaderLogoFilePath. May require uploading their logo as a Standard file


