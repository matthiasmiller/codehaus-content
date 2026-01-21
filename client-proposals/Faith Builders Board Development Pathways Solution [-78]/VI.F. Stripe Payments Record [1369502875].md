6.6. Stripe Payments Record

  


Requirements

The Solution will support receiving credit card payments, probably using AppHosting's existing Stripe Payment records. 

  


The Solution also should be able to record and track payments via check. 

  


The Stripe Payment records include fields such as: 

  * Charge Details: 
    * Stripe Charge Type
    * ID
    * GMT Date
    * GMT Time
    * Source
    * CC Last 4
    * Amount
    * Description
    * Complete
    * Stripe ID
    * Success
    * Error Message
    * Customer ID
  * Customer Details: 
    * Type
    * Stripe Cust Num ID
    * Name
    * Invest ID
    * Token
    * Type
    * Last 4
    * Active
    * Stripe ID



  


Additional details to be determined in IDD.

  


Development Specification

TODO_IDD: Tim Reitz 08/22/2023: See the following details for Stripe records: [https://docs.google.com/spreadsheets/d/1HS_KLdkXaa436p-VEmFPIsu9FGEpcRM2/edit#gid=365509092](https://docs.google.com/spreadsheets/d/1HS_KLdkXaa436p-VEmFPIsu9FGEpcRM2/edit#gid=365509092).

  


  


DONE_SB: Tim Reitz 08/22/2023: Do you want to be able to accept payment via cash or check as well as card? If so, we'd need to think through an invoicing process, how to follow up, etc. 

Ben Reitz 08/23/2023: Sent an email today.

Ben Reitz 08/23/2023: From the client: Yes. Check and Card. Don’t think cash is necessary.

DONE_SB: Tim Reitz 08/29/2023: How would you like to handle the check purchases? Idea:

  * In sign-up process, give option for Payment Type (Card / Check)
  * If Card, proceed as we've discussed
  * If Check,
    * Allow Rep to set up the account and view subscription, but subscription isn't active yet (no lessons sent, no content viewed)
    * Send an "invoice" instead of a receipt
    * Rep writes and sends a check
    * When FB receives and processes the check, the subscription is unlocked/activated and the receipt and welcome member



TODO_IDD: Tim Reitz 09/11/2023: Ben emailed on 9/7 ("Final touches on your High-Level Design"), and client was fine with this approach. 

_MM: Tim Reitz 08/22/2023: Can they use these same records for collecting other payments (cash, check)?

TODO_IDD: Tim Reitz 08/29/2023: Matthias would not use the same records. Probably just use the Payments RG on the Subscription.
