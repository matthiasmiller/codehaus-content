5.3. Tract Record

  


Requirements

Overview: The Tract record is used to track financial and logistics details about timber tracts.

  


Accessed via: Tracts Report

  


Sections (see corresponding subsections for details):

  * Tract Details section
  * Contract Details 1 section
  * Contract Details 2 section
  * Logger Details section
  * Financial Details section
  * Notes section
  * Pulpwood Loads section
  * Prospectus Comparison section



  


Data Access:

  * View record: Visible for users with the View Tracts, Yard Tallies, and Pulpwood Loads permission
  * Edit and Delete record: For users with the Edit and Delete Tracts permission
  * Specific details: 
    * Tract Details section: Visible for users with the View Tracts, Yard Tallies, and Pulpwood Loads permission
    * Logger names: Visible for users with the View Tracts, Yard Tallies, and Pulpwood Loads permission in lists, records, etc. throughout the system (especially on Yard Tally records)
    * All other fields: Only visible to users with the Edit and Delete Tracts permission



  


Other Notes:

  * Pulpwood goes straight to a paper mill or other location, and is tracked in tons.
  * Payments schedules:
    * Owner Payments are reconciled monthly.
    * Logger Payments are reconciled weekly.
    * Adjustable Tiered Percentage-based Landowner payments are settled on a monthly schedule.
    * Flat Rate Date-based Landowner payments are settled according to the Payment Due Date (see the Payment record). There will be a Landowner Payment Reminder for Flat-Rate Date-type payments (see corresponding section of this proposal).
    * Flat Rate Harvest-based Landowner payments are determined by the forester.
  * Note that this record should have a name, date, and time stamp for Created and Last Modified.
  * Tract records cannot be merged with each other.



  


Development Specification

Mockup: 

Google Sheets: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=50572512](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=50572512)

  


Designer: [https://zch.apphosting.zone/Reports/Standard/Designer/Std_Preview_Database_Level?Asks=AskParentID%3D105&SinglePane=true&State=Tr1GcI4u7tA](https://zch.apphosting.zone/Reports/Standard/Designer/Std_Preview_Database_Level?Asks=AskParentID%3D105&SinglePane=true&State=Tr1GcI4u7tA)

  


Prospectus Comparison RG example from client: [https://docs.google.com/spreadsheets/d/1gwoTPoejJDvYrneOS2gqxeo0M239F0PV/](https://docs.google.com/spreadsheets/d/1gwoTPoejJDvYrneOS2gqxeo0M239F0PV/)

  


Ellis Miller 12/15/2022: 

DONE_MM: Matthias, I think this means that we use the Catalog Editor "Require Field Restrictions" setting for the Database Level and  list all 100+ fields as restricted fields and define just a handful of them as always available. This is a lot of CPU usage for scrubbing, but I don't think we have other options. It's similar to what we do on the User Profile record. Does this sound right?

Matthias Miller 12/27/2022: OK

  


Ellis Miller 12/15/2022:

[ ] BID: New level and a lot of complexity: 1 DAY

[ ] BID: Restricted data for all fields (1 DAY)
