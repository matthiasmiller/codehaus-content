9.3. View Register

Overview: Register

[X] In this report we display all the transactions of a specific financial account for specified date range.

[X] This has a Balance column which is the running sum of all the debits and credits.

[X] It has some similarities with General Ledger report but the columns are different.

[X] In our system we have an AppHosting setting "Default Account for Register" where we can set any asset or liability type of account.

[X] When we run "View Register" report the account in "Default Account for Register" is selected by default but we can select any other asset or liability type of account in the ask prompt.

  


AppHosting.zone settings:

[X] If an user has the permission "View accounting data" then "Accounting Settings" section is visible.

[X] In this section, there is a setting "Default Account for Register".

[X] This displays a list of all active non-parent asset/liability accounts. (Note: Parent accounts cannot have transactions.)

[X] It can be left blank as this is not a required field.

  


View Register report:

[X] Level: Accounting Transaction

[X] Displays all the transactions of the selected asset / liability account for the specified date range.

  


Jobs:

[X] [[PC0114975]] - Accounting: Create Check Register

  


Menu link:

[X] Accounting | Accounting Tools | View Register

  


Ask Prompts:

[X] From

\- Default is today -90 days.

\- If blank, then considers first transaction date as From date.

  


[X] Through

\- Default is today.

\- If blank, then considers last transaction date as Though date.

  


[X] Account

\- Drop list of all asset and liability active non parent accounts.

\- This is a required prompt.

\- Default is "Default Account for Register" from AppHosting.zone settings.

  


Title:

[X] Register Account: <Account Name>

  


Columns:

[X] Date

[X] Transaction Number

\- Links to transaction detail screen

[X] Reference

[X] Contact 

\- Displays "(Multiple Contacts)" if more than 1 contact is linked in the transaction lines.

[X] Account

\- Displays "Multiple accounts" if more than 1 account is affected apart from account for register. 

[X] Description

[X] Debit

[X] Credit

[X] Balance

\- Displays the running sum of debits and credits

[X] C/R

\- Reconciliation status specified in the transaction lines.

  


Sorting:

[X] Sorted by Transaction date + transaction ID + Account Name + Reference

  


Buttons:

[X] New Transaction

\- Opens a new transaction detail

  


Preface: 

[X] Transactions from <"mmmm dd, YYYY"> through <"mmmm dd, YYYY">

  


No Records Found Msg:

[X] No transactions found.

[X] End date should not be prior to Start date.

  


Go to Row:

[X] The focus is on the last row.
