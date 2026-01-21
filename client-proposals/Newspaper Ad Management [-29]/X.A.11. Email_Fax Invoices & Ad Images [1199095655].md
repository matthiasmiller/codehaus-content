10.1.11. Email/Fax Invoices & Ad Images

  


Requirements

This feature allows for faxing or emailing invoices along with the corresponding ad image(s) to customers who have selected email or fax as their invoice preference. These can be sent on an individual basis or to all such customers at once. 

  


There will be the following Menu option for batch-sending the invoices and ad images: 

  * Send All Email/Fax Invoices & Ad Images



  


This batch-sending process is described in the "Print/Send Invoices" section of this proposal.

  


And there will be the following link on the Customer/Ads Page, as mentioned in that section:

  * Email/Fax Invoices & Ad Images



  


Clicking on this link will open the same report described in the "Print/Send Invoices" section of this proposal, but filtered to only show invoices for the current customer. As descrbed there, clicking the "Send All Email/Fax Invoices" button would generate an email for the customer.

  


Development Specification

Tim Reitz 03/09/2021: Any time we email/fax invoices, the image should go along.

  


Attaching Ads Images to Emails with Invoices: Maybe have an Ads Proof memo on the invoice and when an Email or Fax invoice is generated, automatically copy over the ad images. Or maybe link to the underlying S3 file or maybe link to the associated ads. This can be determined by the development team. The main reason to link it to the ad is so the invoice would update if they update the proof. One more idea is to add a custom field to the line items RG of the invoice that allows linking it back to a specific ad.
