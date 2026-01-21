10.6. Journal Entries

Overview:

  *  A Journal is a book in which all the transactions of a business are recorded. Every transaction affects two accounts, one is debited and the other one is credited.



  


Jobs:

  * [[PC0077938]] - E00 - Accounting: Define basic reports
  * [[PC0091021]] - Accounting reports: Journal Entries



  


Report:

[X] This report displays all the transaction rows from Transaction record.

[X] We do not have a grand total row in this report [[PC0092543]]

[X] Level: Accounting Transaction.

[X] Regression testing is supported for this report.

  


Menu link:

[X] Accounting | Accounting Reports | Journal Entries

  


Ask Prompt:

[X] Transaction ID

\- Displays transaction rows for this specific transaction ID. Also see "Report ask prompts" in the left pane.

[X] Report Period

\- Default is Year to Date. [See more on "Report ask prompts" on the left pane for all the combinations.]

[X] Through

\- Default is last transaction date. [See more on "Report ask prompts" on the left pane for all the combinations.]

[X] Class(es)

\- Displays all the classes list. Both active and inactive classes are there in the list. Default blank.

\- The transaction lines with Classes are filtered.

[X] Contains Text

\- Matches the transaction text in Reference, Description, Contact, Supporting Details or AcctTransLineNotes

  


Title:

[X] Journal Entries <Start Date> through <End Date>. [See more on "Report Title" on the left pane.]

[X] Dates are in the format <mmmm dd, yyyy>.

  


Columns:

[X] Date

[X] Account Name

[X] Debit

[X] Credit

[X] Class - Coded in [[PC0091021]]

[X] Journal Reference - (Only in XLP system) Coded in [[PC0089386]]

[X] Notes

\- Displays transaction line notes followed by supporting details. See AcctTransNotesDisplayForRpt.

  


Sorting:

[X] Transaction date + Transaction ID

  


Grouping:

[X] Transaction ID

  


No Records Found Msg:

[X] "End date should not be prior to Start date." when start date is later than the end date.

[X] "No transactions found."
