5.2. Contact Types

  


Requirements

The system should use the following Contact Types (listed here in alphabetical order):

  * Customer (business or individual, defaulting to individual; pays BE Barns) 
  * Dealer (business or individual, defaulting to business; paid by BE Barns) 
  * Driver (Member) (individual only; paid salary, plus a % of Move Jobs; paid by BE Transit)
  * Office Worker (Member) (individual only; paid hourly OR salary; paid by BE Barns) 
  * RTO Company (business only; pays and paid by BE Barns and BE Transit) 
  * Salesperson (Member) (individual only; under BEB, paid daily rate + commission) 
  * Salesperson (Non-member) (individual only; compensation not handled by the database)
  * Shop Worker (Member) (individual only; paid by piecework OR salary; paid by Benchmark Buildings)
  * Vendor (business or individual, defaulting to business)



  


The Contact Type will be a required field for all contacts and there will not be an option for an "Other" type.

  


Contact Types will be configured on Contact Type records and viewed on a Contact Types report (both AppHosting standard) accessible from the Advanced Menu via a "Configure Contact Types" menu option.  

  


Contacts will have certain custom sections and fields on their record, depending on their contact type (see corresponding sections in this proposal). 

  


If any non-Customer contact (e.g. Shop Worker, Dealer, etc.) buys a building, they should have a separate Customer-type contact record created to handle that.

  


If a Contact changes from one Contact Type to another, it should retain the field information from the previous Contact Type. This information would be hidden with the custom section(s) for the old Contact Type, but would reappear if the Contact is changed back to that Contact Type.

  


Note that there will be specific permissions/restrictions for various Contact Types with user logins (based on the corresponding User ID/User Group. A Full Admin user can be of any Contact Type and will have access to everything in the database.

  


*Done.

  


Development Specification

These contact types will be specially handled in the QuickBooks sync.

  


TODO_CCI: Do we need any custom fields on the Contact Type record to handle payments, etc. (like the Client? and No-Charge Vehicles fields in ZWA)?
