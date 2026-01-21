3.3. User Groups

TODO_AP: Ben Reitz 11/14/2025: Compare/standardize as needed.

  


The Solution uses various User Groups to determine permissions for different categories of users. Each user has a User Profile in the Solution that is assigned to a User Group. Note that the User Group (used for User Profiles / user logins) is distinct from the Contact Type (used for Contact records).

  


The following are the User Groups to be used in this Solution. The data access details included here are generalizations (see the Permissions section of this proposal for full details).  

  


  * "Full Administrators" User Group (Used by senior staff. Users in this group have full access to the system, including configuring permissions and user accounts.) 
    * Account Type: "Administrator"
  * "Admin - Without Manage Deliveries" User Group (Used by senior staff. Users in this group have access to view and edit everything except for editing the Production Calendar and the Admin-only fields on the Production Line record.) 
    * Account Type: "User"
  * "Standard Users" User Group (Used by all other users, such as office staff and sales reps. Users in this group have access to edit Contacts, Orders, and Deliveries, but are not able to edit the Production Calendar, Admin-only fields on the Production Line record, or configure permissions and user accounts.) 
    * Account Type: "User"
  * "Standard Users - With Manage Deliveries" User Group (Used by all other users, such as office staff and sales reps. Users in this group have access to edit Contacts, Orders, and Deliveries, and the Production Calendar are not able to edit the Admin-only fields on the Production Line record, or configure permissions and user accounts.) 
    * Account Type: "User"



  


Other Notes:

  * All User Groups are set up and configured within the system. This can be done by CodeCrafters or an admin user.
  * Other restrictions will not need to be specially configured within the Solution, as they are handled by coding.


