15.3.1. Payments Dashboard

TODO_NM

  


The Payments dashboard will have a screen that prompts for Contact, with a list of all (active?) contacts.

  


Selecting a Contact will show a list of payment methods. Each payment method will show:

  * The last 4 digits of the card
  * The expiration date
  * A button to mark the card as the default payment
  * A button to delete the card
  * A button to update the expiration date



  


It will also show a list of payments with:

  * Date (most recent first)
  * Amount
  * Button issue a refund (will prompt to a refund amount, defaulting to the full amount)



  


TODO_TR: We could add support for Stripe subscriptions, but I'm leaning towards waiting for automation until we can do precise billing, OR using the Quick Transaction Report (new name welcome).

  


TODO_TR: If we want to take payments from multiple sources, we could eventually enhance this to prompt for an invoice number, then store the CC payment on the invoice, as well as provide options to receive a cash / check payment.
