10.3. Handling Prepaying

  


Requirements

This prepay/credit system is designed to handle prepayments. This might be built out as a future addition rather than part of the initial solution. 

  


Overview:

PNP offers a Prepay Discount if a customer prepays for ads (currently 5%). See additional details in the corresponding section of this proposal.

  


Information about a customer's available credit will be shown in the Prepay/Credit section on the Customer/Ads Page (see that section of this proposal).

  


Each Ad Detail has a "Pay with Credit" checkbox that will be reflected on the individual runnings of that ad. If this is checked for a running of an ad, the system will apply credit from the customer's Available Credit to that ad when it is invoiced, and apply the 5% Prepay Discount.

  


If a customer simply wants to add a certain credit amount to their account, they can pay that much and it would be  applied to their Available Credit, from which payments for future "Pay with Credit" ads can be drawn. 

  


If a customer wants to prepay for a certain ad for a certain period of time, the amount they pay would be the ad price multiplied by the number of times they want to run the ad, and reduced by the Multi-Run or Special Discount (as applicable) and the 5% Prepay Discount, and including Special Placement Charges (as applicable). If this is for ads that are already scheduled and marked "Pay with Credit", the amount would automatically show up in the Prepay section of the Customer/Ads Page. If not, the User would need to calculate and invoice this manually, accounting for the 5% discount.

  


As ads are run for a customer with available credit, the ads marked "Pay with Credit" are invoiced as usual and the appropriate Prepay Discount and credit amount is automatically applied to them. The invoices are automatically marked Paid if the available credit covers the full amount, and the paid invoice is sent to the customer. If there is not enough available credit to cover the full amount, the balance is displayed on the invoice and billed to the customer. 

  


Contact Customizations: The Customer/Ads Page will be customized to handle tracking and adding credits. See more details in the Customer/Ads Page section of this proposal. 

  


Invoice Customizations: Invoices will be customized to handle adding, storing, and using credits. See more details in the the Invoice Details section of this proposal.

  


Development Specification

Credits are to be stored on Invoice when it is marked paid. Available credit is used by calculating the total credit of all paid invoices.
