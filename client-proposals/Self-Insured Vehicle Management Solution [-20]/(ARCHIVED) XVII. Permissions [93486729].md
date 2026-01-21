17\. Permissions

  


Requirements

Development Specification

Ellis Miller 08/18/2020:

 

Permissions -

We will likely code this as we are doing various screens, adding 1 day for bid.

 

CanEditRecord: Contacts, Vehicles, Claims.

 

Use restricted data for Payment Status/Date. Make sure that you can't edit a record where data is restricted.

 

All Admin reports should be called Std Admin. They should be visible on menu for Admin. Subsets should include UserIsAdmin so that the report is empty for-non-admins.

  


  


  


All users will be able to view all people, vehicles, and claims. Admins should be able to edit all records. Agents will only be able to edit records for their own clients. They should not be able to edit a contact's agent. Only Admins should be able to delete any records.

  


Some reports will only be visible to administrators.

  


Invoices will be visible to all users. However, invoices will only be editable and payment status/date will only be visible based for:

  * Admins, who can have access to all invoices
  * Fund Managers, who have access to invoices for all clients using their fund
  * Agents, who have access to invoices for all their clients



  


When configuring users, the default users should not have permission to view report settings. This prevents them from viewing admin reports.

  


Note that Fund Managers will NOT have special permissions to manage other agents' records.

  


  


Murshid Rahman 10/13/2022: Coded in [[PC0126543]] - ZWA - Permission Regarding Invoices

See also [[PC0128597]] - ZWA - Record Restrictions

  


[[PC0127766]] - ZWA - Only Admins Can Delete Any Record

  


Development Specification

Ellis Miller 08/18/2020: 

  


Permissions -

We will likely code this as we are doing various screens, adding 1 day for bid.

  


CanEditRecord: Contacts, Vehicles, Claims. 

  


Use restricted data for Payment Status/Date. Make sure that you can't edit a record where data is restricted.

  


All Admin reports should be called Std Admin. They should be visible on menu for Admin. Subsets should include UserIsAdmin so that the report is empty for-non-admins.
