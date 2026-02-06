12.3.9. Deposit Record

  * Deposit (section)
    * Accounting Company
    * Date
    * Account
    * Ref #
    * Memo
    * Total (field)
    * Difference (Total - Sum of Items)
    * If Total is set and Difference is not NA/zero:
      * Error on save: "The deposit total does not match the itemized total."
    * If Total is unset and Difference is negative:
      * Warning on save: "The deposit total is empty. It will be updated to the itemized total of $1,234.56."



  


  * Miscellaneous Items
    * Customer Name
    * Account
    * Ref #
    * Amount
    * Memo



  


  * Payments
    * Embedded spreadsheet with the following columns
      * Payment ID
      * Included (checkbox)
      * Payment Customer (auto-calculated and read-only)
      * Payment Amount (stored value; automatically set to the payment amount)
      * Payment Date (auto-calculated and read-only)
      * Payment Method (auto-calculated and read-only)
      * Open Payment (link to open the payment)
    * Validate that a payment is not included on multiple deposits



  


  * Record History
    * View Accounting Transactions (link)
    * Modification History (link)



  


TODO_Permissions for editing RG 

  


Menu:

  * Deposits
  * Create Deposit 
    * This prompts for accounting company then creates a new deposit and autopopulates the RG with all undeposited payments for the company.


