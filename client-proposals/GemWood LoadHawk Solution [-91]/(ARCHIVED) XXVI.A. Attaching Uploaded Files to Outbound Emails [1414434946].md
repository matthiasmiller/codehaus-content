26.1. Attaching Uploaded Files to Outbound Emails

  


Requirements

Sean Miller 04/30/2025: Moved to [[[IN11439](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11441&)]] - ZGW - Attaching Uploaded Files to Outbound Emails

  


  


Special handling could be designed and coded to allow for attaching uploaded files to emails (i.e. the Buyer Grade Report PDF from the Buyer that was uploaded to the Delivery Ticket could be attached to the "Delivery Ticket Closed" email). This is a feature that the Silverloom platform does not currently support.

  


Development Specification

_VA: Tim Reitz 12/03/2024: This is an email that is sent automatically when a Delivery Ticket is closed. Should look different from the Member Payment Issued email to help avoid confusion.

Includes:

[X] Title includes the

[X] Body: (memo in SS) "this delivery ticket has been closed"

[X] Delivery Ticket Printout PDF (generated from the software)

[ ] Buyer Grade Report (__

_EM: Tim Reitz 12/03/2024: DD would like to include this, but a lot of the Members are receiving these emails via ibyFax, so including a link doesn't do any good.

Could they take a screenshot and paste it into a memo, to be printed in a PDF? (but they've had trouble with screenshots not being clear enough when sent this way)

Can we somehow generate a new PDF from an uploaded PDF? 

_EM: Tim Reitz 12/06/2024: Possible options (Ellis wants to discuss further with Josh): 

  * Doing coding to be able to attach the uploaded file (from S3). 
    * Would be cheapest to do this as a separate email
    * More expensive to include it with other content (i.e. the main email)
  * It would be a cheap option to include screenshots pasted into memos, but we're not very confident that it would be a good option. 



Let's include this as an add-on feature in the pricing.
