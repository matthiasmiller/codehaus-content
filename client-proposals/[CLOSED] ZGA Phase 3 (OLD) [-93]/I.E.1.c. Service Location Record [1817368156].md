1.5.1.3. Service Location Record

  


Requirements

Overview: The Service Location record tracks locations for doing work orders. A non-editable "Shop" location is used for shop jobs, and various other locations are used for service truck jobs.

Note that this replaces the existing "Service Locations" simple list.

  


Accessed via: Configure Service Locations report

  


Sections and Fields: 

  * Location Name (required; plain text field; validated against duplicates)
  * Active (checkbox; defaults to checked; record cannot be marked as inactive if it is referenced on one or more open / active records (currently just Incidents) -- error on Save: "This Location is referenced by one or more open Incidents and therefore cannot be deactivated.")
  * Location Category (auto-set and read-only; sets to "Shop" if the Location Name includes the word "shop", otherwise sets to "Service Truck") 
  * Uses Quality Control (auto-set and read-only; checkbox; checked if Location Category = "Shop") 



  


Data Access: 

  * All Users



  


Special Considerations: 

  * Copy Record: Clear "Location Name"
  * Delete Record: Disallow deletion if the record is referenced by another active / open record -- error message: "This record is referenced by one or more other active / open records and cannot be deleted."
  * Merge Record: Allow merging; no special considerations



  


Other Notes:

  * The following Service Location record will be hard-coded by CCI (non-editable in the software):
    * Name: "Shop"
    * Active: Checked
    * Service Location: "Shop" (default) 
    * Uses Quality Control: Checked (default)
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1Hks1tTQjdnymInK23UzzDXrY3aRrCnxRkN9dUOnYjwo/edit#gid=739777323](https://docs.google.com/spreadsheets/d/1Hks1tTQjdnymInK23UzzDXrY3aRrCnxRkN9dUOnYjwo/edit#gid=739777323)

  


BID: 6 Hours
