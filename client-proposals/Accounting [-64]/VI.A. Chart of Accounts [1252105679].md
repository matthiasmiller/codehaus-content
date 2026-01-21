6.1. Chart of Accounts

Coded in [[PC0077836]] - Accounting: Define Chart of Accounts 

  


From Wikipedia,"A chart of accounts (COA) is a created list of the accounts used by an organization to define each class of items for which money or the equivalent is spent or received. It is used to organize the finances of the entity and to segregate expenditures, revenue, assets and liabilities in order to give interested parties a better understanding of the financial health of the entity.". In the accounting module we need a way to create/modify a chart of accounts. For now we will add one Chart of Accounts for the system and in future we might need the ability to ship additional ones.

  


Nice introductions to chart of accounts including samples:

  * [https://www.accountingcoach.com/chart-of-accounts/explanation](https://www.accountingcoach.com/chart-of-accounts/explanation) \- nice intro including samples
  * [https://en.wikipedia.org/wiki/Chart_of_accounts](https://en.wikipedia.org/wiki/Chart_of_accounts) \- more discussion including several templates



  


Account Types

We have the following account types:

  * Asset
  * Liability
  * Equity
  * Income
  * Expense



  


These will be used for the major groupings in reports (e.g. Balance Sheet, Income Statement, Chart of Accounts, etc). The list is not user-configurable.

  


Chart of Accounts

Accounts can either be sorted alphabetically or manually. This is controlled by the "Allow manual ordering in chart of accounts" (Config_ManualOrderChartOfAccts) system switch. For XLP, this is set to "No".

  


We'll use a report that displays the chart of accounts. It will have the following buttons:

  * Row-independent buttons: Organize, New Account.
  * Row-sensitive buttons: View Account, Edit Account, New Sub-Account, Delete Account (See [[PC0091386]]), (note that we will add the delete account button after the first release, and view general ledger button will be added in a separate job but for the first release), View General Ledger .



  


The maximum level of accounts in the hierarchy is controlled by the system switch Config_NumberOfAccountLevels  ([[PC0086237]]), currently we allow up to 5 levels (for XLP we set it to 4).

  


Button Actions

Organize

Opens another report (editable) with two columns: Account Name and Move After. In the second column user can specify for an account a manual order; for each account this column shows only those accounts where the account can be moved in the chart of accounts.

In this view there will be two buttons: Save Changes, Close.

  * After modifying, user can save changes. 
  * Close will simply open the chart of accounts, in non-editable mode.



  


New Account

Opens up a new account detail screen. Once saved the account is ordered alphabetically.

  


View Account

Opens account detail screen.

  


Edit Account

Opens up the account detail screen in edit mode.

  


New Sub-Account

This is similar to the "New Account" button with the difference of defaulting the "Sub-account of" field to the currently selected account. Of course that means, Type and sub-type are also the same as the parent account.

  


Delete Account...

We may add this button later to the report in [[PC0091386]]. For now user can delete an account from the account detail screen provided user has appropriate permissions and/or validations do not fail.

  


View General Ledger

This will be done in [[PC0089750]].

  


Validations for Modifying Chart of Accounts

1\. Delete account: account cannot be deleted if it has

[X] child accounts.

[X] transactions.

2\. New sub-account: 

When a sub-account is created all transactions have to be moved to another account. This requires [[PC0091246]]. For now we will just add validation that for an account with transaction we cannot add a sub account.

3\. Edit Account:

Sub-account of:

[X] An account cannot be set as it's own parent account.

[X] An account cannot set a child account as it's parent.

[X] An account cannot set an account as parent if it will exceed maximum level of accounts.

[X] An inactive account cannot be a parent of an active account.

Account is active:

[X] If not all descendants are inactive, it cannot be set as inactive.

Account type:

Account type cannot be changed if 

[X] it has child accounts.

[X] transactions were entered for it.

4\. Organize

If parent account changes for a manually ordered accounts, it will be sorted default in the siblings.

5\. Split

To split a single account into a parent/child account:

  * Rename the original account to the CHILD ACCOUNT NAME. All linked transactions will now show that new name.
  * Create a new account with the PARENT ACCOUNT NAME.
  * Edit the original account (in #1) to link to the parent account (in #2).



  


Technical Details

We will use an underlying Chart of Accounts record which will store any manually ordered accounts in an RG. We will use macros to show Manually Ordered Accounts + All other accounts alphabetically in each of the types. This makes so that a newly created account is automatically added to the chart of accounts (we don't have a way to automatically add it when saving the newly created account and I'd like to avoid the two-step add process).

  


We'll show all row-sensitive buttons next to each account name as columns, including the view account button. This makes the links look nicer (as opposed to having the account names appear as links, in which case there are indents before account names depending on account level and the links appear longer than the account name).

  


Organize button:

We will use an editable report for organizing the chart of accounts. On save, it will run an x30 import that modify the respective chart of accounts record. We added a Chart of Accounts lookup record in [[PC0078489]], we can use that and add the RG.

  


In a later release we may add more than one chart of accounts, so most macros, and components are set up that way (and requires passing in a chart of accounts name, and for the default passing in an empty string will work). Following are the things needed if we want to use chart of accounts in any report for now:

  * Use the sort key from chart of accounts in the sort expression, or in the group by expression for totals and sub-totals only report.
  * For performance reasons, add a local macro in the report as locFinAcctOrderedList, which is basically FinAcctOrderedList( "Chart of Accounts").
  * Also add a local macro to generate sort key, the definition of which would be similar to FinAcctSortKeyFromChart but will use the locFinAcctOrderedList macro instead.



Use GetIndentForFinAcct to add indent to account name, to show hierarchy.
