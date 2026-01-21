2.1. Permissions

  


Requirements

All Pickup & Delivery information (including contacts) will be restricted to Pickup & Delivery Personnel. These will be controlled via special "Pickup & Delivery Users" and "Pickup & Deliver Admins" HR groups.

  


Users in the "Pickup & Delivery Admins" group will have full permission to the entire Pickup and Delivery section. Users in the "Pickup & Delivery Users" group will not have permission to edit the schedule, configure the routes, or view guest ratings (see Phase 2).

  


For example, potential roles with access to this may include:

  * Director
  * Manager
  * Driver
  * Assistant



  


These can be configured within the system

  


Most of the use will be under the "Shared" user account, which is always signed it. This user will need to be assigned a "Route Supervisor" role to be included in the appropriate group.

  


The individual responsible for scheduling should be assigned a separate "Pickup & Delivery Scheduling" role that gives them full access to the Pickup and Delivery features.

  


Development Specification

Matthias Miller 09/22/2020: 

[ ] On the routes menu, add a ConfigRoutes_ContactType list macro (based on ContactTypes list). Default to "".

  


Add these macros:

[ ] ConfigRoutes_IsRoutesUser (true)

[ ] ConfigRoutes_IsRoutesAdmin (ConfigRoutes_IsRoutesUser AND UserIsAdmin)

  * Can configure
  * Can see review #s (see below)



  


  


FOR MATTHIAS TO CODE -- In ZNH:

[ ] Add the two types of groups to OrgGroups

[ ] You can check whether the current user is a member using "In(CurrentUserContact, LookupOrgGroupAllMembers(...))"

[ ] Override ConfigRoutes_IsRoutesUser to check whether they're a member of the users OR admins group

[ ] Override ConfigRoutes_IsRoutesAdmin to check whether they're a member of the users group

[ ] ZNH would override Custom_ContactEmploymentIsVisible to exclude these ContactTypes from the Std Employees report. This does not need to be handled generically.
