7.9.8. Event - <Event Type> (Internal) Section

  


Requirements

  * "<Event Type> (Internal)" section (visible if Event Type = Industry Forum, Info Meeting, or Launch Meeting; section label conditionally includes the Event Type for the selected Type; visible to Regional Reps and Super Admins): \
    * Note that at some point this could be included for Annual Summit events as well, if Summit-specific items are added. 



  


General fields (always included by default or according to the configuration of the Event Type):

  * Region (visible if the selected Event Type has the "Displays Region & Rep" checkbox checked; optional; drop list of Regions; defaults to blank) 
  * Regional Rep (visible if the selected Event Type has the "Displays Region & Rep" checkbox checked; auto-set and read-only; displays the Rep for the selected Region) 
  * Symbiz Presenter (required if Event Status = "Scheduled" OR "Complete"; drop list of all active Contacts) 
  * View Contact (link; visible in Edit Mode if a Contact is selected in the Symbiz Presenter field; opens the corresponding Contact record)
  * Additional Presenters (optional; with the following behaviors / details: 
    * multi-select drop list of all active Contacts except the selection in the Symbiz Presenter field if there is one, in alphabetical order; 
    * defaults to blank; 
    * if a selection is made in "Symbiz Presenter" that matches a selection in this field, the corresponding selection in this field is cleared, to avoid having the same person as both the main Presenter and an Additional Presenter) 
  * Event Host (optional; drop list of all active Contacts; defaults to blank; used to track the individual or organization who is "hosting" the Event) 
  * View Contact (link; visible in Edit Mode if a Contact is selected in the "Event Host" field; opens the corresponding Contact record)
  * Host Phone (read-only macro; displays the primary phone number (the top non-Fax number on the Contact record) for the selected "Event Host")
  * Host Email (read-only macro; displays the top primary email address for the selected Event Host; displays as a link to send an email)
  * Event Notes (memo; can be used for attaching documents and links)



  


  


Industry Forum fields: No internal Industry Forum-specific fields at this point. 

  


  


Info-Meeting fields:

  * Set Up Launch Meeting (visible if Event Type = Info Meeting and if there is no Linked Launch Meeting; link; with the following behaviors / details: 
    * clicking this prompts the user to save the current record, then creates a new Launch Meeting-type Event record with the "Linked Info Meeting" field defaulted to the current record, which also copies/sets relevant fields as specified in the Launch Meeting section; 
    * note that a special button on the new Launch Meeting record will allow for setting up the Registrations - see corresponding spec): 
  * Linked Launch Meeting (link; visible if Event Type = Info Meeting and if there is a Launch Meeting with this Info Meeting set in its "Linked Info Meeting" field; auto-set and read-only; displays the Event ID for the Launch Meeting linked to this Info Meeting)



  


  


Launch Meeting fields:

  * Linked Info Meeting (visible if Event Type = Launch Meeting; optional; drop list of Info Meeting-type Event records that are not already linked to a Launch Meeting; with the following additional behaviors / details: 
    * when the Launch Meeting is created from an Info Meeting, this defaults accordingly, otherwise defaults to blank; 
    * when this field is set, the below fields are defaulted, overriding any existing values in those fields: 
      * Time Zone = same as Info Meeting
      * Event Format = same as Info Meeting
      * Venue = same as Info Meeting
      * Address fields = same as Info Meeting
      * Region = same as Info Meeting 
      * Symbiz Presenter = Regional Rep of Info Meeting 
      * Event Host = same as Info Meeting; 
    * warning on the field if changed from a non-blank value: "You have changed the linked Info Meeting. If this was a mistake, change it back or refresh the page."; 
    * when out of Edit Mode, this is a link to open the corresponding Info Meeting)
  * View/Edit Info Meeting (link; visible in Edit mode if Event Type = Launch Meeting and if an Info Meeting is selected; located to the right of the "Info Meeting" field; opens the corresponding Info Meeting in a new tab)
  * Create Registrations from Info Meeting (visible after the record has been saved the first time if Event Type = Launch Meeting and if an Info Meeting is selected; button; with the following additional behaviors / details: 
    * hidden if all registrants for the Linked Info Meeting have a Registration record for the Launch Meeting; 
    * clicking this button runs the "Create Registrations from Info Meeting" automatic process that looks for registrants from the Info Meeting that don't already have Registration records for the Launch Meeting, and creates Registration records for them - see details in the automatic process spec)
  * Create New Group (visible if Event Type = Launch Meeting; link; with the following behaviors / details: 
    * creates a new Growth Ring Group record with the various fields defaulted - see the corresponding spec; 
    * opens a new tab if in Edit Mode; 
    * note that if multiple Groups need to be created, the user can use the "Ctrl + Click" keyboard shortcut to open multiple new tabs) 
  * View <X> Linked Group(s) (visible if Event Type = Launch Meeting and there is at least one linked Group; link; with the following behaviors / details: 
    * includes the number of Growth Ring Groups that have the Linked Info Meeting set in their "Info Meeting" field; 
    * opens the "Growth Ring Groups by Info Meeting" report, filtered to the Linked Info Meeting; 
    * note that the Solution does not need to track which Launch Meeting a Group came from)



  


Development Specification

Change Requests:

  * Tim Reitz 02/01/2025: [[[IN10960](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10962&)]] - ZSB - Events - Misc. Changes from 1/13/25 Client Walkthrough



  


TODO_: Tim Reitz 06/28/2025: If Annual Summit-specific items are added: 

[ ] Event record: Have this section always visible for all Event Types, including the Summit. 

[ ] Event Type record: Add checkboxes to include/exclude all of the Presenter and Host fields, and spec / set them appropriately for each Event Type
