10.3.2. Adding Credit

  


Requirements

Credit can be added in three main ways:

  * Through the "Create Prepayment Invoice for Balance" link on the Customer/Ads Page
  * Through the "Create Prepayment Invoice for Amount" link on the Customer/Ads Page
  * Manually on an invoice (either on an invoice with ads or on a separate invoice)



  


Adding credit through the "Create Prepayment Invoice for Balance" link on the Customer/Ads Page: 

  * Clicking the link generates and opens an unsaved invoice for that customer. 
  * The embedded spreadsheet in the Credits section would be prefilled with line items for all the current and future scheduled "Pay with Credit" ads for the customer. The line items could include: 
    * Ad Size (listed with the full Ad Price)
    * Multi-Run/Special Discount (as applicable)
    * Prepay Discount
    * Special Placement Charge (as applicable). 
  * Any existing Available Credit for the customer would be subtracted from this total (as an "Applied Credit" line items), and the balance would be listed in the "Purchased Credit" line of the Itemization section. This balance should equal the "Total Credit to Collect" on the Customer/Ads Page. 
  * Review the invoice and save it. It can then be paid via credit/debit card or billed to the customer. 



  


Adding credit through the "Create Prepayment Invoice for Amount" link on the Customer/Ads Page: 

  * Clicking the link generates and opens an unsaved invoice for that customer. 
  * The embedded spreadsheet in the Credits section would be prefilled with the "Custom Credit to Collect" amount from the Customer/Ads Page (not linked to any Sales Item). This amount would be listed in the "Credits" line of the Itemization section. Note that existing Available Credit for the customer would NOT be subtracted from this total. Also, the other line items listed above would not be necessary for this method. 
  * Review the invoice and save it. It can then be paid via credit/debit card or billed to the customer. 



  


Adding credit manually on an invoice:

  * Open an existing invoice for the desired customer (for example, from the Invoices section on the Customer/Ads Page) or create a new invoice for the customer (for example from the Create Invoice link in the Invoices section)
  * Enter the desired credit amount in a new line on the Credits embedded spreadsheet and manually enter a description OR select from the Codes. Note that existing Available Credit for the customer would NOT be subtracted from this total. Also, the other line items listed above would not be necessary for this method.
  * Review the invoice and save it. It can then be paid via card or billed to the customer.



  


Development Specification

To generate the prepayment invoice, use a report with an autopush New Detail button. Use ask prompts and if needed detail variables to pass information to populate the invoice items. John will want to avoid additional clicks if possible. Ellis, let's negotiate if you think this is overly expensive. 

  


  


Notes: 

Tim Reitz 02/11/2021: John says that we need the flexibility to allow customers to make changes - he would lean toward credit.

  


Tim Reitz 02/15/2021: Matthias says we can't go down the middle (we have to either do credit or prepaid)...

  * Basic idea: 
    * Total "Pay with Credit" items
    * Subtract Total Available Credit (as a negative amount; could have a discount/SKU "Applied Credit" that could only be added to an invoice as a credit...)
    * Pay the balance
    * Have a Credits RG on the Invoice detail (mimic the itemization RG)
      * These would display under the Itemization section on the invoice printout (as a separate section), below the Sub Total...
    * Have a line for Prepay Discount in the Credits RG and the Itemization RG. 
    * Have a Prepay Discount SKU (another option would be to have a Prepay discount % on a per-sku basis...)



  


To add credit, take all future scheduled prepay ads and related charges/discounts and put them in the Credit RG on the invoice, subtract any current Available credit, and bill for the balance. 

  


To use credit, add a single line item to the credits RG for "Applied Credit" and the amount. The ads being paid would be on the Invoice RG. No credit checkbox. 

  


Have a line for Prepay Discount in the Credits RG and the Itemization RG. The prepay discount would be taken off the Invoice RG basd on the line items that are entered there. The prepaid ads being paid should correspond to the amount of credit being used.
