6.3.2. Jobs Awaiting Scheduling Report

  


Requirements

Overview: This is a custom, editable, multi-pane report of Proposals that have been awarded and are in need of scheduling.

  


Accessed from: 

  * Main Menu | Proposals | Jobs Awaiting Scheduling (opens the report directly, bypassing the filter screen)
  * The "Awarded Jobs Awaiting Scheduling" email (weekly email alert) 



  


Title: "Jobs Awaiting Scheduling" 

  


Left Pane: Displays one row for each Proposal that has been awarded but has at least one Group not scheduled (specifically, at least one "Group Awarded" checkbox checked and at least one "Group Scheduled Start Date" = blank). 

Preface: "Jobs with at least one Group awaiting scheduling." 

  


Columns: 

  * Proposal # (link to open the record) 
  * Awarded Date (displays the "Proposal Result Date") 
  * Job Target Start Comments
  * Job Scheduled
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

  


Right Pane: Displays one row for each Group needing scheduling from the last-selected Proposal on the left pane (specifically, with "Group Awarded" checkbox checked and "Group Scheduled Start Date" = blank). 

Preface: "Groups needing scheduling from the last-selected Proposal in the left pane."

  


Columns: 

  * Proposal # 
  * Section
  * Group Description
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



  


Development Specification

Change Requests: 

  * Tim Reitz 11/25/2025: Added in [[[IN11677](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11679&)]] - ZLP - Job Scheduled Tracking


