10.3.1. "Device Linked with Account" Email Merge

Overview: This is an email merge that is sent automatically to Account Managers when a Device is linked to an Account that they manage. This email is sent via the "Send "Device Linked with Account" Email" automatic process on the first Save after "Account" has been changed on a Device record.

  


From:

TODO_VA: Tim Reitz 01/23/2026: From "automation@" 

 TODO_VA: Tim Reitz 01/15/2026: Probably add a System Switch or a Silverloom Settings for the send from email address - like we recently did for ZLP? Or ZGW? Or ??

Tim Reitz 01/22/2026: Modeling this after XFB. 

  


To: <Primary Email address(es) for each "Account Manager" on the current "Account" selected on the Device record>

  


CC: N/A

_GZ:

TODO_VA: Tim Reitz 01/23/2026: CC the reseller. 

  


BCC: __ 

TODO_VA: Tim Reitz 01/23/2026: Yes to BCC. 

_NM: Tim Reitz 01/16/2026: Thoughts on including a System Switch for the BCC email? [if the client wants to BCC everything] 

TODO_VA: Tim Reitz 01/22/2026: Let's do it in Silverloom Settings. 

  


Reply To: <Primary Email address(es) for the "Account Reseller" on the current "Account" selected on the Device record>

  


Subject: "Device Linked to Account <Account #>"

  


Attachments: N/A

  


Body:

  


The following Device has been added to an Account that you manage:

  


Device: <Traccar Device Identifier>

TODO_VA: Or just the "Device ID"

Account: <"Account #" of the newly-linked Account (the top row of the "Account Linking History" non-embedded spreadsheet)>

Date & time: <date and time of the modification, in the "MM/DD/YYYY at H:M AM/PM" format>

  


This change was made by <"Short Display Name" of the Contact for the user who saved the changes>.

  


Additional Comments: <contents of the "Device Transfer Comments" field for the top row of the "Account Linking History" non-embedded spreadsheet>

  


Please reply to this email to __ your Account Reseller with any questions.

  


Thank you!

  


Other Notes:

  * N/A


