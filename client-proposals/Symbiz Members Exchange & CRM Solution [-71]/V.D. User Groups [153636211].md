5.4. User Groups

  


Requirements

The Solution will use various User Groups to determine permissions for different users. Each user's User Profile is assigned to a User Group. Note that the User Group is distinct from the Contact Type and Organization Role.

  


The following are the User Groups to be used in this Solution. The data access details included here are generalizations (see the "Data Access Controls" and "Permissions sections of this proposal for full details). 

  


  * Super Admin + System Admin: This is the standard AppHosting "Administrators" user group (with the name changed to "Super Admin + System Admin"), and has full access to the entire database. For database security purposes, this is not used for all Super Admin users, but users in this group will be set as Super Admins. Used for Symbiz personnel who need full access to administrate the software, and for designated CCI support personnel. Users in this group have access to view and edit all information in the database, including user groups. 



  


  * Super Admin: Used for the rest of the users with the Symbiz Super Admin role. Users in this group have access to view and edit all information of the Symbiz data in the database, but not all of the software administration. 



  


  * Standard User: This is a standard AppHosting user group. Used for standard Members, Facilitators, and Regional Reps, with the further breakdown of data access defined by their role (based on the checked role checkboxes on the Contact record.



  


Other Notes:

  * The User Groups are hard-coded, meaning that any changes should be coordinated with CH/CCI.
  * Other restrictions will not need to be specially configured within the Solution, as they are handled by coding.



  


Development Specification

Tim Reitz 02/16/2024: [[[IN9078](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9080&)]] - ZSB - User Groups - Pre-Deployment Changes
