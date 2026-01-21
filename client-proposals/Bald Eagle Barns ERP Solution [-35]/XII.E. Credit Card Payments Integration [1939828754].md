12.5. Credit Card Payments Integration

Tim Reitz 10/18/2021: This could be a future piece... 

  


BEB currently uses Authorize.net, which allows the drivers to process payments in the field, but they have not given dealers access to that account to process that.

  * Card Non Present - running at 2.25% + no per transaction
  * This is a significant increase, with the amount of dollars running through--the only reason for the low rate is because of the volume amount
  * Authorize.net and Stripe were the two that IdeaRoom worked with…



TODO_J: Is there just one Authorize.net account, or muliple?

Tim Reitz 08/10/2021: Jason thinks it's just one. He doesn't think we need to have more than one at this point, though it could be helpful in the future... 

  


DONE_CH: Look into integration with Authorize.net. Will it be worth it for them to do that integration and stick with A.net? Or will it be better to switch to Stripe?

TODO_TR: Very doable. It's probably better to stay w/ A.net for better rates. See

[https://developer.authorize.net/api/reference/index.html#payment-transactions](https://developer.authorize.net/api/reference/index.html#payment-transactions)

[https://github.com/AuthorizeNet/sample-code-python/blob/master/PaymentTransactions/charge-credit-card.py](https://github.com/AuthorizeNet/sample-code-python/blob/master/PaymentTransactions/charge-credit-card.py)
