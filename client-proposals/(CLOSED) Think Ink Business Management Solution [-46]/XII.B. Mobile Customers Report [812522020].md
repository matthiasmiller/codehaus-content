12.2. Mobile Customers Report

  


Requirements

Options: 

  * AppSheet 
    * CCI could give exports for Incidents (which has Contact and the custom Customer Details section), and maybe set up a Scheduled Task to export it periodically (or on demand). 
    * Process: 
      * Export all Open Incidents from the Solution as an Excel file (directly to Google Drive if able; otherwise to email) 
      * Sync spreadsheet to AppSheet 
      * Use AppSheet to view incident/customer information, make calls, open addresses, etc.
      * Probably would NOT be editing the incidents in AppSheet
    * Jesse is willing to make the app with AppSheet in-house
  * Simple report: [https://demo.apphosting.zone/Reports/User/Personal/Matthias.Miller/Mobile_Address_Mockup?View=Settings&State=iy1lGoiokl4&](https://demo.apphosting.zone/Reports/User/Personal/Matthias.Miller/Mobile_Address_Mockup?View=Settings&State=iy1lGoiokl4&) . 
  * 


  


  


  


TODO_IDD: If we go forward with the AppSheet, we'll need to spec out an Incidents export (and a basic procedure for using it) and this report will go away. OR, if we go with the simple report that Matthias mocked up we should update below to match. 

  


  


  


This is a custom basic report of customers that should make mobile use easier.

  


This would be accessed from a "Mobile Customers Report" menu option on the Home Menu. 

  


Title: Mobile Customers Report

  


Columns: 

  * Customer Name (link to record)
  * Phone (phone number; tap to dial)
  * Email (email; tap to email)
  * Google Maps (display "Link"; links to open the customer's address in the Google Maps App)



  


Grouped by: Active (at top), Inactive 

  


Sorted by: Customer Name

  


Filters: 

  * Name (text field; ignore punctuation in results) 
  * Sales Rep (default to current user) 



  


Buttons: N/A

  


Menu Visibility: All users  

  


Other Notes:

  * This whole report needs to be narrow enough to display on a phone screen.



  


Development Specification

Mockup:[https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=883257779](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=883257779)

Austin Priest 06/10/2022: I mocked up two options here. TODO_TR You could review this.

  


  


DONE_CH: Tim Reitz 06/09/2022: The guy who does a lot of the work on the road is hesitant to give up Badger. Jesse is wondering again what options we have for mobile use - integration with Badger, mobile app for using AHZ, etc. Jesse's preference is to replace Badger (to avoid double entry, etc.). Thoughts?

Tim Reitz 06/09/2022: Jesse asked if I was familiar with AppSheet ([https://about.appsheet.com/home/](https://about.appsheet.com/home/)). Maybe we could push the Mobile Contacts report to a Google Sheet that's linked to AppSheet??? Maybe we could use AppSheet for checkins somehow and push that back into the Solution via an export/import???

Matthias Miller 06/14/2022: DONE_JM:

  * Does he need to create new incidents?
  * Does he need to edit existing text on incidents?
  * Or does he just need to append text to incidents?
  * Or do they want to build out a fully-custom mobile interface as a Badger replacement?



Example interface could be:

  * Click into a contact to see a list of incidents. Clicking the incident opens a prompt with "New Comments" (plain text). The list of incidents also has a New Incident button that prompts for a title and automatically assigns it to the sales person + contact. It also has a Comments text box (plain text)



I would really, really prefer not to hold up Phase 1 for this.

DONE_CH : Tim Reitz 06/15/2022: Talked with the client today.

  * He thinks that accessing the name, phone, and address is the most important.
    * He might show the screenshot of Matthias' mobile report ([https://demo.apphosting.zone/Reports/User/Personal/Matthias.Miller/Mobile_Address_Mockup?View=Settings&State=iy1lGoiokl4&](https://demo.apphosting.zone/Reports/User/Personal/Matthias.Miller/Mobile_Address_Mockup?View=Settings&State=iy1lGoiokl4&)) to his team
    * But at this point he's thinking they probably won't do anything for mobile in the Solution at this point (other than the export - see below)
  * Entering notes, creating new incidents, etc., could be done with a tablet.
  * He thinks that AppSheet would give them what they want, or at least a basic version of it. He made a basic app with that the other day, and found it to be really simple and handy.
    * We could give exports for Incidents (which has Contact and the custom Customer Details section), and maybe set up a Scheduled Task to export it periodically (or on demand). 
    * Process: 
      * Export all Open Incidents from the Solution as an Excel file (directly to Google Drive if able; otherwise to email) 
      * Sync spreadsheet to AppSheet 
      * Use AppSheet to view incident/customer information, make calls, open addresses, etc.
      * Probably would NOT be editing the incidents in AppSheet
    * He is willing to make the app with AppSheet in-house



TODO_CCI: Matthias/Ellis, what are your thoughts? 

Matthias Miller 06/15/2022: I'm a little sad to see him going outside our ecosystem, but it is the only way that he's going to get a native app. It might not be terrible to implement an OData provider via WSGI that would allow pulling information from the AHZ system into AppSheet. See [https://pyslet.readthedocs.io/en/latest/odatav2/provider.html](https://pyslet.readthedocs.io/en/latest/odatav2/provider.html)

  


  


Matthias Miller 06/09/2022: 

[https://demo.apphosting.zone/Reports/User/Personal/Matthias.Miller/Mobile_Address_Mockup?View=Settings&State=iy1lGoiokl4&](https://demo.apphosting.zone/Reports/User/Personal/Matthias.Miller/Mobile_Address_Mockup?View=Settings&State=iy1lGoiokl4&)

Tim Reitz 06/13/2022: Possibly this?

TODO_JM

  


The next question is whether they want to give up formatting to be able to edit notes on mobile. We can possibly push them into a child screen with editable expressions -- but not sure if that gets too complicated. The other options is an X30 that defaults the values to the current record, allows you to edit, then pushes the values back onto the record.

Matthias Miller 06/14/2022: See above comments

  


Ellis Miller 06/14/2022: Name search. Split on spaces and search first name, last name, and contact override.

  


  


HL Est: 6 Hours
