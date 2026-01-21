11.1. New Bill

See "Module: Accounts Payable" on the left pane for more details of the feature.

  


Accounts Payable Module was coded in [[PC0107891]] - Accounting: Accounts Payable Module

  


Overview:

  * This is a quick link to create a bill type transaction record. This uses an autopush report for that.



  


Jobs:

  * Initially coded in [[PC0114896]] - Accounts Payable: Create bill
  * Changed the design to use New Detail button was coded in [[PC0115146]] - Accounts Payable: New bill should open a detail screen
  * Later some tweaking was done in [[PC0115768]] - Accounts Payable: Tweak create bill feature



  


Report:

[X] An autopush report that opens a transaction detail screen with some fields filled up as per ask answers. An user may modify the transaction detail and save the record.

[X] Level: None

  


Menu link:

[X] Accounting | Accounts Payable | New Bill

  


Ask Prompts:

[X] Bill date

\- This is a required prompt with Today as default value.

\- This sets the transaction date in the transaction record.

[X] Due date

\- This sets the Due Date in transaction detail, Accounts Payable section. 

[X] Payee [drop list]

\- This is a drop down of all contacts and organizations (both active and inactive).

\- This sets the Contact in the transaction detail

[X] Amount [number]

\- This is a required prompt.

\- Sets the amount for the credit account

[X] Accounts payable account [drop list]

\- Drop list of all liability type of accounts with subtype of "Accounts Payable".

\- Only active accounts are displayed in the list.

[X] If "Accounts Payable Account" is set in the AppHosting.zone Settings.

\- This drop down is hidden when there is only 1 payable type of account in the Chart of Accounts.

\- If there is more than 1 payable type of account then the default is the account from AppHosting.zone settings.

[X] If there is no active payable account in the chart of accounts, then a label is displayed at the bottom saying "* There is no Accounts Payable account in the chart of accounts."

  


Title:

[X] Create Bill Transaction

  


Buttons:

[X] New Transaction - Autopush button that sets the following fields in the transaction detail

[X] In transaction record the following fields are set as per the ask answers

[X] Date - from the Bill date prompt.

[X] Contact - from the Payee prompt.

[X] Transaction Lines -> Account Name - from AppHosting.zone "Liability Suspense Account".

[X] Transaction Lines -> Debit - from the Amount prompt.

[X] Transaction Lines -> Account Name - from the "Accounts Payable Account" prompt.

[X] Transaction Lines -> Credit - from the same Amount prompt.

[X] Due Date - from the Due date prompt.
