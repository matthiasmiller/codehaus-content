5.7. Master Pricing Table Record

  


Requirements

Overview: This is a special record type used to hold the Master Pricing Table. There will only be one record of this type in the Solution. It will be shipped with the system and initial prices will be populated during deployment.

  


Accessed via: 

  * Main Menu | Pricing | Master Pricing Table



  


Sections and Fields: 

  * Master Pricing Table (embedded spreadsheet with the following:) 
    * Columns: 
      * Min Value (required; number field to 2 decimals; first row is always 0.00; validate against duplicates)
      * Max Value (auto-set and read-only; number field to 2 decimals; calculated based on the next row's Min Value, displaying 0.01 less; blank on final row)
      * Dropoff Price (required; number field rounded to the nearest 2 decimals; price for dropping off furniture)
      * White Glove Price (required; number field rounded to the nearest 2 decimals; price for dropping off and setting up furniture)
      * Dropoff % (auto-set and read-only; number field rounded to the nearest 2 decimals; expression of Dropoff Price as % of the midpoint between Min Value and Max Value)
      * White Glove % (auto-set and read-only; number field rounded to the nearest 2 decimals; expression of White Glove Price as % of the midpoint between Min Value and Max Value)
    * Automatically sorted by: Min Value
    * Validate on save that first row is 0.00: "The first row must have a Min Value of 0.00."
    * Buttons to insert/append/remove rows: "+" / "-" 
    * Show 20 rows without scrolling



  


Data Access: 

  * Editable: Employees & Support



  


Special Considerations: 

  * Copy Record: Disallowed.
  * Delete Record: Disallowed.
  * Merge Record: Disallowed.



  


Other Notes:

  * Note that this record should have a name, date, and time stamp for Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

[mockup](https://docs.google.com/spreadsheets/d/1_Tudd70CPRwzIzN4-dMivx01EvGpOJC3oQsPPvOzItQ/edit#gid=0 "https://docs.google.com/spreadsheets/d/1_Tudd70CPRwzIzN4-dMivx01EvGpOJC3oQsPPvOzItQ/edit#gid=0")

  


Ellis Miller 05/24/2024: 4 hours

  


The shipped record will not have pricing info, but we can create a simple x30 to bring in prices and have sample data to import for developers and test system. Jonathan can help provide the data.

  


[ ] Lookup list with a single list item, Investortools owned list so that users can't add more.

[ ] The entire RG should be visible on a laptop screen, so I'm guessing 20 rows.

[ ] For DroffOff % calculation use DropOffPrice / Average(MinValue, MaxValue)

[ ] Similar for White glove
