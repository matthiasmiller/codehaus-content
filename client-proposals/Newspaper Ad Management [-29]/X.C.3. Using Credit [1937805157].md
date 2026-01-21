10.3.3. Using Credit

  


Requirements

When auto-invoicing ads (from the menu option or from the Customer/Ads Page), available credit should be applied automatically to invoices with "Pay with Credit" ads.

  


The ads, as well as any Multi-Run/Special Discount and any Special Placement Charges, should be entered in the Itemization embedded spreadsheet as usual, along with any corresponding Prepay Discount line items.

 

The credit is applied to the invoice as a single line item in the Credits embedded spreadsheet for the amount needed to cover the "Pay with Credit" items in the Itemization embedded spreadsheet (or the full Available Credit amount if there is not enough). This single line item should have "Applied Credit" as the Description.

  


When an invoice that has applied credit and a zero balance, the status should be automatically updated to Paid.

  


If there is not enough credit to pay for the ad or invoice, the system should apply the full available amount to the invoice, and the customer should be billed for the difference. There should be a warning on save/creation of invoices like this - "The selected customer does not have enough available credit to pay for the selected "Pay with Credit" ads, and needs to be billed". This warning should not display if the credit covered all the "Pay with Credit" ads and the remaining balance due is for other ads.

  


Using Lump-Sum Credit: 

If the customer wants to use (apply) a lump amount of credit to a purchase, the user should click the "Apply Credit" button in the Itemization section of the invoice to automatically apply credit from the customer's Available Credit. This calculates and applies the correct Prepay Discount and Applied Credit based on the Invoice Balance and the Available Remaining Credit. This amount will not be editable. It will apply up to the full Available Credit amount if needed. 

  


Overpay Situations: If a customer overpays, the overpayment amount would be added to their credit balance. The User would change the invoice status to Draft, add the overpayment amount as a credit, change the invoice status to Paid, and save it. A new copy of the invoice can be sent to the customer if desired.

  


Development Specification

Apply Credit Button: Rough explanation on how to calculate the amounts:

  * Add all prepay items in the itemization RG
  * Add all applied credit AND available credit
  * Find the TOTAL amount of credit that can be applied to the invoice, regardless (this should use the same method we use when calculating a new invoice)
    * Add an adjustment to make the total of prepay percentages match the new required amount
    * Add an adjustment to make the total of all applied credit match the new required amount


