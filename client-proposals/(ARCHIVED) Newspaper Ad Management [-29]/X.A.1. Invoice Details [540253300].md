10.1.1. Invoice Details

Columns:

Invoices should have the following columns: 

  * Quantity (default to 1 and read-only for ads; editable and default to 1 for credit purchases)
  * Sales Item Code (this would not show on the printout)
  * Description (based on the editable expression on Configure Publication)
  * Unit Price (based on 
  * Price (Quantity x Unit Price)



  


Itemization Line Items:

Invoices for Ads would use the following format: 

  * The first line item would be for the ad
  * The second line item would be for the Multiple Run or Special Discount, if any; this would be displayed as a negative number in the Unit Price and Price columns
  * The next line item would be for Special Placement charges, if any (these do not get discounted by any discount)



  


For invoices with multiple ads, this pattern will repeat multiple times as needed. 

  


  


Check/Cash/Card Payments:

The invoice detail should have a "Receive Payment" link that opens the Receive Payment page. See more details in the corresponding section of this proposal. 

  


Auto-Pay: 

If the Customer has the auto-pay option selected for a stored card, the payment should be run automatically when the invoice is marked Invoiced. See more details in the Payments section of this proposal. 

  


Discounts & Fees: 

Customizations are being made to the Discounts & Fees child screen, accessible via the Discounts & Fees button. See more details in the Terms and Late Fees sections of this proposal. 

  


Prepay/Credit:

Invoices will receive customizations for adding or using prepay credit.

  


Credits will be stored on invoices and linked out to the corresponding Customer/Ads Pages.  

  


Customization to the Itemization section: 

Above "Total Amount", the following items should be added:

  * Available Remaining Credit (read-only; display the total for the selected Customer)
  * Apply Credit (button; see details in the Handling Prepaying section and subsections of this proposal)
  * Credits (read-only; total amount of credit purchased and applied on this invoice - the Total Purchased Credit and Total Applied Credit from the Credit section; read-only; auto-fill from the Credits section of the invoice; positive for net purchased credit, negative for net applied credit)



  


Credit section: This is a new custom section on the invoice below the Itemization section. It contains the following: 

  * Credits embedded spreadsheet: This will have the same columns as the Itemization embedded spreadsheet. Line items for purchased credit would be positive numbers, and line items for applied credit would be negative numbers.
  * Total Purchased Credit (read-only; sum of Purchased Credit field in the Credits embedded spreadsheet)
  * Total Applied Credit (read-only; total of Applied Credit field in the Credits embedded spreadsheet; negative number)



  


Items from the Credits embedded spreadsheet will appear on the invoice printouts as line items, like the items from the Itemization Spreadsheet.
