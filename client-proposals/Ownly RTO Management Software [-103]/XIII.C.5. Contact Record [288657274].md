13.3.5. Contact Record

Overview: The Solution uses the standard Silverloom Contacts module, utilizing the standard Contact record with its contact sections and fields, which may have custom behaviors. Additional custom sections & fields may be added as well. Any customizations are noted as such in the spec. 

  


The Solution can track individuals and organizations/businesses separately, and has the ability to link an individual contact to an organization contact. 

  


Accessed via:

  * Contacts Report
  * Links on Contract records



  


Sections and Fields: The sections and fields for this record are specced out in subsections below.

  


Modification History: This contains the following standard feature for modification tracking: 

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
  * The Contact ID is automatically added to the end of each Contact's name. This allows for handling contacts with the same name. The Contact ID is removed/hidden in various places, such as __. 
  * Contact IDs will increment across all contacts for all rental companies



  


Silverloom supports:

  * duplicate customer names across companies.
  * importing and showing previous customer account #'s in drop lists (from other systems)
  * controlling the # of digits for the Contact ID
  * setting the starting contact ID



  


Seth Miller 09/03/2025: TODO_Backlog: there is a Invoices section now visible on all contacts. It was automatically included when we added invoices to the system. The section displays any uncanceled invoices, link to view invoices, and link to create a new invoice for the contact. Do you want this section? If so, do you only want it on certain contact types?

  


  * If a Contact changes from one Contact Type to another, any fields specific to the previous Contact Type are hidden, and cleared on Save. If desired, this can be changed to retain field information (customization).


