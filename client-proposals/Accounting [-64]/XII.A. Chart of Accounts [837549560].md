12.1. Chart of Accounts

See  Records | Chart of Accounts in the left pane for more details of the feature.

  


Overview:

  * Chart of accounts is the report where we can add / delete / reorder financial accounts.
  * Can have both numbers and names that are configured by system switch “Use alphanumeric account number”.
  * Indentation on the account names helps understand the account hierarchy easily.
  * Gives an overview on the number of transactions happening on each individual account.
  * Last transaction date column gives an idea when it was used last time.
  * Links to General Ledger report.
  * Coded in [[PC0077836]] - Accounting: Define Chart of Accounts



  


Report:

[X] Level: Financial Account.

[X] Displays active accounts by default.

[X] The rows with inactive accounts are displayed in gray font in the report.

[X] Click sorting is disabled in this report. Coded in [[PC0114132]].

  


Menu link:

[X] Accounting | Accounting Configuration | Chart of Accounts

  


Ask Prompt:

[X] Active Accounts Only (checkbox)

\- Coded in [[PC0104564]]. Filters the inactive accounts.

\- Default is checked.

  


Title:

[X] Chart of Accounts

  


Columns:

[X] Account Number

\- Visible if ConfigAcct_UseAccountNumber system switch value is true.

\- Indent the Account Number based on their hierarchy (parent child relation).

\- Note: This is paired with "Name" column and there is no indentation.

\- Inactive accounts are displayed in gray font.

  


[X] Name

\- Visible if ConfigAcct_UseAccountNumber system switch value is true.

\- Paired with "Account Number" column.

\- Never displays any indentation.

\- Inactive accounts are displayed in gray font.

  


[X] Account Name

\- Visible if ConfigAcct_UseAccountNumber system switch value is false.

\- Indent the "Account Name" based on their hierarchy (parent child relation).

\- Inactive accounts are displayed in gray font.

  


[X] Inactive

\- Visible if "Active Accounts Only" ask prompt is unchecked.

\- Displays text "Inactive" in gray font for inactive accounts.

  


[X] # of Transactions

\- Displays the count of transactions where the financial account has been used.

\- Displays the count in red font if the financial account is a parent account. (Note: We do not allow transaction in a parent account but it can happen that a child account was created later.)

\- Coded in [[PC0104570]]

  


[X] Last Transaction Date

\- Displays the transaction date of the latest transaction that involves this financial account.

\- Coded in [[PC0104570]]

  


[X] View Account

\- Report link

\- Opens financial account detail screen.

  


[X] Edit Account

\- Report link

\- Opens financial account detail screen in edit mode

  


[X] New-Sub-Account

\- Report link

\- Opens a new financial account detail with parent account set.

\- If the subtype of parent accounts is Bank Accounts / Credit Cards, "Uses Reconciliation" checkbox is checked by default.

  


[X] View General Ledger

\- Report link

\- Opens General Ledger report for this account from first transaction date till today.

\- Starting Balance is hidden.

  


Sorting:

[X] Based on Chart of Accounts record order.

  


Grouping:

[X] Financial account types.

  


Buttons:

[X] View Account

\- Row sensitive Report link

\- Opens financial account detail screen.

  


[X] Edit Account

\- Row sensitive Report link

\- Opens financial account detail screen in edit mode

  


[X] New-Sub-Account

\- Row sensitive Report link

\- Opens a new financial account detail with parent account set.

\- If the subtype of parent accounts is Bank Accounts / Credit Cards, "Uses Reconciliation" checkbox is set.

  


[X] View General Ledger

\- Row sensitive Report link

\- Opens General Ledger report for this account from first transaction date till today.

\- Starting Balance is hidden.

  


[X] Organize

\- Visible if ConfigAcct_ManualOrderChartOfAccts switch is true.

\- Opens "Std Chart of Accounts - Organize.r20" with default ask answers.

  


[X] New Account

\- Opens a new financial account detail screen.

  


Disable Column Click Sorting:

[X] Since the account types and hierarchy is very important in this report, click sorting is disabled.

  


No Records Found Msg:

[X] No accounts found.
