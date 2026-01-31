11.0.5. **Event - Launch Meeting (Internal) Section

  


Requirements

_VA: Archive once we have these sections settled. 

  


Launch Meeting (Internal) section (visible if Event Type = Launch Meeting; visible only to Regional Reps and Super Admins) 

  


  * Linked Info Meeting (optional; drop list of Info Meeting-type Event records that are not already linked to a Launch Meeting; when the Launch Meeting is created from an Info Meeting, this defaults accordingly, otherwise defaults to blank; when this field is set, the below fields are defaulted, overriding any existing values in those fields; when out of edit mode, this is a link to open the corresponding Info Meeting; warning on the field if changed from a non-blank value: "You have changed the linked Info Meeting. If this was a mistake, change it back or refresh the page.")
    * Time Zone = same as Info Meeting
    * Event Format = same as Info Meeting
    * Venue = same as Info Meeting
    * Address fields = same as Info Meeting
    * Region = same as Info Meeting 
    * Symbiz Assignee = Regional Rep of Info Meeting 
    * Launch Mtg Organizer = same as Info Meeting
  * View/Edit Info Meeting (link; visible in Edit mode to the right of the "Info Meeting" field if an Info Meeting is selected; opens the corresponding Info Meeting in a new tab)
  * Create Registrations from Info Meeting (button; visible after the record has been saved the first time; hidden if all registrants for the linked Info Meeting have a Registration record for the Launch Meeting; clicking this button runs the "Create Registrations from Info Meeting" background process that looks for registrants from the Info Meeting that don't already have Registration records for the Launch Meeting, and creates Registration records for them - see details in the background process spec)
  * Symbiz Assignee (required if Status = "Scheduled"; drop list of Regional Reps and Super Admins; defaults to the Regional Rep for the Info Meeting; this is the person responsible for heading up the Launch Meeting)  
  * View Contact (link; visible in Edit Mode if a Contact is selected in the Symbiz Assignee field; opens the corresponding Contact record)
  * Region (visible if the selected Event Type has the "Displays Region & Rep" checkbox checked; optional; drop list of Regions; defaults to blank) 
  * Regional Rep (visible if the selected Event Type has the "Displays Region & Rep" checkbox checked; auto-set and read-only; displays the Rep for the selected Region) 
  * Launch Mtg. Organizer (optional; drop list of all active Contacts; defaults to blank; when created from an Info Meeting, defaults to match the Info Mtg. Organizer, otherwise defaults to blank; used to track the individual or organization who is "hosting" the Launch Meeting, which might not always be the same as the Info Mtg. Organizer) 



 Ellis Miller 06/21/2024: _VA: Consider changing to "Organizer".

Tim Reitz 07/01/2024: Done in combined section

  * View Contact (link; visible in Edit Mode if a Contact is selected in the Launch Mtg. Organizer field; opens the corresponding Contact record)
  * Organizer Phone (auto-set and read-only; displays the top phone number for the selected Organizer)
  * Organizer Email (auto-set and read-only; displays the top primary email address for the selected Organizer; displays as a link to send an email)
  * Event Notes (memo; can be used for attaching documents and links) 
  * Create New Group (link; visible if Event Type = Launch Meeting; creates a new Growth Ring Group record with the below fields defaulted; opens a new tab if in edit mode; note that if multiple Groups need to be created, the user can use the "Ctrl + Click" keyboard shortcut to open multiple new records in separate new tabs;  
    * Defaulted fields:
      * Growth Ring Group ID: Defaults to blank, but is required to save the new record 
      * Region: Sets to the Region set on the Info Meeting linked to the Launch Meeting 
      * Regional Rep: Sets based on the Region
      * Info Meeting: Sets to the Info Meeting ID for the Info Meeting linked to the Launch Meeting
  * View <X> Linked Group(s) (link; includes the number of Growth Ring Groups that have the linked Info Meeting set in their "Info Meeting" field; opens the "Growth Ring Groups by Info Meeting" report, filtered to the linked Info Meeting; note that the Solution does not need to track which Launch Meeting a Group came from)



  


Development Specification

Ellis Miller 06/20/2024: 

[ ] Linked Info Meeting: Helper List: Let's create an EventsByType.ndx and then use EventsByTypeNdxConcat, filtering out only Info Meetings that don't have linked Launch Meetings

[ ] The EventLaunchMeetingLinkedInfoMeetingID field will have OnChange statements to copy in the 6 bulleted fields as well:

OnChange: EventTimeZone = EventField( NewDetailValue, EventTimeZone)

...

Create an index of LaunchMeetingsByInfoMeetingID.ndx

2 Hours

  


[ ] For "Create Registrations from Info Meeting" visibility -- a EventLaunchMtgHasMissingRegistrations (or LaunchMeetingEventHasMissingRegistrations) that looks at the registrations for the linked Info Mtg and compares to the registrations for this Launch. Consider having an index of EventID + ContactID or ContactID + EventID to make this faster. The link runs the x30 in the next section. 2 hours.

  


[ ] various fields 2 hours

[ ] Create New Group - Auto-push into detail screen. 1 hour

[ ] View <X> Linked Groups -- use GrowthRingGroupsByInfoMeetingID.ndx 1 hour
