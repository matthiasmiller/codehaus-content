8.2.5. Bad Debt

Seth Miller 01/27/2026: TODO_SETH. Spec and delegate [[PC0189385]]

  


NOTE: Once the contract closes, we will need to write this off as bad debt.

  


  * Proposal:
    * Bad Debt works like security deposit / CRA, except it's backwards (customer pays out first, then HOPEFULLY pays back in)
    * At contract closure
      * Create a payment in the RG that pays off all outstanding invoices using Bad Debt
    * Any future payments against bad debt will Incur Bad Debt for the amount of the payment
      * Only available in the admin portal
    * Could validate against outstanding invoices if you have a bad debt balance on a contract



  


TODO_SETH
