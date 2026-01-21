1\. Overview

Chart of Accounts:

  * A robust Chart of accounts where we can add/delete/reorder accounts.
  * Can have both numbers and names that are configured by system switch “Use alphanumeric account number”.
  * Indentation on the account names helps understand the account hierarchy easily.
  * Gives an overview on the number of transactions happening on each individual account.
  * Last transaction date column gives an idea when it was used last time.
  * Links to General Ledger report.



  


Financial Accounts:

  * An account that has transactions cannot be deleted. It can be made inactive.
  * Has the ability to mark as a contra account.
  * Can be linked with contacts.
  * Can be marked as “Uses reconciliation”.
  * Entering budget amounts is possible but preferable is to use budget reports.



  


Transactions:

  * Transaction can use 2 status (Posted|Voided) or 3 status (Draft|Posted|Voided) for better controlling depending on configuration “Allow draft transactions”.
  * Only users with required permissions will have the ability to view / modify transactions.
  * Supporting details to preserve attached files / documents.
  * Description, Reference, Notes in transaction lines, can be added on each transaction.
  * Speed keying saves time while entering transaction data rows.
  * Class is automatically populated in transaction lines if they are defined in the accounts.
  * Contact or Organization can be linked directly on transaction lines.
  * Bills can be created directly from the menu page to help users.



  


Class:

  * Has the ability to mark transactions as of different classes. This helps to track similar transactions and generate reports quickly based on those classes.



  


Accounts Receivable Invoice Linking:

  * Invoice is a standalone module in AppHosting.zone and can be linked to accounting module as well
  * If linked then accounting transactions can be created directly from the invoice.



  


Accounts Payable:

  * New Bills can be created from menu.
  * Aging Bills report displays the bills due in coming days.



  


Check Register:

  * In AppHosting setting "Default Account for Register" where we can set any asset or liability type of account.
  * View Register report displays the register for asset or liability type of accounts.



  


Contact linking:

  * In transaction detail we can link any contact to any transaction line.



  


Accounting Reports:

Income Statement:

  * “Detail level” can be specified for better readability.
  * Income statements can be displayed by months for the current year.
  * For each item in this report, General Ledger for the same time period can be opened.
  * Filtering by date, class etc.



Balance Sheet:

  * Has the ability to display amounts on 2 dates for easy comparisons.
  * Filtering by date, class etc.



General Ledger:

  * Has an option to display starting balance and ending balance to help auditors.



Journal Entries:

  * Filtering by date, class etc.
  * Clicking on the Account Name opens up the corresponding transaction detail.



Trial Balance:

  * Displays a message when there is a mismatch on amounts.
  * Takes to the general ledger directly for easy auditing.
  * Filtering by date, class etc.



Transactions:

  * Sub-pane helps to see the transaction lines without opening each detail.
  * Transaction details can be opened from the report
  * Supports “Duplicate transactions” for a faster data entry of repeating transactions.
  * Can be filtered down with interactive ask prompts.



Accounting Summary by Contacts:

  * Transactions linked to any contact are easier to find.



Bills:

  * Bills report displays all the accounts payable transactions at a glance.



Aging Bills:

  * The payables are grouped in different date ranges to get a clear idea about urgent payables.



  


Account Budgets:

  * Easy entry of budget amounts from an editable report which is similar to defined Chart of accounts.  
  * Allows entering total amount directly, it is automatically distributed to number of months.



  


Reconciliation:

  * An editable report helps to mark “C/R” to clear or reconcile transactions.
  * The running balance column helps comparing with the official statements.



  


Subtypes:

  * While creating a financial account, we can set up the subtype of the account.



  


Closing Accounting Periods:

  * When a period is closed the transactions become uneditable on and prior to that date.
  * Only permitted users can unlock a closing period.



  


Locking Accounting Transactions:

  * Support locking transactions so that users cannot edit transactions prior to locking date.
  * This is not exactly like closing. User with appropriate permission can unlock locking date.



  


Import / Export:

  * Supports importing accounts and transactions with the help of input file.
  * Has option to export all accounts and transactions to excel file.



  


Report Alerts:

  * If a transaction is in draft status for more than 15 days, a report alert pops up.



  


Miscellaneous:

  * Can be connected with the  “Accounts Receivable” module.
  * Can be connected with the “Invoicing” module.


