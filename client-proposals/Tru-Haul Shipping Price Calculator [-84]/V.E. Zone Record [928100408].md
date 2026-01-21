5.5. Zone Record

  


Requirements

Overview: Tru-Haul uses Zones to help with delivery routes.

  


Accessed via:

  * Zones report



  


Sections and Fields: 

  * Active (checkbox; defaults to checked;
    * If checkbox is not checked (Zone is inactive) and the Zone Route is inactive, validation error on the field when attempting to reactivate the Zone / check the checkbox: "The linked Zone Route is inactive and must be made active before this Zone can be reactivated.")
  * Zone (read-only and auto-set as "<Zone Number> \- <Zone Name>")
  * Zone Number (required; number field; no decimals; validate against duplicates)
  * Zone Name (optional; plain text field; validate against duplicates)
  * Zone Route (required; drop list of active Routes)
  * View Linked Zip Codes (link to Zip Codes report; filtered by Zone)



  


  * Bottom Bucket Master Dropoff $ (auto-set and read-only; displays the Dropoff price for the smallest bucket in the Master Pricing Table)
  * Bottom Bucket Zone Dropoff $ (auto-calculated; editable; number to 2 decimal places, rounding to the nearest whole dollar amount but still showing ".00" at the end; this is the lowest Curbside Dropoff price for the Zone; calculated via the following calculation: <Bottom Bucket Master Dropoff $> * <Bottom Bucket Ratio>; if edited, the Bottom Bucket Ratio is also updated accordingly; example for this field's calcuation:
    * If Bottom Bucket Master Dropoff $ = 78.00, and
    * The Bottom Bucket Ratio is set to 3.000, then
    * This calculates & rounds to 234.00)
  * Bottom Bucket Ratio (required; auto-calculated; editable; number to 3 decimals; must be between 0.25 and 15.00 -- validation error message on the field or on Save if out of range: "The Bottom Bucket Ratio must be between 0.25 and 15.00."; this is the ratio to apply for this Zone to the lowest bucket in the Master Pricing Table; calculated via the following calculation: < Bottom Bucket Zone Dropoff $> / <Bottom Bucket Master Dropoff $>; if edited, the Bottom Bucket Zone Dropoff $ field also is updated accordingly; example for this field's calcuation:
    * If Bottom Bucket Master Dropoff $ = 78, and
    * The Bottom Bucket Zone Dropoff $ is set to 100.00, then
    * This calculates and rounds as needed to 1.282)



  


  * Top Bucket Master Dropoff $ (auto-set and read-only; displays the Dropoff price for the largest bucket in the Master Pricing Table)
  * Top Bucket Zone Dropoff $ (required; auto-calculated; editable; number to 2 decimals; this is the highest Curbside Dropoff price for the Zone; calculated via the following calculation: <Top Bucket Master Dropoff $> * <Top Bucket Ratio>; if edited, the Top Bucket Ratio is also updated accordingly) 
  * Top Bucket Ratio (required; auto-calculated; editable; number to 3 decimals; must be between 0.25 and 15.00 -- validation error message on the field or on Save if out of range: "The Top Bucket Ratio must be between 0.25 and 15.00."; this is the  ratio to apply for this Zone to the largest bucket in the Master Pricing Table; calculated via the following calculation: < Top Bucket Zone Dropoff $> / <Top Bucket Master Dropoff $>; if edited, the Top Bucket Zone Dropoff $ field also is updated accordingly) 



  


Data Access: 

  * Visible to and editable by: Employees & Support



  


Special Considerations: 

  * Copy Record: Edit pricing information
    * Clear Zone ID and Name
  * Delete Record: Edit pricing information
    * Disallow if referenced in the database (by a Zip Code)
  * Merge Record: Edit pricing information



  


Other Notes:

  * The Ratio numbers are anchored on 1.0 (so 1.0 does not change the $ amount). 
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard)



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1_Tudd70CPRwzIzN4-dMivx01EvGpOJC3oQsPPvOzItQ/edit#gid=1023608429](https://docs.google.com/spreadsheets/d/1_Tudd70CPRwzIzN4-dMivx01EvGpOJC3oQsPPvOzItQ/edit#gid=1023608429) 

  


Change Requests: 

  * Tim Reitz 07/02/2024:  [[[IN10033](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10035&)]] - [[PC0167205]] - ZTH - Record - Zone (changes made in the original testing job) 
  * 


  


Ellis Miller 04/18/2024:  CCI: 8 hours

[ ] Make this a lookup list, Linked record so displays as link

[ ] Call the lookup field ZoneID and auto-set as Concat(" \- ", ZoneNumber, ZoneName)

[ ] Updated OnChange from both fields

[ ] View Linked Zip Codes - not visible for new records, just runs report

  


[ ] The Ratio fields are simple fields (ZoneBottomBucketRatio, ZoneTopBucketRatio). 

[ ] The $Adj are editable macro (ZoneBottomBucketDropoff$....) -- talk to Mizan or Ellis if you have questions on implementation

  


[ ] Add ZonesByRoute.ndx
