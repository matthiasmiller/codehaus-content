7.10. Event Registration Record

  


Requirements

Overview: The Event Registration Record will be used to track registration for a linked Event. Each record will track information one Registrant and one Event.

  


Accessed via: 

  * Admin | Event Management | New Registration (opens the "New Registration prompt screen" with all prompts blank opens a new blank record)
  * Contact Record
  * Event Record
  * Event Registration Report



  


Sections and Fields: See the corresponding sub-sections below

  


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

Change Requests:

  * Tim Reitz 06/04/2025: Added in [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)
  * Tim Reitz 01/20/2025: [[[IN10946](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10948&)]] - ZSB - Events - Improvements for Creating Registrations 
  * Tim Reitz 02/01/2025: [[[IN10958](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10960&)]] - ZSB - Events - Registration Record - "Event Type" Link 
  * Tim Reitz 03/29/2025: [[[IN11104](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11106&)]] - ZSB - Events - Registration Record - "Add Registrant for Same Event" Link
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=2018481079](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=2018481079)
