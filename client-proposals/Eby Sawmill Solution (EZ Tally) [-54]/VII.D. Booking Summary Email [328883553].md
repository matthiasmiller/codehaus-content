7.4. Booking Summary Email

  


Requirements

Overview/Purpose: This email is sent to an individual Customer contact when Eby's has completed a Booking. It contains information about the Booking and the individual Export Tallies in that Booking. It includes two file attachments of the Export Tally Breakdown (one PDF and one Excel).

  


If a Customer contact has multiple email addresses, this email will be sent to the one listed as Primary, and the other addresses will be CC'd as well. If a Customer does not have an email address specified, the email is sent to David Mussleman instead.

  


Sent via: The "Email Booking Summary" link on the Booking record. 

  


From: as set in AppHosting.zone Settings (initially [eztally@ebysawmill.com](mailto:eztally@ebysawmill.com))

  


To:

  * The Primary email address for the Customer for a selected Tract who have an email address set on their Contact record (or to [david@ebysawmill.com](mailto:david@ebysawmill.com) if no email address is set on the Contact record) 
  * Any additional email addresses set in AppHosting.zone Settings



  


Cc: as set in AppHosting.zone Settings (initially [durrel@ebysawmill.com](mailto:durrel@ebysawmill.com)) 

  


Bcc: as set in AppHosting.zone Settings (initially [tally@ebysawmill.com](mailto:tally@ebysawmill.com)) 

  


Reply To: as set in AppHosting.zone Settings (initially [david@ebysawmill.com](mailto:david@ebysawmill.com)) 

  


Subject: Booking <ID> Summary 

  


Attachments:

  * PDF file of the Booking Summary printout (see the corresponding Printout section of the proposal) 
  * Excel file of the Booking Summary printout (see the corresponding Printout section of the proposal)



  


Body: as set in AppHosting.zone Settings, initially the following: 

Hello,

  


Please see attached booking, load information, and tallies for Booking <Booking ID>, <Total Loads> loads, <Description>. See the links below for photos of each load.

  


<list of links to the photos for each Export Tally on the selected Booking, one link/line for each photo in the following format:>

Load <Yard Tally ID> \- Image <Image ID>

Load <Yard Tally ID> \- Image <Image ID>

  


Thanks,

  


David Musselman III

814.767.8060

[david@ebysawmill.com](mailto:david@ebysawmill.com)

  


  


Other Notes:

  * The links to the photos will probably looks something like the following: 
    * [https://ebys.wsgi.apphosting.zone/images/<BookingID>/<ExportTallyID>/<ImageID>/](https://ebys.wsgi.apphosting.zone/images/<BookingID>/<ExportTallyID>/<ImageID>/) 
  * Anyone with the image links can view the images.
  * Image links will expire after 6 months.
  * There normally are 10 loads/tallies per Booking, but there can be more (up to 30 or so).
  * If there is no email address for the Customer, the email body will start with the following note: "This email was sent to you because the Customer has no email address set on the Contact record."



  


Development Specification

Tim Reitz 11/09/2022: 

  * Send individually from the Booking Record (Email Booking Summary link)



  


Ellis Miller 12/21/2022: .

  * 500 Up front / $25 / month for "Public facing attachments"



  


Ellis Miller 12/21/2022: 

[ ] Memo Expression Requirements: Booking

[ ] The memo links can be done by using the [[URL Display text]] syntax. Talk to me if you have questions.

  


BID: 8 HOURS
