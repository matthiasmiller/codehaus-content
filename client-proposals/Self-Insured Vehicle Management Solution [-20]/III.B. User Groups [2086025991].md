3.2. User Groups

  


Requirements

The Solution uses various User Groups to determine permissions for different categories of users. Each user has a User Profile in the Solution that is assigned to one or multiple User Groups. Note that the User Group (used for User Profiles / user logins) is distinct from the Contact Type (used for Contact records).

  


The following are the User Groups to be used in this Solution. The data access details included here are generalizations (see the Permissions section of this proposal for full details).  

  


  * "Administrators" User Group (Used for Admins. Users in this group have access to view and edit everything in the Solution.) 
    * Account Type: "Administrator"
    * Notes: N/A (blank)
    * Restricted Data Policy: N/A  
  * "Batch Processes" User Group (Used for Silverloom background tasks, etc. (not by real people). Users in this group have access to view and edit limited items in the Solution.) 
    * Account Type: "User"
    * Notes: N/A (blank)
    * Restricted Data Policy: "Default" (see corresponding spec)
  * "Standard Users" User Group (Used for non-Admin agents. Users in this group have access to view non-Admin features, and can edit data for their own clients.) 
    * Account Type: "User"
    * Notes: N/A (blank)
    * Restricted Data Policy: "Agents" (see corresponding spec) 



  


Other Notes:

  * All User Groups are set up and configured within the system. This can be done by CodeCrafters or by any user with the "Edit User Groups and Profiles" Permission.
  * Other restrictions will not need to be manually configured within the Solution, as they are handled by coding.



  


Development Specification

TODO_NM / TODO_EM: Tim Reitz 08/01/2025: It looks like they might have been set up automatically (at least for the ZWW system). Is that the case, or do they need to be set up manually for each WA system?
