6.4. Subscription Record

Overview: Subscriptions will be used to track a Lesson that an Organization has purchased. They can be viewed on a Subscriptions report.

  


Accessed via: (TBD in IDD)

  


Sections and Fields: 

  * Subscription Details (includes fields such as):
    * Subscription Status (auto-set and read-only or a drop list; options such as Pending, In Progress, Complete, Cancelled; details to be determined in IDD)
    * Organization (auto-set and read-only; based on the Organization that signed up for the Subscription)
    * Pathway (auto-set and read-only; based on the Pathway that was selected at sign-up) 
    * Start Year (required; selected at sign-up)
    * Start Month (required; selected at sign-up)
    * Sending Week of Month (required; selected at sign-up)
    * Sending Day of Week (required; selected at sign-up)
    * # of participants (auto-set and read-only; displays the number of active participants in the Participants embedded spreadsheet) 
    * Send books (required; drop list of Yes / No; if set to Yes, the Solution reminds FB personnel to send the physical copies of the books used in the Pathway to the Board Rep at the conclusion of the Pathway; note that shipping should have an extra charge if sent outside the US) 
    * Cancel Subscription (checkbox; if checked, the Lesson communications will no longer be sent to the Organization)



  


  * Participants Section (embedded spreadsheet of the following):
    * Columns: 
      * Active (checkbox; defaults to checked)
      * First Name (required; plain text)
      * Middle Name (optional; plain text) 
      * Last Name (required; plain text)
      * Method of Delivery (required; drop list of: Email, Fax, Mail; conditional on the participant's country)
      * Email (required if Method of Delivery is Email, otherwise optional)
      * Fax (required if Method of Delivery is Fax, otherwise optional)
      * Mailing Address (separate columns for Address Line 1 and Line 2; required if Method of Delivery is Mail) 
      * Completed (checkbox; automatically filled when the Participant completes the Pathway; details TBD in IDD)
    * Automatically sorted by: First by Active / Inactive, then by Name (alphabetical)
    * Buttons to append/remove rows: "+" / "-" (validate against removing an Active participant) 
    * Show 10 rows without scrolling.



  


  * Pricing Details Section (includes fields such as):
    * Price per Seat
    * Add-ons
    * Total Cost
    * Payments (embedded spreadsheet with information such as:) 
      * Payment Type (Check / Card) 
      * # of Seats (editable; defaults to the # of remaining unpaid seats for the Subscription) 
      * Total Amount (auto-calculated) 
      * Link to Stripe Payment 
      * Check # (editable and required if Type = Check) 
      * Send Receipt (possibly) 
    * Link to Receipts (possibly) 



  


  * Payments Section (includes fields to track payments, both card and check, made for the subscription) 



  


  * Email Tracking Section 
    * Embedded spreadsheet of email responses, with option to manually add rows
    * Other details to be be determined in the IDD



  


Data Access: (TBD in IDD)

  


Special Considerations: (TBD in IDD)

  * Copy Record: 
  * Delete Record: 
  * Merge Record: 



  


Other Notes (details to be determined in the IDD):

  * Allow for superficial edits like spelling or grammar changes. 
  * When someone is added to a subscription in progress, the price for the new seat probably will be the current price (if the subscription price per seat has changed). But if it is enough simpler to grandfather them in at the original price, that could be considered as well. 
  * If a seat is added, the organization is billed the full price (not prorated). 
  * If a seat is added, the new participant should receive all of the past Lessons that were sent out (so that he can receive the full content of the pathway). 
  * If a seat is removed, no refund. 



  


Other Notes: 

  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).


