10.5. Commision Payment Issued Email

  


Requirements

Overview: This email merge is used to notify a Salesperson that commission payment has been issued. It is sent from a Delivery Ticket record when a user checks the "Commission Paid" checkbox.

  


From: The email address specified in SMTP settings

  


To:

  * Any primary email address(es) for the Salesperson selected on the Delivery Ticket



  


CC:

  * N/A



  


BCC:

  * N/A



  


Reply To: Same as the "From" email address

  


Subject: "Commission Payment Issued"

  


Attachments: 

  * N/A



  


Body:

  


Hello, 

  


Your commission payment has been issued by GemWood for the following delivery ticket(s):

<List of included Delivery Tickets and their Sales Commission amounts in the following format:

<Ticket #> $<Sales Commission $>

<Ticket #> $<Sales Commission $>

etc.>

  


Total: $<Sum of all Sales Commission $ in the email>

  


Thank you! 

  


Other Notes:

  * The GemWood logo and signature line are hard-coded at the bottom of this email merge.



  


Development Specification

Change Requests:

  * [[[IN11670](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11672&)]] - ZGW - Add "Internal Fee Payout Sent" and "Sales Commission Paid" emails


