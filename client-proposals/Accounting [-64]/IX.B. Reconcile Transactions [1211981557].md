9.2. Reconcile Transactions

Jobs:

  * [[PC0111551]] - Add basic support for clearing/reconciling transactions



  


\- If the subtype of parent accounts is Bank Accounts / Credit Cards, "Uses Reconciliation" checkbox is checked by default.

  


Report:

[X] Level: Accounting Transaction.

[X] The purpose of this report is to match the account transactions with a bank statement or similar document.

[X] Editable report where user can mark any transaction row as Reconciled or Cleared.

[X] This report has a special running sum column named "Balance".

[X] The amount is negative or positive based on the account type .

[X] Disable Column Click Sorting is disabled in this report.

  


Menu link:

[X] Accounting | Accounting Tools | Reconcile Transactions

  


Ask Prompt:

[X] From (date)

[X] Through (date)

[X] Account to reconcile (drop list)

\- Required, Filtered list, accounts that has "Uses Reconciliation" checked in account record.

[X] Hide starting balance (checkbox)

\- Default false

[X] Reconciliation status (Blank = All) (multi-select list)

\- AcctTransReconcileOptions list consisting "Cleared | Reconciled".

  


Title:

[X] Reconcile Account: <Selected account name>

  


Columns:

[X] Date

[X] Transaction Number

[X] Link to Transaction detail screen.

[X] Debit

[X] Credit

[X] Balance

[X] This column displays the running sum of the Debits and Credits.

[X] Custom column

[X] Hidden in generic accounting system.

[X] Journal Reference in XLP

[X] C/R

[X] Shows a list of "C | R | Blank" as the first letter of reconciliation statuses.

[X] Editable and need to press "Save Changes" to save.

[X] Notes

[X] Displays transaction line notes followed by supporting details. See AcctTransNotesDisplayForRpt.

[X] Contact

  


Sorting:

[X] Transaction date + Transaction ID + Transaction row number

  


Grouping:

[X] Starting Balance

[X] Ending Balance

[X] Unchecking "Hide Starting Balance" checkbox should hide Starting Balance.

[X] Unchecking "Hide Starting Balance" checkbox should display "Balance" instead of "Ending Balance".

  


Buttons:

[X] Menu button: Mark as Cleared

[X] Menu button: Mark as Reconciled

[X] Menu button: Clear Reconciliation

Note: In the following job we removed some more buttons.

[[PC0115762]] - Accounting: Remove "Mark All" options from the reconcile transactions report

  


Preface:

[X] Transactions from January 02, 2019 through November 09, 2022

  


No Records Found Msg:

[X] "No transactions found."

[X] "End date should not be prior to Start date."
