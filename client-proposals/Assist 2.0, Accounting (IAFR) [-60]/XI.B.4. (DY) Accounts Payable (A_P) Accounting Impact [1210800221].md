11.2.4. (DY) Accounts Payable (A/P) Accounting Impact

FGI Configuration:

  * Vendor Invoice section with:
    * Received Not Vouchered account (choice from list of accounts)
    * Accounts Payable account (choice from list of accounts)



  


Accounting Company record:

  * Add a section for "Vendor Invoices (Customized for InSight)". It should be an embedded spreadsheet of:
    * Vendor Invoice Payment Type (choice from list of VInvoicePaymentTypes)
    * Default Payment Account (choice from list of asset/liability accounts for the company)



  


Vendor Invoice:

  * Invoice Date (new field; required for new invoices?? TODO_JN)
  * Payment Account (defaulted based on the Payment Type; overridable; required if payment type or payment date is set)



  


Account Transaction:

  * Add a PO ID field to the line item (specified if generated via a PO)
  * Add a Vendor Invoice ID field to the line item (specified if generated via a Vendor Invoice)



  


Create a Purchase Order Accounting Impact report. It should have:

  * Company
  * Transaction Date (based on Reception Date for entering new PO, and based on Invoiced date to reverse the original transaction)
  * Account
  * PO ID
  * Existing Debit
  * Existing Credit
  * Expected Debit
  * Expected Credit
  * Difference Debit
  * Difference Credit



  


Create a Vendor Invoice Accounting Impact report. It should have:

  * Company
  * Transaction Date (based on Invoice Date for expensing it, or Payment Date for recording payments)
  * Account
  * Vendor Invoice
  * Existing Debit
  * Existing Credit
  * Expected Debit
  * Expected Credit
  * Difference Debit
  * Difference Credit



  


Here is the expected IMPACT at each stage:

  * PO Received But Not Invoiced
    * Debit - GL accounts for SKUs
    * Credit - Received Not Vouchered
  * PO at any other time
    * No Impact
  * A vendor invoice can have one or both of these impacts:
    * Vendor Invoice with payment
      * Debit - Accounts Payable
      * Credit - Accounts for Payment
    * Vendor Invoice Without PO, or with Received PO
      * Debit - GL accounts for SKUs
      * Credit - Accounts Payable
  * NOTE:
    * The PO accounting impact should exclude any additional expenses that are linked to a PO.
      * TODO_MM - Rewrite spec to reflect that landed cost should be expensed out under the original SKU.
    * Shipping, Tax, and Additional Expenses (not linked to a PO) are prorated on a per-SKU basis. Be sure to handle discrepancies based on rounding (simply apply the difference to the account with the largest dollar amount.)



  


Both of these need imports that run nightly to push to the accounting system. Model these after the Building Accounting Impact report. Consider including all of these in a single x30list that triggers all accounting impact syncs.

  


Provide a menu option to manually push changes to accounting.
