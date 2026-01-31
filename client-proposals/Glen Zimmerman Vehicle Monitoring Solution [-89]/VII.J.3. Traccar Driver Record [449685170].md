7.10.3. Traccar Driver Record

  


Requirements

* 

  


Overview: This is a custom record type, used to store information about "Drivers" from Traccar. This is a "sync record", not editable interactively in Silverloom.

  


Accessed via: The Traccar Driver report(s) (see corresponding spec)

  


Sections and Fields: 

  * Traccar Driver Details section: 
    * Unique ID (auto-set and read-only interactively; number; no decimals)
    * Name (auto-set and read-only interactively; plain text field; corresponds to the "Name" in Traccar)
    * Attributes (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)



TODO_VA (later): Tim Reitz 01/27/2026: Spec once we have info on the User attributes from JB.

  


  * Record History section: 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to users with the "View Traccar Sync Records" Permission. 



TODO_JB (research): Tim Reitz 01/27/2026: I'm thinking that this record won't really need to be viewed interactively in Silverloom -- does that sound right to you? (we might keep the underlined spec above, just so that CCI testers / support users, etc. can see into it)

  * Editability: Editable only via import, via the Traccar sync. 



  


Special Considerations: 

  * Copy Record: Disallowed
  * Delete Record: Disallowed
  * Merge Record: Disallowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Mockup: N/A
