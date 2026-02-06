10.2.1. "New Account Reseller Transfer Request" Email Merge

Overview: This is an email merge that is sent automatically when a Reseller transfer is requested for an Account record. This is sent to the Account Reseller who needs to approve the transfer request, and all Master Administrators.

  


Sent Via: the "Send "New Account Reseller Transfer Request" Email" triggered automatic process (see corresponding spec) 

  


From: __

_GZ: Tim Reitz 01/22/2026: "automation@" or "no-reply@" or ??

TODO_VA: Tim Reitz 01/23/2026: "automation@"

  


To: __

TODO_VA: Tim Reitz 01/23/2026: to the Account Reseller who needs to approve the transfer request

TODO_VA: Tim Reitz 01/22/2026: which email address? ("Primary", or one from the Traccar Login RG on the Contact record?)

TODO_VA: Tim Reitz 01/22/2026: Also, sometimes Prior and sometimes New

  


CC: 

_GZ: Tim Reitz 01/22/2026: Needed here?

TODO_VA: Tim Reitz 01/23/2026: CC all Master Administrators

  


BCC: __

_GZ: Tim Reitz 01/22/2026: Needed here?

TODO_VA: Tim Reitz 01/23/2026: Yes to BCC. 

  


Reply To: 

_GZ: Tim Reitz 01/22/2026: Needed here?

TODO_VA: Tim Reitz 01/23/2026: Reply To the requesting Reseller

  


Subject: "New Account Reseller Transfer Request"

  


Attachments: N/A

  


Body:

  


A reseller transfer has been requested for the following account, and is needing your approval: <Account #, link to record>.

  


Prior Reseller: <displays the "Prior Reseller" for the corresponding row of the "Account Reseller History" non-embedded spreadsheet>

  


New Reseller: <displays the "New Reseller" for the corresponding row of the "Account Reseller History" non-embedded spreadsheet>

  


Requested by: <displays the "Requested By" for the corresponding row of the "Account Reseller History" non-embedded spreadsheet>

  


Reason / Comments: <displays the "Reason / Comments" for the corresponding row of the "Account Reseller History" non-embedded spreadsheet>

  


If you are the current reseller, please close out the subscription and resolve any other details before approving the request.

  


  


Other Notes:

  * N/A


