8.3. Booking Ready for Invoicing Alert

  


Requirements

Overview/Purpose: This is an internal alert that is sent when a Booking is ready to be invoiced (when all Export Tallies for a Booking have been marked as Loaded). Note that this is the same as the Bookings Ready for Invoicing Email (redundancy seems helpful for this alert).

  


Title: Booking Ready for Invoicing

  


Sent via: A report alert that runs within 20 minutes of when the above condition exists for at least one Booking record. 

  


Action: Link opens the Bookings report with the Status filter set to "Ready for Invoicing". Note that if there is only one Booking ready for invoicing, the Booking will open (skipping the report).

  


User(s) to notify: All Administrators

  


Other Notes: 

  * N/A



  


Development Specification

Ellis Miller 12/22/2022: 

  


[ ] Just make Booking report a report alert with a hidden, ignored vLastViewedAlertID ask prompt. Set up the report alert to run the Booking report with "Ready for Invoicing"

BID: 4 HOUR
