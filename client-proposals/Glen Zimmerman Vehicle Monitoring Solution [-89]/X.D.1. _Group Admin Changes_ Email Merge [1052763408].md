10.4.1. "Group Admin Changes" Email Merge

Overview: This email is sent to users affected by changes to the "Account Group Admins" embedded spreadsheet on an Account Group record. Is it sent via the "__" user-initiated automatic process. 

  


From: <the email address specified in the ""From" email address for notifications:" System Switch>

  


To: <the primary email address on Contact records selected in the "Recipients" prompt of the "__" user-initiated automatic process - see corresponding spec> 

  


CC:

  * 


_GZ: Tim Reitz 09/01/2025: Any CC?

TODO_VA: Tim Reitz 09/04/2025: Master Administrators. [all users in the "Master Administrators" User Group]

TODO_VA: Tim Reitz 10/27/2025: Make sure the email doesn't get sent to CCI full access users.

  


BCC: TODO_: Tim Reitz 01/16/2026: Set this based on the others

  


Reply To: N/A (automatically replies to the "From" address)

TODO_VA: Tim Reitz 09/04/2025: Probably set this to the Primary Group Admin.

  


Subject: "Account Group Administration Changes for <Account Group Name>"

  


Attachments: N/A

  


Body:

Hello <Contact First Name>,

  


Changes affecting you have been made to the following Account Group: <Account Group Name>:

  


<\- <Name> was added as an Group Admin.> 

<\- <Name> was added as an Group Admin and set as Primary.> 

<\- <Name> was set as Primary Group Admin.> 

<\- <Name> was removed from their Group Admin role.> 

<\- <Name> was removed from Primary Group Admin role, but remains a Group Admin.> 

<\- <Name> was changed from Primary to secondary Group Admin.> 

  


The Account Group can be viewed here: <link to Account Group record>

  


Please reach out to a Group Admin a Master Administrator if you have any questions.

  


Thank you for your involvement in __.

TODO_VA:

  


Other Notes:

  * N/A



  


TODO_VA.: Tim Reitz 09/01/2025: Also copy this to the Account record spec and adjust for the Account Manager Change email there, once we have this (initial?) spec complete.
