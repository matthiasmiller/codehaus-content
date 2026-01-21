7\. Emails

  


Requirements

The EZ Tally Solution can send various emails with attachments. Emails are previewed prior to being sent, but cannot be edited. However, the templates can be adjusted by admins on the AppHosting.Zone Settings page. 

  


Sent emails will not appear in the sender's Sent folder, but the BCC feature can be used if the sender wishes to have a copy of all emails that are sent out.

  


The AppHosting.zone Settings page includes a custom Email Templates section with buttons to open up child screens that hold fields for various parts of the emails, such as To, Cc, Reply To, and the email body. This will vary as needed for different emails and will allow Admin users to make changes to these things. See the corresponding section of this living spec for details.

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1184620589](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1184620589)

  


This will use email merges, not email records.

  


We'll need a WSGI for the app, so we can use that for the bookings email.

Ellis Miller 12/21/2022: TODO_EM: Talk to Josh about cost for setting up this for Booking photos.

  


DONE_MM: how much does it cost to get SMS integration set up? Would it be a good option for these alerts.

Monthly cost is $20 + Twilio costs

DONE_TR: Comment in HLD pricer sheet assigned to Josh

DONE_TR/NM: follow up when Josh replies. See the sheet: [https://docs.google.com/spreadsheets/d/1eCNSZ-QCOS4AdjVBVChpgfWZjIIZvsSRMI8tafU7zZI/](https://docs.google.com/spreadsheets/d/1eCNSZ-QCOS4AdjVBVChpgfWZjIIZvsSRMI8tafU7zZI/).

DONE_DM: Tim Reitz 11/17/2022: This is $1,500-$3,000 for setup (depending on complexity). Monthly is $20 + Twilio fees for messages, etc.
