4.2. User Groups

  


Requirements

The Solution will use various User Groups to determine permissions for different users. Each user's User Profile is assigned to a User Group. Note that the User Group is distinct from the Contact Type and Organization Role.

  


The following are the User Groups to be used in this Solution. The data access details included here are generalizations (see the Permissions section of this proposal for full details).   

  


  * Dealer: Used by dealers. Users in this group are restricted to only see specific data relating their own business. This is a Restricted user type that only has access to the Shipping Calculator (view and edit, for their own details) and a few other items. 
    * Home Page Report: MainDir::\Standard\Std Autopush Shipping Calculator.r20
    * Allowed Components: 
      * MainDir::\Standard\Std Autopush Shipping Calculator.r20
      * MainDir::\Standard\Std Quote Email Merge.r20 
      * MainDir::\Standard\Std Quote Word Merge.r20 
      * Restricted Data Policy
    * Restricted Data Policy: Default 
  * Employees: Used by all Tru-Haul employees. Users in this group have access to view and edit the whole Solution. This is an Administrator-type user group, with full permissions. 
  * Support: Used for CodeCrafters support personnel. Users in this group have access to view and edit the whole Solution. This is an Administrator-type user group, with full permissions. 



  


Other Notes: 

  * The "Default" user will be set to be a member of the 'Dealers' Group.
  * Additional user groups may set up and configured within the system. This can be done by CodeCrafters or an admin user.
  * Other restrictions will not need to be specially configured within the Solution, as they are handled by coding.



  


Development Specification

Change Requests:

  * Tim Reitz 07/02/2024: [[[IN10152](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10154&)]] - ZTH - Hide Advanced Menu for Dealers
  * Ben Reitz 06/13/2025: [[[IN10951](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10953&)]] - ZTH - Calculator record - "Print this Quote" button not working
  * 


  


  


Tim Reitz 06/21/2024: See the sample User Groups: 

  * Dealers: 
  * Employees: 
  * Support: 



  


  


Ellis Miller 05/27/2024: Configured in deployment, nothing to change.
