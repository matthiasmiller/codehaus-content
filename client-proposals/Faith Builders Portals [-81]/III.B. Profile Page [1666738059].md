3.2. Profile Page

  


Requirements

Jonathan Bergen 02/27/2024: 

This page will display the following:

  * Logged in as "[you@gmail.com](mailto:you@gmail.com)"
  * School information:
    * School Name
    * Address Line 1
    * Address Line 2
    * City
    * State
    * Zip
    * County
    * Phone
  * Contacts with portal access
    * Contact Name
    * Email
  * Form field to enter email addresses to be given login access.



  


Silverloom:

  


Page Population:

[ ] Add a r20 named Std School Portal - School Contact Info

  * Ask Prompt (list of active schools, required): vAskSchoolName
  * Subset: ContactName = vAskSchoolName
  * Columns:
    * ContactNameWithoutID
    * ContactAddress
    * ContactAddress2
    * ContactCity
    * ContactState
    * ContactZip
    * ContactCounty
    * ContactPhone
    * ConcatRG( "|", ContactRelatedContacts, ContactName, ContactType = Primary type)
    * ConcatRG( "|", ContactRelatedContacts, ContactEmailSingleAddress, ContactType = Primary type)



  


Page Editing:

[ ] Add a x30 to update the School Record with the following values, if they have been changed in the portal:

  * Ask Prompts:
    * vAskContactName: (required, list of active schools)
    * vAskPortalUser: (required, string, will store the email of the portal user.)
  * Columns:
    * ContactAddress
    * ContactAddress2
    * ContactCity
    * ContactState
    * ContactZip
    * ContactCounty
    * ContactPhone



  


Email to request email addition or deletion:

[ ] Add a InvCommand Flask function to create an email to Justin ([secretary@fbscholarship.org](mailto:secretary@fbscholarship.org)) (saying: "[currentuser@gmail.com](mailto:currentuser@gmail.com)" would like "[otheremail@gmail.com](mailto:otheremail@gmail.com)" to be provided with login access to the school portal for #SchoolName#.

  


WSGI:

  


See Figma design for page layout

  


Editing fields:

[ ] If any fields have been changed, display a "save" button. (all fields except for address line2 are required.)

[ ] Clicking this button will run the x30 to update the database, feeding the email address of the portal user into the x30.

  


  


Email to request email addition:

[ ] Run a command to create the email in the system.

  


Development Specification

Jonathan Bergen 02/27/2024:

  


Silverloom:

  


Page Population:

[ ] Add a r20 named Std School Portal - School Contact Info

  * Ask Prompt (list of active schools, required): vAskSchoolName
  * Subset: ContactName = vAskSchoolName
  * Columns:
    * ContactNameWithoutID
    * ContactAddress
    * ContactAddress2
    * ContactCity
    * ContactState
    * ContactZip
    * ContactCounty
    * ContactPhone
    * ConcatRG( "|", ContactRelatedContacts, ContactName, ContactType = TODO_JK type)
    * ConcatRG( "|", ContactRelatedContacts, ContactEmailSingleAddress, ContactType = TODO_JK type)



  


Page Editing:

[ ] Add a x30 to update the School Record with the following values, if they have been changed in the portal:

  * Ask Prompts:
    * vAskContactName: (required, list of active schools)
    * vAskPortalUser: (required, string, will store the email of the portal user.)
  * Columns:
    * ContactAddress
    * ContactAddress2
    * ContactCity
    * ContactState
    * ContactZip
    * ContactCounty
    * ContactPhone



  


Email to request email addition or deletion:

[ ] Add a TODO_JB file to create an email to Justin saying: "[currentuser@gmail.com](mailto:currentuser@gmail.com)" would like "[otheremail@gmail.com](mailto:otheremail@gmail.com)" to be provided with login access to the school portal for #SchoolName#.

  


WSGI:

  


See Figma design for page layout

  


Editing fields:

[ ] If any fields have been changed, display a "save" button. (all fields except for address line2 are required.)

[ ] Clicking this button will run the x30 to update the database, feeding the email address of the portal user into the x30.

  


  


Email to request email addition:

[ ] Run a command to create the email in the system.
