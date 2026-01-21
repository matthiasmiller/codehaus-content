7.8. Export Tally Summary Email

  


Requirements

Overview/Purpose: This email is sent on a per-Export Tally basis to an individual Customer contact who is buying logs from Eby's. It can be sent individually from the Export Tally record. This email includes a PDF attachment of the Export Tally Summary.

  


If a Customer contact has multiple email addresses, this email will be sent to the one listed as Primary. If a Customer does not have an email address specified, attempting to send the email from the link on the Yard Tally record results in the following message: "This customer does not have a primary email address.".

  


Sent via: The "Email Export Tally Summary" link on the Export Tally record.

  


From: as set in AppHosting.zone Settings (initially [eztally@ebysawmill.com](mailto:eztally@ebysawmill.com))

  


To: 

  * The Primary email address of the selected Customer contact 
  * Any address(es) set in AppHosting.Zone Settings (initially N/A) 



  


Cc: as set in AppHosting.zone Settings (initially N/A)

  


Bcc: as set in AppHosting.zone Settings (initially [tally@ebysawmill.com](mailto:tally@ebysawmill.com)) 

  


Reply To: as set in AppHosting.zone Settings (initially N/A) 

  


Subject: Export Tally Summary for Tally <ID> 

  


Attachments:

  * PDF printout of the Export Tally Summary for the corresponding Export Tally (see the corresponding Printout section of the proposal) 



  


Body: as set in AppHosting.zone Settings, initially the following: 

Hello,

  


Please see attached tally number <Export Tally ID> for Booking <Booking ID>. There is a total of <Total Gross Board Feet> board feet. 

  


Thank you for your business.

  


Eby Sawmill LLC 

814.767.8060

[office@ebysawmill.com](mailto:office@ebysawmill.com)

  


Other Notes:

  * As mentioned in the overview, this email is sent on a per-Tally basis, even if multiple Export Tallies are linked to one Booking record.



  


Development Specification

Change Requests: 

  * Tim Reitz 08/31/2024: [[[IN10233](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10235&)]] - ZET - Add Export Tally Summary Printout


