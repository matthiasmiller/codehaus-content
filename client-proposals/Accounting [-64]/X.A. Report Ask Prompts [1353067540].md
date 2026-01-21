10.1. Report Ask Prompts

We have generic ask prompts that are used in a number of accounting reports.

  


Related Jobs:

[ ] We have changed all our multi-select list from multiple lines to 1 line in [[PC0147487]]

  


All the code based ask prompts are mentioned below.

  


Detail level: (Drop List)

[X] Numeric drop list "FinAcctDetailLevels" that displays 1-5.

[X] System switch ConfigAcct_NumberOfAccountLevels is used to set the detail level in client systems.

[X] Displays level of sub-accounts of any financial account based on Chart of Accounts.

[X] Used in 

AppHosting Accounting Std Balance Sheet.r20 Grouping 3 Group By, Group Label

AppHosting Accounting Std Financial Account Budgets.r20 Grouping 1 Group By, Group Label

AppHosting Accounting Std Income Statement.r20 Macro locGroup, locGroupLabel

AppHosting Provident Fund BD Std PF Individual Member Summary.r20 Grouping 2 Group By, Group Label

LAMB Project [XLP] cStd Income Statement.r20 Grouping 3 Group By, Group Label

  


Report Period:

[X] Drop list of "ReportPeriods" consisting the following options. More options were added in [[PC0124517]]

[X] Date Range - Coded in [[PC0101081]]

[X] Through - date is the last transaction date, otherwise today.

[X] From - 

[X] if there is no latest closing date then [FiscalYearStartMonth, 1, year of default end date on the ask]

[X] if there are latest closing date and a prior closing date is before of the default end date then, next day of prior closing date.

[X] but if there is a latest closing date and there is no prior closing date and if latest closing date is not after default end date then next day of latest closing date 

  


[X] Current Week

[X] If this is selected "From", "Through" and "Show amounts by month" prompts are hidden.

[X] Start date: beginning of the week (Sunday).

[X] End date: defaulted to Today.

  


[X] Month to Date

[X] If this is selected "From" and "Show amounts by month" prompts are hidden.

[X] Start date: beginning of the month mentioned in the Through date

[X] End date: defaulted to Today.

  


[X] Quarter to Date

[X] If this is selected "From" and "Show amounts by month" prompts are hidden.

[X] Start date: beginning of the quarter mentioned in the Through date

[X] End date: defaulted to Today.

  


[X] Year to Date - Coded in [[PC0101081]]

[X] Default Through date is last transaction date.

[X] Default Start date is [FiscalYearStartMonth, 1, year of end date]. see also [[PC0100614]].

[X] If the end date month is equal or after FiscalYearStartMonth then the start date is 

[X] [FiscalYearStartMonth, 1, year of end date]. e.g. for date [5/10/2019] and FiscalYearStartMonth 1 start date should be [1/1/2019]

[X] If the end date month is before FiscalYearStartMonth then the start date is 

[X] [FiscalYearStartMonth, 1, previous year of end date]. e.g. for date [1/10/2019] and FiscalYearStartMonth 2 start date should be [2/1/2018]

[X] If this is selected "From" prompt is hidden.

[X] If this is selected "Show amounts by month" prompt is visible.

  


[X] Last Week

[X] If this is selected "From", "Through" and "Show amounts by month" prompts are hidden.

[X] Start date: Start of this week minus 7 days.

[X] End date: Start of this week minus 1 day.

  


[X] Last Month

[X] If this is selected "From", "Through" and "Show amounts by month" prompts are hidden.

[X] Start date: First calender day of this month minus 1 month.

[X] End date: Last calender day of this month minus 1 month.

  


[X] Last Quarter

[X] If this is selected "From", "Through" and "Show amounts by month" prompts are hidden.

[X] Start date: First day of (Quarter start month - 3) and this year/last year

[X] End date: Last calender day of this month minus 1 month.

  


[X] Last Year

[X] If this is selected "From", "Through" and "Show amounts by month" prompts are hidden.

[X] Start date: First calender day of this month minus 1 month.

[X] End date: Last calender day of this month minus 1 month.

  


[X] All Time - Coded in [[PC0155937]] 

[X] This is equivalent to running with the "Date Range" and having both dates blanked.

[X] Selecting "All Time" makes From and Through date prompts hidden

  


Show amounts by month: (Checkbox)

[X] Added in [[PC0088788]].

[X] Amounts are grouped by months and displayed in corresponding month columns followed by a Total column.

[X] This is only visible if "Year to Date" is selected in "Report Period" ask prompt.

[X] Default False.

[X] The number of columns are from start of fiscal year to today. See "Config_FiscalYearStartMonth" system Switch.

[X] Used in the following reports

AppHosting Accounting --> Std Income Statement.r20

LAMB Project [XLP] --> cStd Income Statement.r20

  


Class(es): (Multi-selection list)

[X] Displays all active + inactive classes.

[X] "(Blank Class)" option was added in [[PC0147434]]

[X] Selecting this filters all the transaction rows that do not have class specified.

[X] Used in the following reports

AppHosting Accounting --> Std Accounting Transactions.r20

  


See [[PC0112450]] - Accounting: Support filtering standard reports by classes

In progress: [[PC0113795]] - Remove Inactive Classes from Class Multi-Selection List

  


Hide accounts with zero amounts: (Checkbox) 

[X] Added in [[PC0091110]].

[X] Hides the financial account rows that do not have any transaction amounts.

[X] Default True.

[X] Used in the following reports.

AppHosting Accounting --> Std Balance Sheet.r20

AppHosting Accounting --> Std Income Statement.r20

AppHosting Accounting --> Std Trial Balance.r20

AppHosting Provident Fund BD --> Std PF Individual Member Summary.r20

LAMB Project [XLP] --> cStd Income Statement.r20

LAMB Project [XLP] --> cStd Trial Balance.r20

  


Transaction ID: (String)

[X] Fetches specified transaction record.

[X] Label is "Batch ID" in XLP system.

[X] Used in the following reports.

AppHosting Accounting Std Accounting Transactions.r20

AppHosting Accounting Std Journal Entries.r20

AppHosting Provident Fund BD Std PF Individual Journal Entries.r20

LAMB Project [XLP] Std Search Transaction.r20

  


Contains Text: (String)

[X] Matches the transaction text in Reference, Description, Contact, Supporting Details or AcctTransLineNotes

[X] Used in

AppHosting Accounting Std Journal Entries.r20

AppHosting Accounting Std Accounting Transactions.r20

  


Contacts(s): (Drop list)

[X] Coded in [[PC0114689]]

[X] Displays all contact and organization (both active and inactive) names.

[X] Used in the following reports.

AppHosting Accounting --> Std Accounting Transactions (helper).r20

AppHosting Accounting --> Std Accounting Transactions.r20

AppHosting Accounting --> Std General Ledger.r20

AppHosting Accounting --> Std Transactions by Contact Summary.r20

  


Account Number: (string)

[X] Local macro, used in Std Choice Transaction Accounts.r20, Coded in [[PC0108521]]

  


Account Name: (string)

[X] Local macro, used in Std Choice Transaction Accounts.r20, Coded in [[PC0108521]]

  


Account Type: (drop list)

[X] Displays all account types. i.e. "Asset | Liability | Equity | Income | Expense"

[X] Used in the following reports

AppHosting Accounting --> Std Financial Account Budgets.r20

AppHosting Accounting --> Std Choice Transaction Accounts.r20

  


Account Type(s): (multi-selection list)

[X] Used in the following reports

AppHosting Accounting Std Accounting Transactions (helper).r20

AppHosting Accounting Std Accounting Transactions.r20 Subset

AppHosting Accounting Std Financial Account Budgets - Entry.r20

AppHosting Accounting Std Financial Account Budgets.r20

AppHosting Accounting Std Transactions by Contact Summary.r20

CodeCrafters - CodeCrafters Admin [XCC] cStd Invtools Reconciliation.r22

CodeCrafters - CodeCrafters Admin [XCC] cStd Reconciliation Income Expense Detail.r20

CodeCrafters - CodeCrafters Admin [XCC] cStd Reconciliation Income Expense Summary.r20

CodeCrafters - CodeCrafters Admin [XCC] cStd Reconciliation Salary Cost Review.r20

LAMB Project [XLP] Std Budgets.r20

  


Account Subtype: (drop list)

[X] Coded in [[PC0108521]]

[X] Displays "FinAccountSubTypes" list.

[X] Used in AppHosting Accounting --> Std Choice Transaction Accounts.r20

  


Client System specific:

[X] [[PC0081184]] - XLP - Ability to Inject Client System Ask Prompts in Accounting Reports

[X] In XLP there is Fund, Dept, Location etc. [[PC0090233]] - XLP - Breakdown account name ask prompt

[X] [[PC0103655]] - XLP - Changes to Date Ask Prompt
