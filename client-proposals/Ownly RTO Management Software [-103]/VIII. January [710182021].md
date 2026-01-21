8\. January

Duane Burkholder 01/07/2026: TODO_IDD: I ran into some things when implementing contract definitions.

  * Late Fees: Several of our contracts have language that we do not support. For one of them we can just ignore but one of them we will need to support.
    * 5% of payment or 15.00 whichever is greater -  We could ignore this one because you can just use the fixed amount.
    * 5% of payment or 10 whichever is lessor. - This one we can't ignore as it is a variable that could potentially get us in trouble. That being said if we support the lessor we could support the greater.
  * Damage Waiver Fee: 
    * I forgot that some states disallow Damage Waiver as a feature. Currently we are validating that a contract definition has damage waiver price set.
    * We also have damage waiver fees as a percentage of payment. IL allows us to charge 10% of payment


