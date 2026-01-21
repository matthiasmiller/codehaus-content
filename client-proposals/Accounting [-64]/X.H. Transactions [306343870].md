10.8. Transactions

Overview:

This is a multi-pane report that displays all the Transactions from the database. The left pane displays the transaction ID and other transaction specific details whereas the right pane serves as a preview of all the transaction line rows with corresponding debit and credit amounts. An user can search for the desired transactions with the help of ask prompts. The filtering applies on both the panes.

  


Jobs:

  * [[PC0077938]] - E00 - Accounting: Define basic reports



  


Report:

[X] Left pane displays transaction specific details.

[X] Right pane displays the transaction rows, debit, credits etc transaction line related items.

[X] We allow blank date range coded in [[PC0108588]]

  


Menu link:

[X] Accounting | Accounting Reports | Transactions

  


Ask Prompt:

[X] Transaction ID

\- Displays transaction rows for this specific transaction ID. [See more on "Report ask prompts" on the left pane.]

[X] Invoice Number - Visible if ConfigAcct_TransactionHasLinkedRecs is set.

[X] Report Period

\- Default is Year to Date. [See more on "Report ask prompts" on the left pane for all the combinations.]

[X] Through

\- Default is last transaction date. [See more on "Report ask prompts" on the left pane for all the combinations.]

[X] Account type(s)

[X] Account(s)

[X] Class(es)

\- Displays all the classes list. Both active and inactive classes are there in the list. Default blank.

\- The transaction lines with Classes are filtered.

[X] Incident ID - Visible if ConfigAccounting_HasJobsModule is set

[X] Status

\- Local ask prompt with options "Draft | Posted | Voided".

[X] Contains Text - This filters text from all the following fields.

[X] Reference

[X] Description

[X] Supporting Details

[X] Transaction Line Notes

[X] Transaction Line Contact

[X] Match Key

\- This filter is visible for users with Can view diagnostic accounting data" permission.

  


Title:

[X] Accounting Transactions <Start Date> through <End Date>. [See more on "Report Title" on the left pane.]

[X] Dates are in the format <mmmm dd, yyyy>.

  


Columns:

Left Pane:

[X] Transaction ID

\- Links to the transaction detail.

[X] Date

[X] Status

[X] Contact

[X] Amount

\- This displays the sum of all debit rows or the sum of all credit rows. Note that we have a validation that the sum of debits and sum of credits should be equal in the transaction record.

[X] Reference

\- Reference from the transaction record.

  


Right Pane:

[X] Account Name

[ ] Contact

[X] Debit

[X] Credit

[X] Class

  


Sorting:

[X] Left pane: Transaction Date + Transaction ID in a reverse order. Latest transaction at the top.

[X] Right pane: Account Name in transaction rows.

  


Buttons:

[X] Detail screen

[X] Duplicate Transaction

\- A copy of this transaction is created with Today as the transaction date and initializing few fields.

[X] New Transaction

  


Sub-pane:

[X] The right pane displays the transaction lines from the Transaction ID of the main pane.

  


Footnotes:

[X] Right pane: "* The total of debit/credit may differ with the amount on the left pane as that is the total amount of unfiltered transactions."

  


No Records Found Msg:

Left Pane:

[X] "No transactions found."

[X] "End date should not be prior to Start date."

  


Right Pane:

[X] "No transaction lines found."
