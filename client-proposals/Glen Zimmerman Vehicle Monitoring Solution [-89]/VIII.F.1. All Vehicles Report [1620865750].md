8.6.1. All Vehicles Report

  


Requirements

TODO_VA:

  


Overview: This is a custom report of Vehicle record, with various filters.

  


Accessed from: 

  * Providers | Vehicles | All Vehicles (opens the report directly, bypassing the filter screen)
  * Providers | Vehicles | Vehicle Search (opens the filter screen) 



  


Title: 

TODO_VA

  


Preface: 

TODO_VA

  


Columns: 

  * Owner (__
  * Vehicle Name (link to record)
  * License Plate (__



TODO_VA: Tim Reitz 11/06/2025: Do not include License Plate on the report, due to privacy concerns. 

  * Color (__
  * Year (__
  * Make (__
  * Model (__
  * VIN (__



  


Row-Specific Buttons: N/A

  


Grouped by: __

TODO_VA / _GZ 

Tim Reitz 11/06/2025: Per Glen, would be nice to be able to view only all "Audi A4" vehicles, etc. But standard grouping might be by account. 

Maybe have grouping options? 

  


Sorted by: __ 

TODO_VA / _GZ: Tim Reitz 11/04/2025: What seems most intuitive? 

Tim Reitz 11/06/2025: Per Glen, probably first by Make then by Model [then by Year, then by VIN] 

  


Filters: 

  * Owner (drop list of __; __; defaults to blank = all) 
  * Primary Driver (plain text; searches by partial for "Primary Driver" names on Vehicles; defaults to blank = all)
  * Vehicle Name (plain text; searches by partial; defaults to blank = all) 
  * VIN (plain text; searches by partial; defaults to blank = all) 
  * Search by Partial (visible for Admin users; checkbox; applies to "VIN/Serial #"; defaults to not checked)



_GZ: Tim Reitz 11/04/2025: Do you want this option to search by partial, or always do it (for all users)? 

TODO_VA: Tim Reitz 11/06/2025: All Providers can search by whole or partial (both VIN and License Plate). 

  * License Plate (plain text; searches by partial; defaults to blank = all) 



TODO_VA: Tim Reitz 11/04/2025: Get clarification about the corresponding ask prompt in ZWA: Is this actually simply a plain text field, or are there any special behaviors for it?

  * Year (number; 0 decimals; defaults to blank = all)
  * Make (drop list of __; defaults to blank = all) 



TODO_VA: Tim Reitz 11/04/2025: Methinks we need a simple list for this. Basically the same as ZWA? 

  * Model (drop list of __; defaults to blank = all) 



TODO_VA: Tim Reitz 11/04/2025: Another simple list for this. Again, basically the same as ZWA? 

  


Buttons: 

  * New Vehicle (opens a blank new Vehicle record) 



  


Menu Visibility: 

  * 


TODO_VA

  


Other Notes: 

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1085047341#gid=1085047341](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1085047341#gid=1085047341)
