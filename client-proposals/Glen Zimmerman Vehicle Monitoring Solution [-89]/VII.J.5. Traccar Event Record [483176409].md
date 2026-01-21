7.10.5. Traccar Event Record

  


Requirements

Overview: This is a custom record type, used to store information about "Events" from Traccar. This is a special "sync record", with certain details set via the sync with Traccar (but not editable interactively in Silverloom), and other details editable interactively in Silverloom (but not synced back to Traccar).

TODO_JB (research): Tim Reitz 01/16/2026: Is it fine to have part of this record editable interactively? (see spec below)

  


Accessed via: 

  * Traccar Events report 
  * "Device Events" embedded spreadsheet on Device records 



  


Sections and Fields: 

  * Traccar Event Details section (all fields in this section are set from Traccar): 



TODO_JB: Tim Reitz 01/14/2026: I think I'll want confirmation from you regarding the corresponding field names in Traccar. 

  * Traccar Event ID (auto-set and read-only interactively; number; no decimals; corresponds to the __ in Traccar)
  * Event Type (auto-set and read-only interactively; plain text field; corresponds to the __ in Traccar)
  * Traccar Event Time (auto-set and read-only interactively; UTC date & time in the ISO 8601 format (i.e. "2019-08-24T14:15:22Z"); corresponds to the __ in Traccar)
  * Event Time Zone (auto-set and read-only; __



TODO_: Tim Reitz 10/25/2025: I think we'd have to look at the Event location (Position ID?) to determine this. 

  * Event Date (read-only macro; displays the date from the "Traccar Event Time" field, in the "MM/DD/YYYY" format, based on the "Traccar Event Time" and the "Event Time Zone") 
  * Event Time (read-only macro; displays the date from the "Traccar Event Time" field, in the "HH:MM:SS AM/PM" format, based on the "Traccar Event Time" and the "Event Time Zone")
  * Traccar Device ID (auto-set and read-only interactively; number; no decimals; corresponds to the __ in Traccar)
  * Traccar Position ID (auto-set and read-only interactively; number; no decimals; corresponds to the __ in Traccar; link to the corresponding Traccar Position Record in Silverloom) 



TODO_: Tim Reitz 01/14/2026: Are we doing Traccar Position Records in Silverloom? 

  * Traccar Coordinates (auto-set and read-only interactively; number; no decimals; corresponds to the __ in Traccar) 
  * Google Maps (link; opens the location of "Coordinates" in Google Maps) 
  * Apple Maps (link; opens the location of "Coordinates" in Apple Maps)
  * Traccar Geofence ID (auto-set and read-only interactively; number; no decimals; corresponds to the __ in Traccar; link to the corresponding Traccar Geofence Record in Silverloom)
  * Traccar Maintenance ID (auto-set and read-only interactively; number; no decimals; corresponds to the __ in Traccar)



TODO_JB (research): is there a Traccar Maintenance record that we need?

  * Traccar Attributes (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)



  


  


  * <Service Name> Details section: 
    * Device Description (auto-set and read-only; defaults to the "Device Description" for the Device record matching the "Traccar Device ID", when this record is created) 
    * Device Account (auto-set and read-only; defaults to the "Account #" of the current "Account" on the corresponding Device record when this record is created)
    * Stored Device Primary Driver (hidden; auto-set and read-only; defaults to the "Contact ID" of the "Primary Driver" on the corresponding Device record when this record is created) 
    * Device Primary Driver (read-only macro; displays the current "Display Name" of the "Stored Device Primary Driver") 
    * Override Driver (optional; plain text field; for a user to type in another name if another person was reported as driving the vehicle at the time of the Event) 
    * Override Driver Notes (optional; plain text field; for the user to document additional notes related to "Override Driver") 
    * Device Primary Vehicle (auto-set and read-only; defaults to the "Vehicle Description" of the "Primary Vehicle" on the corresponding Device record when this record is created)   
    * Owner at Time Event (auto-set and read-only; defaults to the "Display Name" of the "Current Owner" when this record is created) 
    * Override Vehicle (optional; plain text field; for a user to type in another VIN if another vehicle was reported as having the Device at the time of the Event) 
    * Override Vehicle Notes (optional; plain text field; for the user to document additional notes related to "Override Vehicle") 



  


  


  * Record History section (visible only to "Upline Provider Roles" for the linked "Account"): 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (visible only to users with the "Full Access" Permission; link to open the report for the record) 



  


  


Data Access: 

  * Visibility: Visible to all users. 
  * Editability: Editable for "Upline Provider Roles" users of the linked Account. 



TODO_GZ: Tim Reitz 01/15/2026: Visibility: Is it fine for all providers to see all Events in Silverloom? Or should we limit it to only uplines?

If we limit to only uplines, we would need to determine how to limit it: Based on Device / Account / Driver?

  


Special Considerations:

  * Copy Record: Disallowed
  * Delete Record: Disallowed
  * Merge Record: Disallowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.  



  


  


TODO_: How to specify the speed limit?

Tim Reitz 07/23/2025: I'm assuming this would be for the "Speed limit exceeded"-type Event

Tim Reitz 01/14/2026: This probably should be deferred to a "Possible Future Item", rather than include the complexity here?? Unless it's simple. 

TODO_BR: Tim Reitz 01/14/2026: Once the devices are up and running, how does the "Speed limit exceeded" Event work in Traccar?

  


Development Specification

Mockup: __

TODO_MOCKUPS: Tim Reitz 01/14/2026: Let's go ahead and do a mockup of this. I had been thinking no mockup, but now it looks like users will be interacting with this record directly, so let's go ahead.
