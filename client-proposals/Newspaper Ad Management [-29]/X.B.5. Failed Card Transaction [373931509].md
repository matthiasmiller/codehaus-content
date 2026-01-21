10.2.5. Failed Card Transaction

  


Requirements

If a card transaction fails for a payment on an invoice that was individually run, the system will leave the invoice as Invoiced and wait to mark the invoice as Paid until the card transaction clears.

  


For batch charging, the system will tell Stripe to charge the cards. As charges come back cleared, it will mark the the corresponding invoices as Paid.

  


If a transaction fails, the system will auto-create a Task to alert the users that the transaction failed and that they need to follow up on it. This new Task should have the following fields filled: 

  * Task Name (set to "Failed Card Transaction")
  * Customer (set to corresponding customer)
  * Publication Date (set to current publication date) 
  * Assignee (set to Unassigned )
  * Comment (set to "A transaction for Invoice <#> for <Customer Name> has failed. Please follow up accordingly."; include the link to the invoice if possible)



  


Development Specification

We could create a macro for SalesFormURL.
