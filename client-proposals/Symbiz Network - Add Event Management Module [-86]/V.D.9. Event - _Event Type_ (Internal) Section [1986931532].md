5.4.9. Event - <Event Type> (Internal) Section

  


Requirements

*Documented 

  


"<Event Type> (Internal)" section (visible if Event Type = Industry Forum, Info Meeting, or Launch Meeting; section label conditionally includes the Event Type for the selected Type; visible to Regional Reps and Super Admins):

  


General fields (always included by default or according to the configuration of the Event Type):

  * Region (visible if the selected Event Type has the "Displays Region & Rep" checkbox checked; optional; drop list of Regions; defaults to blank) 
  * Regional Rep (visible if the selected Event Type has the "Displays Region & Rep" checkbox checked; auto-set and read-only; displays the Rep for the selected Region) 
  * Symbiz Presenter (required if Event Status = "Scheduled" OR "Complete"; drop list of all active Contacts) 
  * View Contact (link; visible in Edit Mode if a Contact is selected in the Symbiz Presenter field; opens the corresponding Contact record)
  * Additional Presenters (optional; multi-select drop list of all active Contacts except the selection in the Symbiz Presenter field if there is one, in alphabetical order; defaults to blank; if a selection is made in Symbiz Presenter that matches a selection in this field, the corresponding selection in this field is cleared, to avoid having the same person as both the main Presenter and an Additional Presenter) 
  * Event Host (optional; drop list of all active Contacts; defaults to blank; used to track the individual or organization who is "hosting" the Event) 
  * View Contact (link; visible in Edit Mode if a Contact is selected in the Event Host field; opens the corresponding Contact record)
  * Host Phone (auto-set and read-only; displays the primary phone number (the top non-Fax number on the Contact record) for the selected Event Host)
  * Host Email (auto-set and read-only; displays the top primary email address for the selected Event Host; displays as a link to send an email)
  * Event Notes (memo; can be used for attaching documents and links)



  


  


Industry Forum fields: No internal Industry Forum-specific fields at this point. 

  


  


Info-Meeting fields:

  * Set Up Launch Meeting (link; visible if Event Type = Info Meeting and if there is no Linked Launch Meeting; clicking this prompts the user to save the current record, then creates a new Launch Meeting-type Event record with the "Linked Info Meeting" field defaulted to the current record, which also copies/sets relevant fields as specified in the Launch Meeting section; note that a special button on the new Launch Meeting record will allow for setting up the registrations - see corresponding spec): 
  * Linked Launch Meeting (link; visible if Event Type = Info Meeting and if there is a Launch Meeting with this Info Meeting set in its "Linked Info Meeting" field; auto-set and read-only; displays the Event ID for the Launch Meeting linked to this Info Meeting)



  


  


Launch Meeting fields:

  * Linked Info Meeting (visible if Event Type = Launch Meeting; optional; drop list of Info Meeting-type Event records that are not already linked to a Launch Meeting; when the Launch Meeting is created from an Info Meeting, this defaults accordingly, otherwise defaults to blank; when this field is set, the below fields are defaulted, overriding any existing values in those fields; when out of edit mode, this is a link to open the corresponding Info Meeting; warning on the field if changed from a non-blank value: "You have changed the linked Info Meeting. If this was a mistake, change it back or refresh the page.")
    * Defaulted fields:
      * Time Zone = same as Info Meeting
      * Event Format = same as Info Meeting
      * Venue = same as Info Meeting
      * Address fields = same as Info Meeting
      * Region = same as Info Meeting 
      * Symbiz Presenter = Regional Rep of Info Meeting 
      * Event Host = same as Info Meeting
  * View/Edit Info Meeting (link; visible in Edit mode if Event Type = Launch Meeting and if an Info Meeting is selected; located to the right of the "Info Meeting" field; opens the corresponding Info Meeting in a new tab)
  * Create Registrations from Info Meeting (button; visible after the record has been saved the first time if Event Type = Launch Meeting and if an Info Meeting is selected; hidden if all registrants for the Linked Info Meeting have a Registration record for the Launch Meeting; clicking this button runs the "Create Registrations from Info Meeting" automatic process that looks for registrants from the Info Meeting that don't already have Registration records for the Launch Meeting, and creates Registration records for them - see details in the automatic process spec)
  * Create New Group (link; visible if Event Type = Launch Meeting; creates a new Growth Ring Group record with the various fields defaulted - see the corresponding section of the proposal; opens a new tab if in edit mode; note that if multiple Groups need to be created, the user can use the "Ctrl + Click" keyboard shortcut to open multiple new tabs)
  * View <X> Linked Group(s) (link; visible if Event Type = Launch Meeting and there is at least one linked group; includes the number of Growth Ring Groups that have the Linked Info Meeting set in their "Info Meeting" field; opens the "Growth Ring Groups by Info Meeting" report, filtered to the Linked Info Meeting; note that the Solution does not need to track which Launch Meeting a Group came from)



  


Development Specification

Change Requests:

  * Tim Reitz 02/01/2025: [[[IN10960](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10962&)]] - ZSB - Events - Misc. Changes from 1/13/25 Client Walkthrough
  * 


  


  


_EM: Tim Reitz 07/01/2024: Do we need to include a checkbox on the Event Type to include this whole "<Event Type> (Internal)" section? I would say it could be included for all Types, but I don't think it would go in the Annual Summit Type.

TODO_VA: Tim Reitz 07/04/2024: 

[ ] Have this section always visible for all Event Types, including the Summit. 

[ ] Remove the existing (empty) Summit section 

[ ] Add checkboxes for all the Presenter and Host fields (to exclude from the Summit)

Tim Reitz 06/28/2025: Moved these notes to the main living spec for future reference. 

  


  


TODO_: Tim Reitz 07/03/2024: Look at adding an "Additional Hosts" multi-select drop list. 

TODO_JS: Tim Reitz 07/04/2024: But maybe this actually was supposed to be for Presenters, not Hosts (I think the client requested it for Presenter, but my notes said Hosts). Sent an email to the client to confirm, but I'm going ahead with the Presenter spec. 

_EM: Tim Reitz 07/04/2024: Are you fine with adding this now, or should we save it for a CR later? I think this would have the same behavior as the Assignee and Additional Assignee fields on ZCH incidents (so the devs probably could copy details from those??)

TODO_VA: Tim Reitz 07/04/2024: Ellis is fine with this idea, but let's leave a note for him to clean up the spec. Ellis is considering interfacing this as an RG so that we can also have notes fields, etc., for each presenter.

Columns:

  * Name
  * Phone
  * Email
  * Notes
  * Primary? 



Tim Reitz 06/28/2025: This apparently didn't happen -- I guess we backburnered this for a while, and then I/we didn't follow up on todo's after the client accepted. Today I wrote up [[[IN11656](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11658&)]] - ZSB - Event Record - Add RG for Presenters. 

  


  


Info Meeting fields (from the previous separate Info Meeting section):

Ellis Miller 06/20/2024:

[ ] Main fields and macros. 2 hours

[ ] Set up Launch Meeting: Auto-push report that opens a new detail screen, setting the EventType="Launch Meeting" and setting EventLaunchMeetingLinkedInfoMeetingID = vAskOrigInfoMeetingID. 1 Hour

[ ] Create a EventInfoMeetingLinkedLaunchMeetingID macro that uses the LaunchMeetingsByInfoMeetingID.ndx to determine the linked LaunchMeetingID. You will use this to determine whether you show the "Set Up Launch Meeting" or "Linked Launch Meeting". You will pass this into the LinkedLaunchMeeting. 1 Hour

  


Launch Meeting fields (copied from the previous separate Launch Meeting section): 

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
