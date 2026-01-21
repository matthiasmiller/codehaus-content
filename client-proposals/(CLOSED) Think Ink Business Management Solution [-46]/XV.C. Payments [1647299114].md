15.3. Payments

  


Requirements

TODO_NM: Tim Reitz 08/12/2022: This is pending further discussion between Matthias/Josh, and might be deferred until after some other items. 

  


  


DONE_JM: How do you want recurring payments to work? What would it be used for? Something like auto-refill?

DONE_CH: Tim Reitz 04/13/2022: This would be for storing card information to do auto-payments. 

Matthias Miller 04/25/2022: This would be in the form of tokens, not actual card information, FWIW.

They are currently using EvoPayments. They're looking to switch. 

DONE_CH: Could we run other payments through this? (to replace their current processing; basically have a standalone Card Payments interface here that is used for things here and outside) Can we run a standalone payment without an invoice, etc.? 

DONE_CH: Any other preferred processors besides Stripe? 

DONE_TR: I think Stripe is a reasonable place to start, although I'm interested (separate discussion) in having a backup processor that we integrate with. If we use the Payments module, yes, we could have a way for them to do one-off charges. We'd have to confirm what it looks like. See [https://stripe.com/pricing](https://stripe.com/pricing)

Tim Reitz 05/03/2022: They are open to using Stripe. However, the client also said the following: "the processor we were looking at switching to uses [https://www.nmi.com/](https://www.nmi.com/). I believe our rates would be a bit cheaper so the development would have some value to us, but I guess see what your team thinks and we’ll go from there."

Tim Reitz 05/04/2022: Client also said, "Regarding the processor, looking at NMI I believe we would be using a 3rd party as it doesn’t seem as if they are a processor themselves??? I can dig into more if I know what questions to ask or Curvin Martin at [curvin@crystalclearmc.net](mailto:curvin@crystalclearmc.net) is the contact."

Tim Reitz 05/04/2022: 

  * It looks like there are some restrictions with NMI for integration.
  * For recurring/automatic payments, it appears that the customer must be physically present for the first transaction or they must enter card information through a website. At the least, this would require more research to determine how it would play out (e.g. can the customer give the card info to Think Ink over the phone and have Think Ink enter it online, etc.).
  * The integration with AppHosting might be through authorize.net (could use any cc service; has its own fees in addition to the processor's; see [https://www.authorize.net/en-us/sign-up/pricing.html](https://www.authorize.net/en-us/sign-up/pricing.html))
  * Developing a new integration could cost $5K-10K.
  * *Connect with Curvin:
    * *Find out what kind of account Think Ink needs
    * *Find out what the pricing would be
    * *Compare with Stripe, consider cost of development + gateway



Tim Reitz 05/05/2022: Sent email today.

Tim Reitz 05/11/2022: Client is fine with using Stripe. 

  


TODO_JM: what do you want in the payments? 

TODO_JM: automated & manual or just manual payments? we're hesitant to do fully automated at this point. maybe batch charges. 

TODO_JM: If automated, how do you want it to work? 

TODO_JM: how do you want refunds to work? 

TODO_TR: Per Matthias, would be to select a payment and choose whether to refund all or part of it. 

TODO_JM: right that sometimes tied to an invoice, sometimes not? 

  


  


TODO_TR: use existing AHZ payments feature, build off of that; add

  * Payment record 
  * Create a Payments Portal - Select a customer or open from a customer
  * Select Payment options/methods
  * Run charge 



  


Have a a Stripe transactions report that can filter by Contact and by Date

  


  


Other Notes: 

  * The Solution would not store credits (would not function as a virtual wallet for contacts). 
  * The Solution should be able to process refunds



  


Development Specification

Tim Reitz 05/04/2022:  [https://secure.nmi.com/merchants/resources/integration/integration_portal.php#credential_on_file_information](https://secure.nmi.com/merchants/resources/integration/integration_portal.php#credential_on_file_information)

When a customer is actively engaged in checkout - either physically present in a store, or checking out online in their browser, that is a Customer Initiated Transaction (CIT).

  


When the customer isn’t actively engaged, but has given permission for their card to be charged, that is a Merchant Initiated Transaction (MIT). In order for a merchant to submit a Merchant Initiated Transaction, a Customer Initiated transaction is required first.
