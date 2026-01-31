11.18. Alternative EPO calculation methods

Seth Miller 10/20/2025: DONE_IDD: Matthias needs to confirm w/ Duane. Matthias Miller 11/03/2025: Confirmed. TODO_SETH

Matthias Miller 07/31/2025: TODO_SETH:  spec. Use something similar to ContractEarlyPayoffAmountInternal

 for each of the payment methods. For early payoff method, have a list of:

Balance x Cash Price % -- current method

Cash Price - (Rent Paid x Rental Fee %)

Cash Price x (Remaining Payments / Total Payments)

  


This needs to be copied to the contract.

  


NOTE: Be sure to handle rounding appopriately. These may vary up to ~$0.10 because of rounding.

See [https://docs.google.com/spreadsheets/d/1Tf04lidWBWhCM5APHtCT5uJVwT5vpXYz07k6IvMrOAU/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1Tf04lidWBWhCM5APHtCT5uJVwT5vpXYz07k6IvMrOAU/edit?gid=0#gid=0) for calculation details
