10.4.1. Customer Portal

  


Requirements

Customer Portal for Account Setup and Payments

  


Two-factor Authentication:

  * Username and Password stored on Contact record.
    * Username must be unique in the system.
    * Store the hashed password using SHA256 HMAC, salt stored on Contact record.



TODO_Permissions: visibility and editability for login fields.

  * SMS or Email one-time code after successful UN/PW
    * Email and SMS codes sent through Silverloom.



  


Pages:

  * Profile
    * First Name
    * Last Name
    * SSN
    * DOB
    * Driver License (Num, State, plus photo)
  * Items
    * Purchase amount
    * Amount remaining
    * Early payoff
  * Payments
    * Upcoming payments
    * Make payment link
    * History



  


Development Specification

Jonathan Bergen 07/10/2025: 

All pages should be pathed, since we want to send links to specific places.
