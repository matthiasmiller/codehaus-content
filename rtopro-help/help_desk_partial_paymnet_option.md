# http://www.rtopro.com/help/help_desk_partial_paymnet_option.htm

# Partial Payment Move Due Date Full Term Option

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Partial Payment Move Due Date Full Term Option

|  [](partial_payment_options.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](credit_card_partial_approvals.md "Next Topic")  
---|---  
  
The option below should only be used if you read and fully understand what it explains below and make sure your employees and customers understand it. This is NOT recommended, use at your own risk. 

We will not provide any support on this feature other than this help topic. [Click here to see other methods of handling partial payments.](partial_payment_options.md)

The option for handling partial payments is one that should be read and understood thoroughly before it is enabled, it is discussed below. This is a custom feature we added for a group of shed rental companies, it was designed to their specs. Some stores love this feature, others have tried it and says it causes nothing but confusion and turn it off after a month or two, and turning this feature off requires some manual work to get your records all straight again(see below for more info). This method requires a lot of employee training and customer training and we do not recommend using this feature.

Enable Moving Due Date Full Term For Partial Payments:

![clip0017](clip0017.png)

In Store Setup under the Store Setup tab the option is "For partial payments move due date the full term and track Back Rent Due". If this option is checked and a partial payment is paid the due date would be moved the full term (week, month) and the balance of the payment would show up as "Back Rent Due" the next time you pull up the customer on the payment screen.

An example of how this feature works is below:

Monthly contract $100 payment, due 7/1/2016

If they pay $150.00 with this feature enabled their next due date would be moved to 9/1/2016 and they would show $50.00 in back rent due.

If on the next payment the customer pays the regular payment amount plus the back rent due the contract would be back to normal. If they pay less the following would occur depending on how much they pay.

1\. If they pay an amount equal to the back rent due: Due date would not be changed and back rent due would now = 0

2\. If they pay an amount less than back rent due: Due date would not be changed and back rent due would be reduced by the amount paid.

3\. If they pay an amount greater than back rent due but less then back rent due plus normal payment: Due date would be advanced the full term and back rent due would be adjusted accordingly, an example of this is below:

If normal payment is $10.00 and back rent due is $5.00

If they pay $6.00: due date would be advanced and back rent due would now = $9.00

If they pay $12.00: due date would be advanced and the back rent due would = $3.00

Back rent due does not affect the contract balance, the contract balance is the contract amount - amount paid. Back rent due does affect the payoff amount as a discount is not given on any back rent due. Back rent due can be edited in Contract Maintenance (Point of Sale menu option 3).

This option can be password protected in Security (Setup menu option 5). When it is password protected there will be a button on the payment screen to enable this way of handling partial payments. If it is not password protected and this option is checked in Store Setup all partial payments will be handled as described here. Also note that if a customers payment is $100 a month and they pay you $220 (2 full payments + a $20 partial payment) with this option enabled their due date would be moved 3 months and it would show they owe $80 in back rent.

Back rent due is not necessarily late rent, it represents the amount of money due to pay to the contracts current due date. For example if somebody has a monthly payment of $100 due on 7/1/2011, and they pay $50 on 7/1/2011, with this feature their due date would be set to 8/1/2011 and it would show $50 in back rent due, this $50 represents the amount of money they owe you to actually pay them through 8/1/2011. Customers often can not understand how they could owe what the system calls "Back Rent" when they are paid ahead, this is often what confuses customers and why many stores decide to quit using this feature after enabling it. In the aforementioned example if it is 7/15/2011 and you tell the customer their due date is 8/1/2011 but they owe $50 in back rent it is hard for them to understand this.

Note: This option only affects the following contract types: Rent to Own, Rent to Rent, Lease (except federal lease), G as agent type, O other type and B club only agreements. 

Enabling this option is not recommended, it is confusing for customers and employees. You will also collect less late fees with this option enabled since late fees are calculated on due date and with this option enabled due dates will be advanced further than the customer is really paid through. Make sure you read this help topic thoroughly and understand how this works before enabling. 

If this option is not enabled when partial payments are paid the rent is broke down into a daily rate and the due date is moved the amount of days the partial payment would pay for. For instance if a monthly payment was $100 and the customer paid $50 it would move their due date 15 days. If they paid $150 their due date would be advanced 45 days.

Please note if you enable this feature, then want to disable it you should first go into each contract under contract maintenance and remove any back rent due and optionally move the due date back to what it should be. For instance if a customers payment is 100 monthly and it shows 50 in back rent due and their due date is 3/1/2015 that means their actual due date should be 2/15/2015, since this is what their due date would have been if the payment was taken without this feature enabled.

To find contracts that have back rent due because of this feature you can use the SQL string below, from the Custom SQL string reports page (Revenue Reports Menu option E):

select * from contracts where backrentdue > 0 and status = 'OPEN'

![image43](image43.jpg)
