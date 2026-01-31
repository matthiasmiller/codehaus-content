11.4. Permissions

  


Requirements

The Solution includes various custom permissions that control visibility and/or editability of various portions of the solution, including reports, records, and parts of records. These permissions normally are enabled on a per-User Group basis, allowing all Users in a Group to access the corresponding information.

  


The table below lists the relevant permissions in the Solution and the User Groups that have the corresponding permissions enabled:

  


Permissions| AdministratorUser Group| <B>User Group| <C> User Group| Etc.  
---|---|---|---|---  
Standard Permissions:|   
|   
|   
|   
  
Edit the Contact Type lookup record| [X] | [ ] | [ ] |   
  
Create/Edit Other User Profiles| [X] | [ ] | [ ] |   
  
  
| [ ] | [ ] | [ ] |   
  
Custom Permissions:|   
|   
|   
|   
  
Edit Depreciation Settings| [X] | [ ] | [ ] |   
  
Edit Historical Depreciation| [X] | [ ] | [ ] |   
  
View PII| [X] | [ ] | [ ] |   
  
Edit Products| [X] | [ ] | [ ] |   
  
Edit Contract Scripts| [X] | [ ] | [ ] |   
  
Edit Contract Definitions| [X] | [ ] | [ ] |   
  
Edit RTO Payments| [X] | [ ] | [ ] |   
  
Create Stripe Charges| [X] | [ ] | [ ] |   
  
Edit Contracts| [X] | [ ] | [ ] |   
  
Edit Notes| [X] | [X] | [X] |   
  
Edit Note Templates| [X] | [ ] | [ ] |   
  
Edit Note Types| [X] | [ ] | [ ] |   
  
  
  


Other Notes:

  * By default, users in the Administrator User Group have all Permissions, and therefore have full view & edit access to the whole Solution.



  


Seth Miller 07/16/2025: TODO_PERMISSIONS: what other permissions do we need? Do we want separate permissions for deleting records?

Matthias Miller 07/30/2025: At a very high level, there will be:

  * Differing levels of admins
  * Need to view and/or edit accounting permissions
  * Read-only permissions for view-only
    * Matthias Miller 07/30/2025: We will bump this towards the end of the project, since it will become clearer as this gets built out. I am labeling these as TODO_PERMISSIONS so that we can get them out of our search for now.



  


Seth Miller 10/17/2025: Consider investor level permissions

  


Seth Miller 10/17/2025: Search the entire document for TODO_Permissions.

  


Development Specification

TODO_: Internal / design help notes: 

  * The proposal should refer to specific permissions in the design rather than the user groups that are expected to have that permission.
  * If there is confusion or difficulty thinking in terms of permissions, we may be able to list both permissions and the group names, but this makes it harder to keep the living spec up to date and the coding will be done based on the permissions.



  


  


TODO_PERMISSIONS - Consider delete record
