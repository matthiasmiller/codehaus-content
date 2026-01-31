10.3.2. "Device Unlinked from Account" Email Merge

Overview: This is an email merge that is sent automatically to Account Managers when a Device is unlinked from an Account that they manage. This email is sent via the "Send "Device Unlinked from Account" Email" triggered automatic process on the first Save after "Account" has been changed on a Device record.

  


From: __ 

TODO_VA: Tim Reitz 01/23/2026: From "automation@" 

  


To: <Primary Email address(es) for each "Account Manager" on the previous "Account" for the Device record>

_NM: Tim Reitz 10/01/2025: How to do this for the previous Account's Account Managers? Hidden field? Modification History? Something else? 

TODO_VA: Tim Reitz 10/08/2025: Since this is a trigger, we can specify "old values" and use those. The description that's here already should be enough for the devs. 

  


CC: N/A

TODO_VA: Tim Reitz 01/23/2026: CC the reseller. 

  


BCC: 

TODO_VA: Tim Reitz 01/23/2026: Yes to BCC. 

  


Reply To: <Primary Email address(es) for the "Account Reseller" on the previous "Account" for the Device record>

  


Subject: "Device Unlinked from Account <Account #>"

  


Attachments: N/A

  


Body:

  


The following Device has been removed from an Account that you manage:

  


Device: <Traccar Device Identifier>

TODO_VA: Update once the same item is finalized on the "Linked" email. 

Account: <"Account #" of the previously-linked Account (the next-to-top row of the "Account Linking History" non-embedded spreadsheet)>

Date & time: <date and time of the modification, in the "MM/DD/YYYY at H:M AM/PM" format>

  


This change was made by <"Short Display Name" of the Contact for the user who saved the changes>.

  


Additional Comments: <contents of the "Device Transfer Comments" field for the top row of the "Account Linking History" non-embedded spreadsheet>

  


Please reply to this email to __ your Account Reseller with any questions.

  


Thank you!

  


Other Notes:

  * N/A


