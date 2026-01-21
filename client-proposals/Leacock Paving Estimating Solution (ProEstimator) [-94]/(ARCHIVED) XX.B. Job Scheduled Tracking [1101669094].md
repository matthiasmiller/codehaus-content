20.2. Job Scheduled Tracking

  


Requirements

_SM: Tim Reitz 07/07/2025: Let's write this up as a "future" CR. 

Sean Miller 07/07/2025: [[[IN11677](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11679&)]] - ZLP - Job Scheduled Tracking

  


The following feature could be added to facilitate the hand-off process from the Sales Rep to the scheduling team. This is currently a bottleneck/pain point. 

  


Estimated Cost: TBD

  


Initial Spec: 

  


Part 1: New "Jobs Awaiting Scheduling" Report:

  


Overview: This is a custom, editable, multi-pane report of Proposals that have been awarded and are in need of scheduling.

  


Accessed from: 

  * Main Menu | Proposals | Jobs Awaiting Scheduling (opens the report directly, bypassing the filter screen)
  * The "Awarded Jobs Awaiting Scheduling" weekly email alert



  


Title: "Jobs Awaiting Scheduling" 

  


Left Pane: Displays one row for each Proposal that has been awarded but has at least one Group not scheduled (specifically, at least one "Group Awarded" checkbox checked and at least one "Group Scheduled Start Date" = blank). 

Preface: "Jobs with at least one Group awaiting scheduling." 

  


Columns: 

  * Proposal # (link to open the record) 
  * Awarded Date (displays the "Proposal Result Date") 
  * Job Target Start Comments
  * Job Scheduled (editable as a "Yes"/"No" drop list)
  * Job Scheduled Start Date (editable)  
  * Customer 
  * Job Name
  * Job Contact 
  * Proposal Date 
  * Sales Rep 



  


Grouped by: N/A

  


Sorted by: Proposal Awarded Date (oldest at the top) 

  


Filters: 

  * N/A 



  


Save Type: Instant Save 

  


Live Updating: No

  


Right Pane: Displays one row for each Group needing scheduling from the last-selected Proposal on the left pane. 

Preface: "Unscheduled Groups for the last-selected Proposal in the left pane."

  


Columns: 

  * Proposal # 
  * Section
  * Group Description
  * Group Awarded
  * Group Awarded Date 
  * Group Target Start
  * Group Scheduled Start Date (editable) 



  


Grouped by: N/A

  


Sorted by: N/A (same sequence as they appear on the Groups embedded spreadsheet) 

  


Filters: 

  * Proposal # (required; plain text; sets to the last-selected Proposal in the left pane) 



  


Save Type: Instant Save 

  


Live Updating: Yes (to cause the right pane to update immediately when edits are made to the selected row in the left pane, to avoid edit collisions / errors) 

  


Buttons: 

  * N/A



  


Menu Visibility: All users

  


Other Notes:

  * Editable columns respect the same editability conditions as the corresponding fields on the Proposal record. 



  


  


Part 2: New "Jobs Awaiting Scheduling" Weekly Email Alert: 

Overview: This is an internal email that is sent to contacts with the "Receives Jobs Awaiting Scheduling Email" checkbox checked to alert them that there are proposals / jobs ready to be scheduled.

  


It is sent via the "Send Jobs Awaiting Scheduling Email" Automatic Process (see corresponding spec). It includes following items (which cannot be edited on a per-sending basis, since this is automatically sent):

  


To: <the primary email address for any contacts with the "Receives Jobs Awaiting Scheduling Email" checkbox checked> 

  


CC: N/A 

  


BCC: N/A 

  


Subject: "Jobs Awaiting Scheduling" 

  


Body: <text specified in "Default Text for Jobs Awaiting Scheduling Email" in Silverloom Settings> 

  


Other Notes:

  * N/A



  


Part 3: Contact Record: 

  * Employee Details section:
    * Receives Jobs Awaiting Scheduling Email (checkbox; visible to and editable by users with the "Create/Edit Other User Profiles" Permission; determines whether the Contact receives the notification)



  


Part 4: Silverloom Settings:

  * Email Settings Section:
    * Configure Jobs Awaiting Scheduling Email (button; opens a child screen with the following: 
      * Default Text for Awarded Jobs Awaiting Scheduling Email (multi-line plain text field that supports expressions; with the following details / behaviors:
        * this is used for setting & storing the default text for the internal email that is sent - see corresponding spec; 
        * warning on Save if blank;
        * to be initially set to the following at deployment of the Solution, but may be edited by Leacock Paving or CodeCrafters: 



One or more jobs have been awarded and are ready for scheduling.

  


View Report: <link to the "Jobs Awaiting Scheduling" report>

  


Thank you!

  


Part 5: Automatic Process:

  * Name: "Send Jobs Awaiting Scheduling Email"
    * Description: Sends the "Jobs Awaiting Scheduling" email to any contacts with the "Receives Jobs Awaiting Scheduling Email" checkbox checked if the "Jobs Awaiting Scheduling" report is not blank.
    * Category: Email Notifications 
    * Notes: N/A
    * Initiated: Weekly; Mondays at 7:00 AM
      * Note that this might be changed, based on the scheduler's preference 
    * Should Wait On: N/A
    * Commands: TBD
    * Prompts: 
      * TBD
    * Action(s): 
      * TBD



  


Development Specification

Tim Reitz 06/26/2025: Client sees this as a Phase 2 item.
