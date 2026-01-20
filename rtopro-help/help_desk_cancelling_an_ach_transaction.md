# http://www.rtopro.com/help/help_desk_cancelling_an_ach_transaction.htm

# Cancelling or Refunding an ACH transaction

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** »No topics above this level« 

# Cancelling or Refunding an ACH transaction

# 

|  [](welcome_welcome_1.md "Parent Chapter")  
---|---  
  
Cancel an ACH Transaction

You can generally only cancel an ACH transaction the same day of the transaction.

Below are instructions to follow if you want to try to cancel an ACH transaction that has already been sent to the Profituity ACH server. If you are not sure if the transaction has been sent to the ACH server or not call 352-383-9375 for instructions to determine if it has been sent or not. You can see which ACH transactions are unsent and sent from the [ACH transaction list](ach_transaction_list.md).

Cancel a sent ACH transaction If you are using the new Profituity API

Please note if you are using the new Profituity API you can cancel sent ACH transactions the same day via their web portal, at this URL: https://platform.profituity.com/MerchantPortal/Payment/PendingPayments

![clip0056](clip0056.png)

The box above will be checked in store setup if you are using the new Profituity API (Note the # to the left could change over time, so it may not always be #36)

Cancel a sent transaction if you are using the Old API, Instructions from Profituity:

Software Support at Profituity does not have the ability to Stop Transactions that you have already exported. If you have such a request, you should call (850) 857-7752 and give Profituity the pertinent information and they will forward it to the ACH department. Then follow up by sending an email to stopach@checksupport.com. You will need to include the Route #, Account #, Check # and Dollar Amount. Requests must be received before 4:00 Central time. This procedure requires the intervention of the programming department and they will charge you $35.00. A good way to keep this from happening to you is to refrain from exporting until as close to 4:30 Central Time as possible. We cannot guarantee that transactions will be stopped but we will make every effort to accommodate your needs.

* * *

Refund an ACH Transaction to a customers bank account (sending an ACH Credit)

If you refund an ACH payment and that ACH transaction was already sent through the ACH system, you can send a refund through the ACH system to the customer. See the important note below, it's a good idea to make sure the original transaction clears before sending a refund.

To send an ACH credit to a customer, pull up that customer under the payment screen, click Credit Card / ACH Info at the top, then click the button "Manually enter a credit or debit for this ACH Account". Fill in the receipt number of the original transaction you are giving the refund for, enter a description, and the amount, be sure "CREDIT" is the box checked and click Save. It generally takes around 5 to 7 days for the credit to hit your customers account, contact your ACH provider if you want a more accurate time frame.

Notes about ACH payments / credits

When you refund a payment that was paid by ACH there is no credit that is sent through the ACH system automatically. Any credit would have to be entered manually. Before entering any credits manually through the ACH system keep the following in mind. When you enter a payment (debit from the customers checking account) in the ACH system there is no guarantee that it will clear, just like when you take a check as payment. So if you enter a payment by ACH and the next day you enter a credit to the customer by ACH, its possible that the debit would get returned (not clear) while your credit to them will clear, basically you would be giving them money back for nothing. Also keep in mind that if you enter a payment for a customer by ACH then credit it manually they are going through the ACH system as 2 separate transactions. Its possible the debit could hit the customers bank account and not clear, causing the customer to be charged an NSF fee by their bank, you wouldn't get your money and then your credit to the customer through afterward. The end result would be you wouldn't get your money, the customer gets hit with an NSF fee by their bank and they get your money you credited to them.
