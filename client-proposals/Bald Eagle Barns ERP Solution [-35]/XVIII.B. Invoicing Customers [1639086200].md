18.2. Invoicing Customers

TODO_TR: clean up/clear out

  


One invoice will be generated per Sales Order, and any payments toward the building (down payment, final payment, etc.) are applied to that invoice.

  


  


  


TODO_CH: Let's outline the process:

  * Sales Order created
  * Customer give down payment (Payment record created)
  * Receipt generated
  * Information pushed to QuickBooks and/OR? invoice printed from database



  


TODO_CH: What should be specced in this section? should more of it go to a new section under QB Syncing? or a new section? not sure of the distinctions/model here...

  


  


We  would not use the AHZ Invoices module. We simply push information to QB for the invoice to be created there.
