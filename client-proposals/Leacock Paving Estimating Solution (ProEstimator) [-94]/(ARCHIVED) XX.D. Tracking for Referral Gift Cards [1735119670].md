20.4. Tracking for Referral Gift Cards

  


Requirements

_SM: Tim Reitz 07/07/2025: Let's write this up as a "future" CR.

Sean Miller 07/07/2025: [[[IN11679](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11681&)]] - ZLP - Tracking for Referral Gift Cards

  


The following feature could be added to facilitate easier tracking of the gift cards that are given to referring parties (those who refer customers to Leacock Paving). 

  


Estimated Cost: TBD

  


Initial Spec: 

  


Part 1: Changes to Silverloom Settings: Add the following new field: 

  * Referral Gift Card Threshold $ (number; 2 decimals; warning on Save if blank: "Referral Gift Card Threshold is blank."; this is used to set the threshold for which referral gift cards are sent to Referring Parties of Proposals that are marked as "Job Scheduled"; to be set to "8,500.00" at deployment) 



  


  


Part 2: Changes to Proposal Record | Customer Acceptance Section: Add the following new field(s): 

  * Add the following to the "Job Scheduled" checkbox spec: 
    * when checked, "Needs Gift Card" is checked on change if "Total Proposal Price $" is greater than or equal to the "Referral Gift Card Threshold $" in Silverloom Settings; 
    * when unchecked, "Needs Gift Card" is unchecked on change, unless "Gift Card Sent" is already checked; 
  * Needs Gift Card (hidden; checkbox; automatically checked/unchecked based on the "Job Scheduled" checkbox - see corresponding spec) 
  * Gift Card Sent (visible if "Needs Gift Card" checkbox is checked; checkbox + date, which toggle; with the following details / behaviors: 
    * when the checkbox is checked, the date defaults to the current date; 
    * this is used to track whether the gift card has been sent to the Referring Party; 
    * in the future, this could be based off of a "Job Completed" checkbox / date, rather than the "Job Scheduled" checkbox) 
      * Note: Located below the "Referring Party" field



  


  


Part 3: New "Referral Gift Cards" Report: Add the following new report: 

Overview: This is an editable report of Proposal records with the "Gift Card Sent" checkbox visible. It can track both sent gift cards and ones that need to be sent. For ones that need to be sent, this report can be used to view referrals by quarter (based on the Job Scheduled Start Date) and to mark items as sent.

  


Accessed from: 

  * Main | Administration | Referral Gift Cards (opens the report directly, bypassing the filter screen)
  * The "Referral Gift Cards to Send" notification 



  


Title: Referral Gift Cards 

  


Columns: 

  * Proposal # (link to record) 
  * Customer (displays the "Display Name") 
  * Customer Phone (helpful for situations where the Referring Party does not have an address entered yet, for the user to be able to contact the Customer to request the address) 
  * Customer Email (helpful for situations where the Referring Party does not have an address entered yet, for the user to be able to contact the Customer to request the address) 
  * Total Proposal Price $ 
  * Referring Party (displays the "Short Display Name"; link to Contact record; helpful for situations where the Referring Party does not have an address entered yet, for the user to be able to open the Contact record and enter the address) 
  * Referring Party Address (displays the full address, in the standard 2- or 3-line format) 
  * Referral Gift Card Sent (editable; checkbox; displays as "Yes" / "No" drop list for editing) 



  


Grouped by: 

  * First by: "Not Sent" / "Sent" (based on the "Gift Card Sent" checkbox) 
  * Second by: Job Scheduled Start Month (displays in the following format: "MMMM YYYY"; based on the "Job Scheduled Start Date"; earliest date / month at the top) 



  


Sorted by: 

  * First by: Job Scheduled Start Date (earliest date at the top) 
  * Second by: Proposal # (alphabetically) 



  


Filters: 

  * Exclude Sent (checkbox; defaults to not checked; if checked, any "Sent" items are excluded and only the "Not Sent" items are included) 
  * Job Scheduled Date Start (optional; date; defaults to blank = all; looks at the "Job Scheduled Start Date")
  * End (optional; date; defaults to blank = all; looks at the "Job Scheduled Start Date")



  


Buttons: 

  * Save Changes (saves changes for edited rows) 



  


Menu Visibility: 

  * All users



  


Save Type: Save Button

  


Other Notes: 

  * N/A



  


  


Part 4: New "Referral Gift Cards to Send" Notification / Report Alert: 

  


Overview/Purpose: This displays a quarterly in-app notification for the user(s) responsible for sending referral gift cards. 

  


Details: 

  * Title: Referral Gift Cards to Send
  * Displays: On the first date of every calendar quarter (January, April, July, October), if there are any Proposal records that meet the following criteria: 
    * "Gift Card Sent" is visible and blank and 
    * "Job Scheduled Start Date" is in the past
  * Action: Opens the "Referral Gift Cards" report
  * User(s) to notify: Any users with the "Receives "Referral Gift Cards to Send" Notification" checkbox checked on their Contact record
  * Dismiss type: Auto-dismiss when all items that meet the above "Displays" criteria are resolved



  


Other Notes:

  * N/A



  


  


Part 5: Changes to the Contact Record | Employee Details Section: Add the following new field: 

  * Receives "Referral Gift Cards to Send" Notification (checkbox; if checked, the user linked to the Contact record receives the corresponding notification)



  


Development Specification

Tim Reitz 06/26/2025: Pe client today, let's hold off on this. It would be a nice feature to have, but it should wait until the software is tracking the project completion date (to base it off of that). 

We could give him a customized user report in the meantime to easily track referrals.
