4.1.2. Contact Type Record

TODO_AP: Tim Reitz 07/20/2024: update this

  


Overview: Contact Types will be configured on Contact Type records and viewed on a Contact Types report (both Silverloom standard features).  

  


Accessed via: Configure Contact Types report

  


Sections and Fields: 

  * Active (checkbox; standard field; defaults to checked; a Contact Types cannot be deactivated if it is being used by an active Contact)
  * Type (required; text field; standard field)
  * Supported Entity Types (checkboxes; standard fields; at least one of the first two is required to be filled:)
    * Individual (checkbox; defaults to checked)
    * Organization (checkbox)
    * Default to Organization (checkbox; editable if "Organization" is selected)



  


Data Access:

  * TODO_



  


The Solution will use the following Contact Types (listed here in alphabetical order):

  * Customer Individual
  * Customer Organization
  * Other Individual
  * Other Organization
  * Payee
  * Salesperson
  * Trucker
  * Vendor
  * Vendor Organization



TODO_AP: Tim Reitz 07/20/2024: Add the following details to all: (business or individual, defaulting to ___; does/does not have login access) 

  


  


The Contact Type is/is not a required field for all contacts and there is/is not an option for an "Other" type.

TODO_: Yes or no? Have a catch-all "Other" type?

  


Other Notes: 

  * The initial list of Contact Types mentioned in the proposal is set up by CCI. .



  


  * Contacts may have certain custom sections and fields on their record, depending on their contact type (see corresponding sections in this proposal). 



TODO_: Yes or no? 

  


  * If any non-Customer contact (e.g. Vendor, Employee, etc.) makes a purchase, they should have a separate Customer-type contact record created to handle that.



TODO_: Yes or no? What to do in this situation?

  


  * If a Contact changes from one Contact Type to another, it should retain the field information from the previous Contact Type. This information would be hidden with the custom section(s) for the old Contact Type, but would reappear if the Contact is changed back to the previous Contact Type.



TODO_: Yes or no?

  


  * Note that this record should have a name, date, and time stamp for Created and Last Modified (standard), as well as a link to access Modification History.


