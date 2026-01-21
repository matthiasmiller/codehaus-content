7.10.6. Traccar Geofence Record

  


Requirements

Jonathan Bergen 07/25/2025: Not sure that we need this.

_GZ: Tim Reitz 09/12/2025: Do you anticipate using Geofences?

Tim Reitz 09/18/2025: Glen is planning to consider this more, but he's interested in it. At the least, we probably would be sending people to Traccar to define the geofences, then pulling info into Silverloom to be able to select a geofence / turn it on and off for a Device or Driver / etc. 

TODO_GZ: Tim Reitz 10/09/2025: Let's follow up with Glen at some point. 

  


TODO_JB: Tim Reitz 09/18/2025: What would be our capabilities for doing geofences? 

\- Just a link to send the user to Traccar to set it up? 

\- Integration to display the Geofence feature from Traccar within Silverloom? 

  


  


Overview: This is a custom record type, used to store information about "__" from Traccar. This is a "sync record", not editable interactively in Silverloom.

TODO_VA:

  


Accessed via: __

TODO_VA:

  


Sections and Fields: TODO_VA:

  * Traccar Geofence Details section: 
    * Traccar Geofence ID (auto-set and read-only interactively; number; no decimals; corresponds to the __ in Traccar)
    * Name (auto-set and read-only interactively; plain text field; corresponds to the __ in Traccar)
    * Description (auto-set and read-only interactively; plain text field; corresponds to the __ in Traccar)
    * Area (auto-set and read-only interactively; plain text field; corresponds to the __ in Traccar)
    * Calendar ID (auto-set and read-only interactively; number; no decimals; corresponds to the __ in Traccar)



TODO_JB: is there a Traccar Calendar record that we need?

  * Attributes (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)



  


  * Record History section (visible to __): TODO_VA: 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: TODO_VA:

  * Visibility: __
  * Editability: __



  


Special Considerations:

  * Copy Record: Disallowed
  * Delete Record: Disallowed
  * Merge Record: Disallowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Mockup: N/A

  


Tim Reitz 09/17/2025: From Jonathan's early research: 

"id": 0,

"name": "string",

"description": "string",

"area": "string",

"calendarId": 0,

"attributes": { }
