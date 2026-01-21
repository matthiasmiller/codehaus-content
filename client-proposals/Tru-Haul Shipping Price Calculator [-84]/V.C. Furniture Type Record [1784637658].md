5.3. Furniture Type Record

  


Requirements

Overview: The software supports defining furniture types.

  


Accessed via:

  * Furniture Types Report



  


Sections and Fields: 

  * Active (checkbox; defaults to checked; can be used to deactivate a type)
  * Name (required; plain text field; validate against duplicates)
  * Sort Order (number field with no decimals; used to determine the order that types are displayed on the calculator screen; validate "The sort order must be between 1 and 99.")
  * Pricing Ratio (required; number field to 2 decimals; ratio to apply to Master Pricing Table for this type, Example: 0.90 will price this furniture type at 90% of the Master Price, Validation Error if out of range: "The Pricing Ratio must be between 0.25 and 5.00.") 
  * White Glove Delivery Only (checkbox; defaults to not checked; if checked, the Furniture Type is excluded from Curbside Dropoff pricing calculations; if unchecked, it is included in Curbside Dropoff calculations) 



  


Data Access: 

  * Editable: Employees & Support



  


Special Considerations: 

  * Copy Record: No
  * Delete Record: Edit pricing information
  * Merge Record: No



  


Other Notes:

  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard)



  


Development Specification

Change Requests: 

  * Tim Reitz 07/02/2024: [[[IN10166](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10168&)]] - ZTH - Furniture Type Record - Make Curbside Dropoff Pricing Optional 
  * 


  


  


Mockup: [mockup](https://docs.google.com/spreadsheets/d/1_Tudd70CPRwzIzN4-dMivx01EvGpOJC3oQsPPvOzItQ/edit#gid=1777842829 "https://docs.google.com/spreadsheets/d/1_Tudd70CPRwzIzN4-dMivx01EvGpOJC3oQsPPvOzItQ/edit#gid=1777842829")

  


Ellis Miller 05/27/2024: CCI: 2 hours

[ ] Lookup record, so no validation required on name

[ ]
