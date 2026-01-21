7.3. Vendor Yard Tally Summary Email

  


Requirements

Overview/Purpose: This email is sent on a per-Yard Tally basis to an individual Vendor contact who has sold logs to Eby's. It can be sent individually from the Yard Tally (computer or yard app), or batch sent when Eby's settles payments for Vendors. This email includes a PDF attachment of the Yard Tally Summary.

  


If a Vendor contact has multiple email addresses, this email will be sent to the one listed as Primary. If a Vendor does not have an email address specified:

  * attempting to send the email from the link on the Yard Tally record results in the following message: "This vendor does not have a primary email address.".
  * attempting to send the email for only that Vendor from the button on the Payments reports results in the same message. 
  * attempting to send the email for multiple Vendors, including that Vendor and at least one other Vendor with an email address, from the button on the Payments reports does not display any error message. 
  * attempting to send the email from the Yard App does not result in any error message. 



  


Sent via:

  * The "Email Yard Tally Summary" link on Yard Tally record.
  * The "Send Yard Tally Summaries for Selected Pmts" button on the Payments reports.
  * The "Email Yard Tally Summary" / email icon buttons in the Yard App.



  


From: as set in AppHosting.zone Settings (initially [eztally@ebysawmill.com](mailto:eztally@ebysawmill.com))

  


To:

  * The Primary email address for the Vendor for a selected Tract who have an email address set on their Contact record 
  * Any additional email addresses set in AppHosting.zone Settings



  


Cc: as set in AppHosting.zone Settings (initially N/A)

  


Bcc: as set in AppHosting.zone Settings (initially [tally@ebysawmill.com](mailto:tally@ebysawmill.com)) 

  


Reply To: as set in AppHosting.zone Settings (initially N/A) 

  


Subject: Yard Tally Summary for Tally <ID> 

  


Attachments:

  * PDF printout of the Yard Tally Summary for the corresponding Yard Tally (see the corresponding Printout section of the proposal) 



  


Body: as set in AppHosting.zone Settings, initially the following: 

Hello,

  


Please see attached tally number <Yard Tally ID> scaled on <Yard Tally Created Date (mm/dd/yyyy)>. There is a total of <Total Board Feet> board feet and a total value of $<Total Value>.

  


Thank you for your business.

  


Eby Sawmill LLC 

814.767.8060

[office@ebysawmill.com](mailto:office@ebysawmill.com)

  


Other Notes:

  * As mentioned in the overview, this email is sent on a per-Tally basis, even if multiple Yard Tallies are linked to one Payment record.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1158742920](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1158742920)

  


Ellis Miller 12/21/2022:

[ ] Left pane prompts:

[ ] BookingsByCustomer.ndx

[ ] TalliesByBooking.ndx

[ ] TalliesByBookingIDAndContainerID.ndx (added for Booking report)

  


Right Pane:

[ ] Note that this is not row-dependent, it is simply a different view to all of the data in the left pane.

  


  


  


BID: 1 Day
