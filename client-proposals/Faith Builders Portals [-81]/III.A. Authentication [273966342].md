3.1. Authentication

  


Requirements

  * There will be separate links on the fbep.org website for each portal.
  * Each link will lead to a page with a field for an email address.
  * If the email address that is entered is listed as a Primary-type role, a one-time login link will be sent to the email address.
  * If the email does not match, Justin's contact information will be provided. He'll have to add them directly to the system by adding their email to the contact record.



  


Silverloom:

[ ] Add an r20 named Std School Portal - Validate Login Email:

  * Ask Prompt (string, required): vAskEmailAddress
  * Subset:
    * Contact Type = "School"
    * vAskEmailAddress is listed for a Primary-type related contact.
  * Columns:
    * ContactName



  


WSGI:

  


Login page

[ ] Create a login page with one field for the email address.

[ ] When the form is submitted, run a GET request from Silverloom, using the value of the field for the ask prompt.

Conditional:

[ ] If there are no schools returned, display the error: "Your email address provided is not recognized. Please contact Justin Kauffman at [secretary@fbep.org](mailto:secretary@fbep.org) to have this email address added."

[ ] If there is at least one school, show the list of schools to which the email address has access to.

[ ] When a school is selected, display a button called "get login link".

[ ] When this button is clicked, send a one-time login link to the email address entered.

[ ] Display the message: login link sent. This link will expire in 24 hours. Resend link in 1 minute. (counting down.)

  


Email login

Email format:

"This is a one-time login link to Faith Builder Scholarship Services portal for SchoolName, which will expire in 24 hours."

link

[ ] This link will lead directly to the portal "Profile" page.

[ ] The email used to log in will tag along, and be stored as a session variable to be used to track who has made the changes.

  


Development Specification

Jonathan Bergen 02/27/2024:

  


Silverloom:

[ ] Add an r20 named Std School Portal - Validate Login Email:

  * Ask Prompt (string, required): vAskEmailAddress
  * Subset:
    * Contact Type = "School"
    * vAskEmailAddress is listed for a Primary-type related contact.
  * Columns:
    * ContactName



  


WSGI:

  


Login page

[ ] Create a login page with one field for the email address.

[ ] When the form is submitted, run a GET request from Silverloom, using the value of the field for the ask prompt.

Conditional:

[ ] If there are no schools returned, display the error: "Your email address provided is not recognized. Please contact Justin Kauffman at [secretary@fbep.org](mailto:secretary@fbep.org) to have this email address added."

[ ] If there is at least one school, show the list of schools to which the email address has access to.

[ ] When a school is selected, display a button called "get login link".

[ ] When this button is clicked, send a one-time login link to the email address entered.

[ ] Display the message: login link sent. This link will expire in 24 hours. Resend link in 1 minute. (counting down.)

  


Email login

Email format:

"This is a one-time login link to Faith Builder Scholarship Services portal for SchoolName, which will expire in 24 hours."

link

[ ] This link will lead directly to the portal "Profile" page.

[ ] The email used to log in will tag along, and be stored as a session variable to be used to track who has made the changes.
