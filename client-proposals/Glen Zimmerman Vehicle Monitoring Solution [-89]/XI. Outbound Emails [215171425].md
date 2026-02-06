10\. Outbound Emails

The Solution sends the following outbound emails. Some are sent via the "mailto" feature on the browser, opening an email draft in the user's default email client, with various things defaulted, and some are sent automatically by the software (requiring SMTP settings to be configured).

  


  


  


_GZ: Tim Reitz 09/01/2025: Would you have a specific email for outbound emails?

Tim Reitz 09/04/2025: Per the client today,

\- Good to have some generic one(s): support@ / billing@ or accounts@ /

\- For communications coming from a specific person, use that person's email

\- when able, have it point back to the administrator or the person responsible for carrying out the role:

\- master level: maybe "admin@__"

\- Group / Group Admin level: the Primary Group Admin's email address

\- Account Reseller level: __

\- essentially go up a level in the uplines (either "From" or "Reply To")

TODO_VA: Tim Reitz 01/13/2026: Follow up on notes here as needed. 

_GZ: Tim Reitz 01/13/2026: We're going to need the email addresses at some point in coding. 

Tim Reitz 01/22/2026: at the least, spec out the first part of the address for organization-level From, CC, BCC. Examples: 

  * no-reply@
  * support@
  * accounts@
  * billing@ / subscriptions@
  * admin@
  * etc



_GZ: Tim Reitz 01/22/2026: Let's go through the specced emails and specify the From / CC / BCC

Tim Reitz 01/23/2026: Went through today. 

  


_VA: Tim Reitz 12/11/2025:  Let's see about BCC'ing an email address so that the service can have a copy of everything that was sent.

_GZ: Tim Reitz 01/13/2026: We'll need this email address from Glen by some point in coding.

TODO_VA: Tim Reitz 01/23/2026: Per Glen today, this would be nice to have a central place to go to for history of emails that were sent. Let's use "historybcc@" for this. 

TODO_VA: Tim Reitz 01/23/2026: Let's include keywords in the emails for easy searching - include "Account #" / "Account Group #" / etc.
