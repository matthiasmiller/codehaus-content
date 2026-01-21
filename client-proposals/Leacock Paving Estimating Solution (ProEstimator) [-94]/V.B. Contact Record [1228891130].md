5.2. Contact Record

  


Requirements

Overview: The Solution uses the standard Silverloom Contacts module, utilizing the standard Contact record with its contact sections and fields, which may have custom behaviors. Additional custom sections & fields may be added as well. Any customizations are noted as such in the spec. 

  


The Solution can track individuals and organizations/businesses separately, and has the ability to link an individual contact to an organization contact. 

  


Accessed via: 

  * Contacts report
  * Links on Proposal records



  


Sections and Fields: The sections and fields for this record are specced out in subsections below.

  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (User ID, date, and time stamp) 
  * Last Modified: (User ID, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users
  * Editability: Editable for all users 



  


Special Considerations:

  * Copy Record: Clear the following fields: 
    * Contact ID 
    * Contact Type 
    * First Name 
    * Middle Name
    * Last Name
  * Delete Record: Deletion is allowed until the record has been referenced by another record, at which point deletion is disallowed. 
  * Merge Record: Merging is allowed without restrictions; the record from which the merge is initiated is completely replaced by the other (deleting all data for the first record). 



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * Custom: Contacts may have multiple Contact Types, as noted in the "Contact Type" field spec. 
  * If a Contact Type is removed from a Contact, any fields specific to the removed Contact Type are hidden, and cleared on Save. If desired, this can be changed to retain field information (customization).



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1529895558#gid=1529895558](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1529895558#gid=1529895558)

  


Ellis Miller 06/10/2025: 

[ ] Standard, but set system switch for multiple contact types.

1 hour
