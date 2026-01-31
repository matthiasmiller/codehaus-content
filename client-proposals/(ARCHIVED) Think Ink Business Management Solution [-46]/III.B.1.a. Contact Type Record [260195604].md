3.2.1.1. Contact Type Record

  


Requirements

Overview: The Solution will use the following Contact Types (listed here in alphabetical order):

  * CUST (business or individual; default to business; does not have login access) 
  * EMP (individual only; may have login access)
  * OTHER (business or individual, default to business; does not have login access) 
  * VEND (business or individual, default to business; does not have login access) 



  


The Solution will use Contact Tags rather than subtypes for contacts (see details in the corresponding section of this proposal).

  


The Contact Type will be a required field for all contacts.

  


Contact Types will be configured on Contact Type records and viewed on a Contact Types report (see corresponding section of the proposal); both are AppHosting standard. 

  


If any non-CUST contact (e.g. VEND, EMP, etc.) makes a purchase or rents a printer, they should have a separate CUST-type contact record created to handle that. Classic Accounting currently operates this way already. 

  


If a Contact changes from one Contact Type to another, it should retain the field information from the previous Contact Type. This information would be hidden with the custom section(s) for the old Contact Type, but would reappear if the Contact is changed back to the previous Contact Type.

  


Each Think Ink user of the Solution should have an EMP-type contact set up in Classic Accounting with a name that matches the user's Sales Rep name from CA. The EMP-type contact will be set up in the Solution via the sync and would be manually linked to that user's login ID. This would facilitate reporting and other features. 

  


Accessed via: The Contact Types report

  


Sections and Fields: 

  * Type (required; text field; standard field)
  * Supported Entity Types (checkboxes; standard fields; at least one of the first two is required to be filled:)
    * Individual
    * Organization
    * Default to Organization? (fillable if "Organization" is selected)
  * Active (checkbox; standard field; a Contact Type cannot be deactivated if it is being used by one or more active Contacts)



  


Data Access: (note that the Type name cannot be edited in the Solution)

  * Editable by Admins (set via "Can edit contact types" permissions)
  * Viewable by all other users 



  


Other Notes:

  * The initial list of Contact Types mentioned in the proposal would be set up by CCI/CH.
  * CA currently has contact types as well; the CA list should be updated to match the Solution's list to avoid sync problems.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=739267949](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=739267949)

  


  


Contact Types:

We will have default types as catalog-defined list items if needed, but we will not ship lookup records. These will be configured during deployment in both testing system and live system.

  


BID: 0.25 day for CCI to add list.

BID: 0.25 day for CH to help configure types if needed.

  


Note that we intentionally do not validate that only customer types are specified on incidents, etc.
