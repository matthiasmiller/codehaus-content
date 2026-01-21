19.9. Done: Proposal Record: Tracking "Entered in QuickBooks"

_VA: Tim Reitz 07/03/2025: Client wants to move forward with this for Phase 1.

  


  


The following feature could be added to document when an "Awarded" Proposal has been entered into QuickBooks.

  


[X] Estimated Cost: $100-200

  


[X] Initial Spec: 

  * Proposal Record: Customer Acceptance section: Add the following (below the "Job Target Start Comments"): 
    * Entered into QuickBooks (visible if "Proposal Result" = "Awarded"; checkbox + date, which toggle)



  


_VA: Tim Reitz 07/03/2025: Client would like to also add a weekly email reminder if any Awarded proposals don't have the "entered" checkbox checked: 

  * [X] Scheduled Task that runs once a week 
  * [X] Lists all that are awarded but don't have this checkbox checked 
  * [X] Would add $200-300 to this price (300-500 total)



  


_EM: Tim Reitz 07/03/2025: Could you review this spec before I disperse it throughout the document? 

_VA Ellis Miller 07/03/2025: Looks good.

  


  


[X] Item 2: Contact Record - new field in the Employee Details section:

  * Receives "Reminder to Enter Proposal(s) into QuickBooks" Email (checkbox; editable for users with the "Create/Edit Other User Profiles" Permission; users for whom this checkbox is checked on their linked Contact record receive the mentioned email notification (see corresponding spec))



  


[X] Item 3: Set Standard ""From" email address for notifications" System Switch

  


[X] Item 4: New Automatic (Scheduled) Process:

  * Name: "Send Reminder to Enter Proposal(s) into QuickBooks"
    * Description: Used to send the "Reminder to Enter Proposal(s) into QuickBooks" email.
    * Category: Email Notifications
    * Notes: Contains the contents of "Actions" point below 
    * Initiated: Weekly on Monday at 8:00am ET
    * Should Wait On: N/A
    * Commands: TBD in coding
    * Prompts: 
      * TBD in coding
    * Action(s): 
      * Runs the email merge to send the "Reminder to Enter Proposal(s) into QuickBooks" email to to any users with the "Receives "Reminder to Enter Proposal(s) into QuickBooks" Email" checkbox checked on their Contact record, if there are any Proposals with "Proposal Status" = "Awarded" and the "Entered into QuickBooks" checkbox not checked.



  


Dev Spec: DO_CCI: Tim Reitz 07/03/2025: Please let me know the scheduled task command once you have that established. Thanks!

  


[X] Item 5: New "Reminder to Enter Proposal(s) into QuickBooks" email:

Overview: This is an internal email that is sent weekly if any Proposals are marked as "Awarded" but do not have the "Entered into QuickBooks" checkbox checked. It is sent via the "Send Reminder to Enter Proposal(s) into QuickBooks" Scheduled Process (see corresponding spec).

  


From: <the email address specified in the ""From" email address for notifications" System Switch>

  


To: <the Primary email address for any Contacts with the "Receives "Reminder to Enter Proposal(s) into QuickBooks" Email" checkbox checked>

  


CC: N/A

  


BCC: N/A

  


Reply To:

  


Subject: "Reminder to Enter Proposal(s) into QuickBooks"

  


Attachments: N/A

  


Body:

The following Proposal(s) need to be marked as entered into QuickBooks:

  


 <embedded report, filtered version of the "Master Proposals Report" with "Proposal Status" = "Awarded" and "Limit to Not Entered into QuickBooks" checked>

  


<link to the report, displayed text is "Link to Report in Silverloom">

_EM: Tim Reitz 07/03/2025: Would the list of proposals be embedded into the email merge, or a filtered version of a report?

_VA Ellis Miller 07/03/2025: The simplest option is just to embed the Proposals report. We could also put a link to the report so that they can do it from the software.  I added that above.

_EM: Tim Reitz 07/03/2025: Sounds good. Does it sound right then to add a hidden filter on the Master Proposals report to limit to "not entered into quickbooks", to handle this?

  


Other Notes:

  * N/A



  


_VA: Add note for email setup in deployment - [[[W0090](https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages&NumberID=-91&)]]

  


  


Item 6: Master Proposals Report: Add a new (hidden?) "Limit to Not Entered into QuickBooks" checkbox
