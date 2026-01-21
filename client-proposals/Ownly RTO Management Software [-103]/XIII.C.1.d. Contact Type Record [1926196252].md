13.3.1.4. Contact Type Record

Overview: Contact Types are configured on Contact Type records and viewed on a Contact Types report (both Silverloom standard features). Note that any customizations are noted as such in the spec.  

  


Accessed via: Configure Contact Types report

  


Sections and Fields: 

  * Active (checkbox; defaults to checked; a Contact Types cannot be deactivated if it is being used by an active Contact)
  * Type (required; plain text field; validates against duplicate Type names)
  * Supported Entity Types (checkboxes; at least one of the first two is required to be filled:)
    * Individual (checkbox; defaults to checked)
    * Organization (checkbox; defaults to not checked)
    * Default to Organization (checkbox; editable if "Organization" is selected; defaults to not checked)



  


Modification History: This contains the following standard feature for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access:

  * TODO_PERMISSIONS



  


Special Considerations: 

  * Copy Record: Allowed; no fields are cleared on copy. (standard)  
  * Delete Record: Allowed until the record has been referenced by another record, at which point deletion is disallowed (standard). 
  * Merge Record: Allowed without restrictions; the record from which the merge is initiated is completely replaced by the other (deleting all data for the first record) (standard).  



  


Custom: The Solution includes the following "shipped" Contact Types, which are hard-coded and included in the Solution automatically as read-only record (requiring coding work to edit):

  * Customer (individual or organization, defaulting to individual)
  * Rental Company (Organization)
  * Rental Rep (individual)
  * Manufacturer (organization)
  * Manufacturer Rep (individual)
  * Dealer (organization)
  * Salesperson (individual)
  * Note that shipped Contact Type records are read-only, as mentioned in the template spec above. 



  


  * Contact records may have certain custom sections and fields, visible depending on their Contact Type (see corresponding sections in this proposal). 



  


  * If any non-Customer contact (e.g. Vendor, Employee, etc.) makes a purchase, they should have a separate Customer-type Contact record created to handle that.


