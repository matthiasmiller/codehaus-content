2.2. Login User Groups

The database will use various User Groups to determine permissions for different users. Each user should be assigned to a User Group. Note that the User Group is distinct from the Contact Type.

  


The following are the User Groups to be configured by CCI/CH and used in this database. The data access details included here are generalizations (see the Permissions section of this proposal for the full details).   

  * Full Admins (also referred to as "admin"): Has full access to the database. This includes the following that are restricted to Full Admin Only: 
    * Company settings
    * Time Sheets for all users
    * Settings and payments for the following: 
      * Member compensation 
      * Dealer commission 
      * Payments between entities



  


  * Secretary Admins (referred to as "secretary"): Has full access to the database except the Admin menu and any items that are Full Admin Only. 



  


  * Office Worker/Member Salespeople (used for Office Workers and Member Salespeople): Has access to most of the database. 
    * Can view and edit all Buildings, Sales Orders, Work Orders, Tasks, etc. 
    * Can approve SO's with Special Order items. 



  


  * Shop Workers: Has limited access to various parts of the database: 
    * View the work orders in progress
    * View and edit own tasks



  


  * Drivers: Has limited access to various parts of the database: 
    * View the delivery schedule 
    * View the work orders available for delivery 
    * View and edit own tasks



  


  * Non-Member Salespeople: Has limited access to various parts of the database. This includes: 
    * Can view & edit all customer records, but cannot see sales information for sales by other dealers. 
    * Can view sales reporting for their own dealer, but not for sales by other dealers. 
    * Can view inventory on their own dealer's lot(s), but not any other inventory. 
    * Can view Buildings they have sold (for which they were the most recent Salesperson for the sale of the building)  
    * Can view Work Orders for which they are the Salesperson, but cannot view the individual Tasks. 
    * Can view Sales Orders for which they are the Salesperson. 



  


Other Notes: 

  * A user of any Contact Type can be an Admin.



  


*Done.
