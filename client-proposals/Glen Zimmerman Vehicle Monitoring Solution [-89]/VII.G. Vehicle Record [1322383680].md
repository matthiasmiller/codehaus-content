7.7. Vehicle Record

  


Requirements

*. 

  


Overview: This is a custom record type, used to track Vehicles that are / have been tracked by Devices. These records are created automatically when a Device reports data from a vehicle VIN that is not present in the Solution, and may also be created manually. 

DONE_JB (research): Tim Reitz 01/16/2026: I'm wondering if Traccar logs the VIN for vehicles connected to the OBDs (on-board devices). I'm guessing this would be on an "Event" record or "Position" record or something like that. 

We've kinda been banking on it, since we're planning to auto-create Vehicle records in Silverloom via the sync when a new VIN is logged in Traccar. But I realized that I'm not specifically seeing VIN details in Traccar, so I'd like some deeper digging on that. 

TODO_VA: Jonathan Bergen 01/21/2026: Yes, the devices should be able to be configured to send the VIN along with the events.

  


Accessed via:

  * All Vehicles Report
  * Links on other records, such as Device and Traccar Event records
  * Providers | Vehicles | New Vehicle (opens a new Vehicle record) 



  


Sections and Fields: The sections and fields for this record are specced out in sub-sections below.

  


Data Access: 

  * Visibility: "All Provider Roles" users; 
  * Editability: "All Provider Roles" users; 



  


Special Considerations: 

  * Copy Record: Disallow
  * Delete Record: Allowed if the Vehicle is not referenced on any other records. 
  * Merge Record: Disallow



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * Unless otherwise noted, all fields that become hidden for any reason retain their values. If they should be cleared, that is noted specifically in the field specs.
  * Heading color (custom): This record type uses a light purple color for section headings.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=966911107#gid=966911107](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=966911107#gid=966911107)
