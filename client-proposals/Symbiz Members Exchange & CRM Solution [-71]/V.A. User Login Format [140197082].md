5.1. User Login Format

  


Requirements

The Solution will user the username/password login format for all users. This means that users with access to the Solution will log in with the following credentials: 

  * Username (either their "User ID" or the email address associated with their User Profile)
  * Password 



  


Note that at this time, Silverloom does not use MFA (multi-factor authentication). Users should be careful to use secure passwords and keep their login credentials safe. 

  


Username Details: 

  * When a member is given login access to the Solution via the standard process for an online Member (the "Create User Login" button on the Contact record), the Solution automatically generates a User ID for that member. This is done in the following format: <FirstName.LastName.ContactID>. 
  * A User ID can be manually set or edited. 



  


Password Details: 

  * The user's password is configured on their User Profile record (not the Contact record). 
  * Default password requirements: Minimum of 8 characters, must include at least 1 letter and 1 number ("Alpha, Numeric"), and must be changed once per year. These settings can be adjusted by an Admin in the System Switches section of the database (but it is not recommended that the requirements be set any looser than this). 
  * Password expiration date: 100,000. These settings can be adjusted by an Admin in the System Switches section of the database (but it is not recommended that the number be set any lower than this)



  


Other Notes: 

  * Note that an email address is required by the database for all User Logins, even if the user is not using the Quick Login format. If a user does not have an email address, one workaround if for the admin to enter a Gmail or Gmail-hosted email address and simply add "+" and the user's name before the "@" symbol. CodeHaus can provide more information on this process. 
  * If desired, CCI will work with Symbiz's website developer to tie in a login link to the Symbiz website.



  


Development Specification

Change Requests: 

  * Tim Reitz 07/22/2024: [[[IN10098](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10100&)]] - ZSB - User Login - Users can now use email or User ID to log in
  * Ben Reitz 05/01/2025: [[[IN11330](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11332&)]] - ZSB - Passwords - Stop passwords from needing to be changed?


