7.10.2. Traccar User Record

Overview: This is a custom record type, used to set and store information about "Users" from Traccar. This is a "sync record", not editable interactively in Silverloom. It is created and modified via automatic processes in Silverloom, based on details set on Account and Contact records, and the data is synced to Traccar. Data is not synced back from Traccar to Silverloom for this record.

  


Accessed via: __

TODO_:

  


Sections and Fields: 

  


  * Silverloom Details section:
    * Record ID (hidden; auto-set and read-only; unique identifier for the record) 



TODO_JB: Tim Reitz 01/20/2026: Or can/should we just use the Traccar Unique ID as the Silverloom ID too? 

  * Linked Contact (auto-set and read-only; list field of "Display Name" values for individual Contact records; displays as a link to the Contact record) 
  * Linked Account (auto-set and read-only; __ 



TODO_VA: Tim Reitz 01/20/2026: blank if for a provider

  


  * Traccar User Details section: 
    * Unique ID (auto-set and read-only interactively; number; no decimals; corresponds to the __ from the Traccar User)



TODO_JB: Tim Reitz 12/10/2025: This would be the number that displays in the URL for Users. Apparently a hidden field on the screen in Traccar.

  * Name (auto-set and read-only interactively; plain text field; corresponds to the "Name" field on the Traccar User) 
  * Email (auto-set and read-only interactively; plain text field; corresponds to the "Email" field on the Traccar User) 
  * Password (plain text field; not used in Phase 1) 



TODO_JB: Tim Reitz 01/20/2026: I think we can leave this blank, since we're planning for the Welcome email to include the password reset link. It appears to not be a required field in Traccar.

Tim Reitz 01/20/2026: At some point, we maybe would want to be able to set it from Silverloom. 

  


  * Traccar User Preferences section:
    * Phone (
    * 


TODO_VA: Tim Reitz 12/10/2025: Let's spec out the rest of the "Preferences" fields from Traccar.

  


  * Traccar User Location section:
    * 


TODO_VA: Tim Reitz 12/10/2025: Not sure if this is needed?

  


  * Traccar User Permissions section:
    * 


TODO_VA: Tim Reitz 12/10/2025: Let's spec out the rest of the "Preferences" fields from Traccar.

  


  


  * Traccar Attributes section
    * Attributes (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)



TODO_JB (research): Tim Reitz 01/20/2026: What kind of field is this / what does it do? Not sure if we'd use it or not. 

  


  * Traccar Connections section:



TODO_JB (research): Tim Reitz 01/16/2026: Just confirming that it's fine to bring in the "Connection" items from Traccar (pretty sure we're going to need a lot of those). 

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



  


  


  


  * Record History section (visible to __): TODO_: 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to __. 



TODO_VA: Tim Reitz 01/20/2026: All providers, or only Full Access? 

  * Editability: Editable only via import (for all users). 



  


Special Considerations:

  * Copy Record: Disallowed
  * Delete Record: Disallowed
  * Merge Record: Disallowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.


