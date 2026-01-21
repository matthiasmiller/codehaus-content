7.7. Booking Ready for Invoicing Email

  


Requirements

Overview: This is an internal email that is sent when a Booking is ready to be invoiced (when all Export Tallies for a Booking have been marked as Loaded).

  


Sent via: A database trigger that runs as soon as the above condition exists (sent once for each occurrence) 

  


From: as set in AppHosting.zone Settings (initially [eztally@ebysawmill.com](mailto:eztally@ebysawmill.com))

  


From: as set in AppHosting.zone Settings (initially [david@ebysawmill.com](mailto:david@ebysawmill.com))

  


Cc: as set in AppHosting.zone Settings (initially N/A)

  


Bcc: as set in AppHosting.zone Settings (initially N/A) 

  


Reply To: as set in AppHosting.zone Settings (initially N/A

  


Subject: Booking <ID> Ready for Invoicing

  


Attachments: N/A

  


Body: as set in AppHosting.zone Settings, initially the following:

David, 

  


Booking <ID> is ready to be invoiced: <link to Booking record>. 

  


Other Notes:

  * N/A



  


Development Specification

Ellis Miller 12/21/2022: 

[ ] Memo is Booking expression requirements

[ ] Need to define a trigger.

BID: 1 Day
