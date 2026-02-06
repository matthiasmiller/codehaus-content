5.5. Event Registration Record

  


Requirements

*Documented 

  


Add the following new record / record type:

  


Overview: The Event Registration Record will be used to track registration for a linked Event. Each record will track information one Registrant and one Event.

  


Accessed via: 

  * Admin | Event Management | New Registration (opens the "New Registration prompt screen" with all prompts blank opens a new blank record)
  * Contact Record
  * Event Record
  * Event Registration Report



  


Sections and Fields:  

  


  * Add Registrant for Same Event (at the top of the screen, above the "Registration Summary (Public)" section; visible to Regional Reps and Super Admins; requires the user to save the current Event Registration record, then opens the "New Registration" prompt screen", with "Event" defaulted to the Event selected on the current record)



  


  * Registration Summary (Public) Section (visible to everyone who can see the Event record; included to allow other users to view the registration list for an Event): 
    * System ID (hidden field; auto-set and read-only; unique identifier for the record)
    * Event (auto-set and read-only; displays the Event ID selected in the "Event" field; displays as a link to the Event record)
    * Registrant (auto-set and read-only; displays the name of the Contact selected in the "Registrant Name" field; displays as a link to the Contact record) 



  


  


  * Registration Details Section (visible to the Registrant selected in the "Registrant Name" field, all uplines, and all Regional Reps):
    * Event (required; drop list of all Event IDs, sorted by Event Date + Name with the newest dates at the top; filters down as you type; warning on Save if changed after the initial Save: "The selected Event has been changed. To continue, click Continue. Otherwise, click Ignore and Save and reset the Event."; defaults to blank) 
    * View Event (link; visible in Edit mode if an Event is selected in the drop list; located to the right of or below the Event drop list; opens the corresponding Event record) 
    * Event Type (auto-set and read-only; dynamically displays the Event Type from the selected Event; not a link)
    * Event Status (auto-set and read-only; dynamically displays the Event Status from the selected Event)
    * Event Date (auto-set and read-only; dynamically displays the Event Date from the selected Event) 
    * Event Time (auto-set and read-only; dynamically displays the Event Time from the selected Event) 
    * Registration Deadline (auto-set and read-only; dynamically displays the Registration Deadline from the selected Event; see note in "Additional Validations" below about warnings after certain saves past the deadline date) 
    * Registration Status (required; drop list of Event Registration Status list items ("Attending", "Tentative", and "Canceled"); with the following additional notes:
      * defaults to "Attending";
      * if "Attended" = "Yes", this must = "Attending" \- validation error message on Save: "Registration Status must set to Attending.";
      * can be set to "Tentative" if it is uncertain if the registrant will attend, or can be changed to "Canceled" if the registrant decides to not attend after all;
      * note that this tracks the "RSVP" of the Registrant, not the actual attendance;
      * see note in "Additional Validations" below about warnings after certain saves past the deadline date) 
    * Attended (drop list of blank/Yes/No; defaults to blank; tracks the actual attendance of the Registrant; required if Event Status = Complete)



  


  


  * Registration Details (Internal) Section (visible only to Regional Reps and Super Admins):
    * Notes (optional; plain text) 
    * Lead Follow-up Completed (editable checkbox \+ date, which toggle; used to track whether someone has followed up with the Lead after the Info Meeting; with the following behaviors:
      * visible if the following are true:
        * Event Status is not Canceled 
        * Event Type = Info Meeting,
        * Registrant Type = Lead,
        * Lead Status field on the Registrant's Contact record is not "Inactive Lead";
          * note that this last item is dynamic and the checkbox disappears if the Contact's Lead Status is changed to "Inactive Lead";
      * defaults to not checked;
      * checking this checkbox automatically checks the "Follow-up Completed" checkbox on the "Lead Details" section of the Contact record for the Registrant - see corresponding spec; 
      * if the Contact becomes a Member, the checkbox does not disappear because it depends on the Registrant Type for the Registration record, which is static; 
      * if it already is checked and Lead Status is changed to "Inactive Lead", it remains checked, even though it hidden, so that reporting works correctly) 



  


  * Current Lead Status (visible if Event Type = Info Meeting or Launch Meeting and if Registrant Type = Lead; auto-set and read-only; dynamically displays the current Lead Status from the Lead's Contact record)



  


  


  * Registrant Details Section (visible to the Registrant, all uplines, and all Regional Reps): 
    * Registrant Name (required; drop list of all active Individual Contacts; when created from a Contact record, defaults to that Contact; otherwise defaults to blank; warning on Save if changed after the first Save: "The selected Contact has been changed. To continue, click Continue. Otherwise, click Cancel and reset the Contact."; validate against multiple Registrations for the same Contact and Event - error on the field: "This contact already has another Registration record for the same Event") 
    * New Lead (visible to Regional Reps and Super Admins in edit mode if Registrant Name is blank, to make it easy to add new leads who register or who were in attendance; link; opens a new Contact record with Type = Lead) 
    * View Contact (visible to the right of the Registrant Name field in Edit mode if a Registrant is selected; link to open the corresponding Contact record) 
    * Registrant Type (auto-set and read-only; displays the Contact Type / Org Role of the selected Contact (Lead, Standard Member, Facilitator, Regional Rep, Super Admin, Other Individual); used for informational tracking and KPI calculations; displays the information as of the time the contact was added to the record, and does not change here if changed on their Contact record; does not display as a link to anything) 
    * Organization Name (auto-set and read-only; sets to the top organization on the Organization table on the Contact record; displays the information as of the time the contact was added to the record, and does not change here if changed on their Contact record) 
    * Phone (auto-set and read-only; displays to the primary phone number (the top non-Fax number first phone number) for the selected Contact at the time that the Registration record was created)
    * Email (auto-set and read-only; sets to the the top primary email address for the selected Contact at the time that the Registration record was created; displays as a link to send an email)
    * Address (auto-set and read-only; sets to the primary address on the Contact record at the time that the Registration record was created; displays in the standard 2-line address format)
    * Industries (auto-set and read-only; comma-separated list of all Industries that are selected on the Registrant's Contact record at the time that the Registration record was created, in the sequence in which they are listed there) 
    * "Note: details are as of the registration date." (informational note in gray font to help clarify that all of this information is static and does not update if changed on the Contact record) 
    * Bringing Guest (required; drop list of blank/Yes/No; defaults to blank)



  


  


  * Guest Details Section (visible if Bringing Guest = Yes; otherwise hidden; visible to the Registrant, all uplines, and all Regional Reps):
    * Guest First Name (required if the section is visible; plain text field; defaults to blank; used for documenting a spouse or other guest that the registrant is bringing along) 
    * Guest Last Name (required if the section is visible; plain text field; defaults to blank; used for documenting a spouse or other guest that the registrant is bringing along) 
    * Guest Type (required if the section is visible; drop list of blank/Spouse/Other Guest; defaults to blank)
    * Guest Organization (optional; plain text field)
    * Same as Main Registrant (checkbox; defaults to not checked; if checked, the following details are duplicated as read-only text from the corresponding fields for the main registrant's the primary address at the time that the Registration record was created: 
      * Phone
      * Email 
      * Address Line 1
      * Address Line 2
      * City 
      * State / Province 
      * Zip)
    * Guest Phone (optional; phone number field; visible if "Same as Main Registrant" checkbox is not checked)
    * Guest Email (optional; email address field; visible if "Same as Main Registrant" checkbox is not checked)
    * Guest Address Line 1 (optional; plain text field; visible if "Same as Main Registrant" checkbox is not checked)
    * Guest Address Line 2 (optional; plain text field; visible if "Same as Main Registrant" checkbox is not checked)
    * Guest City (optional; plain text field; visible if "Same as Main Registrant" checkbox is not checked)
    * Guest State / Province (optional; drop list of State and Province abbreviations; visible if "Same as Main Registrant" checkbox is not checked)
    * Guest Zip (optional; number field; visible if "Same as Main Registrant" checkbox is not checked)



  


  


  * Pre-Summit Meet & Greet Section (visible if Event Type = Annual Summit; visible to the Registrant, all uplines, and all Regional Reps):
    * Registrant Attending M & G (required; drop list of blank / Yes / No; defaults to blank)
    * Guest Attending M & G (visible and required if Bringing Guest = Yes; drop list of blank / Yes / No; defaults to blank)



  


  


Additional Validations: 

  * Warning on the first Save after both of the following are true: (1) Registration Deadline is in the past and (2) the Registration Status was just set to "Attending" from something else: "The registration deadline is in the past, but you can still submit the registration."
  * Warning on Save if changes are made to any field other than "Attended", "Notes", and "Lead Follow-up Completed" when the Event Status of the linked Event = Complete or Canceled: "You are about to save changes to a registration for a <Complete / Canceled> Event. Are you sure you want to continue?" 



  


  


Data Access:

  * See Data Access Controls section and the sections/fields spec for details.
  * Summary:
    * Fully visible and editable for Regional Reps and Super Admins.
    * Some fields visible for the selected Member.  
    * Very basic information visible to all Standard Members (to allow them to see who is registered for a Public or "All Members"



  


  


Special Considerations: 

  * Copy Record: N/A (prevent copying) 
  * Delete Record: Prevent deletion if "Registration Status" is not "Canceled"
  * Merge Record: N/A



  


  


Other Notes:

  * Note that at some point data access controls could be changed to allow members (and even non-members) to register themselves and edit their own Registrations. 
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

  * Lead Follow-up Completed (editable checkbox \+ date, which toggle; used to track whether someone has followed up with the Lead after the Info Meeting; with the following behaviors:...



_VA: Tim Reitz 12/10/2024: update this spec, somewhat based on the screenshot. But: checkbox + date are editable and toggle. 

TODO_VA: Tim Reitz 12/10/2024: Is the corresponding checkbox on the Contact record visible to the member? (once they convert to a member) 

TODO_EM: If yes, does the visibility here affect the visibility there? 

  


  


Change Requests:

  * Tim Reitz 01/20/2025: [[[IN10946](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10948&)]] - ZSB - Events - Improvements for Creating Registrations 
  * Tim Reitz 02/01/2025: [[[IN10958](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10960&)]] - ZSB - Events - Registration Record - "Event Type" Link 
  * Tim Reitz 03/29/2025: [[[IN11104](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11106&)]] - ZSB - Events - Registration Record - "Add Registrant for Same Event" Link
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=2018481079](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=2018481079) 

  


  


Ellis Miller 06/21/2024: 

[ ] For visibility of most sections, consider something like EventRegistrationCanViewDetails (registrant and uplines)

[ ] For visibility of internal sections, consider something EventRegistrationCanViewInternalFields (Super Admin and Regional Reps)

  


  


Registration Summary (Public)

1 Hour

  


Registration Details

[ ] Warning when changing event for existing registration- not super complex but a bit of work

[ ] Lead Follow-up Completed

[ ] Add a macro EventRegShowLeadFollowupCompleted -- returns true if the checkbox should be visible

[ ] Use a stored EventRegStoredLeadFollowupCompleted boolean field

[ ] Add a macro EventRegIsLeadFollowupCompleted that is a YesNo list macro. It returns an empty string if the event is not an info meeting. Otherwise it returns Yes if NOT EventRegShowLeadFollowupCompleted OR EventRegStoredLeadFollowupCompleted . So if the linked lead becomes a member, the macro returns changes to Yes since followup is completed. This makes so it will be correct in reports. 

Tim Reitz 11/04/2024: Visibility condition: EventType is "Info Meeting" AND LinkedEvent NOT Canceled AND RegistrantType is Lead AND LinkedContact's LeadStatus <> "Inactive" 

Tim Reitz 11/04/2024: Other notes: 

  * If the contact becomes a member, the checkbox does not disappear because it's looking at the RegistrantType (which is static). 
  * If it already is checked, and Lead Status is changed to "Inactive Lead", I think we want it to stay checked, even if it's hidden. That way reports work correctly. 



  


4 Hours

  


Registration Details

[ ] Warning when changing name for existing registration.

[ ] Registrant Type -- this should be a stored field that is set when you select a contact. Same for other snapshot fields that don't change.

6 Hours

  


Guest Details

[ ] "Same as Main Registrant" will set a SameAsMain 

Tim Reitz 04/29/2024: When checking the "Same as Main Registrant" checkbox: Use an expression that either pulls from the contact record or is stored here. If the checkbox is checked, the Guest contact fields will be replaced by read-only macros that display the corresponding details from the main registrant.

2 Hours

  


Meet & Greet

1 hour

  


Special Considerations

1 hour
