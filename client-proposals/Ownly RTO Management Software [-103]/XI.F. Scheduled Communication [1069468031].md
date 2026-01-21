11.6. Scheduled Communication

Setup

  


  * System Switches
    * Set SMTP switches



  


  * RTO Company
    * Override Sending Email Address
    * Sending Email Address (show system switch value if unset)
    * Memo for Email Footer



  


  * Scheduled Task
    * Daily SMS x30
    * Daily Email x30



  


  * Communication Template
    * Name
    * [ ] Send SMS
    * [ ] Send Email



  


  * For Email
    * Subject
    * Body
  * For SMS
    * Contents - allows embedded expressions



  


  * Main Screen
    * Condition (list of conditions; "(advanced)" and read-only if multiple rows in the RG or if the single row does not have "Equal To")
    * Value (value) -- "(advanced)"
  * Ellipsis button shows the full RG
    * Drop List
      * # Days Past Due
      * # Days Until Due
      * # Days Since Grace Ended
      * # Days Until Grace Ends
      * # Days Since Last Payment
    * Comparison
      * Less Than
      * Less Than or Equal To
      * Equal To
      * Greater Than or Equal To
      * Greater Than
    * Value
      * (number)
  * Validation:
    * Require at least 1 "Equal To" comparison
    * Add an OnInit to show 1 row with "# Days Past Due" and "Equal To"



  


  * Add a "Do Not Text" checkbox on the contact
  * Add a "Do Not Email" checkbox on the contact.
  * Automatically include a link at the bottom of each email with a URL that goes to the WSGI that allows them to unsubscribe (or optionally, to re-enable). Say something like:



  


By unsubscribing from email notifications, you will no longer receive email invoices, receipts, or notifications for payment.
