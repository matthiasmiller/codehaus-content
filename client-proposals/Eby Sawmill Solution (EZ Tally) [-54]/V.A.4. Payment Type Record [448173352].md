5.1.4. Payment Type Record

  


Requirements

Overview: Payment Types are used to determine various information on Payment records, such as what Contact Type can receive the payment and which fields are visible.

  


Accessed via: View Payment Types report

  


Sections and Fields: 

  * Active (checkbox; defaults to filled)
  * Name (required; text field; validate against active Payment Type records with duplicate Names)
  * Code (numeric string; auto-set and read-only; used in the Payment ID) 



  


Data Access:

  * View record: All users (specifically to allow users to view Description, Abbreviation, Hotkey in lists, records, etc. throughout the system)
  * Read-only for all users



  


Other Notes:

  * These records are set up in development and are not editable by users in the Solution.
  * The Solution includes the following Payment Types: 
    * Landowner Flat 
    * Landowner % 
    * Logger 
    * Vendor



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=38481763](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=38481763)

  


Simple record with shipped lookup data.

  


Code the "View Payment Types Report" as part of this.

  


BID: 3 hours
