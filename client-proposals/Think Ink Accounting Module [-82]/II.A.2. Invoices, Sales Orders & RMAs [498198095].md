2.1.2. Invoices, Sales Orders & RMAs

  


Requirements

The Solution will use the standard Invoices feature. An invoice can be one of three subtypes:

  * Sales Order
  * Invoice
  * Return Merchandise Authorization



  


Sales Orders & Invoices: 

  


The Sales Order record will be converted into an Invoice by specifying an Invoice Date. This allows deposits / payments to be included on the same record.

  


Return Merchandise Authorization (RMAs): 

  


The Solution will include an option to create a new RMA. When the Contact is selected on the RMA, it will show an embedded spreadsheet of returnable items and their remaining quantities. It will show:

  


  * Return (checkbox)
  * Date (reverse sort)
  * Invoice Number
  * SKU
  * Description
  * Qty
  * Price



  


Clicking the "Return" checkbox will add the item with a negative entry to the itemization spreadsheet.

  


The itemization spreadsheet should also show a "Return Reason", which would be a configurable list of return reasons. This would also show a Return Fee % and a Return Fee $ column for each line items. The subtotal and totals in the RMA would show a negative amount.

  


The RMA will have an "Approved" or "Received" checkbox/date to turn the RMA into a credit that adjusts the customer balance.

  


Business Process: For reference, here is the Think Ink Customer Returns process:

  


RRA (return merchandise authorization)

Customer Returns-current process

  


1\. Customer reaches out to Think Ink to return an item.

  


2\. Think Ink issues an RMA (currently just being done using an incident in apphosting with whatever notes are

needed. Return reason, etc). Ideally a list from customer's previous invoices could be populated and picked

from. And also a reason for return from drop list.

  


3\. Customer returns product with RMA No included

  


4\. Customer credit memo is then created from notes found in RMA incident (ideally the RMA incident would be

linked or converted to the credit memo somehow)

  


5\. A return fee is applied on a per line item basis, this should be manual as it varies on a per case basis on the

amount. It is typically a % and not a set $ amount

  


6\. RMA incident is closed.

  


7\. Customer is credited back in either direct payment form or credit to account.

  


Development Specification

TODO_IDD - We need to exclude sales orders from sales reports.
