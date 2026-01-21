3.4. Permissions

  


Requirements

TODO_VA: Tim Reitz 04/14/2025: Once we have the spec documented here, let's make sure the test and live systems are in sync with each other and this spec. 

[X] Live system has a Batch Processes user group, which is not in the test system

[ ] Test system has both an "Admin" and an "Administrator" user

Tim Reitz 04/28/2025: Ben made note to ask Ellis about this

  


\------------

The Solution includes various custom permissions that control visibility and/or editability of various portions of the solution, including reports, records, and parts of records. These permissions normally are enabled on a per-User Group basis, allowing all Users in a Group to access the corresponding information.

  


The table below lists the relevant permissions in the Solution and the User Groups that have the corresponding permissions enabled:

  


Permissions| Full AdministratorsUser Group| Admin - Without ManageDeliveries| Batch Processes| Standard Users| Standard Users -With ManageDeliveries| Web Services  
---|---|---|---|---|---|---  
Standard Permissions:|   
|   
|   
|   
|   
|   
  
Edit the Contact Type lookup record| [X] | [X] | [X] | [X] | [ ] | [ ]   
  
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ]   
  
| Includes all  standard Permissions as applicable.  
| Includes all  standard Permissions as applicable.  
| Includes non-Admin standard Permissions  
| Includes non-Admin standard Permissions  
| Includes non-Admin standard Permissions  
| Includes non-Admin standard Permissions  
  
Custom Permissions:|   
|   
|   
|   
|   
|   
  
Triple D-Specific Permissions| [X] | [ ] | [ ] | [ ] | [X] | [X]   
Manage delivery scheduling| [X] | [ ] | [ ] | [ ] | [X] | [X]   
Manage Truss Date| [X] | [ ] | [ ] | [ ] | [ ] | [ ]   
  
|   
|   
|   
|   
|   
|   
  
  
|   
|   
|   
|   
|   
|   
  
  
|   
|   
|   
|   
|   
|   
  
  
|   
|   
|   
|   
|   
|   
  
  
|   
|   
|   
|   
|   
|   
  
  
  


  


Other Notes: (may be included in the proposal or may be deleted)

  * By default, users in the Administrator User Group have all Permissions, and therefore have full view & edit access to the whole Solution.



  


  


TODO_: Internal / design help notes: 

  * The proposal should refer to specific permissions in the design rather than the user groups that are expected to have that permission.
  * If there is confusion or difficulty thinking in terms of permissions, we may be able to list both permissions and the group names, but this makes it harder to keep the living spec up to date and the coding will be done based on the permissions.



  


Development Specification

Change Requests: 

  * Sean Miller 05/05/2025: [[[IN11172](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11174&)]] - ZTD - Add Truss Date feature (prev. "Add Truss Scheduling")
  * Ben Reitz 05/08/2025: [[[IN10789](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10791&)]] - ZTD - Allow for linking Orders and Deliveries


