9.8.6. Main Traccar Events Report

Overview: This is a custom report of Traccar Event records, with various filters. Note that this report is also used in various filtered versions accessed from other places in the Solution.

  


Accessed from:

  * Advanced | Traccar Sync Records | Traccar Events
  * Filtered version: "View Linked Event(s)" link on individual Contacts



TODO_VA: Tim Reitz 01/15/2026: Add this link. And spec the report.

  * Filtered version: "View Linked Event(s)" link on Vehicle records



  


Title: 

  * Main title: "Traccar Events" 
  * Suffix(es):
    * if "Device" filter is set: " for Device <Device ID>" 
    * if "Primary Device Driver" filter is set: " (Driver: "<Display Name>")"
    * if "Primary Device Vehicle" filter is set: " (Vehicle: "<Vehicle Description>")"



  


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

  


Grouped by: N/A 

  


Sorted by:

  * First by: "Event Date" (most recent at the top) 
  * Second by: "Event Time" (most recent at the top) 



  


Filters: 

  * Event Date Start (optional; date; looks at the "Event Date"; defaults to blank = all)
  * End (optional; date; looks at the "Event Date"; defaults to the current date)
  * Event Types (optional; multi-select drop list of "Traccar Event Types" list items; defaults to blank = all)
  * Device (optional; drop list of "Device Description" values for all Device records; defaults to blank = all)
  * Device Account (optional; drop list of "Account #" values for all Account records; defaults to blank = all)
  * Device Primary Driver (optional; drop list of "Display Name" values for all individual Contacts; defaults to blank = all)
  * Device Primary Vehicle (optional; drop list of "Vehicle Description" values for all Vehicle records; defaults to blank = all) 



  


Buttons: 

  * N/A



  


Menu Visibility: All Users

  


Other Notes:

  * N/A


