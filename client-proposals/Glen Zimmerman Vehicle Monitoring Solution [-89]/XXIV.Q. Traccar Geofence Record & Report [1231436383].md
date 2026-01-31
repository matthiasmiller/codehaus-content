24.17. Traccar Geofence Record & Report

  


Requirements

*Done. 

  


The following record and report is a possible future item that could be added as part of Phase 2 (or before or after). 

  


Traccar Geofence Record: 

Overview: This is a custom record type, used to store information about "Geofences" from Traccar. This is a "sync record", not editable interactively in Silverloom.

  


Accessed via: The "Traccar Geofences" report(s) (see corresponding spec) 

  


Sections and Fields: 

  * Traccar Geofence Details section: 
    * Traccar Geofence ID (auto-set and read-only interactively; number; no decimals; details TBD)
    * Name (auto-set and read-only interactively; plain text field; details TBD)
    * Description (auto-set and read-only interactively; plain text field; details TBD)
    * Area (auto-set and read-only interactively; plain text field; details TBD)
    * Calendar ID (auto-set and read-only interactively; details TBD)
    * Attributes (auto-set and read-only interactively; details TBD)



  


  * Record History section (visible to __ TBD) 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: __ TBD 
  * Editability: __ TBD 



  


Special Considerations:

  * Copy Record: Disallowed
  * Delete Record: Disallowed
  * Merge Record: Disallowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


  


Traccar Geofence Report: This is a report that is similar to the other reports for Traccary sync records - details TBD.

  


Development Specification

Mockup: N/A

  


Tim Reitz 01/27/2026: Let's bump this to Phase 2 / future.

  


TODO_JB: Tim Reitz 09/18/2025: What would be our capabilities for doing geofences? 

\- Just a link to send the user to Traccar to set it up? 

\- Integration to display the Geofence feature from Traccar within Silverloom?
