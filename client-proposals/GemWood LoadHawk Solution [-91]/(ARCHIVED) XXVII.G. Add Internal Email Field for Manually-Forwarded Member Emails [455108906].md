27.7. Add Internal Email Field for Manually-Forwarded Member Emails

Sean Miller 04/29/2025: Moved to [[[IN11425](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11427&)]] - ZGW - Add Internal Email Field for Manually-Forwarded Member Emails

  


  


Currently the manually-forwarded emails for Members are specced to be sent to the internal GemWood email address specified in SMTP settings (probably [gemwood@timberdriven.com](mailto:gemwood@timberdriven.com)), for GemWood to manually download and attach the Buyer Grade Report file(s) and forward the email on to the Member. However, if a different internal GemWood email address is desired for handling these manually-forwarded emails to Members, the following could be added: 

  


Silverloom Settings: Add the following field to the custom Email Settings section: 

  * Internal Email for Forwarding (email field; used for sending the internal email if the "Manually forward web link attachments" checkbox is checked on a Member's Contact record; warning on Save if blank) 



  


Member Contact record & Delivery Ticket Closed Email specs: Update to note that the email would go to this email address rather than the "internal GemWood email address specified in SMTP settings". 

  


Estimated Cost: $100-200
