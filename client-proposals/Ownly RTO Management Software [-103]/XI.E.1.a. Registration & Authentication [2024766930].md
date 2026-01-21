11.5.1.1. Registration & Authentication

TODO_JB

  


Signup:

  * Email
  * Verify with
    * Account #
    * Contract #



  


  * Send OTP to verify email & confirm on Contact record
  * Prompt for 2FA:
    * Phone ending in x1650
    * Phone ending in x4445
    * Other Phone ________
  * Verify phone & stomp 2FA on contact record



  


  * Password
    * 12+ characters
    * At least one of upper, lower, punctuation, and digit



  


  * Checkbox to agree to terms of service



Jonathan Bergen 11/24/2025: TODO_IDD: where do the ToS come from? RTO CO-specific or global to the Ownly system?

Jonathan Bergen 01/08/2026: Going with RTO CO-specific

  


  * Partial signups should time out in <24hr



  


Contact Record:

  * Add a Verified checkbox to email and phone RGs that gets set anytime they confirm an OTP
  * Portal section
    * [ ] Disable login
    * Portal Email
    * Portal 2FA Phone #
    * Last Login Date / Time
    * Hidden fields
      * Portal Salt
      * Portal Hashed Password
  * Validate against multiple portal emails
    * validate that the portal email + phone is in the respective RGs



  


  


Login:

  * Email
  * Password
  * By using this website, you agree to terms of service (with link).
  * Forgot Password



  


TODO_IDD:

  * Consider 2FA + [ ] Trust this device for 30/60/90 days.
  * OR require touchpoints inside the app to re-request 2FA?
    * Payments  > 1 monthly payment
  * Log the date/time/IP of accepting the terms of service



  


Portal:

  * Allow updating email and/or phone after confirming OTP


