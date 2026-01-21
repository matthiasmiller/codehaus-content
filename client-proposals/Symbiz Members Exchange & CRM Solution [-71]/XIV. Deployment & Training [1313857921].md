14\. Deployment & Training

  


Requirements

CodeCrafters/CodeHaus will provide support and training for users, especially the admins, throughout the deployment of the software. This may include Zoom calls, recorded video walkthroughs, phone calls, emails, technical support, in-person work, etc. 

  


Admin users may be given access to a test system prior to/during deployment to allow for practicing and learning the system.

  


The background processes / scheduled tasks will be configured by CCI/CH as part of deployment.

  


Development Specification

DONE_DH: Tim Reitz 06/01/2023: What do you see as best? 

Tim Reitz 06/01/2023: Delbert personally likes the recorded video walkthrough. 

Could also look at a live in-person training at the next Symbiz Summit. 

  


access to the test system  or a deploy system

  


Jonathan Bergen 11/15/2023: User Groups:

Standard User:

This group will hold all non-admin users. Permissions for these users are determined by macros that check if they are a Facilitator and/or Regional Rep.

[ ] Create a Standard User group in deployment.

  


Symbiz Super Admin:

This group will hold all users who should have full access to records and reports, but not the system backend.

[ ] Create a Symbiz Super Admin group with the "is Symbiz Super Admin" permission.

[ ] This group should have permission to Edit the Contact Type Record.
