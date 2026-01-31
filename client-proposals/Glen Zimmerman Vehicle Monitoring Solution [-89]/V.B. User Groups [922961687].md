5.2. User Groups

  


Requirements

*Done. 

  


The Solution uses various User Groups to determine permissions for different categories of users. Each user has a User Profile in the Solution that is assigned to one or multiple User Groups. Note that the User Group (used for User Profiles / user logins) is distinct from the Contact Type (used for Contact records).

  


The following are the User Groups to be used in this Solution. The data access details included here are generalizations (see the Permissions section for full details). 

  


  * "Full Access Users" (custom):
    * Account Type: "Administrator"
    * Notes: "Used for <System Name>-specific Administrative users. Users in this Group have full view & edit access to the entire database." 
    * Restricted Data Policy: N/A 



  


  * "Group Admins & Account Resellers" (custom):
    * Account Type: "User"
      * Note that this is a restricted user group. 
    * Notes: "Used for Group Admins, Account Resellers, and Reseller Reps. Users in this Group have access to view & edit most of the database." 
    * Restricted Data Policy: N/A 



  


  * "Support - Silverloom" (standard; set up manually):
    * Account Type: "Administrator"
    * Notes: Used for CodeCrafters employees and representatives with access to the software for support purposes. Users in the Group have full view & edit access to the entire database. 
    * Restricted Data Policy: N/A 



  


  


Other Notes:

  * Unless otherwise noted, User Groups are hard-coded, meaning that any changes should be coordinated with CodeCrafters. 
  * Other restrictions do not need to be manually configured within the Solution, as they are handled by coding.
  * A few special User Profiles are included to manage various background tasks and processes. These include: 
    * "Administrator" (standard) 
      * Account Type: "User"
      * Notes: "Used for Standard Drivers, Account Managers. Users in this Group have very limited view & edit access." 
      * Restricted Data Policy: N/A 
    * "SYSTEM" (standard) 
      * Account Type: "User"
      * Notes: "Used for Standard Drivers, Account Managers. Users in this Group have very limited view & edit access." 
      * Restricted Data Policy: N/A 
    * "Traccar Sync" (custom; used to run the sync with Traccar; set up by CodeCrafters at deployment)
      * Account Type: "User"
      * Notes: "Used for Standard Drivers, Account Managers. Users in this Group have very limited view & edit access." 
      * Restricted Data Policy: N/A



  


Development Specification

TODO_NM (review): Tim Reitz 01/22/2026: Let's make sure that restricted user groups is the way to go (these users will need to be able to view and edit a lot of things, but not the Standard folder, report settings, etc.).
