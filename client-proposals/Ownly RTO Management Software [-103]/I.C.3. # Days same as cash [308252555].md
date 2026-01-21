1.3.3. # Days same as cash

TODO_IDD how to do calculations for # days same as cash.

  


Related to contract closure

  


From Duane:

  


I suspect that if set up a contract from a contract def and choose an option that includes 90 days same as cash then we would have a way to pay it off for the cash value - anything paid + sales tax. Probably a button or something like that on the payment page. The moment you pass the SAC time frame the button disappears. 

  


that explanation above could be spring as long as we had a manual way to do it in Jan

  


  


Matthias Miller 12/04/2025: For a same as cash, all rent payments get put towards cash price. Two options:

  


  * Update historical rows to make them all-cash payments
  * Create correction rows with cash amounts > payment amount (weird!)



  


  * On the 90th day, Cash Price + Tax - Everything Paid
  * On the 91st day, it's an EPO



  


Simple way to handle it:

  * Rental Payment = Payment > Cash Price Amount
  * EPO = Payment = Cash Price Amount
  * Same as Cash = 



  


TODO_DB - Accounting impact

  


es, we don't have it perfected in practice yet due to cleanup but when fully complete the 4000 accounts will have a parent account Revenue and the child accounts: Rental Revenue, Building Sales, EPO, LDW, Service Fees... my goal is to improve tracking and reporting to identify trends quicker and create additional transparency across revenue: sources. This structure is better suited for me to be able to manage the company even if some of the revenue accounts should be captured in other income. | view the 90 DSAC as a building sale and reclass the payments towards the price of the building.

  


In an ideal world would you or would you not find value in automating that process. In other words upon the final payment of the SAC the reclassification of rental payments to Building Sales would happen automatically. The question is not a sales pitch but rather a further questioning in case there are other steps in your process Next question, do you ever split rental payments by their percentages? In other words the rent portion and the building portion or do you consider rental payments as strictly rental
