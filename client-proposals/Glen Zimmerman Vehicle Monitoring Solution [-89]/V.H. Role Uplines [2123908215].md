5.8. Role Uplines

  


Requirements

*Done. 

  


Due to the complexity of "uplines" and "downlines" in roles, the following pre-determined uplines and downlines are defined and hard-coded in the system: 

  


  * "All Provider Roles": Includes Contacts/users with the following roles: 
    * All users with the "Full Access" Permission (i.e. "Master Administrators" & CodeCrafters Support users) 
    * All "Group Admin" users
    * All "Account Reseller" & "Reseller Rep" users



  


  * "Upline Provider Roles": Includes Contacts/users with the following, to be evaluated in relation to a specific Contact/user/Account/Device: 
    * All users with the "Full Access" Permission 
    * "Group Admin" users for the linked "Account Group" and "Upline Groups" for Accounts on which the Contact is included as an "Account Member" (Account Manager or Driver. 
    * "Account Reseller" & "Account Rep" users for Accounts on which the Contact is included as an "Account Member" (Account Manager or Driver).



  


Development Specification

Visual overview of hierarchy / roles: 

Master Administrator - full access to entire system  
---  
Reseller - individual or organization with reps; financial management & support for Accounts they sell| Group Admin - oversight / management of Accounts in Group and Downline Groups  
Account Manager - each Account has one primary manager and optional additional managers  
Device - in one Account (at a time)| Driver \- tied directly to one or more Devices and (indirectly through Devices) to one or more Accounts  
  
  

