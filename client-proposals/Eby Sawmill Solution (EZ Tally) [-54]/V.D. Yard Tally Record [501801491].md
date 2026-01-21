5.4. Yard Tally Record

  


Requirements

Overview: The Yard Tally record is used to store information about individual logs when they come into the yard and are purchased.

  


Accessed via: Yard Tallies Report

  


Sections (see corresponding subsections for details): 

  * Tally Info section
  * Logs section
  * Tally Summary section
  * Payments section



  


Data Access:

  * If the Status = Open or Confirmed:
    * View and edit for: Users with the Edit Open/Confirmed Yard Tallies permission
  * If the Status = Closed:
    * View only for: Users with the View Tracts, Yard Tallies, and Pulpwood Loads permission
    * View and edit for: Users with the Edit All Yard Tallies permission 
  * Delete only by: 
    * Users with the Edit All Yard Tallies permission 
    * Only if Status = Open (disallow if Status = Confirmed or Closed)



  


Validations: 

  * If an user edits a Closed record, show a warning on Save - validation message: "You are about to save changes to a Closed Yard Tally, which may result in data discrepancies."



  


Other Notes: 

  * Note that this record should have a name, date, and time stamp for Created and Last Modified.
  * If the Source for a Yard Tally record is changed, appropriate fields from the previous Source should be cleared.



  


Development Specification

Change Requests: 

  * Tim Reitz 06/20/2024: [[[IN10070](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10072&)]] - ZET - Yard Tally Record - Payment Linking Not Cleared when Source is Changed. Note: this includes details for fields that should be cleared when Source is changed. 
  * 


  


Mockup:

  * Google Sheets: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1013722773](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1013722773)



  


  * Designer: [https://zch.apphosting.zone/Reports/Standard/Designer/Std_Preview_Database_Level?Asks=AskParentID%3D17&SinglePane=true&State=Tr1GcI4u7tA](https://zch.apphosting.zone/Reports/Standard/Designer/Std_Preview_Database_Level?Asks=AskParentID%3D17&SinglePane=true&State=Tr1GcI4u7tA)



  


Ellis Miller 12/16/2022: 

  


BID: 

[ ] Adding Custom DB Level

[ ] Record-level editing, warnings

[ ] Status

2 HOURS
