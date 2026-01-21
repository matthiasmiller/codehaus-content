6.2.1. All Contacts Report

  


Requirements

Overview: This is the standard Silverloom Contacts report. Note that any customizations are noted as such in the spec.

  


Accessed from: 

  * Main Menu | Contacts | All Contacts (opens the report directly, bypassing the filter screen)
  * (custom) Displayed as the left pane of the "View Contacts" multi-pane report (see corresponding spec) 



  


Title: Contacts

  


Columns: 

  * Name (displays the "Display Name"; link to Contact record)
  * Type
  * Phone
  * Phone Type
  * Email (link to directly email the Contact)
  * City (displays the City and State)
  * Organization



_VA / _EM: Tim Reitz 09/16/2025: This column is for the legacy Organization records. We need to do a few things: ...

Tim Reitz 09/16/2025: Wrote up [[[IN12198](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12200&)]] - CORE - Cleanup Related to Legacy Organizations. 

TODO_VA: Tim Reitz 09/23/2025: Follow up here once the above CR is done. 

  * Summary



  


Grouped by: Active / Inactive

  


Sorted by: Name (alphabetically)

  


Filters: 

  * Contact Type (multi-select drop list of all Contact Types; defaults to blank = all; report displays results for any Contacts that include any of the selected items) 
  * Name (plain text field; searches the "Display Name")
  * City (plain text field)
  * State (drop list of State abbreviations; defaults to blank = all)
  * Zip (plain text field)
  * Email (plain text field)
  * Phone # (plain text field)
  * Active Contacts Only (checkbox; defaults to checked)
  * Match All of These Conditions (checkbox; defaults to checked)



  


Buttons: 

  * New Contact (opens blank new Contact record)



  


Menu Visibility: 

  * All users



  


Other Notes:

  * N/A



  


Development Specification

Ellis Miller 06/17/2025: 

[ ] Add a System Include If on the main contacts report for Leacock to include this subpane

BID: 2 HOURS

  


Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1825291167#gid=1825291167](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1825291167#gid=1825291167)
