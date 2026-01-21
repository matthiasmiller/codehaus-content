5.4. Zip Code Record

  


Requirements

Overview: The zip code screen lets you assign zip codes to specific zones. Initial data will be imported from the existing system.

  


Accessed via: 

  * Zip Codes report



  


Sections and Fields: 

  * Zip (required; string field; validate "The Zip must be 5 digits."; validate against duplicates)
  * Zone (optional; drop list of available zones; defaults to blank; if a Zone is selected, the corresponding Zip Code will be available for shipping)
  * Route (auto-set and readonly; route for the linked zone)
  * City (required; plain text field)
  * State (required; drop list of all US states, sorted alphabetically; defaults to blank)
  * Latitude (optional; number field to 6 decimals; validate "Latitude must be between -90 and 90.")
  * Longitude (optional; number field to 6 decimals; validate "Longitude must be between -180 to 180.")



  


Data Access: 

  * Editable: Employees & Support



  


Special Considerations: 

  * Copy Record: No
  * Delete Record: Edit pricing information
    * Validate: "A Zip Code record cannot be deleted if it has a Zone specified."
  * Merge Record: No



  


Other Notes:

  * Latitude and Longitude are not currently used in the system, but are imported from source data.
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard)



  


Development Specification

[mockup](https://docs.google.com/spreadsheets/d/1_Tudd70CPRwzIzN4-dMivx01EvGpOJC3oQsPPvOzItQ/edit#gid=1144457436 "https://docs.google.com/spreadsheets/d/1_Tudd70CPRwzIzN4-dMivx01EvGpOJC3oQsPPvOzItQ/edit#gid=1144457436")

  


Ellis Miller 04/29/2024:  4 hours

[ ] "ZipCode" Lookup record

[ ] Main field is simply "ZipCode" \-- no validation required, validate it is 5 numeric digits (InRange( Value( Field), 10000, 99999) AND Length(Field) = 5

[ ] other fields are "ZipCodeZone", etc.

[ ] Route is a simple ZoneField(ZipCodeZone, ZoneRoute)

  


[ ] Create an ZipCodesWithZones.ndx that is a 5-byte text index for all zip codes with a Zone specified.
