10.2.4. "New Account Member Welcome" Email Merge

  


Requirements

TODO_VA: Tim Reitz 12/30/2025: Add a "welcome email" that sends on the first Save after a new row is added to the "Account Members" RG on an Account record. 

Tim Reitz 01/08/2026: Adding more notes, and breaking out into checkboxes: 

[X] Sent via the "Send "New Account Member Welcome" Email" triggered automatic process

[X] Sends to "Traccar Login Email" address for the row. 

[X] Includes a login link (technically the password reset link) for Traccar, and any necessary instructions for logging in & setting up the account.

[ ] And instructions for logging into Traccar 

[ ] And instructions for accessing the Portal 

[ ] And a note about needing to agree to the EUA

  


[X] Probably have a memo in Silverloom Settings to specify the email body.

  


Existing note: The email that goes to the new user includes the Password Reset link ([https://x6rildfvs.traccar.com/reset-password](https://x6rildfvs.traccar.com/reset-password)). The end user resets their password with this (they can't get in otherwise, since they don't have the initial password).

  


\------------

  


Overview: This is an email merge that is sent automatically to new account members (Account Managers and Drivers) when they are added.

  


Sent Via: The "Send "New Account Member Welcome" Email" triggered automatic process

  


From:

_GZ: Tim Reitz 01/22/2026: "automation@" or "no-reply@" or accounts@ or the Resller??

TODO_VA: Tim Reitz 01/23/2026: From "automation@" 

  


To: <the "Traccar Login Email" for the corresponding new Account Member> 

  


CC: 

_GZ: Tim Reitz 01/22/2026: Any needed here? 

TODO_VA: Tim Reitz 01/23/2026: CC existing Account Manager(s). Not the reseller. 

  


BCC:

_GZ: Tim Reitz 01/22/2026: Any needed here? 

TODO_VA: Tim Reitz 01/23/2026: Yes to BCC 

  


Reply To: 

_GZ: Tim Reitz 01/22/2026: Any needed here? 

TODO_VA: Tim Reitz 01/23/2026: Reply To the reseller. 

  


Subject: "Welcome to <Service Name>!" 

  


Attachments: N/A

  


Body: 

TODO_VA: Tim Reitz 01/22/2026: Let's move this to a memo in Silverloom Settings. 

  


<FirstName>, 

  


Welcome to <Service Name>! 

  


Your Account # is __

  


Your Account Reseller is __

  


Your Account is under the __ Account Group 

  


There are a few software tools available to you: 

<Service Name> Portal: <__ link> 

  


Traccar Web Interface: To log in for the first time, go to [https://x6rildfvs.traccar.com/reset-password](https://x6rildfvs.traccar.com/reset-password) and enter the email address that you used to sign up with <Service Name>. 

  


Traccar Manager App: Available for both iPhone and Android devices: 

  * iPhone: [https://apps.apple.com/us/app/traccar-manager/id1113966562](https://apps.apple.com/us/app/traccar-manager/id1113966562)
  * Android: [https://play.google.com/store/apps/details?id=org.traccar.manager](https://play.google.com/store/apps/details?id=org.traccar.manager)



  


Reply to this email to __ your Account Reseller. 

  


Other Notes:

  * N/A



  


Development Specification

Tim Reitz 01/23/2026: It would be cool to include a copy of the current EUA PDF with the welcome email. We would need this job to do it: [[[IN12242](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12244&)]] - CORE - Add ability to attach PDF doc archive files for email attachments.
