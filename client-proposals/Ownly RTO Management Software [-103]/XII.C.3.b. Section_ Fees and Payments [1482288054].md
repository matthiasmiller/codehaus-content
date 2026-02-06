12.3.3.2. Section: Fees and Payments

  * Fees and Payments section
    * View Fees and Payments (admin only) (child screen with RG history of fees and payments)



Seth Miller 10/20/2025: TODO_Permissions who should be able to view this RG? Who should be able to edit?

  * Update Fees on Save (non RG checkbox; visible based on the system switch ContractsAutoIncurEventsStartDate)
  * Fees and Payments RG (all fields editable in import; visible for admins)



  


  * Take a Payment (link to WSGI) 
  * Fee and Payment History (report link; opens the Fee and Payment History report for the record)
  * Forgive Fees (opens the
  * Current Due Date (displays the current due date)
  * Update Current Due Date (import; allows updating the current due date to any future date; cannot be set to an older date; creates a "System Note" documenting the due date change)



  


  


The Fees and Payments (aka Events) RG is how Ownly keeps track of what the customer owes and has paid.

  * RG 
    * Period (date; required)
    * Type (list of Event Types; required)
      * Damage Waiver Fee
      * Rent
      * Late Fee
      * Security Deposit
      * CRA
      * Processing Fee
      * Delivery Fee
      * Redelivery Fee
      * Reinstallation Fee
      * Reposession Fee
      * NSF Fee
    * Adjustment Type (list of Adjustment Types; required)
      * Incurred
      * Forgiven
      * Used
      * Paid
      * Refunded
      * NSF
    * Due Date (auto-calculated date; Period + # of Days override)
    * Subtotal (number; two decimals; required)
    * Cash Price Amount (number; two decimals; visible and required if Event Type is Rental Fee)
    * Taxable (checkbox)
    * Tax (auto-calculated)
      * Blank if the row is not taxable
      * For Incurred Rows this is the subtotal * the tax rate
      * For Paid Rows this is the amount from the Paid Tax Amount field 
    * Total (auto-calculated; Subtotal + Tax)
    * Forgiveness Reason (string; visible and required if Adjustment Type is Forgiven)
    * Entered (date)
    *     * Paid Tax Rate (number; 5 decimals; visible for "Paid" rows; the tax rate at which the payment was made)
    * Paid Tax Amount (number; 2 decimals; visible for "Paid" rows; the tax rate at which the payment was made)
    * Calculated Tax Rate (auto-calculated; 5 decimals)
      * For Incurred Rows this is a sum of the Tax Jar rates for State, County, City, and Other
      * For Paid rows this is the same rate as above, but pulled from the Incurred row for the period + event type
    * Calculated Tax Amount (auto-calculated; 2 decimals; Subtotal * Calculated tax rate)
    * Paid Tax Difference (auto-calculated; 2 decimals; visible for Paid rows; Paid Tax Amount - Calculated Tax Amount)
    * State (list of states; required for incurred rows)
    * State Rate (number; 5 decimals; required for incurred rows)
    * County (string; required for incurred rows)
    * County Rate (number; 5 decimals; required for incurred rows)
    * City (string; required for incurred rows)
    * City Rate (number; 5 decimals; required for incurred rows)
    * Other (string; optional)
    * Other Rate (number; 5 decimals; required for incurred where Other is not empty)
    *     * Subtotal Balance (auto-calculated; 2 decimals; visible for incurred rows; subtotal - subtotal from all paid rows for the event + period)
    * Tax Balance (auto-calculated; 2 decimals; visible for incurred rows; Subtotal Balance from above * calculated tax rate)
    * Total Balance (auto-calculated; 2 decimals; visible for incurred rows; Sum of Subtotal Balance and Tax Balance from above)
    *     * Payment ID (hidden; link to payment)


