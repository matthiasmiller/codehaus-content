7.10.4. Traccar Device Record

  


Requirements

*

  


Overview: This is a custom record type, used to store information about "Devices" from Traccar. This is a "sync record", not editable interactively in Silverloom.

  


Accessed via: The "Traccar Devices" report (see corresponding spec) 

  


Sections and Fields:

  * Traccar Device Details section: 
    * Unique ID (auto-set and read-only interactively; number; no decimals; corresponds to the unique ID from the Traccar Device; note that this is the ID included in the URL in Traccar)



TODO_JB (research): Tim Reitz 01/27/2026: Same as for User -- Thoughts on how we would set this?  

  * Name (auto-set and read-only interactively; plain text field; corresponds to the "Name" in Traccar) 
  * Identifier (auto-set and read-only interactively; plain text field; corresponds to the "Identifier" in Traccar)
  * Traccar Connection Status (auto-set and read-only interactively; plain text field; corresponds to the __ in Traccar)
  * Last Update (auto-set and read-only interactively; UTC date & time in the ISO 8601 format (i.e. "2019-08-24T14:15:22Z"); corresponds to the "Last Update" in Traccar)
  * Position ID (auto-set and read-only interactively; number; no decimals; corresponds to the "Position ID" in Traccar)



TODO_JB (research): Tim Reitz 01/27/2026: Is this the last Position record tied to this Device?

  


  


  * Traccar Extra section: 
    * Group Name (auto-set and read-only interactively; number; no decimals; corresponds to to the "Group" in Traccar)
    * Phone (auto-set and read-only interactively; plain text field; corresponds to the "Phone" in Traccar)
    * Model (auto-set and read-only interactively; plain text field; corresponds to the "Model" in Traccar)
    * Contact (auto-set and read-only interactively; plain text field; corresponds to the "Contact" in Traccar)
    * Category (auto-set and read-only interactively; plain text field; corresponds to the "Category" in Traccar)
    * Disabled (auto-set and read-only interactively; checkbox field; corresponds to the "Disabled" in Traccar)



  


  * Traccar Attributes section: 
    * Attributes (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)



TODO_VA (later): Tim Reitz 01/27/2026: Spec once we have info on the User attributes from JB.

  


  * Traccar Connections section: 
    * Geofences (
    * Notifications (
    * Drivers (
    * Computed Attributes (
    * Saved Commands (
    * Maintenance (
    * __



TODO_VA (later): Tim Reitz 01/27/2026: Spec once we have info on the User connections from JB.

  


  


  * Record History section: 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to users with the "View Traccar Sync Records" Permission. 



_NM: Tim Reitz 01/27/2026: Same as question on User record regarding how to spec. I think the same requirements apply here.

TODO_VA: Tim Reitz 01/30/2026: Same as on Traccar User record. 

  * Editability: Editable only via import, via the Traccar sync. 



  


Special Considerations:

  * Copy Record: Disallowed
  * Delete Record: Disallowed
  * Merge Record: Disallowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Mockup: N/A
