7.5. Landowner Flat Payments Due Email

  


Requirements

Overview: This is an internal email reminder that is sent when there are Flat Rate Date-based Payments for Landowners that are coming due (not needed for Harvest-based flat payments). This should be triggered a week before the payment Due Date (one email per day that includes all payments that are coming due). 

  


Sent via: The "Daily Payment Emails" background process that runs at 7:00am on the day that is 7 days before the Payment Due Date, and continues to run as long as the payment is due

  


From: as set in AppHosting.zone Settings (initially [eztally@ebysawmill.com](mailto:eztally@ebysawmill.com))

  


From: as set in AppHosting.zone Settings (initially [eztally@ebysawmill.com](mailto:eztally@ebysawmill.com))

  


Cc: as set in AppHosting.zone Settings (initially [leo@ebysawmill.com](mailto:leo@ebysawmill.com)) 

  


Bcc: as set in AppHosting.zone Settings (initially N/A) 

  


Reply To: as set in AppHosting.zone Settings (initially N/A) 

  


Subject: Landowner Flat Payments Due

  


Attachments: N/A

  


Body: as set in AppHosting.zone Settings, initially the following: 

David,

  


There are landowner flat payments due for the Tract(s): 

  


<list of Tracts>

  


Open the report to view/pay: <link to the Landowner Flat Payments Due Report>.

  


Other Notes:

  * There will also be a reminder in the Solution for this same thing, as there is value in redundancy for alerts like this (see the corresponding section of the proposal for details about the system alert)



  


Development Specification

Ellis Miller 12/21/2022: NOTE that we will need to define a scheduled task for this.

  


BID:

[ ] None-level expression requirements for memo

4 Hours
