10.6. Internal Fee Payout Issued Email

  


Requirements

Overview: This email merge is used to notify a Payee that an internal fee payment has been issued. It is sent from a Delivery Ticket record when a user checks the "Paid" checkbox in the "Internal Fee Payouts Breakdown" table.

  


From: The email address specified in SMTP settings

  


To:

  * Any primary email address(es) for the Payee selected on the corresponding row on the "Internal Fee Payouts Breakdown" table on the Delivery Ticket



  


CC:

  * N/A



  


BCC:

  * N/A



  


Reply To: Same as the "From" email address

  


Subject: "Internal Fee Payout Issued"

  


Attachments: 

  * N/A



  


Body:

  


Hello, 

  


Your internal fee payout has been issued by GemWood for the following delivery ticket(s):

<List of included Delivery Tickets and their Payout amounts in the following format:

<Ticket #> $<Payout $>

<Ticket #> $<Payout $>

etc.>

  


Total: $<Sum of all Payout $ in the email>

  


Thank you!

  


Other Notes:

  * The GemWood logo and signature line are hard-coded at the bottom of this email merge.



  


Development Specification

Change Requests:

  * Ben Reitz 10/08/2025: [[[IN11670](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11672&)]] - ZGW - Add "Internal Fee Payout Sent" and "Sales Commission Paid" emails


