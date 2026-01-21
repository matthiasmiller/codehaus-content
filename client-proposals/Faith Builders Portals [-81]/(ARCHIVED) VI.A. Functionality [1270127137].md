6.1. Functionality

  


Requirements

Section: Contact Information

  * Business Name (read-only)
  * Business Address (editable)
  * Business Phone Numbers (editable)
  * Business Emails (editable)
  * Related Contacts (editable, can add new contacts)
  * SSN/FEIN number (read-only, last 4 digits shown)
  * Anonymous Donor (editable)
  * Preferred Name (editable)



  


Section: SPE Member Application (displays details from this year's member application. This is chosen from a droplist of applications for the Business.)

  * Status (read-only)
  * Total Amount (editable if the member is not Admitted)
  * School Designations: table with columns:
    * School (editable if the member is not Admitted)
    * County (editable if the member is not Admitted)
    * Scholarship Org. (editable if the member is not Admitted)
    * % of Total (read-only)
    * Amount (editable if the member is not Admitted)



  


<Save> button

  


Development Specification

Silverloom:

  


Contact Info Population:

[ ] Add a r20 named Std SPE Business Portal - Contact Population

  * Filters:
    * vAskBusiness (list of businesses)
  * Subset:
    * Business Name = vAskBusiness
  * Columns:
    * Name
    * Address
    * Phone numbers
    * Emails
    * Related Contacts
    * SSN/FEIN number (last 4)
    * Anonymous Donor
    * Preferred Name
    * Member Apps (list of members applications for the current year.)



  


SPE Member Application Population:

[ ] Add a r20 named Std SPE Business Portal - Application Population

  * Filters:
    * vAskSPEMemberAppID (selected by the user from the droplist of applications.)
  * Subset:
    * SPEMemberAppID = vAskSPEMemberAppID 
  * Columns:
    * School
    * County
    * Scholarship Org.
    * Amount



  


Page Editing:

When the "save" button is clicked, all of the changes made to the page will be sent into db with an x30. The editability of field will be gatekept on the front-end, since the user won't be able to see any error spawned by the x30 when writing to the db.
