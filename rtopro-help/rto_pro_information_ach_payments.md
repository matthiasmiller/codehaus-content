# http://www.rtopro.com/help/rto_pro_information_ach_payments.htm

# [ACH](javascript:void\(0\);) Payments

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Information >

# [ACH](javascript:void\(0\);) Payments

# 

|  [](rto_pro_information_credit_card_processing.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_information_features.md "Next Topic")  
---|---  
  
ACH stands for "Automated Clearing House". It is an electronic debit or credit that can be initiated from any checking or savings account for either one time payments or recurring payments.

ACH is now integrated in RTO Pro. Your customers with a checking or savings account can pay their payments via ACH. They can pay by ACH on a recurring basis or just as a one time payment.

See this page for pricing and more details about ACH in RTO Pro: <http://www.rtopro.com/integrated_ach.aspx>

For returned ACH you can still charge an NSF fee but you are only getting charged $1.95 compared to the $10.00 to $30.00 most banks charge for checks returned to you.

ACH Check conversion is also optionally available with the purchase of a Burroughs SmartSource Edge Check scanner. These are available for around $300.00 at <http://www.burroughsstore.com> or at <http://www.unilinkinc.com/>. ACH Check Conversion or ACH ARC is where you scan checks you receive and submit them electronically through the ACH system instead of depositing them at your bank. This is included at no extra cost with the RTO Pro ACH system (except for the per transaction fee same as all ACH transactions). When a check bounces you would be charged the $1.95 returned ACH fee instead of the $10 to $30 NSF fee banks commonly charge.

To setup a customer to pay by ACH all you have to do is get their account and routing number, this information is saved in RTO Pro. Then set which contracts are to be paid automatically by ACH. Then when you run Autopay you click one button and all your customers who's contracts are due to be processed will automatically be ACH Debited and their payments will be entered in 1 step. You can have 1 or 1000 customers setup for ACH and they are all processed with 1 click! Your checking account will be credited the next day for all ACH Debits processed.

ACH can also be used as a telephone authorized one time payment. If a customer calls and wants to pay by ACH you can accept their payment over the phone.

Call RTO Pro Software at 352-383-9375 for more information.

[If you are a RTO Pro customer and are ready to get setup for ACH click here for instructions and paperwork to get started.](http://www.rtopro.com/integrated_ach.aspx)

How to use ACH for Autopay in RTO Pro

1. When a customer wants to pay by ACH enter their ACH info: Alt-E from the Payment Screen or click on the "Credit Card / ACH Info" button on any customer screen. Click on the "Print ACH Authorization Form" button to print an Authorization form for the customer to sign.

![image23](image23.gif)

2. For each contract the customer wants to pay automatically by ACH or Credit Card enter the number of payments to pay at a time (generally 1) and how many days before they are due to process the ACH (generally 0, which would be the day they are due). You set this up in Contract Maintenance (Point of Sale Menu option 3) or push F11 twice from the Payment Screen. You can also enter this information when you load a new rental.

![image25](image25.gif)

3. Go to Autopay (Point of Sale Menu > Alt-A) and click the "Process Now" button. Anybody who is setup to pay by ACH or Credit Card will be charged and their payment will be entered in one step. It doesn't matter if you have 1 or 1000 customers setup they are all processed in 1 click. When you run the End of Day Report, all ACH transactions that have been processed will be sent off to the server.

The ACH funds are generally credited to your account the next day. ACH can also be used for 1 time payments also.

![AutopayScreenNoMarkings](autopayscreennomarkings.png)

If you want to accept ACH as a payment form from the Payment or other screen make sure you check the box in Store Setup under the "Credit Card/ACH" tab that says "When entering ACH as a payment form on the Payment screen process through the ACH system" (Line 13).

When using ACH as a payment form for 1 time payments you will be prompted if it is a signed, telephone or web authorized ACH transaction. For a telephone authorized transaction you need to record the customer's authorization or get an authorization by email. For a regular ACH transaction you should get a signed ACH Authorization form.

When processing ACH payments from anywhere besides Autopay the transactions are saved to your transaction folder but are not sent to the ACH server right away. There are 3 ways to send the transactions.

1\. From the Autopay screen click the "Send ACH transactions to server" button.

2\. When you run the End of Day program any unsent transactions will be sent automatically.

3\. If you have manual transactions entered and then you run Autopay the manual transactions will be sent with the recurring transactions if there are any.

Notes about ACH payments

When you refund a payment that was paid by ACH there is no credit that is sent through the ACH system automatically. Any credit would have to be entered manually. Before entering any credits manually through the ACH system keep the following in mind. When you enter a payment (debit from the customers checking account) in the ACH system there is no guarantee that it will clear, just like when you take a check as payment. So if you enter a payment by ACH and the next day you enter a credit to the customer by ACH, its possible that the debit would get returned (not clear) while your credit to them will clear, basically you would be giving them money back for nothing. Also keep in mind that if you enter a payment for a customer by ACH then credit it manually they are going through the ACH system as 2 separate transactions. Its possible the debit could hit the customers bank account and not clear, causing the customer to be charged an NSF fee by their bank, you wouldn't get your money and then your credit to the customer through afterward. The end result would be you wouldn't get your money, the customer gets hit with an NSF fee by their bank and they get your money you credited to them.

An ACH transaction can generally only be cancelled before it is sent through the ACH system, so if you need to cancel an ACH make sure you do it before you send transactions through the ACH system and before you run the end of day program where it would be sent automatically. [Visit the topic here for instructions on how to cancel an ACH transaction after it has been sent to the ACH server.](help_desk_cancelling_an_ach_transaction.md)
