16.1.2.2. Fees & Payments

Seth Miller 10/20/2025: THIS is old. Archiving

  


  


  * Fees (RG)
    * Fee Type (rental, DWF, Late, and fees from the Other Fees RG)
    * Due Date 
    * Fee Subtotal
      * Must be non-zero
      * if the amount is negative we assume this is a forgiveness row
    * Date Incurred (for any non-rental/DWF fee)
    * Taxable (checkbox)
    * Tax Amount (Fee Subtotal * Tax Rate)
    * Fee Total (Fee Subtotal + Tax Amount) Seth Miller 08/26/2025: TODO_IDD: does this look right?
    * Forgiveness Reason (required if amount is negative)
    * Amount Paid (macro calculating from the cached payment amounts). Not visible on forgiveness rows?
    * Amount Remaining (Fee Amount - Amount Paid - Forgiven amount) Not visible on forgiveness rows?



  


  * Rental Fee cannot be forgiven



  


Seth Miller 08/26/2025: TODO_IDD: what is the workflow for forgiving fees?

One option I thought of:

  * Have a "Forgive Fee" link in the RG. 
    * This is an import under the hood and requires saving the record before running. 
    * Prompts for amount to forgive (which must be less than or equal to the amount remaining for the fee) and forgiveness reason. 
    * Not visible for Rental Fees or fees that have been paid in full



  


TODO_IDD: confirm with Duane that we can edit due dates on any open period (overdue and unpaid or next unpaid)

TODO_IDD: design for moving period end dates

  


  


Seth Miller 08/26/2025: TODO_IDD: where do we store the tax rate?

  


  * Payments (RG)
    * Payment ID
    * Fee Type
    * Due Date
    * Payment Amount



  


  


Rental Fee Type due dates define the periods
