10.3.1. User Groups

The Solution uses various User Groups to determine permissions for different categories of users. Each user has a User Profile in the Solution that is assigned to a User Group. Note that the User Group (used for User Profiles / user logins) is distinct from the Contact Type (used for Contact records).

  


The following are the User Groups to be used in this Solution. The data access details included here are generalizations (see the Permissions section of this proposal for full details).  

TODO_PERMISSIONS: 

  * Note that data access should be driven by Permissions rather than by User Group. 
  * Note that we should avoid using "Administrator" as a User Group name, to avoid confusion or over-use. 
    * TODO_: Let's find and replace "admin" and "administrator" as able/needed.



  


  * "_____" User Group (Used for ___. Users in this group have access to view and edit ___.) 
    * Account Type: "__"



  


Other Notes:

  * The User Groups are hard-coded, meaning that any changes should be coordinated with CodeCrafters. 
    * OR 
  * All User Groups are set up and configured within the system. This can be done by CodeCrafters or an admin user.
  * Other restrictions will not need to be specially configured within the Solution, as they are handled by coding.


