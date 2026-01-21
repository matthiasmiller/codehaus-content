7.1. Landowner Payment Summary Email

  


Requirements

Overview/Purpose: This email is sent to Landowners of Tracts for which the Purchase Type is "Adjustable Tiered Percentages", and is sent out when Eby's settles their payments. The email includes a PDF attachment of the Landowner % Payments Summary Report printout.

  


If there are multiple landowners for the Tract, the email is sent to all of them who have an email address set on their Contact record. If a Contact has multiple email addresses, this email will be sent to the one listed as Primary. There is no warning if there are missing email addresses for any Landowner contacts (and those therefore will be skipped).

  


Sent via: The "Send Landowner Summaries for Selected Pmts" button on the Payments reports. 

  


From: as set in AppHosting.zone Settings (initially [eztally@ebysawmill.com](mailto:eztally@ebysawmill.com))

  


To:

  * The Primary email address for all Landowners for a selected Tract who have an email address set on their Contact record 
  * Any additional email addresses set in AppHosting.zone Settings



  


Cc: as set in AppHosting.zone Settings (initially [leo@ebysawmill.com](mailto:leo@ebysawmill.com))

  


Bcc: as set in AppHosting.zone Settings (initially [tally@ebysawmill.com](mailto:tally@ebysawmill.com))

  


Reply To: as set in AppHosting.zone Settings (initially [david@ebysawmill.com](mailto:david@ebysawmill.com))

  


Subject: Payment Summary

  


Attachments:

  * PDF printout of the current Landowner % Payments Summary Report for the selected Landowner (see the corresponding Printout section of the proposal)  



  


Body: as set in AppHosting.zone Settings, initially the following: 

Hello,

  


Your most recent timber tract statement is attached. If you have any questions about it do not hesitate to reach out to me. 

  


Thanks,

  


David Musselman III

814.767.8060

[david@ebysawmill.com](mailto:david@ebysawmill.com)

  


Other Notes:

  * N/A



  


Development Specification

Tim Reitz 11/09/2022: 

  * Batch sending from the Payments Due report (Email Selected Paid Payments button) 
  * Send to individual contact from Payment record (Email Payment Summary link)



  


Ellis Miller 12/21/2022: 

[ ] The AppHostingSettingEmailBody_LandOwnerPayment(?) memo field as an expression field at the Contact level.

[ ] The filename is in the Printout spec.

  


[ ] Merge r20 with multi-select Contacts prompt (I think the Paid Payments can be translated to Contacts, if not, we will add a multi-select Payment IDs prompt).

[ ] To is the email address for the Contact.

  


BID: 6 HOURS
