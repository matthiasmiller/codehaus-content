6.2. Financial Accounts

Coded in [[PC0078489]] - E00 - Accounting: Define Financial Account related Lookups

  


Heading Title:

[X] "New Account" until the record is saved

[X] <Financial Account Name> after the record is saved.

  


Fields:

[X] Name (string)

\- Editable if UseAccountNumber switch is false.

\- Uneditable and displays Account Number + Label if UseAccountNumber switch is true.

\- Shows a warning on change "Changing the account number will affect all historical accounting data."

  


[X] Active (checkbox) - By default True.

  


[X] Account Number (string) - visible if UseAccountNumber switch is true

\- Shows a warning on change "Changing the account number will affect all historical accounting data."

  


[X] Label - visible if UseAccountNumber switch is true

\- Shows a warning on change "Changing the account number will affect all historical accounting data."

  


[X] Sub-account of (choice report)

\- A choice report opens with all active accounts sorted as per the chart of account.

\- The selected account is set in FinAccountParent hidden field.

  


[X] Contra Account (checkbox)

  


[X] Type (drop list)

\- Displays the unchangeable list FinAccountTypes.

  


[X] Subtype (filtered drop list)

\- Filtered list of subtypes are displayed based on the selected "Type".

\- If the subtype of an accounts is Bank Accounts / Credit Cards, "Uses Reconciliation" checkbox is checked by default.

 

[X] Uses Reconciliation (checkbox)

\- If the subtype of parent accounts is Bank Accounts / Credit Cards, "Uses Reconciliation" checkbox is checked by default.

  


[X] Link with (drop list)

\- Visible if ConfigAcct_EnableAccountLinking is True.

\- Displays "FinLinkingReferencedRecords" list. This list has "Contact" as an element and this is overridden in Provident Fund catalog.

\- Coded in [[PC0098420]].

  


[X] Link Type

\- Visible if ConfigAcct_EnableAccountLinking is True.

\- Displays "FinLinkingTypes" list. This list is overridden in the following catalogs

AppHosting Provident Fund BD

CodeCrafters - CodeCrafters Admin [XCC]

\- Coded in [[PC0098420]].

  


[X] Linked Contact (choice report)

\- Visible if ConfigAcct_EnableAccountLinking is True.

\- Uses a choice report to display all contacts and set the contact in FinAccountLinkedContact hidden field.

  


[X] Description (string)

  


[X] Default Class (drop list)

\- Only active class list.

\- Coded in [[PC0086409]]

  


Client system fields:

In XLP

[X] Fund 

[X] Department

[X] Location

[X] Account Code - Added in [[PC0078683]]

[X] Sub-acct Code

In AppHosting Accounting Check Printing.txt

[X] FinAccountUsesCheckPrinting

  


RG fields:

[X] Budget related fields.

  


Child Details:

[X] Internal Fields(AHZ-only)

\- Visible only for developers.

\- Contains the fields regarding budget and order in chart of accounts.

  


Links:

[X] Budget

\- Open budget report

  


[X] Modification History

  


Validations:

[X] Coded in [[PC0114131]]

[X] "Length of account number must not exceed 20 characters."

[X] "Changing the name will affect all historical accounting data."

[X] "Changing the account number will affect all historical accounting data."

[X] "Changing the label will affect all historical accounting data."

[X] "Duplicate account numbers are not allowed."

  


[X] "Changing account name/number/label warns about affecting all historical data." But if we change the name/number/label back to the original before saving the changes made, we may skip warning about it.

[X] "This account cannot be deleted since this account has transaction(s)."

  


Client system validations:

[X] [[PC0114133]] - XLP - Consider warning on fund/dept/loc/code changes on financial account

 

  


Buttons:

[X] Document Archive

  


Report link:

[X] Accounting | Accounting Configuration | Chart of Accounts and then New Account.

  


Referenced:

[X] In Accounting Transactions record, we can select class in Transaction RG.

\- See Accounting Transactions on the left pane.
