7\. Module: Accounts Payable

Types of Payables:

Accounts payable are debts that must be paid off within a given period to avoid default.

Common short term Payables are

  * Payroll costs 
  * Business income taxes
  * Short-term loans. 



  


Long-term debts include 

  * Lease payments 
  * Retirement benefits 
  * Individual notes payable



  


Trade payables constitute the money a company owes the vendors for inventory-related goods, such as business supplies or materials that are part of the inventory.

  


In our system:

Accounts Payable bills will simply be transactions with some extra fields filled. The summary of the process is as follows.

  


Menu Location:

In the Accounting tab there is a section "Accounts Payable". This has items

  * New Bill
  * All Bills
  * Aging Bills



  


New Bills report link:

[X] This runs an autopush report that has the following items in the ask prompt

[X] Bill date

\- This is a required prompt with Today as default value.

\- This sets the transaction date in the transaction record.

  


[X] Due date (optional)

\- This sets the Due Date in transaction detail, Accounts Payable section 

  


[X] Payee (optional)

\- This is a drop down of all contacts and organizations (both active and inactive).

\- This sets the Contact in the transaction detail

  


[X] Amount

\- Sets the amount for the credit account

\- This entry is required.

  


[X] Accounts payable account

\- Drop list of all liability type of accounts with subtype of "Accounts Payable".

\- Only active accounts are displayed in the list.

[X] If "Accounts Payable Account" is set in the AppHosting.zone Settings.

\- This drop down is hidden when there is only 1 payable type of account in the Chart of Accounts.

\- If there is more than 1 payable type of account then the default is the account from AppHosting.zone settings.

[X] If there is no active payable account in the chart of accounts, then a label is displayed at the bottom saying "* There is no Accounts Payable account in the chart of accounts."

  


The process of adding bills:

[X] Clicking on the New Bill link opens an ask prompt.

[X] When the answers are provided and Continued, it runs an autopush report that creates a new Transaction record

[X] In transaction record the following fields are set as per the ask answers

[X] Date - from the Bill date prompt.

[X] Contact - from the Payee prompt.

[X] Transaction Lines -> Account Name - from AppHosting.zone "Liability Suspense Account".

[X] Transaction Lines -> Debit - from the Amount prompt.

[X] Transaction Lines -> Account Name - from the "Accounts Payable Account" prompt.

[X] Transaction Lines -> Credit - from the same Amount prompt.

[X] Due Date - from the Due date prompt.

  


[X] In transaction detail there is a new section "Accounts Payable" is visible if a bill is created from this link.

  


[X] Accounts Payable section is visible whenever there is a transaction row and a credit amount for a financial account that is of type Liability and subtype Accounts Payable.

  


[X] Also there is a New Bill button to add a bill in the All Bills report.

  


Process of repayment:

NOTE: In Multi-company accounting system this process would not work until we can set the Company somehow.  

[X] To pay a due bill the user can choose any of the following processes.

[X] Run Accounting | Accounts Payable | All Bills report.

\- This report displays all the bill records that have a due amount

[X] Open the transaction detail from Transaction ID column.

[X] In the transaction detail press the "Record Payment" button.

\- This open the Create Payment Transaction autopush report.

[X] This report has the following ask prompts

[X] Bill ID

\- Bill ID is set from the detail screen.

  


[X] Payment date

\- Required, default is Today

  


[X] Payment amount

[X] Pay from account

\- Displays a list of all active accounts of Asset type which have a subtype "Cash Accounts" or "Bank Accounts".

\- Default is "Default Cash / Bank Account" from the AppHosting.zone settings.

  


[X] Accounts payable account

\- Drop list of all liability type of accounts with subtype of "Accounts Payable".

\- Only active accounts are displayed in the list.

[X] If "Accounts Payable Account" is set in the AppHosting.zone Settings.

\- This drop down is hidden when there is only 1 payable type of account in the Chart of Accounts.

\- If there is more than 1 payable type of account then the default is the account from AppHosting.zone settings.

  


[X] Clicking continue would create a bill payment transaction.

[X] User can also manually create a transaction and provide a bill ID to create bill payment transaction.
