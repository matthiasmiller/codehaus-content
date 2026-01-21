6.8.4. Tract Profitability Overview Report

  


Requirements

Overview: This is a report of Tracts with a Status = "Contract Signed", "Harvest Started", and "Harvest Paused" (with the option to include Tracts with the Status of Harvest Complete). This report shows the profit/loss for tracts as of the current date, and has one row for each Tract, totals for each section, and a grand total. This report can be used for various applications, including in the monthly inventory process to provide an estimate of the standing timber inventory value (considering the Net Loss of incomplete Tracts to be the amount of timber that is still standing). 

  


Accessed from: Financial | Analysis | Tract Profitability Overview (bypasses the filter screen to open the report directly). 

  


Title: Tract Profitability Overview

  


Columns: 

  * Tract Name (link to record; no totals)
  * Income (displays the total income for the Tract)
  * Expense (displays the total expenses for the Tract)
  * Net Profit/Loss (shows as a positive number for profit/negative if a loss; see details in Other Notes below; total rows show sum)
  * narrow blank spacer column
  * Harvest Start (visible if "Include Complete Tracts" filter is selected; shows the Harvest Started Date from the Tract)
  * Harvest Ended (visible if "Include Complete Tracts" filter is selected; shows the Harvest Ended Date from the Tract, if applicable) 



  


Grouped by: Loss, Profit (all tracts with a net loss at the top, all with a net profit at the bottom)

  


Sorted by: Tract Name

  


Filters: 

  * Include Complete Tracts (checkbox; defaults to cleared) 
  * Harvest Start Date Start (visible if Include Complete Tracts is selected; defaults to blank = all) 
  * Harvest Start Date End (visible if Include Complete Tracts is selected; defaults to blank = all) 



  


Buttons: 

  * N/A



  


Menu Visibility: Users with the View and Edit Financials permission (by virtue of it being on the Financial Menu)

  


Other Notes: 

  * The Net Profit/Loss column shows the sum of the following (same as the Tract Profitability by Tract Report): 
    * Income
      * Timber (total log income for the Tract; looks at the "Harvested Value" on the Tract)
      * Pulpwood (total Pulpwood income for the Tract; sum of Pulpwood Load Amounts from all Pulpwood Load records linked to the Tract record)
    * Expenses
      * Landowner Payments (sum of Payment Totals from all Landowner Payments for the Tract)
      * Logger Payments (sum of Payment Totals from all Logger Payments for the Tract)
      * Freight (displays the "Total Freight $" from the Tract record, which is the total for both logs and pulpwood)
      * Other Expenses (total of Amounts of Misc Expenses for the Tract)



  


Development Specification

Change Requests: 

  * Tim Reitz 08/19/2024: [[[IN10136](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10138&)]] - ZET - Tract Profitability Reports - Fix Totals and Details (prev. Additional Fix for DP Amounts) 
  * Ben Reitz 05/01/2025: [[[IN10943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10945&)]] - ZET - Fix Timber Freight Calculations (prev. Tract Profitability Report - Incorrect formula)
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=982363197](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=982363197)

  


  


BID: 4 HOURS
