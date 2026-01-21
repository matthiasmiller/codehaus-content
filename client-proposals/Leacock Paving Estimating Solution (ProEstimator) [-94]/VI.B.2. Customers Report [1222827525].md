6.2.2. Customers Report

  


Requirements

Overview: This is a custom two-pane report of Contacts with "Customer" selected as a Contact Type (left pane) and linked Proposals (right pane).

  


Accessed from: Accessed from: Main Menu | Contacts | Customers (opens the report directly, bypassing the filter screen)

  


Title: Customers

  


Left pane: This is a report of all Contacts that include "Customer" as a Contact Type: This is the standard Contacts report, filtered to show only items that include "Customer" as a "Contact Type" (see corresponding spec).

  


Title: Customers

  


Preface: N/A

  


Columns: 

  * Name (displays the "Display Name"; link to the Contact record)
  * Phone (link to directly call the Contact) 
  * Email (link to directly email the Contact)
  * City (displays the City and State)
  * Organization(s) (if multiple, displays each on a separate line, separated by semicolons) 



  


Row-Specific Buttons:

  * N/A 



  


Grouped by: Active / Inactive 

  


Sorted by: Name (alphabetically) 

  


Filters: 

  * Name (plain text field; searches the "Display Name")
  * City (plain text field)
  * State (drop list of State abbreviations; defaults to blank = all)
  * Zip (plain text field)
  * Email (plain text field)
  * Phone # (plain text field)
  * Active Contacts Only (checkbox; defaults to checked)



  


Buttons: 

  * New Customer (opens a new Contact record, with "Contact Type" set to "Customer") 



  


Right pane: This is the "Proposals by Customer" Report (see corresponding spec), filtered to the selected Contact in the left pane. 

  


  


Buttons: 

  * Includes the "New Customer Contact" button from the Customers" report in the left pane (see corresponding spec above) standard Contacts report - see corresponding spec. 
  * Includes the "New Proposal" button from the Proposals report - see corresponding spec (note that this creates a new Proposal record for the selected Contact in the left pane). 



  


Menu Visibility: 

  * All users



  


Other Notes:

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=911215041#gid=911215041](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=911215041#gid=911215041)

  


Ellis Miller 06/17/2025: 

Included above (just a menu item)

Tim Reitz 09/23/2025: Now doing a custom report for the left pane.
