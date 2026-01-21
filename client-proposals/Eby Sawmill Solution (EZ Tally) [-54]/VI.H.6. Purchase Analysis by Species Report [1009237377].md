6.8.6. Purchase Analysis by Species Report

  


Requirements

Overview: This is a report from Yard Tallies of logs of a selected Species (and other selected details) that were purchased in a selected time period (based on the Created Date of Yard Tallies). This can be used for end-of-month inventory, etc.

  


Accessed from: Financial | Analysis | Purchase Analysis (bypasses the filter screen to open the report directly). 

  


Title: Purchase Analysis by Species (previously "by Log Code") 

  


Columns with totals: (each row represents all logs of a selected Species + Base Grade) 

  * Description (display <Species Abbreviation> \- <Base Grade>; no total)
  * # of Logs (whole number; total number of logs for the corresponding Species + Base Grade; total = sum)
  * Total Net BF (whole number; total for the corresponding Species + Base Grade; total = sum)
  * Average Net BF (whole number; average for the corresponding Species + Base Grade; total = average)
  * Value (number to 2 decimals; total for the corresponding Species + Base Grade; total = sum)
  * Average Price / mbf (whole number; average for the corresponding Species + Base Grade; calculated as follows: <Value> / <Total Net BF> * 1,000; total = average, calculated as follows: <Total "Value"> / <Total "Total Net BF"> * 1,000, rounded to the nearest whole number) 



  


Grouped by: Species (alphabetical) 

  


Sorted by: Description (lowest Base Grade number at the top) 

  


Filters: 

  * Species (multi-select drop list of all Species; defaults to blank = all) 
  * Base Grade (multi-select drop list of all Base Grades; defaults to blank = all) 
  * Start Date (date; defaults to 30 days before the current day; blank = all; looks at Yard Tally Created Date)
  * End Date (date; defaults to blank = all; looks at Yard Tally Created Date)
  * Source (drop list of Vendor, Tract, defaults to blank = all) 
  * Tract (visible if Source = Tract; list of all Tracts; defaults to blank = all; filters down as you type) 
  * Vendor (visible if Source = Vendor; drop list of all Vendors; defaults to blank = all; filters down as you type) 
  * Log Buyer (drop list of Employee-type Contacts; if a contact is selected, the report will show only results from Yard Tallies created by that user; defaults to blank = all) 



  


Buttons: N/A

  


Menu Visibility: Users with the View and Edit Financials permission (by virtue of it being on the Financial Menu)

  


Other Notes: 

  * For the Grade multi-select filter, show any matches. For example: If Species = White Oak and Grade = 1 and 2, show results for Grade 1 even if there aren't any for Grade 2.
  * Printout: If a user wishes to print this report, it can be done from the Advanced drop-down menu in the top right corner (PDF or Excel). Note that this will be the basic report printout, without customizations.



  


Development Specification

Change Requests: 

  * Ben Reitz 09/17/2025: [[[IN11650](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11652&)]] - ZET - Fix "Average Price" throughout the software
  * 


  


Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1366886049](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1366886049)

  


See client's existing printout: [https://drive.google.com/file/d/1xSwpLgoh_1fNOvT826zSE55TcIZWPJs0/view](https://drive.google.com/file/d/1xSwpLgoh_1fNOvT826zSE55TcIZWPJs0/view)

  


Ellis Miller 12/22/2022: 

[ ] Yard Tallies level, Repeating on Logs

BID: 1 DAY
