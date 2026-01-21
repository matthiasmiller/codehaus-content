12.1. Amazon S3

  


Requirements

The Solution integrates with Amazon S3 for storage of various files. This will reduce the storage cost compared to storing the files directly in the AppHosting database.

  


S3 is used to store the following:

  * Audio/video files for Development Resources
  * Attachments for Development Resources 
  * Possibly other items in the future



  


CodeCrafters/Silverloom manages the Amazon S3 account that is linked to the Members Exchange / CRM Solution. Note that this is different from the original plan, in which Symbiz would have managed the S3 account. 

  


Note that links to files in the S3 account can be opened by anyone with the link, not only people who are logged into the Solution. However, the links automatically expire for everyone after 15 minutes.

  


Development Specification

_JB: Tim Reitz 12/15/2023: Are we also using this for the member profile photo and the Resource cover image? 

TODO_VA: Tim Reitz 06/24/2024: These are just being stored in memo fields on the database (then the thumbnail feature accesses them from there). 

  


Tim Reitz 06/06/2023: make sure each instance has the following RG: 

\- Name (read-only)

\- Download link

\- Date (read-only)

\- Time (read-only)

\- Delete link

\- Add link
