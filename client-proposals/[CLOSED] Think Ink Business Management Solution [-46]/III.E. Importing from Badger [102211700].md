3.5. Importing from Badger

  


Requirements

Check-In information will be migrated from Badger to the Solution. This will be done at the deployment of the Solution, after which the Solution will replace Badger for CRM and check-ins. 

  


The Badger check-ins would be imported into the Solution, creating Check-In incidents through the import. 

  


Think Ink would take care of preparing the CSV file and exporting it from Badger. CCI/CH would provide a template for the import file. 

  


The input file will specify:

  * Title
  * Customer Email
  * Customer Phone
  * Check-In Notes
  * Check-In Date
  * Closed Date (left blank if check-in is still open) 
  * Badger ID



  


The import will match on Badger ID if there is an existing Check-In incident with a matching Badger ID. Otherwise, it will create a new incident. 

  


The import also will set the incident Contact field to the first contact that matches on email (if possible) or phone number (if there is no email). If no contact match is found, the import will add the email address and phone number to the notes field so that a user can manually match up the incident with a contact. 

  


The import will be accessible through the Standard folder via the User Folders option on the Favorites menu.

  


Development Specification

Mockup: None needed

Tim Reitz 08/05/2022: Here is a sample file on Google Sheets (I downloaded a copy as a .csv and shared it with the devs and put a copy in the testing job): [https://docs.google.com/spreadsheets/d/1ftz9xZi9ojVnuRcwbsCaJ93VySAIsuQYR7RXwphZQ08/edit#gid=0](https://docs.google.com/spreadsheets/d/1ftz9xZi9ojVnuRcwbsCaJ93VySAIsuQYR7RXwphZQ08/edit#gid=0)

  


Ellis Miller 06/16/2022: DONE_TR: If we can't match on contact, should we add Email and Phones to the Notes field so that they can manually match things up?

Matthias Miller 06/21/2022: I like this. Let's update above.

  


  


SPEC:

[ ] Add Badger ID

[ ] Simple x30 -- just do a ConcatLookups to find the matching email or phone. This is a bit slow, but it isn't terrible. 

BID: 0.5 Day for CCI coding

  


  


Migration: 0.5 day est for CH, but we will do T&M.
