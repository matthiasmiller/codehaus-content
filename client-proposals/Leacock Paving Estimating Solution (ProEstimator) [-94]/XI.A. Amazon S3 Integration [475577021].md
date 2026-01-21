11.1. Amazon S3 Integration

  


Requirements

The Solution integrates with Amazon S3 for storage of various files. This reduces the storage cost compared to storing these files within the AppHosting Database. 

  


S3 is used to store the following: 

  * Proposal record - Documents Section: Proposal Attachments for the Proposal records (jobsite photos, job plan PDFs, take-off documents, etc.) 



  


CodeCrafters will manage the S3 account and the integration to the AppHosting.zone Solution. CodeCrafters provides up to 1 TB of S3 storage at a cost of $25/month. 

  


Note that links to files in the S3 account can be opened by anyone with the link, not only people who are logged into the Solution. However, the links automatically expire for everyone after 365 days (custom setting). If a new link is needed, a user can open the desired file from the Solution and copy the URL (the expiration is automatically built into the link).

  


Other Notes: 

  * To maximize storage space, photos may be taken at a lower resolution (or resized to a lower resolution prior to uploading).



  


Development Specification

TODO_: Tim Reitz 12/12/2025: Make sure that we're billing them for this. 

  


TODO_: (leave in dev spec) Template for email to Josh when the devs are ready for S3 integration to be set up: 

To: JoshN, main developers, other(s) as needed

Subject: Setting up S3 integration for __ (Client Code) system

Body: 

Hi Josh,

  


We are ready for S3 integration to be set up for the new __ (Client Code) (__ (client / system name)) system. Here is some information:

  * PC for linking work: __
  * Link to test subscription record (__(subdomain)): __ (link)



Tim Reitz 11/12/2025: This has been done already. 

Ben, I can do a reply all to the email that I sent to Josh to request the test system to be set up -- you can just let me know when you're ready for that. Thanks! 

  * Link to main subscription record (__(subdomain)): __ (link)
  * Spec (S3 notes in row __): __ (link)
  * Link expiration: Set to __ days
  * Database level(s): __ (row __ in spec) 



  


We would like for this to be done by __, if possible. Let me know if there's anything else you need from us! Thanks!
