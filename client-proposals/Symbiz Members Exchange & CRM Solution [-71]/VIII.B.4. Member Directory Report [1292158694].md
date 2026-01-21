8.2.4. Member Directory Report

  


Requirements

Overview: This is a report of Member-type Contacts with active memberships ("Active Membership" checkbox is checked). This is used as the main report for viewing active Members (including facilitators, regional reps, and admins). It can be filtered down to show narrower groups of members as well. 

  


Accessed from:

  * Members Menu | Members & Groups | Member Directory (bypasses the filter screen to open the report directly)
  * Admin | Membership Management | Member Directory (bypasses the filter screen to open the report directly)



  


Title: Member Directory

  


Columns: 

  * Member Name (displays the name in the "FirstName LastName" format, including the Contact ID; link to open record) 
  * Group(s) (displays the Growth Ring Group ID(s) for the Group or Groups of which the person is a member; if there are multiple, comma-separated with wrapping text)
    * Note: Remove the "Growth Ring Group Name" and display only the "Growth Ring Group ID".
  * City (displays the City from the Primary address)
  * State / Province (displays the State from the Primary address)
  * Phone (displays the Primary)
  * Email (displays the Primary; if there are multiple, comma-separated with wrapping text)
  * Bio (wide column with wrapping text) 
  * Business Names (comma-separated list of linked Organizations without the Contact ID, with wrapping text) 
  * Industry (if there are multiple, comma-separated, with wrapping text) 



  


Grouped by: The selection on the Group By filter: 

  * Growth Ring Group (alphabetically)
  * Industry (alphabetically)
  * Organization (alphabetically)
  * State / Province (alphabetically)



  


Note that when grouped by Industry, Growth Ring Group, or Organization, the Contact will be listed in every group for which they qualify, since a member may be linked with multiple ones. 

  


Sorted by: Member Name (alphabetically by first name) 

  


Filters: 

  * Name (optional; plain text field; allows for searching partial or complete names; clicking "Continue" runs the report with results that include the exact text entered here; same as the standard Name filter on the Contacts report) 
  * Growth Ring Group (drop list of all Growth Ring Group Descriptions; defaults to blank = all) 
  * Industry (multi-select drop list of all Industries; defaults to blank = all) 
  * Organization Name (drop list of all organizations; defaults to blank = all)
  * State / Province (drop list of all US states and Canadian provinces; defaults to blank = all)
  * Group By (drop list of the following; default to blanks = no grouping:)
    * Growth Ring Group
    * Industry
    * Organization 
    * State / Province
  * Show Bio (checkbox; defaults to filled) 



  


Buttons: 

  * Print Vertical (generates the Member Directory Printout (Vertical) for the current version of the report (but not respecting the "Show Bio" filter selection); see the corresponding section of the proposal for details)
  * Print Horizontal (generates the Member Directory Printout (Horizontal) for the current version of the report (but not respecting the "Show Bio" filter selection); see the corresponding section of the proposal for details)



  


Menu Visibility: All users

  


Other Notes:

  * This report has alternating background colors for the rows (light gray and white).



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1228041910](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1228041910) 

  


For reference, view: [https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=665%3A4000&scaling=min-zoom&starting-point-node-id=9%3A3](https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=665%3A4000&scaling=min-zoom&starting-point-node-id=9%3A3)

  


Note: Tim Reitz 06/08/2023: For a mobile-friendly version of this, we could show just Member Name, Address, and Phone

  


Tim Reitz 05/08/2023: Consider PDF exports.

  


  


Change Requests: 

  * Tim Reitz 04/08/2024: [[[IN9517](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9519&)]] - ZSB - Improvements for Managing Members (prev. Add Features to Search for Individual Members)
  * Tim Reitz 06/01/2024: [[[IN9725](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9727&)]] - ZSB - Member Directory Report - Remove References to Inactive Members
  * Ben Reitz 10/08/2025: [[[IN10201](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10203&)]] - ZSB - Member Directory Report & Printouts - Various changes


