3.5. Reconciliation Report

The Solution would include a report that would prompt for:

  * A Plaid Account
  * A Payment Method
  * A Date Range (defaulting to the last 30 days)



  


Columns:

  * All columns from the record, except Plaid ID.
  * The report should visually differentiate items that are linked to a payment (such as with a green text color).



  


Selecting a transaction on the left would open a Payment record on the right. If a Payment record had already been created, it would re-open the existing Payment record. Otherwise, it should open a new blank Payment record, defaulting the Date and the Payment Method.

  


The Payment would show a link to "Bank Transaction" with a read-only "Transaction Total". The Payment would warn when saving with a different balance than the transaction.

  


To create the payment:

  * Select the Vendor from the list
  * Select appropriate Vendor Invoices
  * Save (confirming that the totals match)


