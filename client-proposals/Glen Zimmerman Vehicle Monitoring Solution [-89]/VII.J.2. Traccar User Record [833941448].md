7.10.2. Traccar User Record

Overview: This is a custom record type, used to set and store information about "Users" from Traccar. This is a "sync record", not editable interactively in Silverloom. It is created and modified via automatic processes in Silverloom, based on details set on Account and Contact records, and the data is synced to Traccar. Data is not synced back from Traccar to Silverloom for this record.

  


Accessed via: The "Traccar Users" report (see corresponding spec) 

  


Sections and Fields: 

  


  * Silverloom Details section:
    * Record ID (hidden; auto-set and read-only; unique identifier for the record) 



TODO_JB (research): Tim Reitz 01/20/2026: Or can/should we just use the Traccar Unique ID as the Silverloom ID too? 

  * Linked Contact (auto-set and read-only; list field of "Display Name" values for individual Contact records; displays as a link to the Contact record) 
  * Linked Account (auto-set and read-only; list field of "Account #" values for all Account records; displays as a link to the Account record; note that this is blank if the Traccar User record is for a provider)



  


  


  * Traccar User Details section: 
    * Unique ID (auto-set and read-only interactively; number; no decimals; corresponds to the unique ID from the Traccar User; note that this is the ID included in the URL in Traccar)



TODO_JB (research): Tim Reitz 01/27/2026: Thoughts on how we would set this? (it appears to be a sequential number set in Traccar -- do we keep track in Silverloom of the last one that was used for Traccar, and use the next one? (hoping that no one manually set up a new device in Traccar with the next number)

  * Name (auto-set and read-only interactively; plain text field; corresponds to the "Name" field on the Traccar User) 
  * Email (auto-set and read-only interactively; plain text field; corresponds to the "Email" field on the Traccar User) 
  * Password (plain text field; not used in Phase 1 - new users receive the a link to the "Reset Password" page, to set their password when they log in for the first time) 



  


  


  * Traccar User Preferences section:
    * Phone (
    * __



TODO_JB (research): Tim Reitz 01/27/2026: Thoughts on how to handle the rest of the "Preferences" fields from Traccar? (Default Map, Coordinates Format, Speed Unit, Distance Unit, etc.) Can we have these all set nicely via a server-level setting? Or should we default them here on the sync record to set them in Traccar?

  * Timezone (__



TODO_JB (research): Tim Reitz 01/27/2026: What seems like the best way to set the timezone from Silverloom? Their list is formatted differently than ours.

  


  


  * Traccar User Location section:
    * Latitude (__
    * Longitude (__
    * Zoom (__



_VA: Tim Reitz 12/10/2025: Not sure if this is needed?

TODO_JB (research): Tim Reitz 01/27/2026: Is it easy to determine what these fields are used for?

  


  * Traccar User Permissions section:
    * Expiration (auto-set and read-only; date field; defaults to __)



TODO_JB (research): Tim Reitz 01/27/2026: Can you determine what this is for?

  * Device Limit (auto-set and read-only; number field; 0 decimals; allows negative numbers; defaults to __)



TODO_JB (research): Tim Reitz 01/27/2026: I think you had been looking at this some the other day when we were talking.

  * User Limit (auto-set and read-only; number field; 0 decimals; allows negative numbers; defaults to __)



TODO_JB (research): Tim Reitz 01/27/2026: I think you had been looking at this some the other day when we were talking.

  * Disabled (auto-set and read-only; checkbox; defaults to not checked)
  * Admin (auto-set and read-only; checkbox; defaults to not checked; note that if this is checked, it overrides any of the below permissions checkboxes)
  * Read-only (auto-set and read-only; checkbox; defaults to checked)
  * Device Read-only (auto-set and read-only; checkbox; defaults to checked)
  * Limit Commands (auto-set and read-only; checkbox; defaults to checked)
  * Disable Reports (auto-set and read-only; checkbox; defaults to not checked)
  * No Email Change (auto-set and read-only; checkbox; defaults to checked)



  


  


  * Traccar Attributes section
    * Attributes (auto-set and read-only interactively; __ field; corresponds to the "Attributes" in Traccar)



DONE_JB (research): Tim Reitz 01/20/2026: What kind of field is this / what does it do? Not sure if we'd use it or not. 

_VA: Jonathan Bergen 01/21/2026: This is an object where we can store whatever we want. I think we would define attributes and then we can add them to users, devices, etc.

{

"id": 0,

"description": "string",

"attribute": "string",

"expression": "string",

"type": "string|number|boolean"

}

TODO_JB (research): Tim Reitz 01/27/2026: Thanks for that info! Would this be interfaced as a read-only memo or plain text field or RG in Silverloom? Or something else? 

  


TODO_JB (research): Tim Reitz 01/27/2026: Regarding how we would define attributes in Silverloom, do you think we'd do that as a special configuration record? Perhaps with an expression field?

  


  


  * Traccar Connections section:



DONE_JB (research): Tim Reitz 01/16/2026: Just confirming that it's fine to bring in the "Connection" items from Traccar (pretty sure we're going to need a lot of those). 

_VA: Jonathan Bergen 01/21/2026: I don't think there's any way to get Connections from Traccar. They basically mean permissions... We can create and delete them from the api.

TODO_JB (research): Tim Reitz 01/27/2026: Should we field anything here in the sync record for them? (if not, where would be the right place to have spec on how they get set?) This would presumably apply to the Traccar Device sync record too.

TODO_: If yes from JB: Tim Reitz 12/10/2025: Let's spec out the rest of the "Connections" fields from Traccar.

  * Devices (__
  * Groups (__
  * Geofences (__
  * Notifications (__
  * Calendars (__
  * Users (__
  * Contributed Attributes (__
  * Drivers (__
  * Saved Commands (__
  * Maintenance (__



  


  


  * Record History section: 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to users with the "View Traccar Sync Records" Permission. 



_NM: Tim Reitz 01/27/2026: What is the correct way to spec these? Providers need to be able to set these via import, but don't need to see them interactively (or on reports, etc.).

TODO_VA: Tim Reitz 01/30/2026: Say that they are visible to everyone, but hide the report menu option behind a permission. 

  * Editability: Editable only via import, via the Traccar sync. 



  


Special Considerations:

  * Copy Record: Disallowed
  * Delete Record: Disallowed



TODO_JB (research): Tim Reitz 01/27/2026: There's an option in Traccar to delete records -- thoughts on allowing it in Silverloom too? Would slightly reduce storage space over time.

  * Merge Record: Disallowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.


