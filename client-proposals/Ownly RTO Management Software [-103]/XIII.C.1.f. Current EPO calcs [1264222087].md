13.3.1.6. Current EPO calcs

When a customer pays off a rental contract early, the system calculates the Early Payoff (EPO) amount based on what’s still owed, minus an early payoff discount, plus any required fees and taxes.

This document explains how that total is determined so you can review or explain it clearly.

1\. Start with the rental balance

We begin with the total contract value and subtract all payments received so far.

That gives the rental balance — the portion of rent the customer hasn’t yet paid.

2\. Remove unpaid rental fees (not discounted)

If there are past-due rental fees, those are excluded from the discounted balance.

They’ll be added back later at full value, since discounts only apply to current/future rent.

3\. Apply the EPO discount

The contract’s EPO Discount % (from ContractRentalFee%) is applied to the balance that’s eligible for early payoff.

This reduces what the customer owes on the remaining rent.

Example:

If $2,850 of rent remains and the discount is 10%, the discount is $285.

4\. Add back fees and CRA tax

After applying the discount, the system adds back:

  * Past-due rental fees (full amount)
  * Other unpaid fees (from ContractFeeBalanceTotal)
  * CRA with tax (the tax portion of any Customer Responsibility Amount)



5\. Subtract untaxed CRA subtotal

Because CRA with tax was added in step 4, the untaxed CRA subtotal is then subtracted back out.

This leaves only the CRA tax in the final payoff — ensuring the customer pays the correct tax but not the CRA itself again.

6\. The result: Early Payoff amount

After all adjustments, the final total is the Early Payoff Amount — the amount due to close out the rental contract early.

Example

Step| Description| Amount  
---|---|---  
Contract total|   
| $5,000  
Amount paid|   
| –$2,000  
Rental balance|   
| $3,000  
Less unpaid rental fees|   
| –$150  
Balance eligible for discount|   
| $2,850  
Less 10% EPO discount|   
| –$285  
Add CRA (with tax)|   
| +$214  
Add unpaid fees|   
| +$150 + $25  
Subtract CRA subtotal|   
| –$200  
Final Early Payoff|   
| $2,754  
  
Summary

The EPO calculation:

  * Discounts only the remaining rent balance
  * Excludes past-due fees from the discount
  * Adds back all unpaid fees and CRA tax
  * Subtracts the untaxed CRA subtotal
  * Produces the customer’s final payoff amount


