11.0.4. **Event - Info Meeting (Internal) Section

  


Requirements

_VA: Archive once we have these sections settled.

  


Info Meeting (Internal) section: (visible if Event Type = Info Meeting; visible for Regional Reps and Super Admins) 

  


  * Info Mtg. Presenter (required; drop list of all Regional Reps and Super Admins)
  * View Contact (link; visible in Edit Mode if a Contact is selected in the Info Mtg. Presenter field; opens the corresponding Contact record)
  * Region (visible if the selected Event Type has the "Displays Region & Rep" checkbox checked; optional; drop list of Regions; defaults to blank) 
  * Regional Rep (visible if the selected Event Type has the "Displays Region & Rep" checkbox checked; auto-set and read-only; displays the Rep for the selected Region) 
  * Info Mtg. Organizer (optional; drop list of all active Contacts; defaults to blank; used to track the individual or organization who is "hosting" the Info Meeting) 



_VA: Tim Reitz 06/21/2024: Consider putting this in the Planning Details section and moving the Launch Mtg Organizer there too.  

Ellis Miller 06/21/2024: Or perhaps combining the Type-specific sections into one section that looks like 3 sections and reusing fields when possible. 

Tim Reitz 07/01/2024: Done in combined section. 

  * View Contact (link; visible in Edit Mode if a Contact is selected in the Info Mtg. Organizer field; opens the corresponding Contact record)
  * Organizer Phone (auto-set and read-only; displays the top phone number for the selected Organizer)
  * Organizer Email (auto-set and read-only; displays the top primary email address for the selected Organizer; displays as a link to send an email)
  * Event Notes (memo; can be used for attaching documents and links) 
  * Set Up Launch Meeting (link; visible only if there is no linked Launch Meeting; clicking this prompts the user to save the current record, then creates a new Launch Meeting-type Event record with the "Linked Info Meeting" field defaulted to the current record, which also copies/sets relevant fields as specified in the Launch Meeting section; note that a special button on the new Launch Meeting record will allow for setting up the registrations - see corresponding spec): 
  * Linked Launch Meeting (link; auto-set and read-only; visible if there is a linked Launch Meeting; displays the Meeting ID for the Launch Meeting linked to this Info Meeting)



  


Development Specification

Ellis Miller 06/20/2024:

[ ] Main fields and macros. 2 hours

[ ] Set up Launch Meeting: Auto-push report that opens a new detail screen, setting the EventType="Launch Meeting" and setting EventLaunchMeetingLinkedInfoMeetingID = vAskOrigInfoMeetingID. 1 Hour

[ ] Create a EventInfoMeetingLinkedLaunchMeetingID macro that uses the LaunchMeetingsByInfoMeetingID.ndx to determine the linked LaunchMeetingID. You will use this to determine whether you show the "Set Up Launch Meeting" or "Linked Launch Meeting". You will pass this into the LinkedLaunchMeeting. 1 Hour
