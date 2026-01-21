7.2.11. Contact Record - Silverloom Contact Settings Section

  


Requirements

  * Silverloom Contact Settings section (standard section): 



  


  * User ID (standard field; visible if "Is Organization" is not checked; drop list of active User IDs that are not already linked to a Contact record; visible to all users; custom editability: editable for __ editable for users with the "Edit User Groups and Profiles" Permission) 



TODO_: Tim Reitz 10/15/2025: Note that details are TBD. This might actually be read-only (if we can use triggers). Or might have an x30 button like ZSB.

If read-only, it would display as a link. If not read-only, probably have a "View / Edit Login Details" link beside it (see notes in Dev Spec).

  


Development Specification

TODO_: Tim Reitz 10/03/2025: Update this spec once the Snippet is updated: [http://zch.apphosting.zone/Detail/Edit/2?RecordType=Snippets&NumberID=-53&State=ctLVLwm53iQ&#](http://zch.apphosting.zone/Detail/Edit/2?RecordType=Snippets&NumberID=-53&State=ctLVLwm53iQ&#).

  


  


Tim Reitz 10/15/2025: If we end up moving this [User ID] to another section (as an editable macro): 

  * User ID (editable macro; displays / sets the hidden "User ID" field in the Silverloom Settings section of the Contact record - see corresponding spec; includes the same behaviors and validations as the hidden field; visible to and editable for __) 



_EM: Tim Reitz 10/04/2025: Do we like the idea of having it here as an editable macro instead of keeping it down in the Silverloom settings section? I'm currently thinking yes. 

Tim Reitz 10/04/2025: Mockups could help give direction on this... 

Tim Reitz 10/04/2025: On the other hand, we could move all of the "Is ..." checkboxes down there to that section (that's what we're doing for ZSB, so doing that here as well would be an exercise in consistency). 

  


_EM: Tim Reitz 09/18/2025: Thoughts on a process similar to ZSB's for creating & linking / unlinking User Profiles? 

Tim Reitz 10/09/2025: Ellis thinks we could this all work without buttons (triggers, etc.)

Tim Reitz 10/13/2025: Per Ellis, we'll plan to have this be done either via button (like ZSB) or automatically (triggers). This would require more research / discussion -- KS office to do research. We can fill out the requirements spec here once we have more details. 

_EM.: Tim Reitz 01/19/2026: When to do this research & spec it out? Note that it now is only for providers, and at this point Nic & I are planning to only allow "Full Access" users to edit User Profile records.

For Phase 1, my proposal is that we keep the standard editability, and let the Master Administrators take care of user management. 

TODO_VA: Tim Reitz 01/20/2026: Yes, let's go with this. 

  * View / Edit Login Details (custom; link; with the following details / behaviors:
    * visible if "User ID" is not blank;
    * visible to __; 
    * opens the User Profile record selected in the "User ID" field)



TODO_: Tim Reitz 09/03/2025: Finish spec.
