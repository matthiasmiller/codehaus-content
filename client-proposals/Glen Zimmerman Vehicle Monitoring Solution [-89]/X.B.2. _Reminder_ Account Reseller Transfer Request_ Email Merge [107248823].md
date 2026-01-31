10.2.2. "Reminder: Account Reseller Transfer Request" Email Merge

_VA: Tim Reitz 11/06/2025: Let's add a reminder email for the Resellers if 1 day / 24 hours have passed since the request was submitted & the reseller hasn't approved it.

TODO_VA: Tim Reitz 01/22/2026: Let's spec out From / To / etc. once we have those determined in the initial request email.

  


\------------

  


Overview: This is an email merge that is sent automatically to Account Resellers when they have a pending Account Reseller Transfer Request that has been awaiting their approval for more than 1 day.

  


Sent Via: Sent Via: This is sent via the "Send "Reminder: Account Reseller Transfer Request" Email" scheduled automatic process (see corresponding spec)

  


From:

  


To:

  * 


  


CC:

  * 


  


BCC:

  * 


  


Reply To:

  


Subject: "Reminder: Account Reseller Transfer Request"

  


Attachments: N/A

  


Body:

  


This is a reminder a reseller transfer has been requested for the following account, and is needing your approval: <Account #, link to record>.

  


  


Other Notes:

  * N/A


