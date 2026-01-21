4\. Credit Card Processing

  


Requirements

We would like the ability to have credit card processing available within the app.

  


We will have the option to store cards on each customer. (For privacy purposes, we will not store the actual card number.) We will be able to deactivate old cards, as well as show the most recently used card.

  


When processing a credit card, we will automatically add a Credit Card Convenience Fee to the invoice to cover the credit card processing cost. We will automatically enter the credit card payment into the accounting system. This allows the fees to be tracked under separate income/expense accounts.

  


Development Specification

Talk to Josh, but I think we:

  * Capture the card
  * Save it to the database
  * Finalize the charge



Then, we can link to Stripe for them to confirm if there's an issue.

  


  


Matthias

This needs more speccing.

  


  


\---

  


Matthias Miller 01/22/2020: Rarely do they pay with a physical credit card.

  * We could pass on the fee to the customer.
  * Add a credit card fee -- to the end.


