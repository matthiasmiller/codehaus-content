8.6. Vehicle Record

  


Requirements

*Done. 

  


Overview: This is a custom record type, used to track Vehicles that are / have been tracked by Devices. These records are created automatically when a Device reports data from a vehicle VIN that is not present in the Solution, and may also be created manually. 

  


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
