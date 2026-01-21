16\. QuickBooks Syncing

The software will sync with QuickBooks Enterprise Desktop.

  


All syncing starts by pulling information from QuickBooks, before attempting to push anything into QuickBooks.

  


Rosewood Rentals --

  * Do a "refresh" that basically pulls all the new data from QB back into the database, and it shows that QB is now satisfied.



Next step is to push Invoices from manufacturing to the sales company.

  * Multiple Line Items for the batch



Delivery to the sales company

  * Multiple Line Items for the batch



Sales company writes checks for those outstanding invoices.

  * This gets automatically created
  * Memo "Delivery Expense" with a Sales Order number
  * "Auto Generated check"
  * Split detail "MEMBER LABOR:SM" \- Memo "WEEKLY DRAW"
  * We need an employee setting to map to the right QB account.



  


Can sync employees

Can sync task payment over...

  * To Print checks in the ledger (what account does it get assigned)
  * "Member's Weekly Draw JD"
  * Memo field -- Weekly Draw
  * Biweekly -
  * For an LLC, the term is correct is to call it a "Weekly Draw" (even if it's paid biweekly)



  


  


  * When buildings are delivered, have a method to trigger invoicing process to pay Benchmark and BE Transit
    * TODO_CH: Tim Reitz 10/26/2021: They do a QB sync twice a week on all orders marked Delivered. On the invoice there should be a line item for each building (include SO #, Serial #, Sales Price, Due Amount) 



  


  


  


Tim Reitz 09/28/2021: Pay details for Dealers are not currently synced to QB, but Jason said it would be nice if it were synced. (would probably use the Dealer Code somehow)
