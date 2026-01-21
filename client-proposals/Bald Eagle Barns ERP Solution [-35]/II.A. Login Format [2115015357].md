2.1. Login Format

  


Requirements

Users can log into their accounts with either a username/password or using a Google account (called "Quick Login"). Shop Workers can log in to the shop dashboard with only a PIN. 

  


The login format (UN/PW or Quick Login) is determined on the user's User Profile. If using the UN/PW format, the password is also set on the User Profile. These are standard features. 

  


Password requirements for BEB: Minimum of 6 characters; at least 1 capital letter, 1 number, and 1 special character ("Alpha, Numeric, Symbol"). This is set in the System Switches section of the database. 

  


Shop PIN: On the User Profile, there will be two custom fields for setting the Shop PIN. Any user can have a Shop PIN configured; this is not limited to only Shop Workers. 

  * New Shop PIN 
  * Confirm Shop PIN 



Validation for these fields: 

  * They must be numeric
  * They must be at least 4 digits
  * They must match each other
  * The PIN must be unique for each user, so that it can be used to uniquely identify the user when they are logging in



  


Other Notes: 

  * Note that an email address is required by the database for all User Logins, even if the user is not using the Quick Login format. If a user does not have an email address, one workaround if for the admin to enter a Gmail or Gmail-hosted email address and simply add "+" and the user's name before the "@" symbol. CodeHaus can provide more information on this process.
  * BEB can set up one or more generic user logins for situations where members are temporarily working in a role other than their normal role (for example, when the service man work on buildings in the shop).



  


*Done.

  


Development Specification

See job about handling both login types: [https://clientscope.invtools.com/Detail/View/2?RecordType=Holding&StringID=PC0122488&NumberID=0&InvestUrl=8-P&State=fKVHIEcvvHQ&](https://clientscope.invtools.com/Detail/View/2?RecordType=Holding&StringID=PC0122488&NumberID=0&InvestUrl=8-P&State=fKVHIEcvvHQ&)

  


Shop Login PIN: 

  * Add a hidden UserShopPINSalt that is set to a random 4-character string when New PIN is changed to a non-blank value.
  * Add a hidden UserShopPINHash that is set to "MD5(UserShopPINSalt + UserNewShopPIN)" if a PIN is set to a non-blank value.
  * Add a macro called UserMatchesShopPIN(pin) that is set to If (NOT IsNA(UserShopPINSalt) AND NOT IsNA(UserShopPINHash), MD5(UserShopPINSalt + pin) = UserShopPINHash). Use this to validate against other users that have the same PIN.



  


Using the "+" feature in Gmail: [https://support.google.com/a/users/answer/9308648?hl=en](https://support.google.com/a/users/answer/9308648?hl=en)

  


  


Tim Reitz 12/07/2021: Users: 

\- Shop workers/Drivers/office workers/admins/RTO/member salespeople: 22-25 

\- Non-member salespeople: 8-9 for now
