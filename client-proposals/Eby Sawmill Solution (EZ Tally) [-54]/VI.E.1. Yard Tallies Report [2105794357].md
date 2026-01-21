6.5.1. Yard Tallies Report

  


Requirements

Overview: The Yard Tallies report is a three-pane report showing Yard Tallies and their corresponding summaries and breakdowns. 

  


Accessed from: Main | Yard Tallies | Yard Tallies (bypasses the filter screen to open the report directly)

  


The left pane shows all Yard Tallies for the selected filters, with each row representing one tally:

Title: Yard Tallies

  


Columns: 

  * Tally ID (link to record)
  * Source (Vendor/Tract)
  * Tract Name (blank if N/A)
  * Vendor (blank if N/A)
  * Total Net Board Feet (show total sum at the top of the column; rounded to the nearest whole number)
  * Total Gross Board Feet (show total sum at the top of the column; rounded to the nearest whole number)
  * Total Value (show total sum at the top of the column; rounded to the nearest 2 decimal places)
  * Eby Freight (Yes/No; blank if N/A)
  * Tally Created Date 
  * Tally Confirmed Date



  


Grouped by: Status (Open, Confirmed, Closed)

  


Sorted by: Tally ID (most recent at the top)

  


Filters (all filters are for the left pane, which in turn affects both right panes): 

  * Date Type (required; drop list of "Past 30 Days", "Date Range"; defaults to Past 30 Days)
    * Note that "Past 30 Days" would include the current day and go 30 days into the past (looks at the Tally Creation Date for tallies with a status of Open, since they don't have a Confirmed Date, and the Tally Confirmed Date for tallies with a status of Confirmed or Closed)
  * Confirmed Date Start (visible if Date Type = Date Range; date; looks at the Tally Confirmed Date; blank = all; defaults to January 1 of the current year)
  * Confirmed Date End (visible if Date Type = Date Range; date; looks at the Tally Confirmed Date; defaults to blank = all)
  * Status (multi-select list of Open, Confirmed, Closed; defaults to blank = all)
  * Source (drop-list of Vendor, Tract; defaults to blank = all)
  * Tract (visible if Source = Tract; drop-list of all Tract Names; filters down as you type; defaults to blank = all)
  * Landowner (list of Landowner-type Contacts; filters down as you type; defaults to blank = all)
  * Logger (visible if Source = Tract; drop list of all Logger-type Contacts; filters down as you type; defaults to blank = all)
  * Vendor (visible if Source = Vendor; drop-list of all Vendor-type Contacts; filters down as you type; defaults to blank = all)
  * Species (drop list of all Species; filters down as you type; defaults to blank = all; if an item is selected, the report shows all Yard Tallies that include at least one log of the selected Species and match other filters; the right panes will show all species for the selected yard tally)



  


  


The top right pane shows a breakdown of the selected Yard Tally from the left pane, with each row representing one log, and a totals row at the bottom:

Title: Yard Tally Breakdown

  


Columns: 

  * Species (total row shows quantity of logs in the following format "<#> logs") 
  * Grade (no total row)
  * Price (no total row)
  * Condition/Comment (displays the Log Condition if one is entered; if the "Other" Condition is entered, also displays the corresponding Comment in the following format: "Other: <Comment>"; wrap text if needed; no total row)
  * Length (for logs with no Cutback, this simply displays the Length; for logs with Cutbacks, this is displayed as "12/8" for a 12-foot full Length and an 8-foot Cutback length; total row shows average, using the full Length)
  * Diameter (total row shows average)
  * Gross Board Feet (total row shows average)
  * Net Board Feet (total row shows average)
  * Log Value (total row shows sum)
  * Tally Sequence (displays the sequence number from the original entry sequence; no total row)



  


Grouped by: N/A

  


Sorted by: Tally Sequence

  


The bottom right pane shows a summary of the selected Yard Tally from the left pane, with each row showing totals for a certain Species + Base Grade, and with a grand total row at the bottom: 

Title: Yard Tally Summary

  


Columns (all total row only): 

  * Species + Base Grade (displayed in the following format: "<Species Abbreviation> \- <Base Grade>") 
  * # of Logs (total rows show sum) 
  * Gross Board Feet (total rows show sum of rounded Gross BF values)
  * Net Board Feet (total rows show sum of rounded Net BF values)
  * % of Total Board Feet (number, rounded up or down to the nearest whole number; show the % of the Total for the corresponding row; looks at Net Board Feet; total rows show sum) 
  * Average Length (number, rounded up or down to the nearest whole number; total rows show average) 
  * Average Diameter (number, rounded up or down to the nearest whole number; total rows show average)
  * Average Board Feet (number, rounded up or down to the nearest whole number; looks at Net Board Feet; total rows show average)
  * Avg. Price ($/MBF) (number to 2 decimals, rounded up or down to the nearest cent; with the following details: 
    * individual row values calculated as follows: <<"Total Value" for the row, rounded to 2 decimal places> / <"Net BF" for the row, rounded to the nearest whole number> * 1,000 with the results rounded to the nearest 2 decimal places>; 
    * total row shows a total average, calculated as follows: <<Total "Total Value", to 2 decimal places< / <Total "Net BF", whole number> * 1,000 with the result rounded to the nearest 2 decimal places>)  
  * Total Value (number to 2 decimals; total rows show sum)



  


Grouped by: N/A

  


Sorted by: Species + Base Grade

  


  


Buttons: 

  * New Yard Tally (opens a new blank Yard Tally record)



  


Menu Visibility: Users with the View Tracts, Yard Tallies, and Pulpwood Loads permission (menu option grayed-out for other users) 

  


Other Notes: 

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1196622067](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1196622067)

  


  


Change Requests: 

  * Tim Reitz 06/06/2024: [[[IN9495](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9497&)]] - ZET - Tract Record & Yard Tallies Report - Add More Totals
  * Tim Reitz 08/19/2024: [[[IN9994](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9996&)]] - ZET - Yard Tallies Report - Remove "Price" Total Row & Change Av. $/MBF Column Heading
  * 


  


  


  


Ellis Miller 12/21/2022: 

Bottom Right Pane:

[ ] Totals-only report on logs

[ ] Use two-line headings and set column widths appropriate. Mockup is a bit rough.

[ ] Price ($/mbf) -- see average notes above.

  


 BID: 1 Day
