7.10.1. Traccar Group Records

DONE_JB (research): Tim Reitz 01/16/2026: I think we'll want a sync record for Traccar Groups. Could you look into the fields that are included for this in Traccar, for me to spec out the sync record for Silverloom?

Jonathan: This is what we currently have:

[

    {

        "id": 9,

        "attributes": {},

        "groupId": 10,

        "name": "Account Group A"

    },

    {

        "id": 10,

        "attributes": {},

        "groupId": 9,

        "name": "Account Group B"

    },

    {

        "id": 11,

        "attributes": {},

        "groupId": 0,

        "name": "Account Group C"

    }

]

  


These records are very basic... maybe an array of attributes would make sense? I have a sense that we'll end up putting things in the attributes RG.

TODO_JB (research): Tim Reitz 01/27/2026: How would you like me to spec this, for estimating / planning / documentation / future support?

  


TODO_JB (research): Tim Reitz 01/27/2026: What all would we be tracking with Groups? I'm thinking: 

  * Account Groups (from Silverloom) 
  * Resellers
  * Accounts?
  * Account Managers? 
  * other?



  


\--------------

*

  


Overview: This is a custom record type, used to store information about "Groups" for Traccar. This is a "sync record", not editable interactively in Silverloom.

  


Accessed via: The Traccar Groups report(s) (see corresponding spec)

  


Sections and Fields:

  * Traccar Group Details section: 
    * Unique ID (auto-set and read-only interactively; number; no decimals; corresponds to the unique ID from the Traccar Group; note that this is the ID included in the URL in Traccar)
    * Name (auto-set and read-only interactively; plain text field; corresponds to the "Name" in Traccar)
    * Attributes (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)



TODO_VA (later): Tim Reitz 01/27/2026: Spec once we have info on the User attributes from JB.

  * Upline Group (auto-set and read-only interactively; list field of Traccar Group records; corresponds to the "Group" in Traccar) 



  


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


