30.4.0.1. (MM/MT/JN) Accounts Payable

  


Requirements

Matthias Miller 08/10/2023: This has been documented elsewhere.

  


Company-Wide Accounting Setting (existing)

  * Default Payables Account
  * Default Payment Account (i.e. checking)



  


On the SKU:

  * Embedded spreadsheet of:
    * District (list of districts)
    * %
    * Account (list of accounts for that district)
  * Validate that the % adds up to 100



  


Purchase Order:

  * Add a "GL Account Override" on the PO
  * Add the following fields:
    * Shipping
    * Tax
    * Discounts
  * Add a "Mark Complete" button that
    * Sets the status to "Complete"
    * Creates an accounting record with appropriate debit/credits (TBD)
  * Add a "Mark Incomplete" button that voids the accounting record and reverses the status from Complete



  


  * Additional Expenses / Freight / Taxes need to be distributed to the accounts for each of the SKUs



  


  * Landed Freight goes to Raw Materials asset account



  


Vendor Invoice:

  * Move the following fields to the PO
    * Shipping
    * Tax
    * Discounts
    * "Include" checkbox (turns into 0 received)
    * Received
    * GL Account Override
  * The Line Item RG turns into a "Purchase Orders" RG. (ONLY show complete purchase orders)
  * Add a "Payment Date" field
  * Add a "Payment Account" field (defaulted to district Default Payment Account)
  * Add a button to "Mark Complete" that would mark it as paid and create linked accounting record
  * Add a button to "Mark Incomplete" that would void the linked accounting record



  


TODO_HLD

  * How to split out GL account (could use a linked RG)
  * How to handle landed freight / freight invoices



  


Development Specification

Dev Spec:

  * Some of these fields are contingent on the accounting module


