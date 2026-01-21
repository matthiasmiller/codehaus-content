5.1.1. Contact Type Record

  


Requirements

Overview: Contact Types will be configured on Contact Type records and viewed on a Contact Types report (both Silverloom standard features).  

  


Accessed via: Configure Contact Types report

  


Sections and Fields: 

  * Active (checkbox; standard field; a Contact Types cannot be deactivated if it is being used by an active Contact)
  * Type (required; text field; standard field)
  * Supported Entity Types (checkboxes; standard fields; at least one of the first two is required to be filled:)
    * Individual
    * Organization
    * Default to Organization? (fillable if "Organization" is selected)



  


Data Access:

  * Editable: Employees & Support



  


The Solution will use the following Contact Types (listed here in alphabetical order): 

  * Dealer (individual or organization, defaulting to organization; does have login access) 
  * Employee (individual, defaulting to individual; does have login access) 
  * Other Individual (individual, defaulting to individual; does have login access)



  


The Contact Type is a required field for all contacts and there is an option for an "Other" type.

  


Other Notes: 

  * The initial list of Contact Types mentioned in the proposal would be set up by CCI/CH.
  * Contacts may have certain custom sections and fields on their record, depending on their contact type (see corresponding sections in this proposal). 
  * If a Contact changes from one Contact Type to another, it should retain the field information from the previous Contact Type. This information would be hidden with the custom section(s) for the old Contact Type, but would reappear if the Contact is changed back to the previous Contact Type.
  * Note that this record should have a name, date, and time stamp for Created and Last Modified (standard), as well as a link to access Modification History.



  


Development Specification

Change Requests: 

  * Tim Reitz 07/02/2024: [[[IN10178](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10180&)]] - ZTH - Contact Record - Make User ID field visible for Organizations


