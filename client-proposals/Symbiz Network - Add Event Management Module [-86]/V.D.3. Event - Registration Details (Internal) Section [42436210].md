5.4.3. Event - Registration Details (Internal) Section

  


Requirements

*Documented 

  


"Registration Details (Internal)" section: (visible for all Event Types; visible for Regional Reps and Super Admins): 

  


  * Registration Coordinator (required; drop list of the Default Registration Coordinator from Silverloom Settings and all active Regional Rep and Super Admin Contact records; defaults to the Default Registration Coordinator) 
  * Registration Email (required; visible if a Registration Coordinator is selected; defaults to the top primary email address for the selected Contact; editable to allow for overriding if desired)
  * Registration Phone (required; visible if a Registration Coordinator is selected; defaults to the primary phone number (the top non-Fax number for the selected Contact; editable to allow for overriding if desired)
  * View Contact (link; visible in Edit Mode if a Contact is selected in the Registration Coordinator field; opens the corresponding Contact record) 
  * Add Registrant (link; opens a new Event Registration record, in a new tab if the Event record is in edit mode, with the Event defaulted) 
  * Print Event Sign-In Sheet (link; generates the Event Sign-In Sheet Printout PDF for the event, with the appropriate conditional fields filled in, and opens it in the browser, where it can be printed or downloaded; see additional details in corresponding section of the proposal) 
  * View/Manage Event Registrations (link; opens the right pane of the Event Registrations report, with the "Event" filter set to the corresponding Event)
  * Generate Registration Export (link; generates an Excel file of the right pane of the Event Registrations Report, filtered to the current Event, to be downloaded) 
  * Generate Name Tag Export (link; generates an Excel file of the Name Tag Export Report for the Event, to be downloaded)
  * Registration Count (displays the following columns with auto-calculated and read-only totals:
    * Registrants (total number of main Registrants for the Event; displays the number of Event Registration records with this Event selected and "Registration Status" = "Tentative" or "Attending")
    * Spouses (total number of Spouses registered for the Event; displays the number of registered Guests on linked "Tentative" or "Attending" Event Registration records with Guest Type = Spouse)
    * Other Guests (total number of non-spouse guests registered for the Event; displays the number of registered Guests on linked "Tentative" or "Attending" Event Registration records with Guest Type = Other Guest)
    * Total (total number of all people registered for the Event; equals the numbers for Registrants + Spouses + Other Guests)
  * Attendance Count (located directly below Registration Count, forming an on-screen table; displays the following columns with auto-calculated and read-only totals:
    * Registrants (total number of main Registrants who attended the Event; displays the number of Event Registration records with this Event selected and "Attended" = Yes)
    * Spouses (total number of Spouses assumed to have attended the Event; displays the number of registered Guests with Guest Type = Spouse for linked Event Registration records with "Attended" = Yes)
    * Other Guests (total number of non-spouse guests assumed to have attended the Event; displays the number of registered Guests with Guest Type = Other Guest for linked Event Registration records with "Attended" = Yes) 
    * Total (total number of all attendees for the Event; equals the numbers for attended Registrants + attended Spouses + attended Other Guests)



  


Development Specification

Change Requests: 

  * Tim Reitz 02/01/2025: [[[IN11090](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11092&)]] - ZSB - Events - Make Registration Coordinator Phone & Email required 
  * 


  


Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/)

  


Ellis Miller 06/20/2024:

[ ] If we don't have a macro for ActiveRegionalRepsAndSuperAdmins, we can create one. EventRegistrationCoordinatorOptions would include these and the Default Coordinator (sorted).

[ ] For the Count macros, use a RegistrationsByEventSum(...) or a similar macro to make it easy

  


Bid: 4 hours
