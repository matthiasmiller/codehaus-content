11.0.3. **Event - Industry Forum (Internal) Section

  


Requirements

_VA: Archive once we have these sections settled.

  


_VA: Tim Reitz 06/21/2024: Consider combining this and the Info Mtg & Launch Mtg sections, with conditionally visible fields and the section heading showing <Event Type>... 

Let's talk with the client to make sure we get a clear path for some of the name fields, etc. 

  


Industry Forum (Internal) section (visible if Event Type = Industry Forum; visibility for users based on the "Event Visibility" field selection, with some fields visible only for Regional Reps and Super Admins):

  


  * Industries (required; visible in Edit mode; multi-select drop list of Industries; defaults to blank) 
  * Included Industries (auto-set and read-only; small read-only memo that displays the selected Industry(ies) in a comma-separated list, in the same sequence in which they appear on the drop list) 



Tim Reitz 06/29/2024: I realized today that these should not be in an "(Internal)" section, so I moved them to a new regular section. 

  * Host (required; drop list of all active Member-type Contacts; filters down as you type; defaults to blank) 
  * Host Phone (auto-set and read-only; displays the top phone number for the selected Organizer)
  * Host Email (auto-set and read-only; displays the top primary email address for the selected Organizer; displays as a link to send an email)



: Tim Reitz 06/21/2024: Could we change this to "Organizer" like the other two? Would need to ask the client about it. 

Tim Reitz 06/26/2024: Emailing the client today (email: Events - mockup & a few questions).

  * View Contact (link; visible in Edit Mode if a Contact is selected in the Host field; opens the corresponding Contact record)
  * Event Notes (memo; can be used for attaching documents and links)



  


Development Specification

Ellis Miller 06/20/2024: Industries: 

[ ] Multi-select that fills in a hidden RG

[ ] We are using the readonly display memo to make sure you can see them all if multiple are selected. 

  


2 hours
