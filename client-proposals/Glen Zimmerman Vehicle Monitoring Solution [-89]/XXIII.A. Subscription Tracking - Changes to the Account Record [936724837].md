23.1. Subscription Tracking - Changes to the Account Record

  


Requirements

_GZ: Tim Reitz 08/19/2025: Should subscription management and invoicing be a "Phase 2" thing? 

_VA: Tim Reitz 08/21/2025: Yes, put this on the back burner until Phase 2.

_VA: Tim Reitz 08/21/2025: For Phase 1, we should probably just have a way to say that the Account is active... Maybe actually a drop list of the Status items, to manually set it...

  


TODO_VA: Tim Reitz 12/04/2025: For Phase 2: Include a status of "Delinquent", with a red on-screen message (and maybe a report alert / email / special color on reports).

  


TODO_VA: Tim Reitz 12/04/2025: For Phase 2: We would need to think through details when changing Account Type and/or Account Owner - i.e. invoicing, billing rates, etc.

  


\------

Account Record: 

  * Changes to the Account Administration section: 



  


  * Account Status (in the section heading (right-hand side); label displays as "Status:"; read-only macro; displays the current Status from the "Account Statuses" list, based on the following logic: 
    * "In Setup": __; not active yet, but devices can be added to the account; tracking service has not started yet; maybe the users don't have access yet. 
    * "Active": __; there is a Service Start Date / "Active" checkbox is checked
    * "Paused": __; "Paused Until" checkbox is checked
    * "Inactive": __; not active, but not closed out yet - awaiting final payment from customer, etc. new devices, etc., cannot be added to the account. 
    * "Closed": __; closed out and done. new devices, etc., cannot be added to the account.



_VA: Tim Reitz 08/21/2025: Some of these might move to Phase 2 / Subscriptions management.

TODO_G: Tim Reitz 08/19/2025: Let's think through  any other items (maybe "Renewal Grace Period", etc.?). 

TODO_: Tim Reitz 07/24/2025: Account: prevent deactivating [Closing] the Account if there are any Active devices

Tim Reitz 08/21/2025: This is easy in Phase 1 (with the drop list), but we'll need to think through the logic for the approach with Subscriptions. 

  


\------

  


  * Changes to the Account Overview Section: 
    * Account Reseller Transfer feature: 



TODO_VA: Tim Reitz 11/06/2025: When we get to subscription management, we'll need to have validation to prevent the Prior Reseller from approving the transfer before the appropriate details are closed out (all outstanding fees have been invoiced, etc.). 

  


\------

  


  * New Subscription section:
    * Service Start Date (__
    * Next Renewal Date (__



TODO_: Service Year renews on the 1st of the month, i.e. from Aug 14, 2025, to Aug 1, 2026; Sep 3, 2025 to Sep 1, 2026. 

  *   * Pause Service (__



TODO_: Tim Reitz 08/19/2025: Button that opens a prompt screen? 

TODO_: Tim Reitz 08/19/2025: Similar / same validations as ending. 

TODO_G: Tim Reitz 08/19/2025: What would you see as the process for pausing service? 

[ ] \- Maybe a minimum length of time 

[ ] \- Maybe a maximum length of time (could be re-Paused) 

[ ] \- If an Account is Paused, the Device should be unplugged / disabled and not used for that time. If activity is tracked, there should be a notification to the Reseller. 

TODO_G: Tim Reitz 08/19/2025: What would you see as the process for un-pausing service? 

  * Service Paused Until (__; date; __
  *   * End Service (__ 



TODO_G: Tim Reitz 08/19/2025: What would you see as the process for ending service? 

[ ] \- To close down an account, there is a process & checklist of things that need to be done 

[ ] \- Returning the OBD(s) (these would technically be owned by the Reseller and leased to the end user) 

\- __

  * validate against ending service if any of the following are true:
    * if there are any active Devices linked to the Account: error on the field: "__";
    * if there are any Invoices with "Status" = "Draft" or "Invoiced": error on the field: "__";
    * if there is an active Subscription: __ TODO_: what would this look like?) 



TODO_G: Tim Reitz 08/14/2025: What would be other reasons for preventing deactivation of an Account?

  


  * Service End Date (__; date; this is the date that service was ended and the Account is considered "Closed" / "Inactive") 



TODO_

  *   *   * Billing Frequency (required; drop list of "Billing Frequency" list items; editable for __) 



TODO_: Tim Reitz 08/19/2025: Can add a simple non-editable list for this. 

  


  * Fees (embedded spreadsheet with the following: 
    * Columns: 
      * Fee Date (__
      * Fee Type (__ 
      * Fee Amount $ (__; positive or negative or zero; __
      * Fee Description (__
      * Invoice (read-only macro; displays the "Invoice #" for the Invoice on which the row is included) 
      * Invoice Status (read-only macro; displays the current "Status" for the Invoice for the row) 
      * View Invoice (link; opens the Invoice for the row, if applicable; displays as "Link")  
      * 


  


  


[ ] \- Invoicing: 

[X] \- There would be the option for Monthly or Annual billing 

[ ] \- If Annual, all due 

[ ] \- If Monthly: 

[ ] \- There would be an upfront fee (setup fee?) 

[ ] \- The rest of the fees would be divided into 12 parts (with the first one being prorated) 

[ ] \- There would be a __% extra fee applied to Monthly accounts

TODO_: Tim Reitz 08/19/2025: For monthly billing frequency, would we add all the rows at Setup / Renewal, then invoice them as the date comes along? Or add them as the date comes along? 

[ ] \- First month would be prorated 

[ ] \- If someone cancels the service early: 

[ ] \- Some fees are non-refundable (setup fee; administrative fee) 

[ ] \- There would be early termination fees, prorated on how much time is left in the Service Year. 

[ ] \- Services would be pre-billed, rather than post-billed

  


  * Current Amount Due $ (__



  


TODO_G: Tim Reitz 08/19/2025: Are there different types of subscriptions? (based on # of users, etc.; or free accounts for certain people, etc.)

  


TODO_G: Tim Reitz 08/19/2025: Who sets the pricing for all the different fees? What control does the Reseller have over that?

  


TODO_G: Tim Reitz 08/19/2025: What do you see as the process for renewing service? 

Who is it done by? (Reseller? Other? what if no reseller - should we require a reseller, and set it to an admin if n/a?) 

[ ] The service would be an annual renewal (license agreements to be reviewed & agreed to) 

[ ] \- When Renewal Date approaches, a notice should go to the Account Manager

[ ] \- Could consider notification type preferences 

[ ] \- At the least would be an SMS message

[ ] \- Could also be via email 

[ ] \- Could also be an in-app notification (if possible) 

[ ] \- There should be an option to print & send via postal mail 

[ ] \- Reminder about the renewal, agreement can be ratified via a "YES" text response

[ ] \- Probably an RG to track renewals, ratification date, etc. 

  


  


  


TODO_G: Tim Reitz 08/19/2025: We have this note: "The service would not automatically terminate if not renewed in time (there would be a grace period with follow-up(s))". 

What would you envision as the process for this grace period? A number of days that admins or resellers can configure, then notifications for the reseller as the dates approach / pass? 

  


  


  


  * User Agreements (



_GZ: Tim Reitz 10/07/2025: For annual agreement, do you need to store a signed copy, or just store documentation of their signature? 

TODO_: Tim Reitz 10/09/2025: Per the client today, we do not need the actual signed document. We should reference the following: 

  * Document (file) name 
  * User ID 
  * Signed Name 
  * Date



  


_GZ: Tim Reitz 10/07/2025: For the annual agreement, what is needed? Just a checkbox or a signature (typed or written)? etc. 

TODO_: Tim Reitz 10/09/2025: Per client, a place to type their name + a checkbox that they have read & agree to it. 

  


TODO_: Tim Reitz 10/09/2025: Technically, the EUA needs to be done on a per-User, per-Account basis. So normally once per User (both Account Managers and Drivers), per Account, per year. 

[ ] I'm thinking this is an RG on the Account, eventually with rows for each linked user each year. 

  


TODO_: Tim Reitz 10/09/2025: A few notifications: 

[ ] For all users: Notification when a new EUA is uploaded, with a link to the new one / instructions to view it on the menu and a note that by continuing to use the service they are agreeing to the new version 

Phase 2: 

[ ] For all Account Managers & Drivers: Annually on their renewal date (the anniversary date of the Account "service start date") (different wording in the notification, but the same EUA and the same signature process)  

[ ] For Resellers: If Accounts / users are late in signing the agreement 

  


TODO_: Tim Reitz 10/07/2025: Let's make sure that we don't create legal liability for CodeCrafters regarding the annual acknowledgment -- "we will track the logged-in User Profile that checks the checkbox" vs. "we will track the person who signed the agreement". 

Tim Reitz 10/09/2025: I discussed this with Glen today. We need to determine the exact wording & process, but probably will include some confirmation / agreement text, a checkbox, and maybe a signature / name field. 

  


\------

All Accounts Report: 

  * Changes: 
    * Add columns for things like Start Date, Renewal Date?, etc.



  


Development Specification

Not included in HLD.
