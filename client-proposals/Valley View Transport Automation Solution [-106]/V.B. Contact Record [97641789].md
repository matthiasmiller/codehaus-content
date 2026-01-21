5.2. Contact Record

  


Requirements

Overview: The Solution uses the standard Silverloom Contacts module, utilizing the standard Contact record with its contact sections and fields, which may have custom behaviors. Additional custom sections & fields may be added as well. Any customizations are noted as such in the spec. 

  


The Solution can track individuals and organizations/businesses separately, and has the ability to link an individual contact to an organization contact. 

  


Accessed via: Contacts report

  


Sections and Fields:

  * Standard Contact Details, Address, Phone, Email, and Notes sections and fields



  


  * Builder custom section (visible if "Contact Type" = "Builder")
    * Builder Region (drop list of Builder Regions)
    * Builder Product Markup (drop list of Builder Product Markups)
    * Customer Builder Rate % Adjustment (number field)



  


  * Customer custom section (visible if "Contact Type" = "Customer")
    * Customer Region (drop list of Customer Regions)
    * Override Customer Base Rate % (checkbox; when checked, makes "Customer Base Rate % Adjustment" field visible)
    * Customer Base Rate % Adjustment (number field; visible if "Override Customer Base Rate %" checkbox is checked)
    * Warehouse Zone (drop list of Warehouse Zones)



  


Data Access:

  * Visibility: Visible to all users (standard). 
  * Editability: Editable for all users (standard). 



  


Special Considerations:

  * Copy Record: Allowed, and the following fields are cleared (standard): 
    * Contact ID 
    * Contact Type 
    * First Name 
    * Middle Name
    * Last Name 
    * Date of Birth
    * User ID
  * Delete Record: Allowed until the record has been referenced by another record, at which point deletion is disallowed (standard). 
  * Merge Record: Allowed without restrictions; the record from which the merge is initiated is completely replaced by the other (deleting all data for the first record) (standard). 



  


Other Notes:

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * Unless otherwise noted, all fields that become hidden for any reason (based on other fields, user permissions, etc.) retain their values. If they should be cleared, that is noted specifically in the field specs, with a "clear if hidden" or similar note.
  * The Contact ID is automatically added to the end of each Contact's name. This allows for handling contacts with the same name.
  * The following entire standard section(s) with all included fields are hidden (custom behavior) in this Solution: 



TBD

  * The following individual standard field(s) are hidden (custom behavior) in this Solution: 



TBD

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=1529895558#gid=1529895558](https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=1529895558#gid=1529895558)
