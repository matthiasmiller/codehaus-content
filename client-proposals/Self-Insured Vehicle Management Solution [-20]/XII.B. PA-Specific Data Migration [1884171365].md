12.2. PA-Specific Data Migration

  


Requirements

Initial Migration:

We will migrate all information based on a master file. All information from the agents must be integrated into the master file before we begin migration.

  


We will import all active clients and all active vehicles. (If we encounter an excess of data integrity issues, we can explore excluding clients who have had no vehicles for 2 or more years.)

  


After migration, we will help you clean up the makes and models on the vehicles.

  


Because the ATV liability code no longer exists, we will import these vehicles as farm vehicles. You will be responsible to make sure any ATVs in the old system are in compliance and correctly classified.

  


Development Specification

[ ] Everything is coming through as a single name. Do we import as contacts, then do a pass to parse everything out and convert to contacts when that's what they should be?

Matthias Miller 07/14/2020: Yes, this isn't a big deal this way....

  


  


  


Matthias Miller 07/23/2020: When working through migration, let's talk about our involvement in the cleanup process

Tim Reitz 07/23/2020: Confirming that MYS is doing the migration and user set up - or what is the level of involvement there?

Matthias Miller 07/28/2020: Yes, I believe MYS will be responsible for importing the data. We will show them how to create users and document them, so they know how to create/manage users.

  


Ellis Miller 08/18/2020:   

  


15 Days

  


3 x30s

  


System switch to disable validation

  


Migration ID fields for matching

  


Reports for Validation Errors

  


Fussing with the data
