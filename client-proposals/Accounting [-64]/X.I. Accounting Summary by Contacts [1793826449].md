10.9. Accounting Summary by Contacts

Overview:

  * Sometimes we want to see all the transactions tied to a contact. The purpose of this report is to display the summation of all the transactions grouped by account type.



 

Jobs:

  *  Added in [[PC0114804]] - Accounting: Add transaction reports by payee



  


Report:

[X] We can track accounting summary by contacts.

[X] This report is not added in regression suit.

[X] Level: Accounting Transaction.

  


Menu link:

[X] This is inside a lightbox.

[X] Accounting | Accounting Reports | more reports | Accounting Summary by Contacts

  


Title:

[X] Accounting Summary by Contacts <Start Date> through <End Date>. [See more on "Report Title" on the left pane.]

[X] Dates are in the format <mmmm dd, yyyy>.

  


Ask Prompts:

[X] From [date]

[X] Through [date]

[X] Account type(s) [multi selection list]

\- List of all account types.

[X] Account(s) [multi selection list]

\- List of all accounts, both active and inactive.

[X] Class(es) [multi selection list]

\- List of all classes, both active and inactive

[X] Contact(s) [multi selection list]

\- List of all contacts, both active and inactive.

  


Columns:

[X] Contact

[X] Amount

\- All the sum of Debit minus sum of Credit from the transaction lines.

  


Sorting:

[X] Contact Name

  


Grouping:

[X] Totals and subtotals only

[X] Grouped by Account type, Contact

  


Buttons:

[X] Detail screen

[X] Open Transaction

\- Opens the transaction report filtered by the selected Contact name.

  


No Records Found Msg:

[X] No transactions found.
