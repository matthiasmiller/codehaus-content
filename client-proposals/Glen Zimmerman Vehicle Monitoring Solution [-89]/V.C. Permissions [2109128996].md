5.3. Permissions

  


Requirements

*Done. 

  


The Solution includes various custom permissions that control visibility and/or editability of various portions of the solution, including reports, records, and parts of records. These permissions normally are enabled on a per-User Group basis, allowing all Users in a Group to access the corresponding information.

  


The table below lists the relevant permissions in the Solution and the User Groups that have the corresponding permissions enabled: 

  


Permissions| "Master Administrators"User Group| "Group Admins" User Group.| "Resellers"User Group| "Support - Silverloom" User Group.  
---|---|---|---|---  
Standard Permissions:|   
|   
|   
|   
  
Edit the Contact Type Lookup Record| [X] | [ ] | [ ] | [X]   
Edit User Groups and Profiles| [X] | [ ] | [ ] | [X]   
  
|   
|   
|   
|   
  
Custom Permissions (in a "<System Name>-Specific" grouping):|   
|   
|   
|   
  
Full Access| [X] | [ ] | [ ] | [X]   
Edit General Inventory Devices| [X] | [ ] | [ ] | [X]   
View Traccar Sync Records| [X] | [ ] | [ ] | [X]   
  
|   
|   
|   
|   
  
  
  


Other Notes: 

  * By default, users in the "Master Administrators" and "Support - Silverloom" User Groups have all Permissions, and therefore have full view & edit access to the whole Solution.



  


Development Specification

Niccolas Miller 01/30/2026: Draft estimate:

Simple permissions: 2 hours

  


Tim Reitz 07/23/2025: None included in the HLD.

  


  


Internal / design help notes: 

  * The proposal should refer to specific permissions in the design rather than the user groups that are expected to have that permission.
  * If there is confusion or difficulty thinking in terms of permissions, we may be able to list both permissions and the group names, but this makes it harder to keep the living spec up to date and the coding will be done based on the permissions.


