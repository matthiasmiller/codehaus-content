3.1.2. Login User Groups

  


Requirements

The Solution will use various User Groups to determine permissions for different users. Each user should be assigned to a User Group. Note that the User Group is distinct from the Contact Type.

  


The following are the User Groups to be configured by CCI/CH and used in this Solution. The data access details included here are generalizations (see the Permissions section of this proposal for the full details).   

  * Administrator: Has full access to the database.
  * Manager: Has access to most of the database, with some exceptions. 
    * Note that this user group may be added in a future phase
  * Standard: Has access to most of the database, but is limited from some things
  * Accounting: Has limited access, mainly only the financial reports. 
    * Note that this user group will be added in a future phase when invoices are added.
  * KC Innovations Cockpit: Only has access to incidents
    * [https://think.apphosting.zone/Detail/Edit/2?RecordType=UserGroups&NumberID=-5&ShowTitleBar=true&](https://think.apphosting.zone/Detail/Edit/2?RecordType=UserGroups&NumberID=-5&ShowTitleBar=true&)
    * This is for a customer that works as a subcontractor, selling products for a commission, to allow them to access the Solution to create incidents directly in the Solution rather than sending everything over via email.
    * Intended to be linked with the Restricted Data Policy "KC_Innovations".



  


Development Specification

Mockup: N/A

  


TODO_IDD / TODO_JM: "Manager" user group. 

  


BID: 0.25 days for CH to support/deploy
