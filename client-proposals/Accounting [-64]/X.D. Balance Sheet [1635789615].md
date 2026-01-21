10.4. Balance Sheet

  


Requirements

Overview:

  * A balance sheet summarizes a company's assets, liabilities and shareholders' equity at a specific point in time (as indicated at the top of the statement). It is one of the fundamental documents that make up a company's financial statements.



  


Jobs:

  * [[PC0088787]] - Accounting reports: Balance sheet



  


Report:

[X] Displays "Asset", "Liability" and "Equity" type of accounts, both active and inactive.

[X] It is expected that summation of all "Asset" accounts should equal the summation of "Liability + Equity" accounts.

[X] Level: Financial Account.

  


Menu link:

[X] Accounting | Accounting Reports | Balance Sheet

  


Ask Prompt:

[X] Detail level

\- Numeric list of 1 to 5. [See more on "Report Ask Prompts" on the left pane.]

[X] As of Date:

[X] Added in [[PC0088787]] as a local macro. Label was changed in [[PC0086103]].

[X] Allows blank date. Coded in [[PC0108588]].

[X] Default to the last transaction date. If there is no data in the system, default it to today.

  


[X] Compare to Date

\- An Amount column is added in the report that displays the Balance Sheet for that date. Coded in [[PC0110847]] and [[PC0110809]].

[X] Class(es)

\- Displays all the classes list. Both active and inactive classes are there in the list. Default blank.

\- The transaction lines with Classes are filtered in the amount calculations.

[X] Hide accounts with zero amounts 

\- Default True. Hides the financial account rows that do not have any transaction amounts. [See more on "Report ask prompts" on the left pane.] Added in [[PC0091254]]

  


Title:

[X] Balance Sheet as of <As of Date>. [See more on "Report Title" on the left pane.]

[X] Dates are in the format <mmmm dd, yyyy>.

  


Columns:

[X] Account: Displays financial account name with indentation as per the chart of accounts.

[X] Amount <mm/dd/yyyy>: Displays total amounts.

[X] Amount <mm/dd/yyyy>: Visible: If "Compare to Date" is not blank.

  


Sorting:

[X] As per the Chart of Accounts hierarchy.

  


Grouping:

[X] 2 groups, "Asset" and "Liability + Equity".

[ ] Enhancements were done in Retained Earnings. See [[PC0149875]] - Support equity account subtypes (T&M)

  


Buttons:

[X] No buttons.

  


No Records Found Msg:

[X] "No accounts found."

  


Display-Completed Message:

[X] "Compare to date should be prior to as of date."

[X] "No transaction records exist as of the specified compare to date."

  


Development Specification

Tariqul Hasan 10/03/2017: Make the balance sheet ready for the accounting module. Some examples of balance sheet at [https://www.accountingcoach.com/balance-sheet/explanation](https://www.accountingcoach.com/balance-sheet/explanation).

  


[ ] Show equity correctly

Incorporate [[PC0088121]] to show equity correctly. We don't need it for LAMB but we do for the generic system. 

  


For now we want to show a "Retained Earnings" row (which results from summing up income and expense) when we report on all the accounts. But in LAMB we have additional ask prompts and we give the ability to select a subset of accounts. If we select a subset of accounts then we won't show the "Retained Earnings" row.

  


A question arises, what do we do if there is a separate "Retained Earnings" account in the system? It doesn't change anything, we just let that be a regular account for now and still show the "Retained Earnings" row as mentioned above (meaning two Retained Earnings rows on the report).

  


[ ] Remove account sub-type

Currently the report groupings are by account type, then account sub-type, and then accounts. Accounting sub-type isn't really a part of the chart of accounts / account hierarchy. Remove account sub-type from groupings.

  


[ ] As of date

Make this required, and it should default to the last transaction date. If there is no data in the system, default it to today.

  


[ ] Show a comparison with previous year

Add a checkbox in the ask prompts 'Show prior year balances', and this is by default unchecked. By default the report will show totals 'as of date' and the second column will be hidden.

  


If 'Show prior year balances' is checked then show the second column and it will show balances as of the closing date prior to 'as of date'. If 'as of date' is a closing date then the second column will show balances as of the prior closing date. Refer to [[PC0089240]] for closing date.

  


[ ] Totals and subtotals only report

Make this report a totals and subtotals only report. We will go with the default formatting of totals for now.

  


[ ] Add "detail level" and groupings

Use the "Number of accounts level" system switch in [[PC0089251]]  and add a "Detail Level" ask prompt that shows a numeric list of 1 to system switch value. Default value for the ask will be the system switch value.

  


The report will show detail based on the value of detail level. Add 10 groupings and those should be conditionally visible depending on the system switch value, and also on the detail level selected.

  


[ ] Column headings

Change the column headings to "Account" and "Amount" as shown below.

  


  


[ ] Report title

Report title should say "Balance sheet as of <date>", even if we show a comparison.

  


[ ] Chart of accounts

The report should be driven by chart of accounts. For development purpose now, use a dictionary list and add a macro that returns the sort key for each account to be able to continue with the rest of the enhancements. When we have the chart of accounts ready we can change the macro definition to use it.

  


The following job is required for this [[PC0077836]] - Accounting: Define Chart of Accounts.
