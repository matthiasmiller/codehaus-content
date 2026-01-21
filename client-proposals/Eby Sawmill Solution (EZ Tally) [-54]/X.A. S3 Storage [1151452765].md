10.1. S3 Storage

  


Requirements

The Solution integrates with Amazon S3 for storage of various files. This reduces the storage cost compared to storing these files withing the AppHosting Database. 

  


S3 is used to store the following: 

  * Images for Export Tallies



  


CodeCrafters will manage the S3 account and the integration to the AppHosting.zone Solution. CCI provides up to 10 GB of S3 storage as part of the monthly base subscription; if more storage is needed, CCI will provide up to 1 terabyte for an additional fee (currently $25/month). 

  


Note that links to files in the S3 account can be opened by anyone with the link, not only people who are logged into the Solution. However, the links automatically expire for everyone after 15 minutes.

  


Development Specification

Mockup: N/A 

  


Dev Spec notes for the designers: 

  * Make sure each instance has an RG with the following: 



\- Name (read-only)

\- Download link

\- Date (read-only)

\- Time (read-only)

\- Delete link

\- Add link (outside the RG)
