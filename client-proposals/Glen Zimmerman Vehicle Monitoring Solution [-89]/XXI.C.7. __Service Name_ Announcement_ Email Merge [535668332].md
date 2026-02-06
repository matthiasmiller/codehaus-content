21.3.7. "<Service Name> Announcement" Email Merge

  


Requirements

*Done. 

  


Overview: This is an email merge that is sent to selected recipients, from an Announcement record when the "Send Email" button is clicked. This also updates the Announcement "Status" to "Sent".

  


From: <the "From" selection on the "<Service Name> Announcement Email>" child screen in Silverloom Settings>

  


To: <the "Email" for each row in the "Recipients" embedded spreadsheet on the Announcement record>

  


CC: N/A

  


BCC: N/A

  


Reply To: N/A ("announcements@" would be set up as an inbox that Master Administrators have access to, so that it can be monitored for replies) 

  


Subject: "<Announcement "Subject">" 

  


Attachments: N/A 

  


Body: "<Announcement "Email Body">" 

  


Other Notes:

  * Each recipient receives a separate email (as opposed to a single email with all recipients in the "To" line). 
  * After the email merge runs to send the email(s), the "Set Email Announcement Status to Sent" automatic process runs to set the Announcement "Status" to "Sent" - see corresponding spec.



  


Development Specification

Tim Reitz 01/20/2026: Note that each recipient will receive a separate email.

  


Tim Reitz 01/23/2026: From "announcements@__". The plan is to have this set up as an operating email address with an inbox, that Master Administrators have access to, so that it can be monitored for responses.
