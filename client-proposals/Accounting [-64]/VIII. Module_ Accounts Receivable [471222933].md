8\. Module: Accounts Receivable

[[PC0107178]] - Accounting: Accounts Receivable Module

  


See also [[PC0107891]] (Accounts Payable).

  


Overview

We currently have a robust stand-alone invoicing module that we would like to tie into our accounting system with an Accounts Receivable module. 

  * It will facilitate the creation of accounting transactions and the noting of their ties to invoices.
  * It will make it easy to see what the transactions for a given invoice are, and when there’s something surprising about the related transactions.



  


Data model

The Invoice doesn’t store any information on itself about what accounting transactions have occurred. In a system that integrates invoices and accounting transactions, the invoice status will be used for controlling the workflow for linking with accounting transactions. When linked with accounting transactions the invoice status will be restricted- can be changed by accounting users mostly.

  


Accounting transaction lines will include a LineItemInvoice field, which will store the invoice ID. A transaction that links to an invoice ID can’t be deleted; neither can an invoice that has transactions referencing its ID. However, the invoice ID is editable. \--[[PC0107890]]

  


Accounting transaction lines will also record amounts in the appropriate account of various types- income, accounts receivable, cash/bank, etc.

  


Sales item record will have a new "Income Account:" drop list of income accounts. This is visible if the income account logic (which can be specified in AppHosting settings) is set to "From Sales Item" in the invoicing settings. In the future, we may support multiple accounts, but right now it will require customization. \--[[PC0108162]]

  


Accounting

Following is a summary of how transaction line entries are created related to an invoice:

  * Income: Credit the "Sub Total" amount to an income account, either at the time of payment (immediate) or at the same time it is recorded in accounts receivable. The income account may be a common account, or different accounts based on the sales item, or it could be customized.
  * Accounts receivable: Debit the invoice total cost when recording accounts receivable (without recording payment) or recording an initial payment to a financial account of type "Asset" and sub-type "Accounts Receivable". Credit the amount paid when recording a payment of any amount.
  * Received payment: Debit the amount paid to a financial account of type "Asset" and sub-type either "Cash Accounts" or "Bank Accounts".
  * Sales discount: Debit the amount in a contra revenue account. [[PC0109421]]
  * Sales tax: Credit the amount to a financial account of type "Liability" and sub-type "Sales Tax Payable". [[PC0108586]]
  * Uncollectible accounts: Amount attributable is the amount that won't be received from the client after the goods were delivered on credit. See [https://www.accountingcoach.com/blog/what-is-bad-debts-expense](https://www.accountingcoach.com/blog/what-is-bad-debts-expense). Right now this requires a manual tie out of accounts by the accountant.
  * Overpaid amount: Though not expected, but the user would be able to enter an amount exceeding the actual invoice total cost via the create payment transaction prompt, or directly in the transaction screen. If done so, the accounting transaction record will end up out of balance and will need to be manually tied to correct accounts. This will also show up in the exception report.



  


Reporting and linking

<n> Linked Transaction \--[[PC0107896]]

Add a link on the invoice record "No Linked Transactions" / "1 Linked Transaction" / "3 Linked Transactions", that shows all the transactions linked with this invoice. This will also be available from the (+) button from the invoice cockpit.

  


Main Invoice Cockpit

The Invoices report will be the primary interface for taking “accounting-relevant” actions with invoices. Actions like issuing an invoice, entering payment etc will be tied to the context menu in the report; the actions will also be on the invoice detail screen. But for the first release, we will do all the actions from the invoice detail screen.

  


The invoice report will become a multi-pane report, similar to incidents. 

  * The left pane will have the following options- Open Invoices, Closed Invoices, All Invoices, Recent Invoices, Recent Transactions.
  * The current invoices report will become the child pane and the search link will run the child report prompting for asks.



  


Recent Invoices

Group by something like “1 day / 2 days / 3 days / last week / last month”, sorting by modified date. We might tap into activity history for this, or start storing modified dates on invoices.

  


Recent Transactions

Use conditionally visible sub-panes in the left pane for this. Group similar to the above. It should show accounting-transaction line items and invoice numbers.

  


Exception report

We'll add an exception report to show the invoices where accounting transactions don't tie out with the invoice status and similar things. [[PC0109283]]

  


Processes

Invoices will continue to have four different possible states: Draft, Cancelled, Invoiced, and Paid. However, in the invoice cockpit report accounting users will see additional group "Paid (not recorded in the accounting system)", if there is any invoice like that.

  


Recording payments for an invoice

When an invoice is issued (marked as Invoiced), or paid (marked as Paid), user will have ways to run processes to create linked accounting entries. These processes will be accessible from either an "Accounting Transaction" section on the invoice detail screen (or from the invoice cockpit later). The processes can be run by users with appropriate accounting permission.

  


If an invoice is marked as "Invoiced", the following links will be visible: Create Accounts Receivable Transaction ([[PC0108358]]) and Create Payment Transaction ([[PC0108359]]). If an invoice is marked as "Paid", the only option available is Create Payment Transaction. Ideally we'd have wished for this [[PC0095850]] and as soon as the status was changed, we would want the relevant transactions be created but for now we wish to go ahead with the two step process of changing the status and clicking on the buttons to create transactions.

  


If an invoice is "Cancelled" or changed back to draft, user will need to void the linked transactions first. We won't lockdown the record, but will show appropriate warnings if the user wants to mark invoice cancelled without first voiding the linked transactions.

  


Let's add an "Accounting Transactions" section to the right of the invoice detail screen. We will show report/import links to transactions etc in this section. This section should be visible to users with accounting permissions if there are linked transactions and status is invoiced/paid. This section will also provide a high level accounting summary.

  


Permissions

New "View Invoices" and "Edit Invoices" permissions will be added for the invoicing module [[PC0108587]]. While users with the invoicing permissions and "Edit Accounting Data" permission will be able to create the transactions for invoices, a user with invoices plus "View Accounting Data" permission will be able to view transaction related information.

  


In a linked accounting system, users who do not have permission to edit accounting data will not be able to change invoice status from Paid to anything else, or Invoiced to Draft/Cancelled once the record is saved. Users with edit accounting data permission will be able to do so, but we will show warnings/instructions to void transactions before doing that. [[PC0108857]]

  


Settings

There will be a system switch ConfigInvoice_LinkAccounting that is true if invoicing is linked to the accounting system. It's only available with the accounting module installed. \--[[PC0107857]]

  


We will have the following AppHostingSettings (Advanced | Admin | AppHosting.zone Settings). These settings can only be modified by users with accounting permissions.

  


Invoicing Settings [[PC0107895]], [[PC0108112]], [[PC0108491]], [[PC0108692]], [[PC0109468]]

  


Income Account Logic: Options for "Use Single Account", "From Sales Item", and "Customized Logic". 

Income Account: Drop list of income accounts (treated as "Default Income Account" if not "Use Single Account")

  


Accounts Receivable Account Logic: Options for "Use Single Account", and "Customized Logic".

Accounts Receivable Account: Drop list of A.R. accounts. In the future, we may support multiple accounts, but right now it will require customization.

  


Default Cash / Bank Account: Drop list of asset accounts of sub-type "Bank Accounts" or "Cash Accounts".

  


Sales Tax Payable Account: Sales taxes will be attributed to this account. This is a liability account of "Sales Tax Payable" sub-type.

  


Sales Discount Account: This is a contra revenue account, used for creating accounting transaction entries for sales discount. Sales discount on invoices can be turned on using system switch.

  


Late Fee Account: This is an income account. Late fees on invoices can be turned on using system switch.

  


Future Enhancements

[[PC0110209]] - Accounts Receivable: Future enahancements
