7.5.0.2. "<Service Name> Announcement" Email Merge

  


Requirements

*. 

  


Overview: This is an email merge that is sent to selected recipients, from an Announcement record when the "Send Email" button is clicked. This also updates the Announcement "Status" to "Sent".

  


From: __

TODO_GZ / TODO_VA:

  


To: <the "Email" for each row in the "Recipients" embedded spreadsheet on the Announcement record>

  


CC: N/A

  


BCC:

TODO_VA: Tim Reitz 01/20/2026: Set this based on the others

  


Reply To: N/A

  


Subject: "<Announcement "Subject">" 

  


Attachments: N/A 

  


Body: "<Announcement "Email Body">" 

  


Other Notes:

  * Each recipient receives a separate email (as opposed to a single email with all recipients in the "To" line). 
  * After the email merge runs to send the email(s), the "Set Email Announcement Status to Sent" automatic process runs to set the Announcement "Status" to "Sent" - see corresponding spec.



  


Development Specification

Tim Reitz 01/20/2026: Note that each recipient will receive a separate email.
