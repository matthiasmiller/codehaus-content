# http://www.rtopro.com/help/processing_transaction_as_credit_card_without_charging_a_card.htm

# Processing a Transaction as Credit Card without charging a card

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Processing a Transaction as Credit Card without charging a card

|  [](help_desk_contacting_x-charge.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](download_update.md "Next Topic")  
---|---  
  
When performing a credit card purchase from the Tendered screen (F6 from Payment), you'll see a window that looks like this:

![CC purchase](hmfile_hash_f3b8bc58.png)

Here you can swipe or enter manually the credit card info and complete a transaction. However, if for any reason you hit the "Cancel" button on the bottom, you will see this:

![CC purchase cancel](hmfile_hash_d70f425c.png)

If you click "Yes", no charges will be processed through Xcharge but the transaction will complete. This will show up in payment history (F12 from Payment) and will say "NotXcharge" in the check number field. This means the customer was credited for the transaction but no charge was processed at the time through Xcharge, but you have given the account a credit of whatever the payment amount was.

If you click "No", the transaction will not close and you may proceed with a different payment method.

This feature can be used anytime you need to flag a transaction as a credit card payment but do not want to charge their card, for instance you may have already charged their card directly through Xcharge or charged their card previously on another transaction that was subsequently reversed and their credit card was not refunded.

A common situation this is used in is as follows: A payment is processed in RTO Pro and paid by credit card and approved in Xcharge, after the payment is done the operator realizes it was not credited correctly, put on the wrong contract etc. The operator then reverses the original transaction but does not refund the credit card. They then re-enter the payment the correct way, flag as a credit card payment but do not want to charge their card again. 
