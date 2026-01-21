12.5.4. Export Transactions

Jobs:

[[PC0110011]] - Accounts Receivable: Enhance standard transaction import/export

  


Report:

[X] When this link is clicked, an excel with all account related info gets downloaded immediately.

[X] Level: Accounting Transactions.

[X] Excel export

[X] In browser: Download only

  


Menu link:

[X] Accounting | Accounting Configuration | Data Import / Export | Export Transactions

  


Title:

[X] Export Transactions

  


Ask Prompt:

[ ] Report Period

[ ] Export Purpose:

Export purposes

1\. View database fields: Exports the system ID's and match keys as stored in the database. Useful for simply viewing data.

  * This will export both the transaction system ID and the match key as it is stored in the database.
  * The standard import can't import from this, see notes below for how the import works.



  


2\. Duplicate (any database): Generates a random match key so that a new record is created on import.

  * This will not export the system ID.
  * It will export a generated match key in this format: "Duplicate:<Transaction System ID>:<RandomCharString(8)>, e.g., Duplicate:1203:WELKSDE2



  


3\. Sync to other database: Exports transactions for another AppHosting database. Generates a match key based on the "Transaction export match key prefix".

  * This will not export the system ID.
  * It will export a match key in this format: <ConfigAcct_TransExportMatchKeyPrefix>:<Transaction System ID>, e.g., SourceSystemID:1203.



We'll add a ConfigAcct_TransExportMatchKeyPrefix system switch that defaults to "SourceSystemID" but may be changed.

  


Columns:

[X] Match Key

[X] Transaction Date

[X] Transaction Status

[X] Transaction Reference

[X] Transaction Contact

[X] Transaction Description

[X] Line Item Account Name

[X] Line Item Contact

[X] Line Item Debit

[X] Line Item Credit 

[X] Line Item Class

[X] Line Item Notes

[X] Transaction Supporting Details

[X] Reconciliation Status

[X] Line Item Linked Invoice #

NOTE : Company ID column was added while coding Accounting Companies feature.

  


Sorting:

[X] Transaction Date + Transaction ID
