11.2. Contact Record

  


Requirements

Overview: The Solution uses the standard Silverloom Contacts module, utilizing the standard Contact record with its contact sections and fields, which may have custom behaviors. Additional custom sections & fields may be added as well. Any customizations are noted as such in the spec. 

  


The Solution can track individuals and organizations/businesses separately, and has the ability to link an individual contact to an organization contact. 

  


Accessed via: 

  * Faith Builders SPE | Contacts | View Contacts
  * Faith Builders Scholarship Services | Contacts | View Contacts
  * And various other reports as noted in the rest of the spec.



  


Sections and Fields: The sections and fields for this record are specced out in subsections below.

  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: 

TODO_TR: Document based on Permission, rather than User Groups. 

  


Special Considerations:

  * Copy Record: Allowed
  * Delete Record: Deletion is allowed until the record has been referenced by another record, at which point deletion is disallowed. 
  * Merge Record: Merging is allowed without restrictions; the record from which the merge is initiated is completely replaced by the other (deleting all data for the first record). 



  


Other Notes:

  * The Contact ID is automatically added to the end of each Contact's name. This allows for handling contacts with the same name. The Contact ID is removed/hidden in various places, such as __. 



TODO_TR: handle duplicates like this, or don't allow duplicates? 

  * If a Contact changes from one Contact Type to another, any fields specific to the previous Contact Type are hidden, and cleared on Save. If desired, this can be changed to retain field information (customization).



  


Development Specification

Change Requests:

  * Ben Reitz 06/24/2025: [[[IN11450](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11452&)]] - XFB - Family Application record - "Learning Disability" should raise eligibility for the student


