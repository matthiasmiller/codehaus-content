10.5. General Ledger

Overview:

  * In accounting, a general ledger is used to record all of a company's transactions. Within a general ledger, transactional data is organized into assets, liabilities, revenues, expenses, and owner's equity.



  


Jobs:

  * [[PC0088789]] - Accounting reports: General ledger



  


Report:

[X] Displays all the transactions of any financial account.

[X] Level: Accounting Transaction

  


Menu link:

[X] Accounting | Accounting Reports | General Ledger

  


Ask Prompt:

[X] Report Period

\- Default is Year to Date. [See more on "Report ask prompts" on the left pane for all the combinations.]

[X] Through

\- Default is last transaction date. [See more on "Report ask prompts" on the left pane for all the combinations.]

[X] Account(s)

\- Multi selection list 

[X] Class(es)

\- Displays all the classes list. Both active and inactive classes are there in the list. Default blank.

\- The transaction lines with Classes are filtered in the amount calculations.

[X] Hide starting balance

\- Default True. Hides the starting and ending balance grouping in the report.

  


[X] Contact(s)

\- Displays all contact and organization (both active and inactive) names.

Title:

[X] General Ledger <Start Date> through <End Date>. [See more on "Report Title" on the left pane.]

[X] Dates are in the format <mmmm dd, yyyy>.

  


Columns:

[X] Date

[X] Transaction Number - Links to transaction details screen.

[X] Debit

[X] Credit

[X] Class

[X] Notes - Displays transaction line note + (Supporting Details: <Notes from supporting details memo>).

[X] C/R

  


Sorting:

[X] Transaction Date + Transaction ID

  


Grouping:

[X] Account Name

[X] Starting Balance

\- Visible when "Hide starting balance" is unchecked.

[X] Ending Balance

\- Visible when "Hide starting balance" is unchecked.

  


Buttons:

[X] New Transaction - this is visible if user has permission to create accounting transactions.

  


Preface: 

[X] If contact(s) are selected in the ask prompt, "Contacts(s): <Contact 1>, <Contact 2> and <Contact 3>" preface is added in this format.

  


No Records Found Msg:

[X] "End date should not be prior to Start date."

[X] "No transactions found."

  


Jobs:

 [[PC0111581]] - Use Ask prompt macros for date range in general ledger report

\- Here changed from local macros to code based macros
