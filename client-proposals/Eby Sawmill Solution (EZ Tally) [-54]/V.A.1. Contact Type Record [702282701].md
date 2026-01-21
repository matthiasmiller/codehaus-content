5.1.1. Contact Type Record

  


Requirements

Overview: Contact Types will be configured on Contact Type records and viewed on a Contact Types report (both AppHosting standard).  

  


Accessed via: Configure Contact Types report

  


Sections and Fields: 

  * Type (required; text field; standard field)
  * Supported Entity Types (checkboxes; standard fields; at least one of the first two is required to be filled:)
    * Individual
    * Organization
    * Default to Organization? (fillable if "Organization" is selected)
  * Active (checkbox; standard field; a Contact Types cannot be deactivated if it is being used by an active Contact)



  


Data Access:

  * View, edit, and delete: Administrator
    * View Type, Supported Entity Types, etc.: Visible for all users in lists, records, etc. throughout the system (especially on Yard Tally records)



  


Other Notes:

  


The Solution will use the following Contact Types (listed here in alphabetical order):

  * Customer (business or individual, defaulting to business) 
  * Employee (individual only) 
  * Forester (business or individual, defaulting to individual) 
  * Landowner (business or individual, defaulting to individual) 
  * Logger (business or individual, defaulting to business) 
  * Vendor (business or individual, defaulting to business)



  


Note that only Employee-type contacts will be linked with user logins (only employees will have login access), but this is not technically restricted on the Contact Type record. 

  


Also note that this list of Contact Types mentioned is hardcoded in the Solution and the details are not editable by users. 

  


The Contact Type will be a required field for all Contact records and there would not be an option for an "Other" Contact Type.

  


Contacts may have certain custom sections and fields on their record, depending on their contact type (see corresponding sections in this proposal). 

  


If a Contact changes from one Contact Type to another, it should retain the field information from the previous Contact Type. This information would be hidden with the custom section(s) for the old Contact Type, but would reappear if the Contact is changed back to the previous Contact Type.

  


Note that this record should have a name, date, and time stamp for Created and Last Modified.

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1191468497](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1191468497)

  


[ ] Permission for editing contact type can be set up when configuring users.

  


[ ] Use Shipped lookup records for these.

  


Coding changes

[ ] Set ConfigContacts_TypeRequired

[ ] Set Shipped lookup records (see above)

[ ] Note that we don't have to blank out fields if type is changed.

  


BID: 2 HOURS.
