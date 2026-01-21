3.8. Financial Configurations

  


Requirements

There should be a custom "Financial Configurations" section on the AppHosting.zone Settings page for setting various financial goals and standards. 

  


Data Access varies by item (see breakdown). All of of these financial settings should be visible and editable for Full Admins. 

  


Fields (grouped here by Data Access): 

  


Full Admin Only: (locked down so that non-Full Admin users cannot see these settings, their values, or the resulting calculations; controlled by the "View & Edit All Financials" setting) 

  * Rate for Benchmark Buildings (%) (required; number field to 1 decimal place; this is used to calculate a % of invoice subtotal before tax; changes to this rate should be applied to all buildings that have not been Delivered)
  * Rate for Bald Eagle Transit (%) (required; number field to 1 decimal place; this is used to calculate the delivery cost for the building; for new building delivery only; % of invoice subtotal after discounts but before tax; changes to this rate should be applied to all buildings that have not been Delivered)  
  * Salesperson Bonus $ (required; number field to 2 decimal places; used to reward salespeople for certain achievements; manually added to paychecks; changes to this are applied to all future applied bonuses)



  


Secretary: (per the client, can be hidden but not restricted; controlled with the "View Referral Payments" permission) 

  * Standard Customer Referral Payment $ (required; number field to 2 decimal places; this is used for the Customer Referral Program for all Contact Types except Dealers; the current rate is $40.00; changes to this are applied to all future noted referrals)
  * Dealer Customer Referral Payment $ (required; number field to 2 decimal places; this is used for the Customer Referral Program for Dealer-type contacts who refer customers; the current rate is $100.00; changes to this are applied to all future noted referrals) 



  


Office Worker/Member Salesperson: (per the client, can be hidden but not restricted; controlled with the "View Weekly Sales Goal" permission) 

  * Weekly Sales Goal $ (required; number field to 2 decimal places; changes to this are applied immediately) 
    * Note that this is currently displayed as a status bar, not displaying numbers, but we can show the numbers if needed 



  


All Member-type users: (per the client, can be hidden but not restricted for non-members; controlled by the "View Shop Build Goal" and "View Pay Period Start Date" permissions) 

  * Shop Build Goal $ (required; number field to 2 decimal places; changes to this are applied immediately) 
    * Note this is currently displayed as a status bar, not displaying numbers, but we can show the numbers if needed 
  * Pay Period Start Date (required; date field; pay periods start every two weeks following this date, e.g. 10/14/2021, 10/28/2021, etc.)



  


*Done.

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=693754442](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=693754442)

  


TODO_CCI: Jason didn't care whether these fields were restricted. However, Matthias is scared about link swapping, browsing, etc. His vote is just to go ahead and restrict these fields.
