11.1.3. Contact Type Record

Overview: Contact Types are configured on Contact Type records and viewed on a Contact Types report (both Silverloom standard features). Note that any customizations are noted as such in the spec.  

  


Accessed via: Configure Contact Types report

  


Sections and Fields: 

  * Contact Type section
    * Active (checkbox; standard field; defaults to checked; a Contact Types cannot be deactivated if it is being used by an active Contact)
    * Type (required; text field;  validates against duplicates standard field)
    * Supported Entity Types (checkboxes; standard fields; at least one of the first two is required to be filled:)
      * Individual (checkbox; defaults to checked)
      * Organization (checkbox)
      * Default to Organization (checkbox; editable if "Organization" is selected)



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access:

  * TODO_NM: Tim Reitz 02/14/2025: Who can access? 



  


Validations: 

  * Error on save: if neither Individual nor Organization are checked.
    * Error Message: "At least one supported entity type must be specified."
  * Error on save: if Active is unchecked and there are active contacts using the Type.
    * Error Message: "This contact type cannot be deactivated because active contacts reference it. (Field: Active)"



  


The Solution will use the following Contact Types (listed here in alphabetical order):

  * Business (organization)
  * Individual (individual)
  * Scholarship Organization (organization)
  * School (organization)



  


Other Notes: 

  * Contact may be marked both Individual and Organization.
  * The initial list of Contact Types mentioned in the proposal would be set up by CCI/CH.
  * Contacts may have certain custom sections and fields on their record, depending on their contact type (see corresponding sections in this proposal). 
  * If a Contact changes from one Contact Type to another, it should retain the field information from the previous Contact Type. This information would be hidden with the custom section(s) for the old Contact Type, but would reappear if the Contact is changed back to the previous Contact Type.



: Yes or no? 

Austin Priest 02/20/2025: _TR No, this is not consistently happening. Do we want to make the spec match current behavior or make the system match the spec?

TODO_NM: Tim Reitz 02/24/2025: Is there an easy way to note which fields are cleared vs. which fields are retained when Contact Type is changed?
