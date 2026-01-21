4\. Reports: Scheduling

  


Requirements

This is an editable report.

  


Prompts:

  * Historical Weeks (number; default to 2)



  


Subset:

  * All incomplete hauls
  * All completed hauls from the past X number of weeks (Start of Week minus # of Weeks)
  * Exclude hauls to Builders (If it's a Dealer location, only include it if it's different from the building's builder)
  * Only include District X buildings
  * Only include unbuilt buildings 5 days before build date (i.e. building deadline)



  


Grouping:

  * Unscheduled (no scheduled date)
  * Week - Date - Hauler - Load #__ (i.e. "This Week - 7/21/21 - Joseph Miller - Load #1")
    * For the week, show "2 Weeks Ago", "Last Week", "This Week", "Next Week", "2 Weeks", etc)



  


Sort By:

  * Build Date
  * STIN



  


Columns:

  * Build Date (read-only)
  * Scheduled Date (editable)
  * Hauler (editable)
  * Load # (editable)
  * Hauler Schedule (read-only; from Hauler contact record)
  * Source (Manufacturer or Dealer name)
  * Destination (Customer address or Dealer name)
  * STIN
  * Sales Order Balance
  * Building Style
  * Building Size
  * Building Schedule Notes (plain text field; editable)
  * Load Remaining Length (Subtotal row that counts down using a hidden column)
  * Load Remaining Count (Subtotal row that counts down using a hidden column)
  * Damaged? (read-only)



  


NOTE: There's no need to sequence buildings on the load.

  


NOTE: The report will need to be refreshed in the browser to get the updated groupings and the updated remaining length/count. The scheduling process can be enhanced in the future.

  


Development Specification

Matthias Miller 08/26/2021: Josh will populate the Locations RG on building creation.
