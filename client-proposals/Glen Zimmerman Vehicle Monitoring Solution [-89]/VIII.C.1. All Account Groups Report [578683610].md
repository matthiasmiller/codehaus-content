8.3.1. All Account Groups Report

  


Requirements

Overview: This is a custom multi-pane report of all Account Group records, with various filters. Pre-filtered versions of this report can be opened from different locations (see corresponding specs).

  


Accessed from: 

  * Providers | Accounts | All Account Groups (opens the report directly, bypassing the filter screen)
  * Providers | Account Groups | Group Search (opens the filter screen) 



  


Title: Account Groups

  


Left pane: 

Preface: 

TODO_VA:

  


Columns: 

  * Group Name (link to record)
  * Primary Group Admin



  


Row-Specific Buttons:

  * N/A



  


Grouped by: Active / Inactive (active at the top)

  


Sorted by: Group Name (alphabetically)

  


Filters: 

  * Group Admin (optional; drop list of __; defaults to blank = all; when one is selected, the report filters to only display Groups for which the selected Contact is included on the "Account Group Admins" embedded spreadsheet)
  *   * TODO_VA:



  


Other Notes:

  * Group Admins can only view records for which they are included on the "__" embedded spreadsheet.



TODO_VA / TODO_GZ: Tim Reitz 08/26/2025: Do we want to do this?

  


_NM: Tim Reitz 08/25/2025: How would it work to show hierarchy right here in this report? Probably a filter that can be set?

TODO_VA: Tim Reitz 12/10/2025: Yes, we can show hierarchy with indentation. Technical details TDB.

TODO_VA: Tim Reitz 12/10/2025: We can turn it on/off with a checkbox filter. 

  


Right pane: Displays the "Accounts by Group" report (see corresponding spec), filtered to the last-selected Group row in the left pane. 

TODO_VA : Tim Reitz 08/28/2025: Let's have this be able to show Accounts for multiple Groups, grouped by Group, so that the user can select multiple. 

TODO_VA Tim Reitz 08/28/2025: Also, let's make sure that the reports are restricted, so that users can't see Accounts that they don't have permissions for. 

  


  


Buttons: 

  * New Account Group (opens a new blank Account Group record) 
  * 


_NM: Tim Reitz 08/26/2025: How would it work to include the "New Account" button from the Accounts report? 

TODO_VA: Tim Reitz 12/10/2025: We can show buttons for both panes. 

  


Menu Visibility: 

  * TODO_VA



  


Other Notes:

  * This is an "auto-push" report, meaning that if there is only 1 row, it opens that record directly.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=680227204#gid=680227204](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=680227204#gid=680227204)

  


Tim Reitz 12/10/2025: For the hierarchy indentation, could do like this report in ZCH: [https://zch.apphosting.zone/Reports/Standard/Std_Billable_Time_for_Incident_Detail?Asks=vAskIncidentID%3D%22IN11732%22](https://zch.apphosting.zone/Reports/Standard/Std_Billable_Time_for_Incident_Detail?Asks=vAskIncidentID%3D%22IN11732%22)
