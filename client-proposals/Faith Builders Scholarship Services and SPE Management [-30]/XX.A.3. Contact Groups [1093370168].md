20.1.3. Contact Groups

  


Requirements

If the Prompt for Contact Group is checked, the communication will prompt for one or more choices of:

  * Admitted SPE Members
  * Pending SPE Members
  * Accountants
  * Schools
  * Other Contacts
  * Interested Parties



  


Contacts are included or excluded from communications based on the following Contact Group criteria:

  * Admitted SPE Members: all members who have an admitted SPE member application for the current tax year.
  * Pending SPE Members: all members with an SPE member application (prefilled or completed) for the current tax year (not including admitted applications).
  * Accountants: all contacts who are listed as an Accountant type related contact on another contact record.
  * Other Contacts: include interested/referred members. This will include any individual or business not marked EITC or Eligible for SPE and who is not included in the above lists.
  * Interested Parties: Other Contacts who are not a primary or secondary related contact.



  


NOTE: If a member has multiple applications, it's possible that they will be included in both the Admitted Members and Pending Members groups. Contacts may be both Other Contacts and Interested Parties.

  


Development Specification

Ellis Miller 02/14/2021: 

  


  * ContactIsAccountant( vContact) -- we will want a ContactByAccountant.ndx or something similar 
  * ContactIsCurrentMember( vContact) -- See definition above
  * ContactIsPendingMember( vContact) -- See definition above
  * ContactIsSchoolContact( vContact) -- ContactType = "School"
  * ContactIsOtherContact( vContact) -- not ContactIsAccountant AND NOT ContactIsCurrentMember AND NOT, etc.



  


Target: 1 day
