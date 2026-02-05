9.2.1. <Service Name> Main Contacts Report

  


Requirements

*Done.

  


Overview: This is a custom Contacts report, with limited data available to the users, to help protect the integrity of customer data usage. Note that since non-"Full Access" users do not have access to report settings, they cannot create customized versions with additional columns, etc. 

  


Accessed from: 

  * Providers | Contacts | View Contacts (opens the report directly, bypassing the filter screen) 
  * Providers | Contacts | Contact Search (opens the filter screen to allow the user to search based on certain criteria)



  


Title: "<Service Name> Contacts"

  


Columns: 

  * Name (displays the "Display Name"; link to Contact record)
  * City
  * State 
  * Church Affiliation 



  


Grouped by: Active / Inactive

  


Sorted by: Name (alphabetically)

  


Filters: 

  * Name (plain text field; searches the "Display Name"; allows searching by partial)
  * City (plain text field)
  * State (drop list of State abbreviations; defaults to blank = all)
  * Account Group (hidden; drop list of "Group Name" values for active Account Groups; defaults to blank = all; if a selection is made here, the report shows Contacts that are included as "Account Members" on Accounts under that Group; note that this is hidden to reduce the amount of detail that most users can access on the Contacts report) 
  * Account Reseller (hidden; drop list of "Display Name" values for active Contacts with the "Is Account Reseller" checkbox checked; defaults to blank = all; if a selection is made here, the report shows Contacts that are included as "Account Members" of Accounts under that Reseller; note that this is hidden to reduce the amount of detail that most users can access on the Contacts report) 
  * Account (hidden; drop list of "Account #" values for active Accounts; defaults to blank = all; if a selection is made here, the report shows Contacts that are included as "Account Members" on that Account; note that this is hidden to reduce the amount of detail that most users can access on the Contacts report)
  * Active Contacts Only (checkbox; defaults to checked) 



  


Buttons: 

  * New Contact (opens blank new Contact record)



  


Menu Visibility: Visible to all users

  


Other Notes:

  * This is an "auto-push" report, meaning that if there is only one result when the filters are set, clicking "Continue" will open that record directly, bypassing the report screen.



  


Development Specification

Mockup: __

TODO_MOCKUPS: Tim Reitz 02/02/2026: This is ready to be mocked up. Please paste the link to the mockup tab into the blank above. Thanks!
