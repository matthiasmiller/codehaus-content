7.10.5. Traccar Position Record

  


Requirements

* 

  


Overview: This is a custom record type, used to store information about "Positions" from Traccar. This is a "sync record", not editable interactively in Silverloom.

  


Note that for Phase 1, all Positions from Traccar are synced into Silverloom. If this eventually creates a storage space problem, there are a few options for addressing that, but for the initial setup, it seems most straightforward to pull it all in.

  


Accessed via: The "Traccar Positions" report (see corresponding spec) 

  


Sections and Fields:

  * Traccar Position Details section: 
    * ID (auto-set and read-only interactively; number; no decimals; corresponds to the "ID" in Traccar)
    * Device ID (auto-set and read-only interactively; number; no decimals; corresponds to the "Device ID" in Traccar)
    * Protocol (auto-set and read-only interactively; plain text field; corresponds to the "Protocol" in Traccar)
    * Device Time (auto-set and read-only interactively; UTC date & time in the ISO 8601 format (i.e. "2019-08-24T14:15:22Z"); corresponds to the "Device Time' in Traccar)
    * Fix Time (auto-set and read-only interactively; UTC date & time in the ISO 8601 format (i.e. "2019-08-24T14:15:22Z"); corresponds to the "Fix Time" in Traccar)
    * Server Time (auto-set and read-only interactively; UTC date & time in the ISO 8601 format (i.e. "2019-08-24T14:15:22Z"); corresponds to the "Server Time" in Traccar)
    * Outdated (auto-set and read-only interactively; __ field; corresponds to the "Outdated" in Traccar)



TODO_JB (research): Tim Reitz 01/27/2026: Is this a checkbox in SIlverloom?

  * Valid (auto-set and read-only interactively; __ field; corresponds to the "Valid" in Traccar)



TODO_JB (research): Tim Reitz 01/27/2026: Is this a checkbox in SIlverloom?

  * Latitude (auto-set and read-only interactively; number; 6 decimals; corresponds to the "Latitude" in Traccar)
  * Longitude (auto-set and read-only interactively; number; 6 decimals; corresponds to the "Longitude" in Traccar)
  * Altitude (auto-set and read-only interactively; number; 2 decimals; corresponds to the "Altitude" in Traccar)
  * Speed (auto-set and read-only interactively; number; 2 decimals; corresponds to the "Speed" in Traccar)
  * Course (auto-set and read-only interactively; __ field; corresponds to the "Course" in Traccar)



TODO_JB (research): Tim Reitz 01/27/2026: What kind of field is this?

  * Address (auto-set and read-only interactively; plain text field; corresponds to the "Address" in Traccar)
  * Network (auto-set and read-only interactively; plain text field; corresponds to the "Network" in Traccar)
  * Geofence IDs (auto-set and read-only interactively; __ field; corresponds to the "Geofence IDs" in Traccar; note that this is not in use for Phase 1)



TODO_JB (research): Tim Reitz 01/27/2026: What kind of field is this? simple string field that can be set with a comma-separated list? or something else?

  * Attributes (auto-set and read-only interactively; __ field; corresponds to the "Attributes" in Traccar)



TODO_JB (research): Tim Reitz 01/27/2026: What kind of field is this? or is it even needed?

  


  


  * Record History section: 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users. 
  * Editability: Editable only via import, via the Traccar sync. 



  


Special Considerations:

  * Copy Record: Disallowed
  * Delete Record: Disallowed
  * Merge Record: Disallowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Mockup: N/A

  


Tim Reitz 09/15/2025: The "Route" report in Traccar appears to display data from Position records: [https://x6rildfvs.traccar.com/reports/route](https://x6rildfvs.traccar.com/reports/route).
