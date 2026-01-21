6.3. Membership Status List

  


Requirements

This is a non-editable simple list used to track the status of a member's membership. It includes the following items:

  


  * Application Approved: 
    * Use case: after the Lead process is complete, this is the first status for a new member when the Contact Type is changed from "Lead" to "Member"; 
    * Logic: if the Initial Invoice Sent checkbox is not filled. 
  * Initial Invoice Sent: 
    * Use case: when the invoice has been sent, but payment has not been received; 
    * Logic: when the Initial Invoice Sent checkbox is filled. 
  * Payment Received: 
    * Use case: when the initial or reactivation invoice has been sent and payment has been received, but the contact's membership has not been activated yet; 
    * Logic: when "Payment Received Date" is set for the top row and the "Active Membership" checkbox is not checked and Membership End Date is not set. 
  * Annual Renewal Due: 
    * Use case: repeating item that happens once a year; 
    * Logic: when the Invoice Sent Date for the latest non-initial row of the Membership History embedded spreadsheet is not set and the Next Renewal Date for the previous row either is within 30 days of the current date or is in the past. 
  * Annual Renewal Invoice Sent: 
    * Use case: once the invoice for the annual renewal payment has been sent to the member; 
    * Logic: when the Invoice Sent Date for the latest non-initial row of the Membership History embedded spreadsheet is set and the Payment Received checkbox for the same row is not filled. 
  * Member Without Group: 
    * Use case: when a member has an active membership but has not yet been assigned to a Growth Ring Group; 
    * Logic: when the "Active Membership" checkbox is checked and the member is not part of any Growth Ring Group. 
  * Ongoing Membership: 
    * Use case: once initial or renewal payment has been received; 
    * Logic: when the "Active Membership" checkbox is checked and the member is part of at least one Growth Ring Group. 
  * Inactive Membership: 
    * Use case: when there is no active membership for the member; 
    * Logic: if the "Active Membership" checkbox is not checked and the Membership End Date is set.



  


This list is universal for all users.

  


Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

  


This list will be set up by CCI as part of the main development. If changes need to be made to this list, it will require some coding work.

  


Development Specification

Mockup: N/A

  


  


Change Requests: 

  * Tim Reitz 04/08/2024: [[[IN9596](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9598&)]] - ZSB - Contact - (Simplified) Clean up Renewal Process & Fields: Changes to Membership Status List


