7.2. Contact Record

  


Requirements

Overview: The Solution uses the standard Silverloom Contacts module, with some customizations. Note that any customizations are noted as such in the spec. The Contact record includes standard contact sections and fields. Note that some of these fields may have custom behaviors.  

  


The Solution can track individuals and organizations/businesses separately, and has the ability to link an individual contact to an organization contact. 

  


Accessed via: Contacts report

  


Sections and Fields: The sections and fields for this record are specced out in subsections below.

  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users
  * Editability:
    * Custom: 
      * Standard fields are editable for users with the "Edit Contact records" Permission (though this may change over time). 
      * Custom sections and/or fields may have more specific editability, based on Permissions - see individual section and/or field specs. 



  


Special Considerations:

  * Copy Record: Clear the following fields:
    * Contact ID
    * Contact Type
    * First Name
    * Middle Name
    * Last Name
  * Delete Record: Deletion is allowed until the record has been referenced by another record, at which point deletion is disallowed. 
  * Merge Record: Merge Record: Merging is allowed without restrictions; the record from which the merge is initiated is completely replaced by the other (deleting all data for the first record). 



  


Other Notes:

  * Contacts with duplicate names are not allowed, and the Contact ID is not automatically added to the end of each Contact's name for differentiation. If duplicate names are needed, an extra identifier can be added, for example: 
    * For individuals, a middle initial or middle name can be added. 
  * GemWood-specific: If a Member purchases lumber from another Member, a Buyer-type Contact should be set up with "(Buyer)" added to the end of the name to distinguish between the Contacts. No additional coding is needed for this approach. 
  * If a Contact changes from one Contact Type to another, any fields specific to the previous Contact Type are hidden, and cleared on Save. If desired, this can be changed to retain field information (would be a customization). 



  


  


Notes about standard sections & fields: 

  * The following entire standard section(s) are hidden (custom) in this Solution: 
    * Executive Notes section: 
      * Executive Notes (standard memo)
  * The following standard field(s) are hidden (custom) in this Solution: 
    * Date of Birth (visible if the Contact is an individual; date field; standard field)
    * Gender (visible if the Contact is an individual; drop list of blank / Female / Male; standard field)



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1529895558#gid=1529895558](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1529895558#gid=1529895558) 

Tim Reitz 01/09/2025: Updated.

  


Change Requests:  *note changes to specific sections in the Dev Spec for those sections* 

  * Ben Reitz 10/08/2025: [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature



  


  


Ellis Miller 12/16/2024: 

[ ] Override our system switches to hide executive notes, date of birth, and gender.

1 hour
