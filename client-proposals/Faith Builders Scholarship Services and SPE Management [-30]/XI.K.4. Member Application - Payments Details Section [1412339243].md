11.11.4. Member Application - Payments Details Section

Payment Details (visible unless the section is empty and the application is inactive):

  * Check Date
  * Check Number (required if Check Date is not blank)
  * Check Amount (required if Check Date is not blank)
  * Check Status (required; drop-list)



List items:

  * Deposited 
  * Scheduled for Deposit 
  * Held 
  * Shredded


  * Deposit Date (required if Check Status is "Deposited" or "Scheduled for Deposit")



  


Validation:

  * Warning on save: if the check date year does not match the Tax Year.
    * Warning Message: "Check date should match the tax year. (Field: Check Date)"
  * Error: if Check Amount is not blank and does not match the Total Amount.
    * Error Message: "Check amount should match the total amount."


