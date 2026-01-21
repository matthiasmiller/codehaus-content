10.7. Trial Balance

Overview:

  * A trial balance is a list of credit entries and debit entries that businesses use to internally audit their double-entry accounting systems. The goal is to confirm that the sum of all debits equals the sum of all credits and identify whether any entries have been recorded in the wrong account



  


Jobs:

  * [[PC0077938]] - E00 - Accounting: Define basic reports
  * [[PC0088790]] - Accounting reports: Trial balance
  * [[PC0107454]] - XLP - Enhance Trial Balance Report
  * [[PC0110132]] - XLP - In Trial Balance starting balance should be zero for Income and Expenses



  


Report:

[X] Level: Financial Account..

[X] Displays net debit or credit for each account on either debit column or credit column.

[X] For asset and expense types of accounts, display amount on Debit column

[X] For liabilities, income and equity types of accounts, display amount on Credit column

[X] Columns are opposite for contra accounts.

[X] Displays a msg "The totals of debits and credits do not balance." if there is a mismatch in total debit / credit.

[X] Regression testing is supported for this report.

  


Override:

[X] Overridden in XLP system. There we have more columns than this generic report. See [[PC0107454]]

  


Menu link:

[X] Accounting | Accounting Reports | Trial Balance

  


Ask Prompt:

[X] As of Date

[X] Class(es)

\- Displays all the classes list. Both active and inactive classes are there in the list. Default blank.

\- The transaction lines with Classes are filtered.

[X] Hide accounts with zero amounts 

\- Default True. Hides the financial account rows that do not have any transaction amounts. Also see the "Report ask prompts" on the left pane. Added in [[PC0091110]]

  


Title:

[X] Trial Balance as of <As of Date>. [See more on "Report Title" on the left pane.]

[X] Dates are in the format <mmmm dd, yyyy>.

  


Columns:

[X] Account Name

[X] Debit

[X] Credit

  


Sorting:

[X] locFinAcctSortKey( FinAccountName)

  


Buttons:

[X] "Open General Ledger" \- Opens general ledger report for the account for the specified date range. Coded in [[PC0108250]]

[X] "Account Name" column has link to open Financial account.

  


Footnotes:

[X] "* The totals of debits and credits do not balance."

  


No Records Found Msg:

[X] "No accounts found."

  


Display-Completed Message:

[X] "The totals of debits and credits do not balance."
