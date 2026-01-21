10.3.1. Prepay Discount

  


Requirements

This is an ad-specific discount that applies to runnings of "Pay with Credit" ads, for as long as there is credit to pay for it. This is configured with a Sales Item and is applied automatically to any ad with the "Pay with Credit" checkbox filled. 

  


If there is not enough credit to pay for the full price of a "Pay with Credit" ad, apply the discount to the portion of the ad that the available credit would cover. 

Example: If there is an ad that costs $100.00 and the customer only has $50.00 in available credit, the credit would cover $52.60 of the original Ad Price (the 5% discount on that portion is $2.60, which takes it down to $50.00), and the customer would be billed for the balance of $47.40. 

  


The Prepay Discount comes off after the Multi-Run or Special Discount has been taken off the total.

Example: A customer wants to run 10 ads with an Ad Price of $100.00 each, and prepay for them. The Multi-Run Discount of 15% would be $15.00 for each ad, reducing the price to $85.00. Then the Prepay Discount of 5% would be $4.25, reducing the price to $80.75. The customer would be invoiced for $807.50 in credit, and when the ads are run and invoiced, they would be reduced to $80.75 each.

  


Note that Special Placement Charges do not get discounted by either the Multi-Run/Special Discount or the Prepay Discount.

  


Development Specification

We should round at each step of calculating prices and discounts.

  


Special Placement charges don't get either the Multi-Run/Special Discount or the Prepay Discount. Ellis can decide whether this should be hard coded or whether we set a flag on the SKU.
