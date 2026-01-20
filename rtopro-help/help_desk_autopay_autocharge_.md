# http://www.rtopro.com/help/help_desk_autopay(autocharge).htm

# Autopay / Autocharge

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Autopay / Autocharge

# 

|  [](automate_ach_send.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](advanced_autopay.md "Next Topic")  
---|---  
  
Autopay is when you have a customer who wants their payment to be charged to a credit card or ACH automatically.

[Watch a demo video on our website on how to set up a customer with Autopay.](http://www.rtopro.com/index_videolb/player.swf?url=video/Setup_autopay\(Audio\).mp4&volume=100)

To use this feature you must use X-Charge for processing your credit card or be setup for ACH through RTO Pro to use the ACH payment option. For more info about X-Charge call 352-383-9375. For more info on ACH payments, [click here.](ach_-_setting_up_and_using_in_.md)

To setup Autopay there are 3 steps, each step is detailed below.

1. The first step is to setup the customers credit card and or ACH account info. You do this by clicking on the "Credit Card/ACH Info" (ALT-A) button on the toolbar in the Customer Maintenance screen(F11 from the payment screen or customer inquiry screen). 

The form below is where you enter credit card and ACH info. The card # can either be typed in or you can swipe the card. The minimum info required is the credit card number and expiration date. If the customer wishes to pay by ACH, make sure you check the "Use ACH for Autopay" checkbox. Note that credit card info saved can also be used from the Payment screen or Load New Rental/Retail Sale screen as a payment form, that way you can just charge the card on file if the customer requests it.

When the credit card # is saved the full card number cannot be retrieved again except for processing purposes.

![Autopayclip0009](autopayclip0009.png)

2. The next step is to setup which of the customers contracts are to be paid by Autopay. You do this from Contract Maintenance (Point of Sale Menu option 3, it can also be done from the Payment Screen by pushing F11 twice after you have the customer pulled up.

"Pay by Autopay" Check this box If this agreement is to be paid automatically through the Autopay process.

"Days before due to Autocharge" If you want the charge to be processed on the day due this should be set to 0, if you want it to be charged the day before it is due enter 1, etc. If you want it to Autopay after the due date enter a negative number (-2 means it would Autopay 2 days after the due date).

![clip0037](clip0037.png)

You can click the "Click to select Autopay PMT Frm" link to select what payment form is to be used for autopay for this contract.

The Advanced Autopay feature allows you to set autopay to run on a contract a different date than their due date, on on a custom schedule, different amount than normal payments, and also to set up a 1 time autopay payment. To set this up go to contract Maintenance (Point of Sale Menu option 3, it can also be done from the Payment Screen by clicking on Contr. Maint.). Click on edit or F11 and then click on "Setup Advanced Autopay". 

[Click here to see Advanced Autopay options](advanced_autopay.md)

3. The final step is to actually run the Autopay function. You can find this in the toolbar on the Point of Sale Menu. When this function is ran it will process all contracts that should be processed that day and charge the credit cards. The payment is entered in RTO Pro automatically and a receipt will be printed showing that it was processed by Autopay.

In Store Setup under the Credit Card tab you can choose to be reminded daily to run Autopay.

![Autopayclip](autopayclip.png)

From the Autopay screen, you may:

1\. See a list of customers who will be auto charged that day and verify that all customers in list are correct.

2\. Run the Autopay and process all ACH transactions and credit cards.

3\. Verify all ACH transactions are correct before sending them to the server.

4\. Check for any ACH returns.

"View ACH Transactions"

[See ACH Payments](rto_pro_information_ach_payments.md)

[See Credit Card Processing](rto_pro_information_credit_card_processing.md)

Notes about ACH payments

When you process ACH payments they have to be sent to the ACH server before you will be paid, this can be done from the Autopay screen and it is done automatically when you run the End of Day. You should always verify all transactions are correct before sending then to the ACH server as once they are sent there is no guarantee they can be stopped. See below for instructions to cancel ACH transactions.

When you accept ACH payments you should check for returns daily and handle them the same way you would an NSF check, either load as an NSF or reverse the original transaction. You can check for returns on the Autopay screen and it is done automatically when you run the End of Day.

When you refund a payment that was paid by ACH there is no credit that is sent through the ACH system automatically. Any credit would have to be entered manually. Before entering any credits manually through the ACH system keep the following in mind. When you enter a payment (debit from the customers checking account) in the ACH system there is no guarantee that it will clear, just like when you take a check as payment. So if you enter a payment by ACH and the next day you enter a credit to the customer by ACH, its possible that the debit would get returned (not clear) while your credit to them will clear, basically you would be giving them money back for nothing. Also keep in mind that if you enter a payment for a customer by ACH then credit it manually they are going through the ACH system as 2 separate transactions. Its possible the debit could hit the customers bank account and not clear, causing the customer to be charged an NSF fee by their bank, you wouldn't get your money and then your credit to the customer through afterward. The end result would be you wouldn't get your money, the customer gets hit with an NSF fee by their bank and they get your money you credited to them.

An ACH transaction can generally only be cancelled before it is sent through the ACH system, so if you need to cancel an ACH make sure you do it before you send transactions through the ACH system and before you run the end of day program where it would be sent automatically.

Call RTO Pro Tech Support for instructions on how to cancel an ACH payment that has not been sent to the server yet or if you are not sure if it has been sent yet or not.

If you need to cancel an ACH transaction that has been sent to the ACH server see the topic here for instructions: [Visit the topic here for instructions on how to cancel an ACH transaction after it has been sent to the ACH server.](help_desk_cancelling_an_ach_transaction.md)

Credit Card processing PCI Compliance notice (payment card industry (PCI))

X-Charge is a PA-DSS validated payment application and is integrated into RTO Pro. Starting with RTO Pro version 5.5.6 our integration method isolates cardholder data from our software. By utilizing XCharge as the only module that handles cardholder data, we follow industry best practices. PA-DSS does not apply to our software because it applies only to applications that store, process or transmit cardholder data.
