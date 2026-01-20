# http://www.rtopro.com/help/help_desk_payoff_with_discount_for_prepaid_rent_option.htm

# Payoff with discount for prepaid rent option

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** »No topics above this level« 

# Payoff with discount for prepaid rent option

# 

|  [](welcome_welcome_1.md "Parent Chapter")  
---|---  
  
"When calculating Payoff give discount on future pre-paid payments also" option in Store Setup under Store Setup tab under the heading Early Payoff EPO calculation.

This setting when checked will give the EPO discount on pre-paid payments also. Example: If a customer has $500 balance and you give a 40% discount and they are paid ahead 2 full months at 50.00 a month. 

With this box checked payoff= $260.00

$500 balance

+$100 pre-paid rent which discount is taken off

x .6 (the amount of balance they pay)

=$360.00

-$100 prepaid rent

=$260.00

Without this box checked payoff = $300.00

$500 balance

x .6 (the amount of balance they pay)

=$300.00

This is for RTO contracts only and this does not apply to the California method of calculating EPO.

Note when this option is checked it can be confusing for customers as the payoff printed on receipts will increase if they do not pay it by the "Payoff good til" date that also prints on the receipts. The reason the payoff will increase is because when a customer is due on 1-1-2010 and they pay on 1-1-2010 for 1 month, on that day they are paid ahead for 1 month so the payoff that day will reflect a discount on that months rent they just paid, if they come in on 2-1-2010 the payoff will be higher because they no longer have any pre-paid rent that is being discounted.

Example below:

On 1-1-2010 if they pay 50 a month and have a balance of 500 and you give 50% discount for EPO. On 1-1 they pay 50. the balance is now 450.00. If they then ask for their payoff that day the payoff would be 200.00 (450 +50 (PPR) = 500 x .5 = 250.00 - 50 (PPR) = 200.00) PPR = prepaid rent.

On 2-1-2010 their EPO would be 450.00 x .5 = 225.00 because they no longer have any prepaid rent since they are due that day.

This option is generally not recommended except for storage building rental businesses where customers will often pay extra payments every month and be paid way in advance. Also note for RTO Pro to calculate the payoff correctly for customers who are paid ahead their due date must not be moved back when they pay extra payments. For instance if somebody is due on 2/1 and they pay 3 payments their next due date should be 5/1. If you move their due date back to 3/1 RTO Pro will not know they are paid ahead and have pre-paid rent.

If you do use this option make sure you tell your customers what it says on the receipt "Payoff good til" which means "This payoff amount is only good til this date and after that it will be a higher amount". Also keep in mind that when you push F8 from the payment screen that payoff is good for THAT DAY ONLY if you have this option checked and the payoff from that screen as well as the actual payoff amount when you go to contract close will change DAILY when you have this option checked.
