8.2.8. Organizations Report

  


Requirements

Overview: This is a two-pane report of Organization-type Contacts and their corresponding Members with filtering options. For Regional Reps and Super Admins, there is the option to include Organizations that are not linked to Contacts with an active membership. Standard Users can only see Organizations linked to active Members.

  


Accessed from: Members Menu | Members & Groups | Organizations (bypasses the filter screen to open the report directly)

  


Title: Organizations

  


Left Pane (displays Organization-type Contacts based on the selected filters):

Columns: 

  * Organization (link to record)
  * Industry (if there are multiple, comma-separated, with wrapping text) 
  * Description (wrapped text)
  * Employees
  * Annual Revenue $ (visible for Regional Reps and Super Admin only)
  * Address (displays the full Primary address in the standard 2- or 3-line format)
  * Phone (displays the Primary)
  * Email (displays the Primary; if there are multiple, comma-separated with wrapping text)



  


Grouped by: Active / Inactive, then by Member Org / Non-Member Org (for users with that visibility)

  


Sorted by: Industry (alphabetically)

  


Right Pane (displays Member-type Contacts that are linked (via the Organizations table on their Contact record) to the most recently-selected Organization in the Left Pane):

Columns:

  * Members (link to Contact record)



  


Grouped by: Active / Inactive 

  


Sorted by: Members (alphabetically)

  


Filters (all apply directly to the left pane): 

  * Industry (drop list of all Industries; default to blank = all)
  * State / Province (drop list of all US states and Canadian provinces; default to blank = all)
  * Show Non-Member Organizations (checkbox; visible only for Regional Reps and Super Admins; if filled, the report includes Organizations that are not linked to at least one Contact with active membership; defaults to cleared)



  


Buttons:

  * New Member Organization (open new Organization Record with Type = Member Organization; only visible for Regional Reps and Super Admins)
  * New Other Organization (open new Organization Record with Type = Other Organization; only visible for Regional Reps and Super Admins)



  


Menu Visibility: All users

  


Other Notes: N/A

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=207246975](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=207246975)
