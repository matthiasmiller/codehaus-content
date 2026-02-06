9.2.2.2. All Resellers Report

  


Requirements

*Done.

  


Overview: This is the "Standard All Contacts" report, filtered to display all Resellers & Reseller Reps (including Master Administrators & Group Admins).

  


Accessed from:

  * Administrators | Contact Management | All Resellers & Reps (opens the report directly, bypassing the filter screen)



  


The following filter(s) are set differently than on the main report:

  * "Contact Role": Set to "Master Administrator", "Group Admin", "Account Reseller", "Reseller Admin", and "Reseller Rep"



  


Other Notes:

  * N/A



  


Development Specification

Mockup: N/A

  


TODO_GZ: Tim Reitz 02/02/2026: Do you want something like this for the resellers & group admins to access too?

Tim Reitz 02/02/2026: If yes, basically duplicate this for the custom contacts report - add a hidden filter for the report + filtered version. 

Filter: 

  * Role (hidden; multi-select drop list of "Contact Roles" list items; defaults to none selected = all; note that this is hidden on this report to prevent users from manually accessing too much data)


