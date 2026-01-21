12.5.1. Import Accounts

Import process:

  * The import of financial accounts involves 3 steps



1\. Import of all financial accounts from the input excel file

2\. Import Chart of Accounts record

3\. Update the chart of accounts

  


Jobs:

[X] [[PC0109186]] - Accounting: Enhance export/import financial accounts

[X] [[PC0112194]] - Accounting: Enhance export/import financial accounts Part 2

[X] [[PC0115462]] - Accounting: Chart of accounts order lost when importing new accounts

[X] [[PC0102646]] - Accounting: Support importing by account number instead of full account name

  


Input file:

  * We can import financial accounts along with their hierarchy as per chart of accounts in our system.
  * For this we need to have an excel input file with the following columns



[X] Account Number (blank if no account number is specified)

[X] Account Name

[X] Active?

[X] Parent Account Number

[X] Parent Account Name

[X] Type

[X] Sub-type

[X] Contra Account?

[X] Description

[X] Place Account After

NOTE : Company ID column was added while coding Accounting Companies feature.

  * We need to make sure that parent accounts are imported before child accounts.
  * If any financial account has the term "deleted" then that account is not imported.


