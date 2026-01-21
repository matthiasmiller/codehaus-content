10.1.3. Terms

  


Requirements

Invoices currently have a field to enter information about terms. This will display a default text, such as "2% discount on balance due if paid within 10 days". The customer will calculate this discount on their own and send their payment, then the software user receiving the payment will manually enter the percentage in the Discounts & Fees on the invoice and mark it paid. 

  


If an ad is being paid with prepaid credit, the Prepay Discount overrides the 2% prompt payment discount. 

  * If an invoice contains only ads that were prepaid, do not include the terms for the 2% discount (the Terms should instead be left blank)
  * If an invoice contains both ads that were prepaid and ads that were not, the 5% prepay discount has already been applied to the prepaid ads, and the 2% discount applies only to the Total Amount that remains (this will be handled automatically since the 2% only applies to the balance due).



  


Development Specification

On the topic of being able to enter a % and have the software calculate the rest, John said, "You need to call up QB and tell them how to do that." :-)
