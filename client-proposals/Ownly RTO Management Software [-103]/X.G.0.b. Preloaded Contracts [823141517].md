10.6.0.2. Preloaded Contracts

TODO_HLD - give a way to block payment methods (ACH & CHECK) on a contract

  


  


Seth Miller 11/14/2025: TODO_IDD. I just found the following notes at the bottom of the spec for contracts. Are these items we need to deal with now?

  * IMPORTANT: Contracts can be preloaded (i.e. entered before the buildings are built or delivered). The software will need to be able to flag contracts that haven’t been updated (i.e. not built or delivered in a timely manner). This will also control the timing of billing and payment to the manufacturer. The software needs to support contracts which end prior to the building being built or delivered.
  * We need validation:
    * If the Rental Company doesn't own the building, we need purchase information.
    * If the Rental Company DOES own the building, we do NOT need purchase information.
    * Matthias Miller 12/03/2025: We can't track this until we have transit tasks, and the payment is on the product record. And the idea of preloaded contracts is in the future.


