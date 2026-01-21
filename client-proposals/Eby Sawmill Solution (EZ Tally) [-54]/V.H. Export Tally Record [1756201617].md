5.8. Export Tally Record

  


Requirements

Overview: The Export Tally is used to track the details of a container load of logs that is linked to a Booking record.

  


Export Tallies normally would be created via the AppHosting Solution on the desktop, but can also be created via the app in the yard.

  


Accessed via: 

  * Export Tallies Report 
  * Export Tallies by Booking Report



  


Sections (see corresponding subsections for details):

  * Export Tally Details section: 
  * Logs section
  * Load Details section:



  


Data Access:

  * View for: Users with the View Export Tallies and Bookings permission
  * Edit for: 
    * If the Status = Open or Confirmed (specifically if the Loaded checkbox is clear): Users with the Edit Open/Confirmed Export Tallies permission
    * If the Status = Loaded or Closed (specifically if the Loaded checkbox is filled): Users with the Edit All Export Tallies permission
  * Delete for: Users with the Edit All Export Tallies permission



  


Validations: 

  * If an Administrator edits a Loaded or Closed record, show a warning on Save.
    * Validation message: "You are about to save changes to a Loaded or Closed Export Tally, which may result in data discrepancies."



  


Other Notes:

  * Export Tally Statuses:
    * "Open": if the Confirmed checkbox is not filled
    * "Confirmed": if the Confirmed checkbox is filled
    * "Loaded": if the Loaded checkbox is filled
    * "Closed": if the Invoiced checkbox is checked for the corresponding Booking
  * Note that this record should have a name, date, and time stamp for Created and Last Modified.



  


Development Specification

Mockup:

  * Google Sheets: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=292963076](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=292963076)



  


  * Designer: [https://zch.apphosting.zone/Reports/Standard/Designer/Std_Preview_Database_Level?Asks=AskParentID%3D73&SinglePane=true&State=Tr1GcI4u7tA](https://zch.apphosting.zone/Reports/Standard/Designer/Std_Preview_Database_Level?Asks=AskParentID%3D73&SinglePane=true&State=Tr1GcI4u7tA)



  


  


Ellis Miller 12/20/2022:

[ ] Custom DB Level

[ ] Basic record, editability, and status. No sections. 2 HOURS

[ ] Use "Loaded" field for visibility / editing.
