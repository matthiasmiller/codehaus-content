15\. <Service Name> End User Portal

  


Requirements

Overview: The <Service Name> End User Portal allows end users (Account Managers and Drivers) to view certain details about their <Service Name> Account, and also perform some basic account-related functions. The capabilities of this portal could be expanded in the future (especially when subscription management is added).

  


Enter Email Screen: 

  * <Service Name> logo
  * Email Address (required; message on the field if the "Submit" button is clicked while this field is blank: "Please fill out this field.")  
  * Submit (button; clickable if "Email Address" is not blank; visible until it has been clicked with "Email Address" not blank)
  * If your email address matches a contact with portal access, you’ll receive a one-time login link. (on-screen message in green font; visible in the location of the "Submit" button after that has been clicked with "Email Address" not blank) 



  


  


My <Service Name> Account Details Screen: Upon clicking the one-time login link, the user is taken to this screen in the Portal: 

  


  * <Service Name> Logo 
  * Logout (button; securely logs out the user; note that the user or someone else with the link can log in again until link expires) 
  * Help (button; opens a lightbox with the following: 
    * Contact us for help.
    * <name> 
    * <title / role> 
    * <phone number> 
    * <email address>



_GZ: Tim Reitz 01/16/2026: would you like a button for technical help? (other than the reseller)

TODO_VA: Tim Reitz 01/23/2026: Yes, Glen thinks this would be helpful. Probably goes to a "support@" email address that goes to multiple people (probably Master Administrators). 

  


  * My Details section (visible to all users): 
    * Name (read-only; displays the "Short Display Name" from the Contact record)
    * Primary Address (read-only; displays the Primary Address from the Contact record, in the standard multi-line format without the addressee name)
    * Mobile Phone (read-only; displays the "Mobile Phone" number for the user, from the "Account Members" embedded spreadsheet on the corresponding Account record in Silverloom)
    * Login Email (read-only; displays the "Traccar Login Email" for the user, from the "Account Members" embedded spreadsheet on the corresponding Account record in Silverloom)
    * Contact Notes (read-only; plain text; displays the "Contact General Notes" from the user's Contact record in Silverloom)



  


  


  * Account Overview section (visible to all users)
    * Account # (read-only; displays the "Account #" from the Account record) 
    * Account Reseller (read-only; displays details about the Account Reseller for the Account (same as the details on the Account record), in the following format:



<Account Reseller "Short Display Name"> 

Phone: <Phone> 

Email: <Email> (displays as as mailto link, to allow the user to open a blank email draft in their default email client)

Address: <Primary Address, in the standard multi-line format without the addressee name> 

  


  


  * Account Advocate (read-only; displays details about the __ for the Account, in the following format:



<"Short Display Name"> 

Phone: <Phone> 

Email: <Email> (displays as as mailto link, to allow the user to open a blank email draft in their default email client)

Address: <Primary Address, in the standard multi-line format without the addressee name> 

TODO_: Tim Reitz 12/31/2025: Finish this up, once we spec out the Advocate feature.

  


  


  * Account Details section (visible only to "Account Manager" users): 
    * Account Group (read-only; displays the "Account Group" from the Account record)
    * Primary Group Admin (read-only; displays details about the Primary Group Admin for the Account Group (same as the details on the Account Group record), in the following format:



<Primary Group Admin "Short Display Name"> 

Phone: <Phone> 

Email: <Email> (displays as as mailto link, to allow the user to open a blank email draft in their default email client)

Address: <Primary Address, in the standard multi-line format without the addressee name> 

  * Account Members (read-only table; mostly reflects the "Linked Devices" embedded spreadsheet from the Account record; includes the following:
    * Columns:
      * Name (displays the "Name" from the "Account Members" embedded spreadsheet from the Account record in Silverloom)
      * Is Account Manager (displays a checkbox, based on the "Account Manager" checkbox on the "Account Members" embedded spreadsheet)
      * Is Primary A. M. (displays a checkbox, based on the "Primary A. M." checkbox on the "Account Members" embedded spreadsheet)
      * Is Driver (displays a checkbox, based on the "Driver" checkbox on the "Account Members" embedded spreadsheet)
      * Mobile Phone (displays the "Mobile Phone" from the "Account Members" embedded spreadsheet)
      * Login Email (displays the "Traccar Login Email Address" from the "Account Members" embedded spreadsheet)
      * Contact Notes (plain text; displays the "Contact General Notes" from the Member's Contact record in Silverloom)
    * Sorted by: Same as the "Account Members" embedded spreadsheet on the Account record)



  


  * Devices (read-only table; mostly reflects the "Linked Devices" embedded spreadsheet from the Account record; includes the following:
    * Columns:
      * Device Description (displays the "Device Description" from the "Linked Devices" embedded spreadsheet on the Account record in Silverloom) 
      * Primary Driver (displays the "Primary Driver" from the "Linked Devices" embedded spreadsheet on the Account record in Silverloom)
      * Device Status (displays the "Device Status" from the "Linked Devices" embedded spreadsheet on the Account record in Silverloom)
      * Last __ Date & Time (displays the "Last __ Date & Time" from the "Linked Devices" embedded spreadsheet on the Account record in Silverloom)



TODO_: Tim Reitz 01/17/2026: Update here once we have the item specced on the Account.

  * Primary Vehicle (displays the "Primary Vehicle" from the "Linked Devices" embedded spreadsheet on the Account record in Silverloom)
  * Date Added (displays the "Date Added" from the "Linked Devices" embedded spreadsheet on the Account record in Silverloom)
  * Date Removed (displays the "Date Removed" from the "Linked Devices" embedded spreadsheet on the Account record in Silverloom)


  * Sorted by: Same as the "Linked Devices" embedded spreadsheet on the Account record)



  


  * Account General Notes (read-only; plain text; displays the "Account General Notes" from the Account record)



  


  * End User Agreement section (visible to all users)
    * View Current End User Agreement (link; opens the PDF of the current End User Agreement, from the top row of the "End User Agreements" embedded spreadsheet in Silverloom Settings) 
    * Agree to End User Agreement (visible if a row exists for the user's Contact with "Agreed To Date" = blank on the Account's "End User Agreements for Account" embedded spreadsheet; button; opens the "Agree to End User Agreement" screen - see corresponding spec) 



  


  


  * Account Actions section (visible only to "Account Manager" users): 
    * Request New User (mailto link; with the following details / behaviors: 
      * opens the "New User Request Email" draft template in the user's default email client, via the mailto feature; 
      * this allows the Account Managers to request a new user / Driver to be added to the Account; note that in the future, this could be replaced with a robust process for an Account Manager to add a new user / Driver without direct input from a Provider - see the Possible Future Features) 
    * Request New Device (mailto link; with the following details / behaviors: 
      * opens the "New Device Request Email" draft template in the user's default email client, via the mailto feature) 



  


  


Accept End User Agreement Screen: 

  * "I have read and agree to the current <Service Name> End User Agreement (effective date: <MM/DD/YYYY>)." (on-screen text) 
  * Name (required; plain text field) 
  * Date (read-only; date; sets to the current date) 
  * Confirm (button; can be selected if "Name" is not blank; selecting this button causes the following to be set on the "End User Agreements for Account" embedded spreadsheet on the Account record in Silverloom:
    * "Agreed To Date": sets to the value of the "Date" field (current date);
    * "Agreed To By Name": sets to the value of the "Name" field; 
    * "Agreed To By User": sets to the email address used to log in to the Portal)



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1648838368#gid=1648838368](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1648838368#gid=1648838368)

  


  


  


Tim Reitz 12/29/2025: Per conversation with Ellis today, we probably would not be charging per-user fees for end users who are only accessing the portal + Traccar. In the future, if enough features are added there might be consideration about user fees, but Ellis thinks Josh would be less likely to request user fees on this one.

  


Tim Reitz 01/16/2026: See XFB example: [https://testfbspe.wsgi.silverloom.io/spe-member-portal/enter-email](https://testfbspe.wsgi.silverloom.io/spe-member-portal/enter-email). 

  


Tim Reitz 01/16/2026: Note that Silverloom keeps track of all attempted submissions. This could be handy for troubleshooting a scenario where someone is repeatedly entering their email incorrectly, etc. See XFB example here: [https://testfbspe.apphosting.zone/Logs/View/Commands?_=vOiaP&](https://testfbspe.apphosting.zone/Logs/View/Commands?_=vOiaP&).
