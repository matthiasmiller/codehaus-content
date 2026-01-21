5.2.2. Changes to Contact - Lead Details Section

  


Requirements

*Documented 

  


Make the following changes to the existing custom Lead Details section of the Contact record (changes indicated with blue / strike-through):

  


  * Lead Details section (visible if Contact Type = Lead or Member, or if there is a Lead Status set; visible to and editable for Regional Reps and Super Admins): 
    * Lead Status (required; drop list of Lead Status items - see corresponding section of the proposal; note that automation could eventually be added to set this based on items like a linked Info Meeting, etc.) 
    * Lead Source (required; drop list of Lead Source items - see corresponding section of the proposal)
    * Initial Conversation (checkbox and date; date defaults to current date when the checkbox is checked, clears when the checkbox is unchecked; both editable only by Super Admin; read-only if "Initial Payment Received" checkbox is filled) 
    * Info Packet Requested (checkbox and date; same behavior as the "Initial Conversation" checkbox) 
    * Info Packet Sent (checkbox and date; same behavior as the "Initial Conversation" checkbox) 
    * Info Meeting Invite Sent (checkbox and date; same behavior as the "Initial Conversation" checkbox) 
    * Attending Info Meeting (checkbox; for Phase 1, this is for reference only, but in the future this could be used to link leads with an Info Meeting that they attended)
    * Info Meeting (auto-set and read-only; with the following behaviors: 
      * if there is one (and only one) Event Registration for a non-canceled Info Meeting for this Contact with "Registrant Type" = "Lead": Displays the Event ID as a link to open the corresponding record; 
      * if there are Event Registrations for multiple non-canceled Info Meetings for this Contact with "Registrant Type" = "Lead": Displays a link with the corresponding number of Info Meeting-type Events ("<#> Info Meetings") to open the Info Meetings by Contact Report for the Contact;
      * otherwise (i.e., if there are no Event Registration records for non-canceled Info Meeting-type Events for this Contact with "Registrant Type" = "Lead"):
        * if the Contact record's current Contact Type = Lead: Displays a "Register for Info Meeting" link, which opens a new Event Registration record, in a new tab if the Contact record is in Edit mode, with "Registrant Name" defaulted; 
        * if the Contact record's current Contact Type ≠ Lead: Displays "No Info Meetings as Lead" in gray text)
    * Attended Info Meeting (checkbox and date; auto-set and read-only; with the following behaviors:
      * becomes checked if there is an Event Registration for this Contact, with "Registrant Type" = "Lead" and "Attended" = "Yes", for a non-canceled Info Meeting with Event Date in the past;
      * date sets to the Event Date for the linked Info Meeting;
      * if there is more than one Registration, looks at the most recent Info Meeting) 
    * Follow-up Completed (checkbox and date; auto-set and read-only; with the following behaviors:
      * if there is at least one Event Registration for this Contact, with "Registrant Type" = "Lead", for a non-canceled Info Meeting with Event Date in the past: Mirrors the current state of the "Lead Follow-up Completed" checkbox on the Registration record;
        * if there is more than one Registration, looks at the most recent Info Meeting
      * otherwise (i.e., if no Event Registration exists as described above): Remains blank) 
    * Register for Launch Meeting (link; visible if the Contact record's Contact Type = Lead and the Contact has no Event Registration for a non-canceled Launch Meeting; opens a new Event Registration record, in a new tab if the Contact record is in Edit mode, with the following fields set: 
      * Event: 
        * if there is at least one Event Registration for this Contact, with "Registrant Type" = "Lead", for a non-canceled Info Meeting with Event Date in the past: Sets to the linked Launch Meeting (if there is one) for the most recent Info Meeting (if there is more than one); 
        * otherwise: Sets to blank;  
      * Registrant Name: Sets to the Contact's Name)
    * Application Approved (checkbox + date; date defaults to current date when the checkbox is filled, clears when the checkbox is cleared; both editable only by Super Admin; when this checkbox is filled, automatically set Contact Type to "Member"; when the checkbox is cleared, automatically set the Contact Type back to "Lead" with a warning message on the field: "Clearing this checkbox changes the Contact Type from Member back to Lead, and will cause member details to be lost. To cancel, refresh the page without saving the changes."; becomes read-only when "Initial Payment Received" checkbox is filled) 
    * Lead Notes (memo)



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=873949625](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=873949625)

  


  


Ellis Miller 06/20/2024:

[ ] NOTE: Everything in this section should only be visible to Regional Rep or SuperAdmin. Compare to visibility in member section.

[ ] 4 checkboxes+dates on top right (Initial Conversation on down) -- farily simple logic, could compare to behaviors of "Initial Invoice Sent" in Member section. 4 Hours

[ ] Info Meeting Link. 4-6 hours

[ ] Create a ContactLeadInfoMeetingCount that counts the number of Info meetings they are registered at with a Registration Type = "Lead". I think we only count non-cancelled mtgs.

[ ] If no registrations and Contact Type = "Lead", use a modified Add Event link

[ ] If one registration, show a link to an Auto-push Open Info Meeting for Contact report (shows info meeting column in case somehow run with multiple meetings and has required prompt for Contact)

[ ] If multiple ones, run the Event Registrations report with "Info Meetings by Contact" parameters. 

[ ] 2 checkbox macros looking at other records. Add a ContactLeadLatestInfoMeetingID that returns the EventID for the latest non-canceled InfoMeeting where the RegistrationType is Lead. 2 hours

[ ] Register for Launch Meeting - auto-push into a new Event Detail, filling in the Launch Meeting ID if we have it, the Contact Name and the Registration Status. 4 Hours

[ ] Application Approved.  2-4 hours
