7.10.3. Traccar Device Record

  


Requirements

_EM.: Tim Reitz 09/11/2025: Should we have one or two Device records in Silverloom?

  * Two records approach:
    * "Traccar Device Record": 1-to-1 directly with Traccar; probably not edited directly in Silverloom.
    * "Silverloom Device Record": includes most/all of the data from the Traccar Device record + Silverloom-specific details (events, etc.), and is used to edit the "Traccar Device Record", and then Traccar indirectly that way.
  * One record approach: A single "Device" record that does it all.



TODO_: Tim Reitz 10/30/2025: TBD with Jonathan's sync research. But Ellis is thinking that we might go either way.  

  


TODO_JB (research): do we need this record, which then passes info on to the Silverloom Device record? Or should the Silverloom record have fields that correspond to the Traccar record?

Tim Reitz 01/15/2026: I'm thinking that we keep this "sync" record, to reduce edit collisions, etc. 

  


Overview: This is a custom record type, used to store information about "Devices" from Traccar. This is a "sync record", not editable interactively in Silverloom.

  


Accessed via: __

TODO_:

  


Sections and Fields: TODO_:

  * Traccar Device Details section: 
    * Traccar Device ID (auto-set and read-only interactively; number; no decimals; corresponds to the __ from the Traccar Device) 



TODO_: Tim Reitz 12/10/2025: Presumably the record ID, displayed in the URL. 

  * Traccar Device Name (auto-set and read-only interactively; plain text field; corresponds to the "Name" from the Traccar Device) 
  * Traccar Unique ID (auto-set and read-only interactively; plain text field; corresponds to the "Identifier" in Traccar)



TODO_: Tim Reitz 12/10/2025: Presumably this is the the "Identifier" that you set on the Device in Traccar? (IMEI, etc.) 

  * Traccar Connection Status (auto-set and read-only interactively; plain text field; corresponds to the __ in Traccar)
  * Last Update (auto-set and read-only interactively; UTC date & time in the ISO 8601 format (i.e. "2019-08-24T14:15:22Z"); corresponds to the __ in Traccar)
  * Position ID (auto-set and read-only interactively; number; no decimals; corresponds to the __ in Traccar)



TODO_: presumably the last Position (Traccar Position) for the Device?

  


  


  * Traccar Extra section: 
    * Group Name (auto-set and read-only interactively; number; no decimals; corresponds to to the __ in Traccar)



TODO_: do we need a Traccar Group Record that corresponds to the Silverloom Group record? Or should the Silverloom record have fields that correspond to the Traccar record?

  * Phone (auto-set and read-only interactively; plain text field; corresponds to the __ in Traccar)
  * Model (auto-set and read-only interactively; plain text field; corresponds to the __ in Traccar)
  * Contact (auto-set and read-only interactively; plain text field; corresponds to the __ in Traccar)
  * Category (auto-set and read-only interactively; plain text field; corresponds to the __ in Traccar)
  * Disabled (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)



  


  * Traccar Attributes section: 
    * Attributes (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)



  


  * Traccar Connections section: 
    * Geofences (
    * Notifications (
    * Drivers (
    * Computed Attributes (
    * Saved Commands (
    * Maintenance (
    * __



TODO_: If yes from JB that we can bring in Connection: Let's spec out these out. 

  


  * Record History section (visible to __): TODO_: 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: TODO_:

  * Visibility: __
  * Editability: __



  


Special Considerations:

  * Copy Record: Disallowed
  * Delete Record: Disallowed



TODO_: Tim Reitz 09/17/2025: (for this an all of the Traccar records) Best to disallow, or allow for Master Administrators?

  * Merge Record: Disallowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Mockup: N/A
