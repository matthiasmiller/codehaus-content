2.3. Purchase Orders

  


Requirements

The Solution will use the standard Purchase Orders with some changes:

  


  * Add a "Drop Shipping" checkbox. When checked, this will show a Ship To that is a list of contacts, instead of SKU Lots.



  


  * Add an option to email these to the vendor. The email subject will simply read "Purchase Order #[ID]" with contents of "Please see the attached purchase order #[ID]". It will attach a PDF of the purchase order



  


  * Add a "View Emails" link that shows all External Actions for emails with the PO ID in the subject line.



  


The Purchase Order will have two additional columns to link it back to the sales order:

  * Sales Order ID
  * Sales Order Line Item ID



  


  


The Sales Order will have an option to generate a Purchase Order that will:

  


  * Create a new purchase order with a PO ID that is "SOID-AUTONUMBER". For example, if you have a sales order 1453, the first PO for that will be "1453-01", the second one "1453-02", etc.



  


  * For each line item, calculate the Qty issued through a PO, and add any line items that have a remaining quantity that have not been sent to a PO.



  


  * Do not allow deleting lines from sales orders that have a linked PO.



  


Development Specification

TODO_IDD - Make sure Josh is on track to get rid off legacy organizations in ZFP / Inventory Management.
