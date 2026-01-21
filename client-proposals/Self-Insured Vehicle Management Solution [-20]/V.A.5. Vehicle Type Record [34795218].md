5.1.5. Vehicle Type Record

  


Requirements

*Done.

  


Overview: This is a custom record that stores information related to specific types of vehicles (e.g. premium, class).

  


Accessed via: Advanced | Configuration | Configure Vehicle Types

  


Sections and Fields: 

  * Vehicle Type section:
    * Name (plain text)
    * Active (checkbox; defaults to checked; with the following details / behaviors: 
      * error on Save if the record is marked as inactive while it is being referenced by an active Vehicle record: "This vehicle type cannot be deactivated because it is referenced by one or more active Vehicles. See the "Type" filter on the All Vehicles report.")
    * Requires VIN (checkbox; defaults to checked)
    * Requires License Plate (checkbox; defaults to checked)
    * Uses Classes (checkbox)
    * Included Classes # (visible and required if the Vehicle Type uses Classes; number; no decimals; must be greater than zero)
    * Additional Classes $ (visible and required if the Vehicle Type uses Classes; number; 2 decimals; must be greater than zero) 
    * Uses & Requires Liability Coverage (checkbox; defaults to checked)
    * Premium Amount $ (required if the Vehicle Type uses & requires Liability coverage; number; 2 decimals; must be greater than zero)
    * Uses <Alternate text for Collision - Long label> Coverage (checkbox; defaults to checked)
    * <Alternate text for Collision - Short label> Entry Fee % (visible and required if the Solution uses Collision Entry Fee and the Vehicle Type uses <Collision> Coverage; number; two decimals; must be greater than zero)
    * <Alternate text for Collision - Short label> Premium $ (visible and required if Solution uses Flat Rate Collision Premiums and the Vehicle Type uses <Collision> coverage; number; two decimals; must be greater than zero) 
    * <Alternate text for Collision - Short label> Premium % (visible and required if Solution uses Percentage Collision Premiums and the Vehicle Type uses <Collision> Coverage; number; two decimals; must be greater than zero)
    * Uses Cargo Coverage (checkbox)
    * Cargo Entry Fee % (visible and required if the Solution uses Cargo Entry Fee and the Vehicle Type uses Cargo Coverage; number; two decimals; must be greater than zero)
    * Cargo Premium $ (visible and required if the Solution uses Flat Rate Cargo Premiums and the Vehicle Type uses Cargo Coverage; number; two decimals; must be greater than zero)
    * Cargo Premium % (visible and required if the Solution uses Percentage Cargo Premiums and the Vehicle Type uses Cargo Coverage; number; two decimals; must be greater than zero)



  


  * Subtypes section:
    * Uses Subtypes (checkbox; controls visibility for the rest of the section)
    * Subtypes (embedded spreadsheet with the following:) 
      * Columns: 
        * Subtype (required; plain text)
        * Max <Alternate text for Collision - Short label> Coverage Amount (number; 2 decimals) 
      * Automatically sorted by: Subtypes (alphabetical)
      * Buttons to append/remove rows: "+" / "-" 
        * Note that the delete button is only visible for rows that are not referenced by an active vehicle and that are not referenced by Silverloom settings
      * Show 10 rows without scrolling 



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record) 



  


Data Access: Admin

  


Special Considerations: 

  * Copy Record: Allowed for Admin users. All the fields are copied except "Name".
  * Delete Record: Allowed for Admin users when not active.
  * Merge Record: Allowed for Admin users when not active.  



  


Other Notes:

  * N/A



  


Development Specification

Change Requests: 

  * Tim Reitz 08/19/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident
  * Tim Reitz 08/23/2025: [[[IN11238](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11240&)]] - ZWA - Pre-ZWW - Clean up various validations
  * Tim Reitz 08/26/2025: [[[IN11236](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11238&)]] - ZWA - Pre-ZWW - Rename Various Fields & Labels
  * 


  


  


TODO_CR: Tim Reitz 08/20/2025: "Premium Amount $" is always visible, even if "Uses & Requires Liability Coverage" is not checked. Let's make this conditionally visible based on the "Uses" checkbox.
