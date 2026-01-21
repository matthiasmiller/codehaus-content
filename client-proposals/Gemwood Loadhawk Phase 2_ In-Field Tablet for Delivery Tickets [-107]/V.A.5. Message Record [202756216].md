5.1.5. Message Record

Overview: This record is used to send an in-app message to members..

  


Accessed via: Main Menu | Mobile App | Send Message

  


Sections and Fields: 

  * Message section: 
    * Subject (plain text)
    * <Date> <Time> (date and time the record was created)
    * Body (multi-line plain text; body of message to be sent to member)
    * Members (virtual embedded spreadsheet; includes one row for every active member contact + any inactive contacts to whom the message was sent)
      * Columns:
        * Include Member (unlabeled checkbox column; sends the message to the member)
        * Member (uneditable)
        * Read (checkbox; uneditable)
    * Members (Debug) (button; visible in test systems; opens the underlying RG of included members)
      * (unlabeled embedded spreadsheet)
        * Columns:
          * Member (drop-list of contacts)
          * Replied (checkbox)
    * Activity History (link to open the report for the record)


