6.3.1. All Vehicles Report

Overview: This is a custom report of Vehicle records, with various filters.

  


Accessed from:

  * Home | Vehicles | Vehicle Search (opens a prompt screen with the below filters, to search for a vehicle in the Solution) 
  * Home | Vehicles | All Vehicles (bypasses the prompt page to open the report directly) 
  * Admin | Admin Searches | Vehicle Search (opens a prompt screen with the below filters, to search for a vehicle in the Solution) 



  


Title:

  * If the "No-Charge Vehicle Report" filter checkbox is not checked: "All Vehicles"
  * If the "No-Charge Vehicle Report" filter checkbox is checked: "No-Charge Vehicles"



  


Preface: N/A

  


Columns: 

  * Owner
  * Year
  * Make
  * Model
  * VIN / Serial # (link to open the Vehicle record)
  * License Plate #
  * Primary Driver
  * N/C
  * Agent
  * Vehicle Type
  * Vehicle Subtype



  


Grouped by: 

  * If "Group By" filter = "Status": Vehicle Status ("Active" / "Inactive")
  * If "Group By" filter = "Agent": Agent (alphabetically)



  


Sorted by: Owner + VIN

  


Filters: 

  * No-Charge Vehicle Report (hidden; checkbox; defaults to not checked; if checked, the report includes only Vehicles with the "No-Charge Vehicle" checkbox checked)
  * Admin Report (hidden; checkbox; defaults to not checked; if checked, __



TODO_CCI: Tim Reitz 07/31/2025: What does this ask prompt do?

Sagar Sagar 12/11/2025: From Admin | Admin Searches | Vehicle Search, this is set to True. When its true, the report title changed into "Admin Vehicle Search". So a new bullet point will be added to the Title section. The section should be something like

  


Title:

  * If the "No-Charge Vehicle Report" filter checkbox is checked: "No-Charge Vehicles"
  * If the "No-Charge Vehicle Report" filter checkbox is not checked and 
    * "Admin Report" checkbox is checked: "Admin Vehicle Search"
    * "Admin Report" checkbox is not checked: "All Vehicles"



  


  * Name (drop list of vehicle owners (all "Client"-type Contacts that have at least one Vehicle) and blank; defaults to blank = all)



TODO_CCI: Tim Reitz 07/31/2025: Is this looking only at active vehicles on the contact records, or also inactive?

Sagar Sagar 12/11/2025: This is looking at both active and inactive vehicles.

  * Type (drop list of active Vehicle Types and blank; defaults to blank = all)
  * Year (number; 0 decimals; defaults to blank = all)
  * Make (drop list of __; defaults to blank = all)
  * Model (drop list of __; defaults to blank = all)
  * VIN/Serial # (plain text; defaults to blank = all)
  * Search by Partial (visible for Admin users; checkbox; applies to "VIN/Serial #"; defaults to not checked)
  * License Plate (plain text; defaults to blank = all)



TODO_CCI: Tim Reitz 07/31/2025: Is this actually simply a plain text field, or are there any special behaviors for it?

Sagar Sagar 12/11/2025: No special behaviors for the ask prompt. We sanitize when we compare.

  * Search by Partial (visible for Admin users; checkbox; applies to "License Plate"; defaults to not checked)
  * Primary Driver (plain text; searches by partial for "Primary Driver" names on Vehicles; defaults to blank = all)
  * No-Charge (drop list of blank / "Yes" / "No"; defaults to blank = all)
  * Agent (Blank = All) (visible for Admin users; drop list of active "In-State Agent"-type Contacts; defaults to the contact for the current user)
  * Status drop list of blank / "Active" / "Inactive"; defaults to blank = all)
  * Group By (drop list of "Status" / "Agent"; defaults to "Status")



  


Buttons: 

  * New Vehicle (opens a new blank Vehicle record)



  


Other Notes: 

  * Inactive items are displayed in gray font. 



  


  


TODO_CCI: Tim Reitz 07/31/2025: Could you review this spec and make sure it looks good to you? Thanks!

Sagar Sagar 12/11/2025: I believe the spec looks good. Thank you!
