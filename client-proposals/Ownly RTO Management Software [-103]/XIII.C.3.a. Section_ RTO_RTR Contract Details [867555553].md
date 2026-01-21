13.3.3.1. Section: RTO/RTR Contract Details

  * RTR/RTO Contract Details section
    * Details (child screen with the following sections. All fields are read-only and copied from the contract definition unless otherwise noted. )
      * Contract Definition
        * Contract Definition ID (contract definition based on rental company, state, and contract type)
        * view (link to open the contract definition)
      * Contract Definition: Rent-to-Own Contract Types
        * RTO Type (list)
        * CRA (checkbox)
        * Disallow Increased Security Deposit (checkbox)
        * # Days Same as Cash (number)
      * Contract Definition: Rent-to-Own Financials
        * Term Length (number)
        * Cash Price % (number)
        * Rental Fee % (number)
        * Rate Divisor (number)
        * Requires Balloon Payment (checkbox)
        * Minimum Price (list)
        * % of Price (number)
      * Contract Definition: Late Fees
        * RG with the following columns:
          * Repayment Cycle (list)
          * Grace Period Days (number)
          * Method (list)
          * Fee $ (number)
          * Fee % (number)
          * Min Fee $ (number)
          * Max Fee $ (number)
          * Tax (number)
      * Contract Definition: Other Fees
        * RG with the following columns:
          * Other Fee Type (list)
          * Amount (number)
          * Taxable (checkbox)
        * Include DWF (Yes/NO list; required; editable; label is based on the rental companies DWF abbreviation)
          * defaults to blank but is required
          * when set to "No" this clears the Damage Waiver row from Other Fees AND removes all unpaid incurred DWFs
          * when set to "Yes" this adds the Damage Waiver row from the contract definition to Other Fees AND incurs fees for all incurred and partially paid or unpaid periods



Seth Miller 11/14/2025: TODO_KS: [[PC0186606]]. Incurring/removing fees is not done yet

  * Contract Entry
    * Security Deposit (number)
    * CRA (number)
  * Payment Calculations
    * Product Effective Value
    * Rental Base
    * Contract Value
    * Period Rental Subtotal
    * Period DWF Subtotal
    * Period Tax
    * Period Payment
    * Security Deposit
    * Cash Due



  


  * RTO Type (list; displays options from the linked contract definition)
  * Term Length (list; displays options from the linked contract definition)
  * Contract Value
  * Contract Balance
  * Payment Terms
  * Monthly Payment
  * Remaining Months
  * Early Payoff Amount


