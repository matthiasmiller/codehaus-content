# http://www.rtopro.com/help/ach_-_setting_up_and_using_in_.htm

# ACH - Setting up and using in RTO Pro

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# ACH - Setting up and using in RTO Pro

# 

|  [](help_desk_inventory_custom_report_viewer.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](automate_ach_send.md "Next Topic")  
---|---  
  
# 

ACH is now integrated in RTO Pro. Your customers with a checking or savings account can pay their payments via ACH. They can pay by ACH on a recurring basis or just as a one-time payment.

ACH stands for "Automated Clearing House". It is a method of accepting electronic debits from checking or savings accounts for payments. In RTO Pro these payments can either be one time payments for rentals or retail sales or they can be setup as automatic recurring payments.

ACH is often thought of as an alternative to credit card payments. The fees for accepting an ACH payment are cheaper versus credit card payments. An ACH payment differs from a credit card payment in that there is no guarantee the transaction will clear, so there is no guarantee you will be paid for the transaction, there is no approval process like with credit cards. Of course, even with credit cards there is no guarantee you will be paid, the charge could always be disputed by the customer. ACH is more similar to accepting a check, you are just accepting it in electronic form. Just like with a check you won't know until a few days after the transaction if it actually cleared or not. There are some services that claim they can verify if a transaction will clear or not but there are NO guarantees with a check or ACH transaction, even if the money is in their account today that doesn't mean it will be there when the transaction hits their bank. 

The advantage of taking ACH over a check is ACH payment can be taken by phone or internet and also when an ACH transaction gets returned (like a bounced check) you are charged much less than what banks charge merchants for bounced checks they deposited. Also, ACH transactions generally will hit the customer's bank account before a deposited check, so the chances of it clearing are more likely. ACH is also more convenient since no trips to the bank are needed, it is all done electronically. 

In RTO Pro ACH check conversion is also available (a compatible check scanner is required). This is where you take checks you receive and instead of depositing them you scan them with the check scanner and run them through electronically.

Here is a guide for understanding how ACH works in RTO Pro:

Step 1: Sign Up

To get information on how to sign up for ACH Integrated Pay, [click here.](http://www.rtopro.com/integrated_ach.html) You must have an account with either ICheckGateway or Profituity (a.k.a. CheckAssist).

Step 2: Store Setup

Before you can charge customers via ACH transaction, you must first enable ACH in your store settings. Do this through the Setup Menu under Store Information Setup in the Credit Card/ACH tab. You'll need to enter your store's ICheckGateway or Profituity information. For more detail on this step, [click here.](_ach_store_setup.md)

Step 3: Save Customer Info, ACH Autopay, and Customer Authorization

For every customer that wishes to use the ACH feature, you'll need to save their ACH info. All you need is a bank account number, routing number, account type, and bank name. This information is entered on the "Credit Card/ACH Info" tab located in the toolbar of the Customer Payment or Customer Inquiry screen, or alternatively in the Customer Maintenance screen.

If the customer wishes to use ACH for Autopay, make sure you check the "Use ACH for Autopay" check box as well.

Make sure you receive authorization from the customer approving you to use ACH/Credit Card Autopay. This can be done with an email from the customer, a recorded over-the-phone confirmation, a WebPay authorization, or print out an ACH authorization form for the customer to sign. For help with customer info, Autopay, and printing authorization forms, [click here.](_ach_customer_info.md)

[Watch a demo video on our website on how to set up a customer with Autopay.](http://www.rtopro.com/index_videolb/player.swf?url=video/Setup_autopay\(Audio\).mp4&volume=100)

Step 4: Using ACH for One-Time Payment

ACH can also be used for one-time transactions. Just make sure you select "H" for the payment form on the Tendered page. For an example, [see here.](_ach_one_time_payment.md)

Step 5: Run Autopay

[To learn how to set up ACH Autopay, click here for Autopay help topic.](help_desk_autopay_autocharge_.md)

Step 6: View ACH Transactions

Click the "View ACH Transactions" on the Autopay screen to see a record of unsent, pending, cleared, and returned transactions. See details here: [ACH Transaction List](ach_transaction_list.md)

Step 7: Send ACH Transactions to your ACH Provider

When ACH is used as a payment form the ACH transaction is saved in the ACH table, but you will not be paid for it until it is sent to your ACH provider. When you run the end of day process any unsent ACH transactions are sent automatically. You can also send them manually at anytime from the Autopay screen. After the transactions are sent it then takes 4 to 7 days before you find out if the transaction cleared or was returned. 

Note that you can turn off the End of Day automatic sending of ACH transactions in store setup. You can also password protect sending of ACH transactions in Security, this will prevent them from being sent automatically through the end of day also.

You can automated the process to send ACH transactions to the ACH system by sending the command line "ach_send" to the End of Day executable (income.exe). So to have ACH transactions sent you could launch for instance "c:\rtowin\income.exe ach_send". This can be scheduled through Windows Task Scheduler. [Click here to see a topic with more info about scheduling the ACH send.](automate_ach_send.md)

Step 8: Manage Returned Transactions

When viewing ACH transactions, select the "Show Returns" bullet in the top left corner of the screen. Select a transaction and right-click to see options. Options include reversing the transactions, checking if selection was previously reversed, loading the transaction as NSF, flagging transaction as already loaded as NSF, and flagging selected transaction as resubmitted to CheckAssist through ERS website. For more detail, [click here.](ach_returned_transactions.md)

Notes about ACH payments

When you process ACH payments they have to be sent to the ACH server before you will be paid, this can be done from the Autopay screen and it is done automatically when you run the End of Day. You should always verify all transactions are correct before sending then to the ACH server as once they are sent there is no guarantee they can be stopped. See below for instructions to cancel ACH transactions.

When you accept ACH payments you should check for returns daily and handle them the same way you would an NSF check, either load as an NSF or reverse the original transaction. You can check for returns on the Autopay screen and it is done automatically when you run the End of Day.

When you refund a payment that was paid by ACH there is no credit that is sent through the ACH system automatically. Any credit would have to be entered manually. Before entering any credits manually through the ACH system keep the following in mind. When you enter a payment (debit from the customers checking account) in the ACH system there is no guarantee that it will clear, just like when you take a check as payment. So if you enter a payment by ACH and the next day you enter a credit to the customer by ACH, it's possible that the debit would get returned (not clear) while your credit to them will clear, basically you would be giving them money back for nothing. Also keep in mind that if you enter a payment for a customer by ACH then credit it manually they are going through the ACH system as 2 separate transactions. Its possible the debit could hit the customers bank account and not clear, causing the customer to be charged an NSF fee by their bank, you wouldn't get your money and then your credit to the customer through afterward. The end result would be you wouldn't get your money, the customer gets hit with an NSF fee by their bank and they get your money you credited to them.

An ACH transaction can generally only be cancelled before it is sent through the ACH system, so if you need to cancel an ACH make sure you do it before you send transactions through the ACH system and before you run the end of day program where it would be sent automatically.

Call RTO Pro Tech Support for instructions on how to cancel an ACH payment that has not been sent to the server yet or if you are not sure if it has been sent yet or not.

If you need to cancel an ACH transaction that has been sent to the ACH server see the topic here for instructions: [Visit the topic here for instructions on how to cancel an ACH transaction after it has been sent to the ACH server.](help_desk_cancelling_an_ach_transaction.md)
