12.2. Customer Refunds

*These probably are the corollary of Payments.

  


Fields

  * Link to a payment + invoice 
  * fields similar to or same as Payments



  


  * These get pushed into QB as checks to be printed, or a CC charges to be processed. Note that for CC charges, these should be tied to the original payment.



  


Needs to create a Credit Memo in QuickBooks to reverse the original item.

Then, needs to optionally issue a check for the balance. This could let us keep the balance in the system.

  


TODO: Can we limit refunds to part of one payment on one invoice? (e.g. if a customer paid 5 invoices in full and need partial refunds on all of them, is it OK to run 5 separate refunds?).

Tim Reitz 10/07/2021: presumably this is how it would be.

  


  


DONE_CH: should we have an alert when a Refund is created? or will the syncing take care of that?

TODO_TR: What kind of alert?
