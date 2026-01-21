6.1.4. Manage Sales Items Report

  


Requirements

Overview: This is the standard editable Silverloom report to view and configure Sales Items in the Solution. Note that any customizations are noted as such in the spec. 

  


Accessed from: Main Menu | Sales | Manage Sales Items (opens the report directly, bypassing the filter screen) 

  


Title: "Sales Items"

  


Columns: 

  * Code (link to open the record)
  * Display Name (custom) 
  * Description (editable) 
  * Category (editable) 
  * PA Oil Index $ (custom; editable)
  * Oil Index Status (custom; displays "Oil Index Out of Date" in red text if visible on the record) 
  * Update to Current (custom; editable; with the following details / behaviors: 
    * displays the corresponding hidden editable macro from the record as a drop list of blank / "Yes" / "No"; 
    * editable here on the report if set to "No", in which case it can be set to "Yes" to update the "PA Oil Index $", like the "Update to Current" button on the Sales Item detail screen) 
  * Unit of Measure (visible, based on the "Sales Item Show UOM" System Switch; editable) 
  * Unit Cost $ (visible, based on the "Sales Item Show Cost & Markup" System Switch; editable)
  * Markup % (visible, based on the "Sales Item Show Cost & Markup" System Switch; editable)
  * Unit Price $ (editable) 
  * Active (editable; Yes/No; when the row is selected, a checkbox appears for editing) 



  


Grouped by:

  * First by: Active / Inactive
  * Second by: Category (alphabetical, with an "Uncategorized" group at the bottom for items with no Category)



  


Sorted by: Code (alphabetical)

  


Filters: 

  * Code (optional; plain text; searches for any matching text in the Codes; defaults to blank = all)
  * Category (optional; drop list of Sales Item Category list items; defaults to blank = all)
  * Description (optional; plain text; searches for any matching text in the Descriptions; defaults to blank = all)
  * Active Items Only (checkbox; defaults to checked)



  


Buttons: 

  * Search (opens a prompt screen with the filters for this report, to search for specific details)
  * New Item (opens a blank new Item record)



  


Menu Visibility: All users

  


Editability: Custom: Editable for users with the "Edit Sales Items" Permission

  


Save Type: Instant Save (when the user clicks away from the edited row) 

  


Other Notes: 

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=677515175#gid=677515175](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=677515175#gid=677515175)

  


Ellis Miller 06/18/2025:

[ ] Make this report "Support System Specific Settings"

[ ] Add the Display Name column for System Include If ZLP

[ ] No coding required for editing permission.

  


[ ] Note that we are moving the link from "Description" to "Code".

[ ] Note that we are changing the report title from "Active Product / Sales Items" to simply "Sales Items"

[ ] Note that we are changing the "Unit Price" column to "Unit Price $"

[ ] Note that we are adding standard columns for "Unit of Measure", "Unit Cost $", and "Markup %", all of which are conditionally visible based on the System Switches.

4 Hours
