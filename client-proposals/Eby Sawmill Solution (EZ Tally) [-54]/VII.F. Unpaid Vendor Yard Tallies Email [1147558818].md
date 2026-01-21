7.6. Unpaid Vendor Yard Tallies Email

  


Requirements

Overview: This is an internal email reminder that is sent when there are Yard Tallies with a Source of Vendor that have not been Closed within 5 days of the Creation Date. 

  


Sent via: The "Daily Payment Emails" background process that runs at 7:00am every day where the above condition exists (resend for the same Yard Tally if it has not been confirmed since the last email was sent)

  


From: as set in AppHosting.zone Settings (initially [eztally@ebysawmill.com](mailto:eztally@ebysawmill.com))

  


From: as set in AppHosting.zone Settings (initially [eztally@ebysawmill.com](mailto:eztally@ebysawmill.com))

  


Cc: as set in AppHosting.zone Settings (initially N/A)

  


Bcc: as set in AppHosting.zone Settings (initially N/A) 

  


Reply To: as set in AppHosting.zone Settings (initially N/A) 

  


Subject: Unpaid Vendor Yard Tallies

  


Attachments: N/A

  


Body: as set in AppHosting.zone Settings, initially the following:

David, 

  


There are one or more Vendor Yard Tallies that have not been Closed in 5 days: <link to the Yard Tallies Report with the Status filter set to "Open" and "Confirmed" and Source filter set to "Vendor">. 

  


Other Notes:

  * N/A



  


Development Specification

YardTalliesOlderUnpaid subset that does an NdxFind for Open/Confirmed items and then checks that date is >= 5 days.

[ ] Add a YardTalliesByStatus.ndx

[ ] Make this a TotalOnly report that sends the email if we have any matching records

  


Will be used by a report alert.

  


BID: 4 HOURS
