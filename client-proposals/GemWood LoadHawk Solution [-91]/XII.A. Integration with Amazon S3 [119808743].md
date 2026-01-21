12.1. Integration with Amazon S3

  


Requirements

The Solution integrates with Amazon S3 for storage of various uploaded files. This reduces the storage cost compared to storing these files within the Silverloom Database. 

  


S3 is used to store the following: 

  * Original Purchase Orders from Buyers (Purchase Order record)
  * Original Delivery Tickets from Members (Delivery Ticket record)
  * Buyer Grade Reports from Buyers (Delivery Ticket record)
  * Member Payment Attachments (Payment record | Member Payment detail screen) 
  * Buyer Payment Attachments (Payment record | Buyer Payment detail screen) 



  


CodeCrafters will manage the S3 account and the integration to the Silverloom Solution. CCI provides up to 10 GB of S3 storage as part of the monthly base subscription (no extra charge), but if more storage space is needed, CCI will provide up to 1 terabyte for an additional fee (currently $25/month as of the time of the Phase 1 proposal). 

  


Note that links to files in the S3 account can be opened by anyone with the link, not only people who are logged into the Solution. However, the links automatically expire for everyone after 180 days (custom). If a new link is needed, a user can open the desired file from the Solution and copy the URL (the expiration is automatically built into the link).

  


Development Specification

TODO_PRICING: Tim Reitz 12/06/2024: Not included in the HLD.

  


TODO_CCI: Tim Reitz 12/31/2024: Note that the expiration date for these links is to be 180 days (this might require work by Josh).
