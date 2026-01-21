9.8. Event Sign-In Sheet Printout

  


Requirements

Purpose/Overview: This printout is used as a sign-in sheet for Event registrants as they arrive to the event, and used for the attendees to mark their preference for post-event follow-up. 

  


Note that there is one template from which printouts for all of the Event Types are generated. 

  


Printed From: "Print Event Sign-In Sheet" link on the Event record

  


File Format/Name: 

  * PDF: "<Event Type> Sign-In - <Event ID>"



  


Fields to be included: 

  * Symbiz logo (on each page) 
  * "Welcome to the Symbiz <Event Type>!" (on the first page only) 
  * "<Event Name>" (on each page) 
  * "<Event Date in the "Month Day, Year" format>, Page <#>" (on each page)
  * "Please fill the “Signed In” checkbox next to your name. If your name is not on the list, please add it at the bottom." (on each page)



  


  * Registration table: 
    * Columns: 
      * Name (pre-filled with the names of all Registrants for the Event, based on all Event Registration records for the corresponding Event that have a Registration Status of "Attending" or "Tentative"; one row for each name; sorted in alphabetical order; in the following format: 
        * If the Registration includes a Guest: "<Registrant LastName, FirstName MiddleName> & Guest (<Registrant Organization>; <Registrant City>"); 
        * If the Registration does not include a Guest: "<Registrant LastName, FirstName MiddleName> (<Registrant Organization>; <Registrant City>")") 
      * Signed In (each cell contains an empty checkbox, for the attendee to check to confirm their attendance) 
      * Exclude from Follow-Up (column visible only if Event Type = Info Meeting; each cell contains an empty checkbox, for the attendee to check if they do not wish to be followed up with after the event) 



  


Handling Page Breaks: Break between rows in the Attendance table

  


Other Notes:

  * The Attendance table always includes 6 blank rows below the pre-filled names, to allow for unregistered attendees to sign in. 
  * Each page should fit at least 20 rows. Note that pages after the first page should have more than 20 rows, since they do not include the heading row for the Registration table.



  


Development Specification

Change Requests:

  * Tim Reitz 07/10/2025: Added in [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)


