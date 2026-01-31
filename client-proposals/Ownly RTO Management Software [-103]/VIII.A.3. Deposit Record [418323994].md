8.1.3. Deposit Record

Seth Miller 01/06/2026: TODO_KS:

[X] [[PC0188352]]. Switch from district to accounting company on deposit records. 

[X] [[PC0188353]]. Refactoring and renaming.

[X] [[PC0188354]]. ZRT Deposit record

[ ] [[PC0188363]] field deposit total

  


Seth Miller 12/16/2025: Standardize from ZFP. Defer the changes to Deposit Total until late January.

  


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


