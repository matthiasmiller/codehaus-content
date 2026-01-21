6.8.5. Tract Profitability by Tract Report

  


Requirements

Overview: This is a two-pane report that shows a miniature income statement over time for one selected Tract. 

  


Accessed from: Financial | Analysis | Tract Profitability by Tract

  * Clicking the menu option first opens a prompt screen with the filters for the report, prompting for a Tract (see Filter details below). Once the Tract is selected, clicking Continue opens the report.



  


Title: Tract Profitability for <Tract Name>

  


Left pane This pane shows a special report of various income and expense categories for the selected Tract, as well as the net profit for the Tract: 

  


It looks something like the following table:

Income|   
  
---|---  
Timber| $  
Pulpwood| $  
Total Income| $  
  
|   
  
Expenses|   
  
Owner Payments| $  
Logger Payments| $  
Freight| $  
Other Expenses| $  
Total Expenses| $  
  
|   
  
Net Profit| +/- $  
  
 

Explanations:

Income

  * Timber (total log income for the Tract; looks at the "Total Log Value" on the Tract) 
  * Pulpwood (total Pulpwood income for the Tract; sum of Pulpwood Load Amounts from all Pulpwood Load records linked to the Tract record)
  * Total Income (sum of Timber and Pulpwood)



  


Expenses

  * Landowner Payments (displays the sum of the following:
    * sum of applied Down Payments (i.e., the sum of "DP Amounts" for all rows in the Down Payments table on the Tract record that are linked to a Payment record) 
    * sum of all "Payment Totals" from all Landowner Payments for the Tract if this sum is non-negative. 
      * Note that if the sum is negative, it means that amounts due to the landowner have not yet reached the down payment total to date.) 
  * Logger Payments (sum of Payment Totals from all Logger Payments for the Tract)
  * Freight (displays the "Total Freight $" from the Tract record, which is the total for both logs and pulpwood)
  * Other Expenses (total of Amounts of Misc Expenses for the Tract)
  * Total Expenses (sum of all above expenses)



  


Notes about expenses: 

  * "Payment Amount" is the "Calculated Amount" for an unpaid Payment record, or the "Check Amount" for a paid Payment record. 
  * Expense Withholding amounts are not included on the report as an expense. If any items related to the Expenses Withholding are to be included as an expense, they should be manually entered in the "Misc Expenses" table on the right-hand side of the Tract record (which is reflected in the report).



  


Net Profit ("Total Income" \- "Total Expenses"; shows as a positive number for profit/negative if a loss)

  


Right pane: This pane shows a simple bar graph, with a bar for Income and a bar for Expenses. 

  * Graph Type: Bar Graph (vertical bars) 
  * Graph Title: Income and Expenses
  * Prompts: N/A
  * Legend: N/A
  * Colors: Default
  * Y Axis Label: "Amount ($)"
  * Y Axis Value: Scale (automatic) 
  * X Axis Label: "Income and Expenses"
  * X Axis Value: Columns for Income and Expenses
  * Series: single, based on Tract
  * Other Notes:
    * The actual amount is listed at the end of each bar (number to 2 decimal places)



  


Filters: 

  * Tract (required; drop list of all Tracts; filters down as you type) 



  


Buttons:

  * N/A



  


Menu Visibility: Users with the View and Edit Financials permission (by virtue of it being on the Financial Menu)

  


Other Notes:

  * N/A



  


Development Specification

Change Requests:

  * Tim Reitz 07/15/2024: [[[IN10071](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10073&)]] - ZET - Tract Profitability by Tract Report - No timber value for Percentage-based Tracts
  * Tim Reitz 08/19/2024: [[[IN10136](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10138&)]] - ZET - Tract Profitability Reports - Fix Totals and Details (prev. Additional Fix for DP Amounts)
  * Ben Reitz 05/01/2025: [[[IN10943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10945&)]] - ZET - Fix Timber Freight Calculations (prev. Tract Profitability Report - Incorrect formula)
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1915642843](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1915642843) 

  


Ellis Miller 12/22/2022:

  


Macros

[ ] Let's create a dictionary TractIncomeExpenseCategories list with these items:

Timber    Income

....

Other Expenses     Expenses

  


[ ] Add a unit test that the value is always Income or Expenses

  


[ ] Add a TractIncomeAmount( vCategory) that has an ifs statement to return the correct amount for each of the income items. Return Div/0 for an unrecognized string so that we find out if someone passes in an incorrect value.

  


[ ] Add a corresponding TractExpenseAmount( vCategory)

[ ] Add a TractTotalIncome that does a ListSubstitute on TractIncomeExpenseCategories and sums the appropriate TractIncomeAmounts

[ ] Do the same for TractTotalExpense

[ ] Add a TractTotalProfit that is Sum(TractTOtalIncome, -TractTotalExpense)

  


[ ] For the Freight expense amount, this could be a macro on the Tract record.  TractTotalFreightExpense: Sum TractTOtalPulpwoodFreight and TractTotalEbyTimberFreight

BID: 8 HOURS

  


REPORT: 

[ ] The report is a Tract-level report that repeats on list for the categories

[ ] Group by List's Lookup value

[ ] Display TractIncomeAmount or TractExpenseAmount

  


[ ] Use expression totals and show TractTotalIncome, TractTotalExpense, TractTotalProfit

4 HOURS

  


GRAPH:

[ ] Tract Level graph with Tract ask prompt

[ ] Two series: Income and Expenses

[ ] Amount: if (GraphSeriesNum=1, TractTotalIncome, TractTotalExpenses)

BID 4 HOURS

  


Tim Reitz 10/24/2022: Add an extra day for graph tweaks (changes might be needed after the initial version is coded).

BID: 8 HOURS
