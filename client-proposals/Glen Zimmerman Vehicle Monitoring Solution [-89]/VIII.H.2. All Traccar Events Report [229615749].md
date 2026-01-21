8.8.2. All Traccar Events Report

Overview: This is a custom report of Traccar Event records, with various filters. Note that this report is also used in various filtered versions accessed from other places in the Solution.

  


Accessed from:

  * __ | __ | Traccar Events



TODO_VA

  * Filtered version: "View Linked Event(s)" link on individual Contact records



TODO_VA: Tim Reitz 01/15/2026: Add this link. And spec the report.

  * Filtered version: "View Linked Event(s)" link on Vehicle records



  


Title: 

  * Main title: "Traccar Events"
  * Suffix(es):
    * if "Primary Device Driver" filter is set: " by Driver (<Display Name>)"
    * if "Primary Device Vehicle" filter is set: " by Vehicle (<Vehicle Description>)"



  


Preface: __

TODO_VA: Tim Reitz 01/15/2026: Once we have data access specced for Traccar Event records: Probably include a note about the subset and that there might be other Events in Traccar that were not imported.

  


Columns: 

  * Traccar Event ID (link to Event record)
  * Event Type
  * Event Date
  * Event Time
  * Device (displays the "Device Description"; link to the Device record)
  * Device Account (displays the "Account #"; link to the Account record)
  * Device Primary Driver (displays the "Display Name" link to the Contact record)
  * Device Primary Vehicle (displays the "Vehicle Description"; link to the Vehicle record)



  


Row-Specific Buttons: N/A

  


Grouped by: TODO_VA

  


Sorted by: TODO_VA

  


Filters: 

  * Event Date Start (optional; date; looks at the "Event Date"; defaults to blank = all)
  * End (optional; date; looks at the "Event Date"; defaults to the current date)
  * Event Types (optional; multi-select drop list of "Traccar Event Types" list items; defaults to blank = all)
  * Device (optional; drop list of "Device Description" values for all Device records; defaults to blank = all)
  * Device Account (optional; drop list of "Account #" values for all Account records; defaults to blank = all)
  * Device Primary Driver (optional; drop list of "Display Name" values for all individual Contact records; defaults to blank = all)
  * Device Primary Vehicle (optional; drop list of "Vehicle Description" values for all Vehicle records; defaults to blank = all)



  


Buttons: 

  * N/A



  


Menu Visibility: All Users

  


Other Notes:

  * N/A


