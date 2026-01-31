8.2.4. Lock Down CRA Payments

Seth Miller 01/27/2026: TODO_SETH. Spec and delegate [[PC0189383]]

  


There are two times the customer can bypass rent to get a building at its cash price:

  * CRA Payout - They've paid in a CRA and they have paid the full contract at reduced terms. We treat this as an Early Purchase.
  * EPO - They pay off their contract early



  


Proposal:

  * Use "Early Purchase" itemization type. Subtotal = Cash Price
    * NOTE: We used to use a Rent row where Subtotal = Cash Price. Going forward (barring old data), Subtotal > Cash Price for all Rent Rows.
    * This should be the LAST ITEM on the waterfall.
    * You cannot refund an EPO.



  


Each of these would specify the $ amount going to the cash price of the building.

  


NOTES:

  * To handle CRA effectively, we must make sure we never incur rent such that the remaining cash price of the building drops below the CRA balance
  * NOTE: To simplify CRA payouts, we will NOT let you ever make any payments the last month of payment on a CRA. You HAVE to do an EPO on it.



  


  * Autopay
    * Show columns for
      * Date
      * Amount from Autopay
      * Amount from Security Deposit
      * Balance
    * ONLINE: Show a message that their security deposit of $123.45 will be used to pay the balance of the contract.
    * ONLINE: Show a message on a CRA contract that the last payment will not be autopayed and must be paid via an EPO. Do not include this payment in the payment schedule.


