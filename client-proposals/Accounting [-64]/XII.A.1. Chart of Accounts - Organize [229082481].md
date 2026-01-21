12.1.1. Chart of Accounts - Organize

See  Records | Chart of Accounts in the left pane for more details of the feature.

  


Overview:

  * In financial reports, the account names are not displayed alphabetically rather based on importance. For example, "Cash in Hand" account should be before "Accounts Receivable" as that conveys more information and user is more interested on this account.
  * We allow moving an account top or bottom with this editable report.
  * For this we have a system switch "ConfigAcct_ManualOrderChartOfAccts".
  * Here the account on selected row can be moved after any other account specifying in the "Move After" column.
  * Saving the changes opens the Chart of Accounts report again with the new order of accounts.



  


Jobs:

[X] [[PC0077836]] - Accounting: Define Chart of Accounts

  


Report:

[X] Editable screen type

[X] Level: Financial Account.

[X] Opens with only active accounts.

[X] However we can move any account after an inactive account as inactive accounts are displayed in the list.

[X] On saving the changes an import runs that updates the chart of accounts record.

[X] The main chart of accounts report is displayed immediately after save.

[X] Click sorting isdisabled in this report. Coded in [[PC0114132]]

  


Menu link:

[X] Accounting | Accounting Configuration | Chart of Accounts and then Organize button

  


Title:

[X] Organize Chart of Accounts

  


Columns:

[X] Account Number

\- Visible if ConfigAcct_UseAccountNumber is true.

\- Maintains indentation as per hierarchy

  


[X] Name

\- Visible if ConfigAcct_UseAccountNumber is true.

\- No indentation.

  


[X] Account Name

\- Visible if ConfigAcct_UseAccountNumber is false.

\- Maintains indentation as per hierarchy

  


[X] Move After

\- Editable column

\- Shows a drop down of financial accounts

\- Only Sibling accounts from the same Account type is displayed in this list

\- Displays any inactive account in this drop down.

  


Sorting:

[X] Based on Chart of Accounts record order.

  


Grouping:

[X] Financial account types.

  


Buttons:

[X] Close

\- Runs Chart of Accounts report with default ask answer.

  


No Records Found Msg:

[X] No accounts found.

  


Run Import After Save:

[X] Runs the import - Std Chart of Accounts - Organize.x30

  


Run Report After Save:

[X] Std Chart of Accounts - Financial Accounts.r20
