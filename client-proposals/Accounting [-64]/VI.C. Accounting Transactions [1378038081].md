6.3. Accounting Transactions

Heading Title:

[X] "Transaction" until the record is saved

[X] "Transaction #<Number>" after the record is saved.

  


Fields:

[X] Date - Default Today.

  


[X] Reference - text field.

  


[X] Status - (drop list)

\- AccountingTransactionStatusList, consists of "Draft | Posted | Voided".

\- When ConfigAcct_AllowDraftTransactions is false, the list is "Posted | Voided".

  


[X] Contact (drop list)

[X] Added in [[PC0113718]]

[X] Returns list of active contacts and organizations.

[X] If you select a contact but have no items in the RG, the first row should default to that.

[X] If all the rows in the RG are the same (ignoring blanks), the main detail screen should update to that.

[X] If the rows in the RG are different, the main detail screen should indicate that. (Test switching back from multiple to single via the main screen, as well as by editing the RG items.)

[X] If all the rows in the RG match, new RG rows should default to that contact.

[X] If the rows do not match, new RG rows should default to blank.

  


[X] Description (string)

[X] Due Date

[X] This is visible only for billing transactions.

  


Hidden Fields:

[X] AcctTransactionUniqueID Coded in [[PC0114847]] - Add a transaction unique ID

[X] This was added while coding Bill feature.

  


RG fields:

Transaction Lines

[X] Account Name - drop down

[X] Debit - number. This is auto-filled if the prior row has a Credit amount.

[X] Credit - number. This is auto-filled if the prior row has a Debit amount.

[X] Class - Drop list

[X] Notes

[X]  *

[X] See [[PC0112451]] - Accounting: Add job tracking module

  


MRG Fields:

[X] Account Name 

[X] [[PC0101085]] - Add choice report to select account in transaction screen

[X] [[PC0108521]] - Ask prompts for the choice report

  


[X] Contact

[X] Debit

[X] Credit

[X] Class

[X] Notes

[X] Bills ID

[X] Visible for bill type transactions.

[X] Reconciliation

[X] Invoice #

[X] Incident ID

[X] Coded in [[PC0112451]] - Accounting: Add job tracking module

  


Child Detail:

[X] Imported Line

[X] This is visible if transaction were imported in the system.

[X] This is visible for users with "Can view diagnostic accounting data" permission.

[X] Coded in [[PC0110011]]

  


Supporting Details section:

[X] Memo

  


Match Key

[X] This button is visible if user has "Can view diagnostic accounting data" permission.

[X] See the Transaction Export from the left pane, for more on Match Key.

  


Internal Fields (AHZ-only)

[X] Child detail that is visible in developer PC (~HasOfficialSource).

[X] Affected Accounts

[X] Affected Bills

  


Buttons:

[X] Document Archive
