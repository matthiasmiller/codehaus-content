17.1.2. Sales Orders

  


Requirements

All customer sales orders are pushed from the database into QuickBooks.

  


The invoice is linked to the customer. It has a few summarized line items:

  * Taxable line for all taxable items
  * Non-taxable line for all non-taxable items



  


The line item should be formatted as "CUSTOMER NAME: SERIAL NUMBER" with a quantity of 1 and the specified amount.

  


It should also set the tax code based on the sales order.

  


Development Specification

Add system switches for:

  * Sales Order Taxable Item Code
  * Sales Order Non-Taxable Item Code


