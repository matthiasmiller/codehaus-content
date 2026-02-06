16.1.3. Prepare Annual Renewals

  * Name: "Prepare Annual Renewals"
    * Description: Adds renewal rows to the "End User Agreements for Account" embedded spreadsheets on Account records. 
    * Category: "Subscription Automation" 
    * Notes: Contains the contents of "Description" point above and "Actions" point below 
    * Initiated: Monthly on the 17th of the month (or on next business day if a non-business day), at 1:00am ET 
    * Should Wait On: N/A 
    * Commands:  __ (TBD in coding) 
    * Prompts: 
      * N/A for Phase 1
    * Action(s): 
      * Looks at all Accounts with "Stored Account Status" = "Active", "Paused", or "Inactive" and with the month and date of "Renewal Anniversary Date" is within 16 calendar days of the current date (disregarding the year). 



_GZ: Tim Reitz 01/06/2026: How far ahead of the renewal date would you want this to run / would you want the users to be notified? 

Tim Reitz 01/07/2026: Asking via email (subject: Questions about service start date / renewal). 

_VA: Tim Reitz 01/08/2026: Per Glen, 2 weeks.

_NM: Tim Reitz 01/08/2026: Should we say X number of days like I did here, or can we just say "is on the 1st of the next month"? 

TODO_VA: Tim Reitz 01/08/2026: Fine to run on the 15th and look at the 1st of the next month. 

  * Add a row to the "End User Agreements for Account" embedded spreadsheets on all Account records that match the above criteria, with the following set: 
    * "Effective Date": sets to the "Upload / Effective Date" for the top row of the "End User Agreements" embedded spreadsheet in Silverloom Settings (the current EUA);
    * "Contact ID": sets to the "Contact ID" for the Primary Account Manager;
  * Sends the "Annual Renewal Notice" Email - see corresponding spec) 



_GZ: Tim Reitz 01/06/2026: What kind of notification should the users get when there is an EUA to agree to? (both initial and renewal) 

Tim Reitz 01/07/2026: Asking via email (subject: Questions about service start date / renewal). 

TODO_VA: Tim Reitz 01/08/2026: Glen was good with an email in both situations (initial and renewal). I'd also do an email for Primary A. M. change.

Tim Reitz 01/08/2026: Actually, I think the EUA note gets included in other emails: 

[ ] Account Member Welcome email 

[ ] Account Manager Changes email 

[X] Annual Renewal Notice email 

TODO_VA: Tim Reitz 01/08/2026: For Phase 2: We could (and probably will want to) add reminders about unsigned / late EUAs, as part of the Subscription management feature. 

  


TODO_VA: Tim Reitz 01/08/2026: "Annual Renewal Notice" Email"

[ ] Sent via the "Prepare Annual Renewals" scheduled automatic process 

[ ] To the Primary Account Manager of all Accounts that are due for a renewal within 14 calendar days 

[ ] "Your annual <Service Name> renewal is coming up on <renewal anniversary>. Please log into the Portal to review and agree to the End User Agreement: <link> 

Also please stay alert for additional communications from your Account Reseller." 

  


TODO_VA: (for Proposals) Add a deployment note: "Enable Scheduled Task(s)"
