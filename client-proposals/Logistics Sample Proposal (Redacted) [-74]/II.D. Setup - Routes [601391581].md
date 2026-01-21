2.4. Setup - Routes

  


Requirements

Routes are designed to model the number of trucks that are on the road. Each route would specify:

  * Name
  * Weekdays
  * Recurring Stops



  


Development Specification

Routes Record Changes

This is based on the Routes record.

  


[ ] Add a RouteContactsPipeList that returns all route contacts. You can do something like this:

  * Create an ActiveContactsByType index
  * Use ActiveContacts if ConfigRoutes_ContactType is blank. Otherwise, use the new index.



  


[ ] Keep the Name field

[ ] Add the Weekdays schedule RG -- don't need to automatically add any rows to new records; don't need to default any fields

  * Weekday -- same as current field, but in RG
  * Default Start Location -- replaces Warehouse field, but in RG; using RouteContactsPipeList helper list
  * Default End Location -- same as Start location
  * Default Start Time -- same as current field, but in RG; required



[ ] Remove Maximum Stops

[ ] Sort by Weekday. Validate against blank or duplicate weekdays.

  


[ ] This should be restricted if not ConfigRoutes_IsRoutesUser

[ ] This should be read-only if not ConfigRoutes_IsAdminUser
