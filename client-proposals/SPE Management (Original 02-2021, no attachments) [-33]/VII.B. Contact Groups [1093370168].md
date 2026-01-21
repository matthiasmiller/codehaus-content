7.2. Contact Groups

  


Requirements

If the Prompt for Contact Type is checked, the communication will prompt for one or more choices of:

  * Admitted Members
  * Pending Members
  * Accountants
  * Schools
  * Other Contacts



  


Members are automatically included or excluded from these based on the following criteria.

  


The Admitted Members will include all members who have an admitted application for the current tax year.

  


The Pending Members will include all members with an application (prefilled or completed) for the current tax year (not including admitted applications).

  


The Accountants will include all contacts who are listed as an Accountant on another contact record.

  


The Other Contacts will include interested/referred members. This will include anyone not included in the above lists.

  


NOTE: If a member has multiple applications, it's possible that they will be included in both the Admitted Members and Pending Members groups.

  


Development Specification

Ellis Miller 02/14/2021: This is included in the 20 days above.

  


  * ContactIsAccountant( vContact) -- we will want a ContactByAccountant.ndx or something similar 
  * ContactIsCurrentMember( vContact) -- See definition above
  * ContactIsPendingMember( vContact) -- See definition above
  * ContactIsSchoolContact( vContact) -- ContactType = "School"
  * ContactIsOtherContact( vContact) -- not ContactIsAccountant AND NOT ContactIsCurrentMember AND NOT, etc.


