5.6. Route Record

  


Requirements

Overview: Tru-Haul uses Routes to determine delivery locations. See glossary.

  


Accessed via: 

  * Routes report



  


Sections and Fields: 

  * Active (checkbox; defaults to checked; validate against deactivating Routes that are being used by one or more active Zone records - error message: "This route cannot be made inactive because it is referenced by the following active zones: <list of zones>")
  * Route Name (required; plain text field; validate against duplicates)
  * Zones (link; opens the Zones report, filtered to the corresponding Route)
  * Route Notes (optional; memo; displayed on calculator; note that this field includes a vertical blue bar alongside the memo field to indicate how long the memo can be before it causes the Quote to break into a second page)



  


Data Access: 

  * Editable: Employees & Support



  


Special Considerations: 

  * Copy Record: Edit pricing information
    * Route Name is cleared
  * Delete Record: Edit pricing information
    * Disallow if referenced
  * Merge Record: Edit pricing information



  


Other Notes:

  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1_Tudd70CPRwzIzN4-dMivx01EvGpOJC3oQsPPvOzItQ/edit#gid=1324290755](https://docs.google.com/spreadsheets/d/1_Tudd70CPRwzIzN4-dMivx01EvGpOJC3oQsPPvOzItQ/edit#gid=1324290755)

  


Change Requests:

  * Ben Reitz 10/14/2025: [[[IN11604](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11606&)]] - ZTH - Quote printout - Fit everything on one page
  * 


  


Ellis Miller 05/24/2024: Lookup record. 2 hours

[ ] Linked record to display as link

Use the ZonesByRoute.ndx for the validation
