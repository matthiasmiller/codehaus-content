5.5.1. Process: Create Event Registration

  


Requirements

*Documented 

Tim Reitz 06/05/2025: This looks like a "User-Initiated" automatic process.

  


Overview: This is a process used to create a new Event Registration record from a Contact or Event record, with various fields defaulted.

  


Interfaced:

  * Via the "Add Event" link in the "Event Registration" section of the Contact record (the Contact is set on the prompt)
  * Via the "Register for Info Meeting" link in the "Lead Details" section of the Contact record (the Contact is set on the prompt)
  * Via the "Register for Launch Meeting" link in the "Lead Details" section of the Contact record (the Event and Contact name are set on the prompt)
  * Via the "Add Registrant" link in "Registration Details" section of the Event record (the Event is set on the prompt) 
  * Via the "Add Registrant" button on the "Event Registrations" report (the Event is set on the prompt screen)
  * Admin | Event Management | New Registration (menu option; all prompts set to blank) 



  


Prompts:

  * Registrant Name (drop-list of all active individual Contacts; sets the "Registrant Name" field on the new Event Registration record)
  * Event (drop-list of all Event IDs; sets the "Event" field on the new Event Registration record) 
  * Bringing Guest (drop list of blank/Yes/No; defaults to blank; sets the corresponding field on the new Event Registration record) 



  


Action(s): 

  * Creates and opens a new Event Registration record based on the set prompts.



  


Development Specification

Tim Reitz 07/04/2024: Auto-push report that launches into a new detail screen. 

  


BID: 4 Hours

  


Change Requests:

  * Tim Reitz 01/20/2025: [[[IN10946](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10948&)]] - ZSB - Events - Improvements for Creating Registrations


