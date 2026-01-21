17.3.1. Permissions

  


Requirements

TODO_TR

NOTE: See [[[W0266](https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages&NumberID=-267&)]] - 110. Restricted Data and Permissions as needed

TODO_JM - ask the client

  


The Solution will contain settings for the following permissions. Note that Admin users should have access to everything, even if not specifically mentioned here. 

  


Configuration Settings: 

  * Edit AppHosting.Zone Settings. This will be enabled by default for administrators. The "AppHosting.zone Settings" menu item will be hidden if the user does not have permission to edit. However, the user will still be able to access these settings through less obvious parts of the system.



  


SKUs: 

  * 


  


Device Models: 

  * 


  


Billing Groups: 

  * 


  


Devices: 

  * 


  


Invoices: 

  * 


  


Time Cards:

  


Development Specification

Mockup: N/A

  


[ ] Add a standard "Can Edit AppHosting.zone Settings", default to Admin, and start using it.

[ ] Add a custom macro to override whether the AppHosting.zone Settings menu option should be visible, and only show it in ZTK if the user has edit permissions.
