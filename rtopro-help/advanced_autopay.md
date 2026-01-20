# http://www.rtopro.com/help/advanced_autopay.htm

# Advanced Autopay

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) > [Autopay (AutoCharge)](help_desk_autopay_autocharge_.md) >

# Advanced Autopay

# 

|  [](help_desk_autopay_autocharge_.md "Previous Topic") [](help_desk_autopay_autocharge_.md "Parent Chapter") [](help_desk_pricingsetup.md "Next Topic")  
---|---  
  
Next Autopay Date: If you want to setup Autopay to pay on a specific date instead of the customers due date you can enter the date here. The auto payments would continue on that date of the month for monthly, or day of week for weekly, instead of on the due date. Leave this box empty to run autopay on the agreement due date. This box can be left empty and autopay amount filled in (below) to pay a different amount on the agreement due date. Please note when you set a date here autopay will run on that date no matter what, even if customer pays a normal payment the day before autopay is set to run. There is a setting in store setup in the CC/ACH tab, autopay section you can check to advance this advanced AP date automatically for normal payments. See this topic here for that option: [Advanced Autopay Next Autopay Date Move for Regular Payments Option](advanced_autopay_next_autopay_date.md)

Autopay Amount: If you want to pay a specific amount by Autopay. The way it would process if the customer owes other charges is it would take as many full payments as possible with the autopay amount and any additional would be applied to their other charges due. For instance if a customer's total payment is $25 a week and they owe $15 in other charges and you setup to autopay $60.00, it would pay 2 full payments and $10.00 toward other charges. Any other processing of extra or short payments would be handled the same as if you entered it from the payment screen just entering the amount and processing.

Please note if autopay amount is entered and next autopay date (above) is left blank, autopay would process the amount entered here on the due date.

Note: There is an option in Store Setup under the Credit Card / ACH tab you can check that will make any extra money paid through autopay go into customer deposit instead of just being applied to their account. If this box is checked and the amount to pay by autopay is greater than the amount currently due, including other charges, the extra amount would go into deposit instead of being handled like explained above. Deposits have to be enabled in your store also.

Make this a ONE TIME Payment: Checking this box would make this a one time autopay, it would process one time, using the settings you have selected, then it would turn off autopay so it would not run again unless it is turned back on.

* * *

Paying on the Nth day of the Nth week every month: To set a contract up to pay on the 3rd Tuesday of every month for instance you can use this option. Choose the week and the day to pay on. Note the date you enter in "Next Autopay Date" will be the next time autopay processes, even if that date does not match your settings, the next date would follow your day and week rules. This cannot be used as a 1 time payment.

For Semi Monthly you can set up a second Nth day/week. It is recommended this is used with Semi Monthly contracts, and you should be sure the due date is set after the latest possible Nth day/week you enter. For example if somebody wants to pay the 1st Tuesday and 3rd Tuesday the first Tuesday could be as late as the 7th, so their due date should be the 7th and 23rd or after, if they are due on the 1st and 16th they could end up having a late fee when it processes on the 7th.

Note this can be used for monthly agreements also, but partial payments are handled like they normally are, so if you enter a Autopay Amount be sure it is enough to pay the full month if paid twice, so daily rate x 31 / 2, or if you use the partial payment feature you can just use monthly payment /2.

![clip0086](clip0086.png)

* * *

Paying Autopay weekly or Bi-Weekly(every 2 weeks)

With this option the next autopay date would be advanced 7 or 14 days after each autopay payment. This is for when you have a monthly customer who wants to pay by autopay weekly or bi-weekly.

![clip0089](clip0089.png)

* * *

Paying on a custom date list: If you want to set up autopay to pay on a custom list of dates you can use this option. See below for examples of how to use this feature.

Please note when using the autopay by custom dates list if the next scheduled date is a past date it would be skipped. For for instance if you set a contract to pay on 3/8, 3/9, and 3/15 and the credit card used for this autopay does not get approved for the 3/8 transaction until 3/10, the 3/9 autopay would be skipped, the next autopay would run 3/15.

The options below would do the following

3/8/2021 pay $10.00.

3/10/2021 pay $10.00

3/11/2021 pay normal payment amount, then keep autopay on, set it to process on the due dates

![clip0040](clip0040.png)

The options below would do the following

3/8/2021 pay $15.00

3/10/2021 pay $10.00

3/15/2021 pay normal payment amount, then keep autopay on, set it to process on 3/15/2021 + 1 term(plus 1 month for monthly contract, plus 1 week for weekly etc.)

![clip0041](clip0041.png)

The options below would do the following

3/8/2021 pay $20.00

3/10/2021 pay $10.00

3/15/2021 pay $25.00, then turn autopay OFF for this contract.

![clip0042](clip0042.png)

* * *

Below is an explanation of how advanced autopay is stored in the contracts table in the database.

Field definition for "autochargepmts", "extrarent", "recupdate" possible values and their meaning.

1 = autopay on the contract due date

-1 = autopay on date in "recupdate", recurring. So 1 term would be added to the "recupdate" date after autopay processes and that would be the next autopay date.

-2 = 1 time payment by autopay, on due date or on date in "recupdate" field if recupdate > 1/1/1900

Custom day / week of the month payments

-3?? = autopay on a custom day/week of the month

-31? = pay on the 1st week of the month

-32? = pay on the 2nd week of the month

-33? = pay on the 3rd week of the month

-34? = pay on the 4th week of the month

-35? = pay on the last week of the month

-3?1 = pay on Sunday

-3?2 = pay on Monday

-3?3 = pay on Tuesday

-3?4 = pay on Wednesday

-3?5 = pay on Thursday

-3?6 = pay on Friday

-3?7 = pay on Saturday

so -314 = pay on Wednesday in the first week of the month

Autopay by custom dates 

The options below are when you enter a list of custom dates to pay by, each date you enter autopay will run, the options below are instructions what to do after the last saved date is paid.

-41 = autopay off after

-401 =autopay by last date after (1 term would be added to the last saved date)

-400 =autopay by due date after

if "extrarent" > 0 that is the amount to pay by autopay, otherwise it is the normal amount due.

if "recupdate" > 1/1/1900 that is the date to pay by autopay, otherwise it is the contract due date.
