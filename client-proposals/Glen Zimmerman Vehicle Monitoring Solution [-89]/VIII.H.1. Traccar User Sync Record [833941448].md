8.8.1. Traccar User Sync Record

  


Requirements

TODO_VA: Tim Reitz 02/02/2026: Doing some major reworking on this record, to store all of the information here rather than on the RGs on other records. Finish speccing this out based on the corresponding RGs / needs. 

  


Overview: This is a custom record type, used to set and store information about "Users" from Traccar. This is a "sync record", not editable interactively in Silverloom. It is created and modified via automatic processes in Silverloom, based on details set on Account and Contact records, and the data is synced to Traccar. Data is not synced back from Traccar to Silverloom for this record.

  


Accessed via: The "Traccar Users" report (see corresponding spec) 

  


Sections and Fields: 

  


  * Silverloom Details section:
    * Silverloom Record ID (hidden; auto-set and read-only; unique identifier for the record) 



TODO_JB (research): Tim Reitz 01/20/2026: Or can/should we just use the Traccar Unique ID as the Silverloom ID too? 

  * Traccar Login Category (auto-set and read-only; list field of "Traccar Login Categories" list items; sets based on the record from which the Traccar User sync record was created) 



  


  * Linked Contact (required; with the following details / behaviors:
    * drop list of "Display Names" for active Contacts, with the following conditional filtering:
      * if "Traccar Login Category" = "Account Group Admin": all active individual Contacts with the "Is Group Admin" checkbox checked;
      * if "Traccar Login Category" = "Account Member": all active individual Contacts;
      * if "Traccar Login Category" = "Account Reseller": all active individual Contacts with the "Is Account Reseller" checkbox checked;
      * if "Traccar Login Category" = "Master Administrator": all active individual Contacts with the "Is Master Administrator" checkbox checked;
      * if "Traccar Login Category" = "Reseller Rep": all active individual Contacts with the "Is Reseller Rep" checkbox checked;
    * becomes read-only after the initial Save; 



_NM: Tim Reitz 02/04/2026: Thoughts on having this editable vs. read-only after save?

TODO_VA: Tim Reitz 02/04/2026: Let's allow them to change it, to allow them to correct a mistake. We're also allowing them to edit Traccar Login Email. Warning on Save if changed.

  * validations:
    * warning on Save if changed from a saved value: "Linked Contact has been changed from "<Display Name>" to "<Display Name>". Are you sure you want to continue?";
    * error on Save if "Date of Birth" is blank on the Contact record: "Date of Birth is required for the Contact. Open the Contact to add this information before saving this record."; 
    * error on Save if "Gender" is blank on the Contact record of any of the Account Members: "Gender is required for the contact. Open the Contact to add this information before saving this record.") 


  * View / Edit Contact (visible if "Linked Contact" is not blank; link; opens the corresponding Contact record) 
  * Traccar Login Enabled (checkbox; with the following details / behaviors: 
    * defaults to checked; 
    * when set, the following field on the same record is affected:
      * "Disabled": sets to the opposite of this field's setting) 



  


  


  * Silverloom Account Group Admin section (visible if "Traccar Login Category" = "Account Group Admin"):
    * Linked Account Group (auto-set and read-only; list field of "Group Name" values for all Account Group records; displays as a link to the corresponding record; sets based on the record from which the Traccar User sync record was created / edited)
    * Group Admin (checkbox; auto-set and read-only; defaults to checked)
    * Primary Group Admin (checkbox; __)



TODO_VA: Tim Reitz 02/04/2026: Bring in details from the Group Admins RG

TODO_VA: Tim Reitz 02/04/2026: Update the Group Admins RG to be a virtual RG like Account Members.

  


  * Silverloom Account Member Details section (visible if "Traccar Login Category" = "Account Member"):
    * Linked Account (auto-set and read-only; list field of "Account #" values for all Account records; displays as a link to the corresponding record; sets based on the record from which the Traccar User sync record was created / edited)
    * Account Manager (checkbox; defaults to not checked; with the following details / behaviors: 
      * note that when this checkbox is checked, the "Is Account Manager" checkbox macro on the linked Contact record is checked;
      * data synced with Traccar (as User permission)) 
    * Primary Account Manager (checkbox; editable if "Account Manager" is checked; defaults to not checked; with the following details / behaviors:
      * error on Save if the linked Account does not have any linked Traccar User sync records with "Primary Account Manager" checked: "The linked Account does not have a Primary Account Manager.";  
      * warning on Save if the linked Account has more than one linked Traccar User sync record with "Primary Account Manager" checked: "The linked Account has more than one Primary Account Manager."; 
      * note that when this checkbox is checked, the "Is Primary Account Manager" checkbox macro on the linked Contact record is checked;
      * data synced with Traccar (as User permission))
    * Driver (checkbox; defaults to not checked; with the following details: 
      * warning on Save if the linked Account does not have any linked Traccar User sync records with "Driver" checked: "The linked Account does not have any Drivers."; 
      * note that when this checkbox is checked, the "Is Driver" checkbox macro on the linked Contact record is checked;
      * data synced with Traccar (as User permission)) 



  


  * Silverloom Account Reseller section (visible if "Traccar Login Category" = "Account Reseller"):
    * __



TODO_VA: Tim Reitz 02/02/2026: I'm not sure of any fields here for Phase 1. ("Linked Contact" might take care of it)

  


  


  * Silverloom Master Administrator Details section (visible if "Traccar Login Category" = "Master Administrator"):
    * __



TODO_VA: Tim Reitz 02/02/2026: I'm not sure of any fields here for Phase 1. ("Linked Contact" might take care of it)

  


  * Silverloom Reseller Rep Details section (visible if "Traccar Login Category" = "Reseller Rep"):
    * Linked Reseller (auto-set and read-only; list field of "Display Name" values for all organization Account Reseller Contact records; displays as a link to the corresponding record; sets based on the record from which the Traccar User sync record was created / edited) 
    * Rep (checkbox; auto-set and read-only; defaults to checked)
    * Reseller Admin (checkbox; __; note that when this checkbox is checked, the "Is Reseller Admin" checkbox macro on the linked Contact record is checked)



  


  


  * Traccar User Details section: 
    * Unique ID (auto-set and read-only interactively; number; no decimals; data synced __ Traccar; corresponds to the unique ID from the Traccar User; note that this is the ID included in the URL in Traccar)



TODO_JB (research): Tim Reitz 01/27/2026: Thoughts on how we would set this? (it appears to be a sequential number set in Traccar -- do we keep track in Silverloom of the last one that was used for Traccar, and use the next one? (hoping that no one manually set up a new device in Traccar with the next number)

  * Name (auto-set and read-only interactively; plain text field; data synced with Traccar; sets to the "Short Display Name" for the "Linked Contact";) 
  * Traccar Login Email (required; drop list of email addresses from the Email" embedded spreadsheet for the "Linked Contact" with the following details / behaviors:
    * error on the field if an email address is selected that has already been saved as the "Traccar Login Email" on any Traccar User sync record in the Solution: "This email address has already been used for another Traccar login (User: <Name>; Account #: <Account #>). Click the View / Edit Contact link to add a new email.";
    * this is the email address that is set as the login email for this person's User login in Traccar;  
    * data synced with Traccar ("Email" field)) 



TODO_VA: Tim Reitz 02/04/2026: Warning on Save if changed.

  


_NM: Tim Reitz 02/02/2026: How to re-use Traccar User records? I.e. if someone has a login with a certain email address, then the login is deactivated, then they want to use the same email address for a different login. Do we leave the closed-out Traccar User record as-is and create a new one with the same email address? Or do we revive the old one and relink it?

With the original approach, I was planning to reopen the old record. But with the new approach, It feels like the workflow would be awkward since we're opening a new Traccar User record... Is it a bad idea to just discard the old records, and only have validation against duplicate Emails on active ones? 

TODO_VA: Tim Reitz 02/03/2026: Nic is inclined to reuse. Let's have the "New" link force a prompt for "Traccar Login Email". If there's a match, it opens that record. If no match, opens a new blank record. 

  * Password (plain text field; not used in Phase 1 - new users receive the a link to the "Reset Password" page, to set their password when they log in for the first time) 



  


  


  * Traccar User Preferences section:
    * Mobile Phone (required; drop list of phone numbers for the "Linked Contact" with "Type" = "Mobile"; with the following details / behaviors: 
      * data synced with Traccar ("Phone" field))
    * Click "View / Edit Contact" to add a new mobile-type phone number. (visible if "Mobile Phone" = blank; on-screen message in gray font) 
    * __



TODO_JB (research): Tim Reitz 01/27/2026: Thoughts on how to handle the rest of the "Preferences" fields from Traccar? (Default Map, Coordinates Format, Speed Unit, Distance Unit, etc.) Can we have these all set nicely via a server-level setting? Or should we default them here on the sync record to set them in Traccar?

  * Timezone (__; data synced with Traccar)



TODO_JB (research): Tim Reitz 01/27/2026: What seems like the best way to set the timezone from Silverloom? Their list is formatted differently than ours.

  


  


  * Traccar User Location section:
    * Latitude (__; data synced with Traccar)
    * Longitude (__; data synced with Traccar)
    * Zoom (__; data synced with Traccar)



_VA: Tim Reitz 12/10/2025: Not sure if this is needed?

TODO_JB (research): Tim Reitz 01/27/2026: Is it easy to determine what these fields are used for?

  


  * Traccar User Permissions section:
    * Expiration (auto-set and read-only; date field; defaults to __; data synced with Traccar)



TODO_JB (research): Tim Reitz 01/27/2026: Can you determine what this is for?

  * Device Limit (auto-set and read-only; number field; 0 decimals; allows negative numbers; defaults to __; data synced with Traccar)



TODO_JB (research): Tim Reitz 01/27/2026: I think you had been looking at this some the other day when we were talking.

  * User Limit (auto-set and read-only; number field; 0 decimals; allows negative numbers; defaults to __; data synced with Traccar)



TODO_JB (research): Tim Reitz 01/27/2026: I think you had been looking at this some the other day when we were talking.

  * Disabled (auto-set and read-only; checkbox; defaults to not checked; data synced with Traccar)
  * Admin (auto-set and read-only; checkbox; defaults to not checked; note that if this is checked, it overrides any of the below permissions checkboxes; data synced with Traccar)
  * Read-only (auto-set and read-only; checkbox; defaults to checked; set via automatic process or via the "Traccar Login Enabled" checkbox; data synced with Traccar)
  * Device Read-only (auto-set and read-only; checkbox; defaults to checked; data synced with Traccar)
  * Limit Commands (auto-set and read-only; checkbox; defaults to checked; data synced with Traccar)
  * Disable Reports (auto-set and read-only; checkbox; defaults to not checked; data synced with Traccar)
  * No Email Change (auto-set and read-only; checkbox; defaults to checked; data synced with Traccar)



  


  


  * Traccar Attributes section
    * Attributes (auto-set and read-only interactively; __ field; data synced with Traccar)



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

  * Devices (__; data synced with Traccar)
  * Groups (__; data synced with Traccar)
  * Geofences (__; data synced with Traccar)
  * Notifications (__; data synced with Traccar)
  * Calendars (__; data synced with Traccar)
  * Users (__; data synced with Traccar)
  * Contributed Attributes (__; data synced with Traccar)
  * Drivers (__; data synced with Traccar)
  * Saved Commands (__; data synced with Traccar)
  * Maintenance (__; data synced with Traccar)



  


  


  * Record History section: 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users  
  * Editability: Editable only via import, via the Traccar sync. 



  


Special Considerations:

  * Copy Record: Disallowed
  * Delete Record: Disallowed



TODO_JB (research): Tim Reitz 01/27/2026: There's an option in Traccar to delete records -- thoughts on allowing it in Silverloom too? Would slightly reduce storage space over time.

  * Merge Record: Disallowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Mockup: 

TODO_MOCKUPS: Tim Reitz 02/03/2026: Could you do an initial mockup for this one, and paste the link into the space above? Thanks!
