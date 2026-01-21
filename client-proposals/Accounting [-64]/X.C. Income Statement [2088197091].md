10.3. Income Statement

  


Requirements

Overview:

  *  An income statement shows a company's revenues, expenses and profitability over a period of time. It is also sometimes called a profit-and-loss (P&L) statement or an earnings statement. It shows your revenue from selling products or services and expenses to generate the revenue and manage your business.



  


Accessed from:

  * Accounting | Accounting Reports | Income Statement (opens a prompt screen with the filters) 



  


Title:

  * Income Statement <Start Date> through <End Date>
    * Note: Dates are in the format <mmmm dd, yyyy>



  


Preface: May include one or multiple of the following in a single line (comma-separated): 

  * "End Date: <Report Period end date>, Start Date: <Report Period start date>" (always visible) 
    * Note: Dates are shown in this format: "mm/dd/yyyy"
  * "Hide accounts with zero amounts: Yes" (visible if the corresponding checkbox is checked)  
  * "Show amounts by month: Yes" (visible if the corresponding checkbox is checked) 



  


Columns: 

  * Account (displays the account name)
  * Amount (visible if "Show amounts by month" is unchecked; displays the total amount of either "Income" or "Expense" associated with the account)
  *  <MMMM, YYYY> format month columns (visible if "Show amounts by month" checkbox is checked; displays a column per month within the specified range)
  * Total (visible if "Show amounts by month" checkbox is checked; displays the total for each row, as well as a grand total for all rows in the group)



  


Grouped by: The following 3 hard-coded groupings: 

  * "Income" 
  * "Expense"
  * "Net Surplus / Deficit" (displays the sum total of "Income" and "Expense" totals) 



  


Sorted by: 

  * Account



  


Filters: 

  * Detail level (list field of 1-5; defaults to 5; a higher number means more sub records are shown in the report)
  * Report Period (list field of "Report Periods"; defaults to "Year to Date"; sets the time range of "Transaction" records to search through)
    * Note: this field directly affects the visibility of the next three fields.
  * From (date field; visible if "Report Period" is set to "Date Range"; defaults to the first day of the current year; determines the range that the report shows results for)
  * Through (date field; visible if "Report Period" is set to one of the following: "Date Range", "Month to Date", "Quarter to Date", or "Year to Date"; defaults to the date of the most recent transaction; determines the end date of the range that the report shows results for)
    * Note: if no prior transaction exists, defaults to today's date.
  * Show amounts by month (checkbox; visible if "Report Period" is set to "Year to Date"; when checked, the report displays columns for each month within the given range) 
  * Class(es) (multi-select list of "Accounting Classes"; defaults to blank = all; determines the class(es) of financial accounts that are shown) 
  * Incident ID (plain text field; visible if system includes "AppHosting Accounting JobsModule.txt"; filters the report by Job ID / Incident ID)
  * Hide accounts with zero amounts (checkbox; defaults to checked; when checked, hides the financial account rows that do not have any transaction amounts)



  


Buttons:

  * Open General Ledger (Row-sensitive link that is displayed in each row; opens general ledger report for the account for the specified date range.)



  


Menu Visibility: 

  * Visible to all Users with access to the Accounting menu option.



  


Other Notes:

  * N/A



  


Development Specification

Tariqul Hasan 10/03/2017: Make the income statement ready for the accounting module. See [https://www.accountingcoach.com/income-statement/outline](https://www.accountingcoach.com/income-statement/outline) for examples.

  


[ ] Remove account sub-type

Currently the report groupings are by account type, then account sub-type, and then accounts. Accounting sub-type isn't really a part of the chart of accounts / account hierarchy. Remove account sub-type from groupings.

  


[ ] Add "detail level" and groupings

Use the "Number of accounts level" system switch in [[PC0089251]]  and add a "Detail Level" ask prompt that shows a numeric list of 1 to system switch value. Default value for the ask will be the system switch value.

  


The report will show detail based on the value of detail level. Add 10 groupings and those should be conditionally visible depending on the system switch value, and also on the detail level selected.

  


[ ] Date range

In it's simplest form the report prompts for start date and end date (this is what we have in the generic report now), for LAMB we have a customized prompt. In both cases:

  * Let's require both the prompts. 
  * End date should default to the last transaction date. If no transaction is available default it to today.
  * Start date should default to the next day of the last closing date. If no closing date is available then default to the first day of the same year as the end date. If the end date is a closing date then start date should be the next day of the closing date prior to the end date.
  * Change the ask names to "From" and "Through".



  


Refer to [[PC0089240]] for closing date.

  


[ ] Breakdown by period

Let's keep it simple for now, add an ask list "Report period" with options "Year to Date" and "Date Range"; default to "Year to Date". This will be the first ask.

  * If "Year to Date" is selected let's hide "From" and show "Through".
  * If "Date Range" is selected let's show both "From" and "Through".
  * In both the cases above the values for "From" and "Through" will be as mentioned above in "Date range".



  


Add another ask "Show amounts by month" (checkbox) and default to False, in which case all the numbers are shown in a single column for the period. If "Show amounts by month" is checked then we would show one column for each month in the date range.

  


[ ] Report title

Change report title to "Income Statement date1 through date2" and printed title will be in two lines.

  


[ ] Ask prompts title

Change the title of the ask prompts to "Income Statement". We will use this as the standard name throughout the report.

  


[ ] Column heading

Change column headings to 'Account' and 'Amount'. If "Show amounts by month" is checked then column headings will be like "Month, YYYY".

  


[ ] Totals and subtotals only report

Make this report a totals and subtotals only report. 

  


[ ] Identify

It would be nice to be able to open general ledger from this report. The identify report should open general ledger for the selected account and the same date range of the income statement. We can do this separately, written up [[PC0089385]].

  


[ ] Chart of accounts

See notes for the same in [[PC0088787]]. For the final implementation of it we need to code [[PC0077836]].

  


[ ] Formatting

  * Confirm with EllisM/JoelI/NahianK before you do this. But I think it's a good idea to think of this as a report that user could print in landscape layout. So, I think it'd be OK to choose a 'width' of the total report that's bit wider than it is now. However, when there is only one column (not broken down by month), it can be printed in portrait layout as well. So much to say, think thru the total (default) width of the report and discuss if needed.
  * Think thru properly underlining the totals. Please discuss this with me when you get to this point.
  * Add Label "Net Surplus / Deficit" on the total line. This was written up in [[PC0083911]]; let's close it.



  


Sagar Sagar 11/27/2017: Lets remove cStd Income Statement from XLP and use standard report.
