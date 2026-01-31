8.2.6. Balloon Payments - TODO_SETH

Seth Miller 01/27/2026: TODO_SETH. Spec and delegate [[PC0189386]]

  


On the Contract:

  * Balloon Payments section
    * Minimum % of Cash Price (2 decimals)
    * Method
      * Combine Final Monthly Payments (included in contract value)
      * Invoice After Contract Term (in addition to contract value)



  


Fee Type:

  * Add a Fee Type of "Balloon Payment"



  


On the Contract:

  * Copy the values across from the definition and store.
  * Calculate the Minimum Balloon Payment (% times Cash Price)
  * Calculate the actual balloon payment
    * For "Combine Final Monthly Payments", round up to the nearest multiple of monthly rent (should always come out to 3mo)
    * For "Invoice After Contract Term" just use the actual amount



  


  * For "Combine Final Monthly Payments":
    * Remove the balloon payment from the contract value (i.e. stop before paying the balloon payment)
    * When calculating invoices, on a 36mo contract, at month 34 you'll invoice 3 months at once.
  * For "Invoice After Contract Term" invoice the balloon payment as a Fee Payment at month 37.



  


NOTE:

  * In no situation should we ever got to a place where the EPO is less than the balloon payment. If this is the case, let's just top off the final non-taxable EPO amount with a "Balloon Payment" item and keep moving. I think this can happen in the 2nd-to-last month of "Invoice After Contract Term"


