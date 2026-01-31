7.2. Contact Record

  


Requirements

*Done.

  


Overview: The Solution uses the standard Silverloom Contacts module, utilizing the standard Contact record with its contact sections and fields, which may have custom behaviors. Additional custom sections & fields may be added as well. Any customizations are noted as such in the spec. 

  


The Solution can track individuals and organizations/businesses separately, and has the ability to link an individual Contact to an organization Contact. 

  


Accessed via: 

  * Contacts reports 
  * Various records, such as Accounts, Account Groups, Devices, etc.
  * Providers | Contacts | New Contact (opens a new Contact record) 
  * Administrators | Manage Contacts | New Reseller (opens a new Contact record with the "Is Reseller" checkbox set to checked)
  * Administrators | Manage Contacts | New Group Admin (opens a new Contact record with the "Is Group Admin" checkbox set to checked)



  


Sections and Fields: The sections and fields for this record are specced out in sub-sections below.

  


Data Access: 

  * Overview: This custom data access is based on a combination of restricted users, record-level restricted data, and conditional visibility. At a high level, specific users can either view or not view specific Contact records. If the user can view the record, there are additional controls defining which sections they can see. Also, if the user can view the record, they can either edit or not edit the record; if they can edit the record, they can edit any sections that they can see, unless there are additional restrictions on specific fields.
  * Visibility (custom):
    * Users with the "Full Access" Permission (i.e. Master Administrators & CodeCrafters Support users): Can view all sections & fields on all Contact records 
    * Group Admin users: Can view all Contact records (some sections / fields are hidden)
    * Account Reseller / Reseller Rep users: Can view all Contact records (some sections / fields are hidden). 
  * Editability (custom):
    * Users with the "Full Access" Permission: Can edit all sections and fields for all Contact records.
    * Group Admin users: Can edit all fields that they can view on: 
      * their own Contact record and 
      * Contact records for Account Managers and Drivers in Accounts that are in Groups that they manage (including Accounts in Downline Groups).
    * Account Reseller / Reseller Rep users: Can edit all fields that they can view on: 
      * their own Contact record and 
      * Contact records for Account Managers and Drivers linked to Accounts for which they or their linked organization Reseller are the "Account Reseller".



  


Special Considerations:

  * Copy Record: Allowed for users with the "Full Access" Permission (custom), and the following fields are cleared (standard): 
    * Contact ID 
    * Contact Type 
    * First Name 
    * Middle Name
    * Last Name
  * Delete Record: Allowed for users with the "Full Access" Permission (custom) until the record has been referenced by another record, at which point deletion is disallowed (standard). 
  * Merge Record: Allowed for users with the "Full Access" Permission (custom) without restrictions; the record from which the merge is initiated is completely replaced by the other (deleting all data for the first record) (standard). 



  


Other Notes:

  * Custom: Any individual Contact can be set as Driver on a Device record. 
  * Custom: To allow for handling Contacts with duplicate names, the Contact's Primary Address is automatically added to the Display Name (so that each Contact record can have a unique name within the Solution). 
    * A separate "Short Display Name" is also included, so that the name can be displayed without the address in some places, such as printouts, emails, etc. (see corresponding specs).  
  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * If a Contact changes from one Contact Type to another, any fields specific to the previous Contact Type are hidden, and cleared on Save. If desired, this can be changed to retain field information (customization).
  * Heading color: This record type uses the standard Silverloom blue color for section headings.
  * The following entire standard section(s) with all included fields are hidden (custom) in this Solution: 
    * "Notes" section & memo
    * "Executive Notes" section & memo
  * The following individual standard field(s) are hidden (custom) in this Solution: 
    * "Override Name" checkbox in the "Contact" section; 
    * "Organization" embedded spreadsheet in the "Contact" section (for linking individual Contacts to organization Contacts)



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=490602906#gid=490602906](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=490602906#gid=490602906)
