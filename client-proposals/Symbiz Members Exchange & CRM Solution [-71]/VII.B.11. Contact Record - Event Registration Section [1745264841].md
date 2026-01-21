7.2.11. Contact Record - Event Registration Section

  


Requirements

  * Event Registration custom section (with the following visibility & editability conditions:  
    * Included if: the Contact is an individual (i.e. if the "Organization" checkbox is not checked) 
    * Visible to: the linked user (if applicable) and all uplines 
    * Editable for: Regional Reps and Super Admins) 



  


  * Event Registrations (read-only embedded spreadsheet of all Event Registration records that are linked to this Contact; with the following:) 
    * Columns: 
      * Event Type
      * Industry (set if Event Type filter = Industry Forum; otherwise blank)
      * Event (displays the Event Name) 
      * View Event (link to open the corresponding Event record; displays as "Link") 
      * Execution Status (visible only to Regional Reps and Super Admins)
      * Date 
      * Time
      * Time Zone
      * Virtual Event (Yes / No)
      * In-Person Event (Yes / No)
      * View Registration (link to open the corresponding Event Registration record; displays as "Link")
    * Automatically sorted by: Event Date, then Event Time
    * Buttons to insert/append/remove rows: N/A
    * Show 6 rows without scrolling 
  * View My Registrations Report (link; opens the "Registrations by Contact" report, displaying all Event Registrations for the Contact) 
  * Add Event (link; visible to Regional Reps and Super Admins; opens a new Event Registration record, in a new tab if the Contact record is in Edit mode, with the registrant Name defaulted to the current Contact)



  


Development Specification

Change Requests:

  * Tim Reitz 06/04/2025: [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)
  * 


  


Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=873949625](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=873949625)

  


  


Tim Reitz 05/01/2024: Event Registrations is a virtual RG.
