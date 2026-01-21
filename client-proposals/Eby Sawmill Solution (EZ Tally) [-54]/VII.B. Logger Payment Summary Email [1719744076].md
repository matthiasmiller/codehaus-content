7.2. Logger Payment Summary Email

  


Requirements

Overview/Purpose: This email is sent to Logger contacts each time Eby's pays them. The email includes a PDF attachment of the Logger Payment Summary Report printout.

  


If a Logger contact has multiple email addresses, this email will be sent to the one listed as Primary. If a Logger does not have an email address specified, the email is sent to David Mussleman instead.

  


Sent via: The "Send Logger Summaries for Selected Pmts" button on the Payments reports.

  


From: as set in AppHosting.zone Settings (initially [eztally@ebysawmill.com](mailto:eztally@ebysawmill.com))

  


To:

  * The Primary email address for the Logger for a selected Tract who have an email address set on their Contact record (or to [david@ebysawmill.com](mailto:david@ebysawmill.com) if no email address is set on the Contact record) 
  * Any additional email addresses set in AppHosting.zone Settings



  


Cc: as set in AppHosting.zone Settings (initially N/A)

  


Bcc: as set in AppHosting.zone Settings (initially [tally@ebysawmill.com](mailto:tally@ebysawmill.com)) 

  


Reply To: as set in AppHosting.zone Settings (initially [david@ebysawmill.com](mailto:david@ebysawmill.com))

  


Subject: Logger Payment Summary - <Logger Name>

  


Attachments:

  * PDF printout of the Logger Payment Summary for the most recent payment to the selected Logger (see the corresponding Printout section of the proposal)



  


Body: as set in AppHosting.zone Settings, initially the following:

Hello,

  


Your most recent payment statement is attached.

  


Thanks,

  


David Musselman III

814.767.8060

[david@ebysawmill.com](mailto:david@ebysawmill.com)

  


Other Notes:

  * If there is no email address for the Logger, the email body will start with the following note: "This email was sent to you because the Logger has no email address set on the Contact record."



  


Development Specification

Tim Reitz 11/09/2022:

  * Batch sending from the Payments Due report (Email Selected Paid Payments button) 
  * Send to individual contact from Payment record (Email Payment Summary link)



  


  


BID:

[ ] Almost identical to LandOwner Payment. See design there.

  


BID: 4 HOURS
