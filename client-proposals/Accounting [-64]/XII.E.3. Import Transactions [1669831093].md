12.5.3. Import Transactions

Import process:

  * The import of accounting transactions requires that all the financial accounts are imported beforehand.



  


Jobs:

[X] [[PC0110011]] - Accounts Receivable: Enhance standard transaction import/export

  


Input file:

  * We can import accounting transactions in our system.
  * For this we need to have an excel input file with the following columns



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

  * We do not import linked invoice ID if invoice linking is not enabled. See ConfigInvoice_LinkAccounting.
  * If Transaction Status is blank in the input file, we set the default transaction status of the system and continue importing.


