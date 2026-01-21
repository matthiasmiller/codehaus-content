12.31. Convenience Fees

Seth Miller 10/20/2025: TODO_Seth: [[PC0185255]].

  * Credit Card Convenience Fees (section) Matthias Miller 08/06/2025: This needs to be controlled via a hidden, read-only system switch that is turned off by default and can only be turned on by a system update.
    * Message -- bold, in red, yellow highlight: "By using this feature, you understand and agree that you are responsible to know your state's specific regulations for convenience fees. Changing convenience fees will not update existing contracts."
      * Update All Contracts - WARNING: This will change all future payments for all active contracts to use the updated convenience fees. (runs x30 that pushes these convenience fees onto active contracts)



  


  * TODO_SETH: The following payment methods get shipped when you turn this on:
    * Debit Card
    * Prepaid Card



  


  * RG of:
    * Payment Method (list of Payment Method; limited to ACH and Credit Card)
    * Fee Type (list of "Dollar Amount" or "Percentage")
    * Fee (editable macro for Fee $ when using Dollar Amount; otherwise, editable macro for Fee %; required)
    * Maximum (editable macro for Fee % when using Dollar Amount; otherwise, editable macro for Fee $)
    * Maximum Fee $ (hidden field; 2 decimals)
    * Maximum Fee % (hidden field; 2 decimals)



TODO_SETH - WE are NOT planning on freezing this on the contract record.

Seth Miller 10/20/2025: TODO_IDD: do we need a way for Convenience Fees to only be added/removed for new contracts (vs all existing contracts)

  


  


  


  


Seth Miller 10/20/2025: TODO_IDD: are convenience fees part of phase 1? 

We will need to think through how to handle fields if a company opts out of convenience fees after supporting them for a time
