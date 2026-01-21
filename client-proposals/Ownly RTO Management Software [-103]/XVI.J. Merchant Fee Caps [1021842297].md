16.10. Merchant Fee Caps

MERCHANT FEE CAPS FOR CONVENIENCE FEES:

  * We could eventually consider getting more sophisticated when it comes to Stripe Payments but it's not necessary so we wont. We would add these fields.
    * Merchant Fee %
    * Merchant Transaction $
  * Note that when calculating the convenience fee of a transaction, you need to account for the convience fee of the overall transaction. For example, to calculate the total payment when using Stripe, you need to use this:
    * Charge Amount = (Target Amount + 0.30) / (1 - 0.029)
    * i.e. To net a $1000, you need a $29.59 convenience fee, charging a total of 1,029.59.


