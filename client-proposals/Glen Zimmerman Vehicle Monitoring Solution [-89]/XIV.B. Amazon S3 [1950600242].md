14.2. Amazon S3

TODO_VA: Tim Reitz 01/17/2026: I think the only thing that we might use this for in photos on the Vehicle record. Let's determine whether we need it. 

  


The Solution integrates with Amazon S3 for storage of various files. This reduces the storage cost compared to storing these files withing the AppHosting Database. 

  


S3 is used to store the following: 

  * Photos on Vehicle records 



  


CodeCrafters will manage the S3 account and the integration to the Silverloom Solution. CodeCrafters provides up to 10 GB of S3 storage as part of the monthly base subscription; if more storage is needed, CodeCrafters will provide up to 1 terabyte for an additional fee (currently $25/month). 

  


Note that links to files in the S3 account can be opened by anyone with the link, not only people who are logged into the Solution. However, the links automatically expire for everyone after 15 minutes (standard). If a new link is needed, a user can open the desired file from the Solution and copy the URL (the expiration is automatically built into the link).

  


\-------------------------

Dev Spec notes for the designers: 

[ ] TODO_CLIENT: How long do you want the link to last? Default is 15 minutes, but it can be set to any number of minutes or days. 

[ ] Make sure each instance has the following RG + "Add" link: 

  * 


[ ] Note the Wiki page for setting up the S3 account with the client: ____ (TODO_) 

[ ] Add a note to the deployment incident to set up the S3 account with the client

[ ] Add a note to the deployment incident to ask Josh (??) to set up the integration in the live system

  


TODO_: (leave in dev spec) Template for email to Josh when the developers are ready for S3 integration to be set up: 

[ ] Sent for test system (development / start of testing) 

[ ] Sent for live system (deployment; can be a reply all to the email for the test system) 

To: JoshN, main developers, other(s) as needed

Subject: Setting up S3 integration for __ (Client Code) system

Body: 

Hi Josh,

  


We are ready for S3 integration to be set up for the new __ (Client Code) (__ (client / system name)) system. Here is some information:

  * PC for linking work: __
  * Link to test subscription record (__(subdomain)): __ (link)
  * Link to main subscription record (__(subdomain)): __ (link)
  * Spec (S3 notes in row __): __ (link)
  * Link expiration: Set to __ days
  * Database level(s): __ (row __ in spec) 



  


Here is your login info for the system: (make sure Josh has a user profile in each system)

  * Username: __
  * Temp. PW: __ 



  


We would like for this to be done by __, if possible. Let me know if there's anything else you need from us! Thanks!
