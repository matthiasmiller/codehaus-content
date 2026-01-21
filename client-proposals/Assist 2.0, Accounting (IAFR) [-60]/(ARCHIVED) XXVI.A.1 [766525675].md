26.1.1

Whenever a building is built:

  * Populate the FGI Breakdown with Standard Cost % for the district.
  * Create an accounting transaction that does the following for each FGI Category:
    * Credits (decreases) the Balance Sheet Source Account by the category's Standard Cost $
    * Debits (increases) the Balance Sheet Destination Account by the category's Standard Cost $



  


Whenever a building is delivered (i.e. sold), create a transaction that does the following for each FGI Category:

  * Credits (decreases) the Balance Sheet Destination Account by the category's Actual Cost $ (if specified) or the category's Standard Cost $
  * Debits (increases) the COGS Expense Account by the corresponding amount
  * Credits (increases) the Income Account by the Sales Order Total
  * Debits (decreases) the Unearned Income Account by the total payments already made
  * Credits (increases) the Accounts Payable by the remaining balance



  


Whenever a payment is made, create a transaction that:

  * Debits (increases) the Banking account by the payment amount
  * If it's not been delivered, credits (increases) the Unearned Income account by the payment amount.
  * If it's been delivered, credits (decreases) the Accounts Receivable account by the payment amount.



  


  


TODO_HLD: Should we migrate existing records over to these 3 costs?

TODO_HLD: Should we wait until we get ALL actual costs, or do we mix/match actual costs?
