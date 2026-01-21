3.2. User Groups

The ProEstimator Solution uses various User Groups to determine permissions for different categories of users. Each user has a User Profile in the Solution that is assigned to a User Group. Note that the User Group (used for User Profiles / user logins) is distinct from the Contact Type (used for Contact records).

  


The following are the User Groups to be used in this Solution. The data access details included here are generalizations (see the Permissions section of this proposal for full details).   

  


  * "Full Access Users" User Group (Used by senior staff. Users in this group have full access to the system, including configuring permissions and user accounts.) 
    * Account Type: "Administrator" 
  * "Senior / Pricing Users" User Group (Used by senior Sales Reps. Users in this group have access to edit Sales Items configurations, but are not able to configure permissions and user accounts.) 
    * Account Type: "User" 
  * "Sales Reps & Standard Users" User Group (Used by all other users, such as office staff and general sales reps. Users in this group have access to edit customers and proposals, but are not able to edit Sales Items or configure permissions and user accounts.) 
    * Account Type: "User" 
  * "Can Edit Automated Proposal Groups" User Group (Used by any user(s) that need to have the ability to create/edit Automated Proposal Group records. This is set up as a special User Group with only one Permission, since the Solution does not allow individual Permissions to be added to a User once the User is part of a User Group. Users in the "System Administrators" User Group can add/remove themselves or other Users.) 
    * Account Type: "User"
  * "Schedulers" User Group (Used by any user(s) that need to have the ability to set the "Scheduled" checkbox and "Scheduled Start" date fields on Proposal records. This is set up as a special User Group since the Solution does not allow individual Permissions to be added to a User once the User is part of a User Group. Users in the "System Administrators" User Group can add/remove themselves or other Users.) 
    * Account Type: "User"
  * "Support - Silverloom" (standard; set up manually):
    * Account Type: "Administrator"
    * Notes: Used for CodeCrafters employees and representatives with access to the software for support purposes. Users in the Group have full view & edit access to the entire database. 
    * Restricted Data Policy: N/A 



  


Other Notes:

  * All User Groups are set up and configured within the system. This can be done by CodeCrafters or an admin user. 
  * Additional User Groups could be added at some point in the future, but should be documented here.
  * Other restrictions will not need to be specially configured within the Solution, as they are handled by coding.


