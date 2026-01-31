7.5.0.2. "<Service Name> Announcement" Email Merge

  


Requirements

TODO_T/J: Move to main spec section. *. 

  


Overview: This is an email merge that is sent to selected recipients, from an Announcement record when the "Send Email" button is clicked. This also updates the Announcement "Status" to "Sent".

  


From: __

_GZ:

TODO_T/J: Tim Reitz 01/23/2026: From "announcements@"

  


To: <the "Email" for each row in the "Recipients" embedded spreadsheet on the Announcement record>

  


CC: N/A

_GZ:

TODO_T/J: Tim Reitz 01/23/2026: CC not needed.

  


BCC:

_GZ:

TODO_T/J: Tim Reitz 01/23/2026: BCC not needed (we're already tracking this in Silverloom)

  


Reply To: N/A

_GZ:

TODO_T/J: Tim Reitz 01/23/2026: Reply To not needed - let's have "announcements@ be an inbox that Master Administrators have access to. 

  


Subject: "<Announcement "Subject">" 

  


Attachments: N/A 

  


Body: "<Announcement "Email Body">" 

  


Other Notes:

  * Each recipient receives a separate email (as opposed to a single email with all recipients in the "To" line). 
  * After the email merge runs to send the email(s), the "Set Email Announcement Status to Sent" automatic process runs to set the Announcement "Status" to "Sent" - see corresponding spec.



  


Development Specification

Tim Reitz 01/20/2026: Note that each recipient will receive a separate email.
