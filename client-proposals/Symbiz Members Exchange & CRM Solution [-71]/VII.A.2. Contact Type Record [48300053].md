7.1.2. Contact Type Record

  


Requirements

Overview: Contact Types will be configured on Contact Type records and viewed on a Contact Types report (both AppHosting standard).  

  


Accessed via: Configure Contact Types report

  


Sections and Fields: 

  * Contact Type section: 
    * Active (checkbox; standard field; a Contact Types cannot be deactivated if it is being used by an active Contact)
    * Type (required; text field; standard field)
    * Supported Entity Types (checkboxes; standard fields; at least one of the first two is required to be filled:)
      * Individual
      * Organization
      * Default to Organization? (fillable if "Organization" is selected)



  


Data Access: See the Data Access Controls section of the proposal for details. 

  


Special Considerations: 

  * Copy Record: N/A
  * Delete Record: Custom behavior: Prevent deletion if the record is referenced anywhere in the Solution: "This Contact Type cannot be deleted because it is referenced by another record in the database." 
  * Merge Record: N/A



  


  


The Solution uses the following Contact Types (all custom Types, listed here in alphabetical order):

  * Lead (individual only; does not have login access; used to track people who are potential members) 
  * Member (individual only; may have login access; used to track people with active and inactive memberships) 
  * Member Organization (organization only; does not have login access; used to track organizations / businesses of current and past members) 
  * Other Individual (individual only; does not have login access; used to track any contacts that are not current or past members)
  * Other Organization (organization only; does not have login access; used to track any organizations that are not linked to current or past members)



  


Other Notes: 

  * The initial list of Contact Types mentioned in the proposal would be set up by CCI/CH.
    * "Lead", "Member", and "Organization" would be set up by the development team and would not be editable in the Solution. 
  * Contacts may have certain custom sections and fields on their record, depending on their contact type (see corresponding sections in this proposal). 
  * If a Contact changes from one Contact Type to another, it will not retain information in sections/fields that were specific to the old Type. This means that if the Type is changed back to the old one, those fields will be blank and will need to be filled in again. 
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Change Requests: 

  * Tim Reitz 04/10/2024: [[[IN9074](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9076&)]] - ZSB - Contact Types - Handle Organizations more cleanly
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1191468497](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1191468497)

  


  


BID: 4 HOURS
