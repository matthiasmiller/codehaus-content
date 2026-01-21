3.3.1.2. Vehicle Type Record

  


Requirements

*Documented. Tim Reitz 08/19/2025

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Overview: This is a custom record that stores information related to specific types of vehicles (e.g. premium, class).

  


Accessed via: Advanced | Configuration | Configure Vehicle Types

  


Sections and Fields: 

Vehicle Type section:

  * Name (plain text)
  * Active (checkbox; defaults to checked)
  * Requires VIN (checkbox; defaults to checked)
  * Requires License Plate (checkbox; defaults to checked)
  * Uses Classes (checkbox)
  * Included Classes # (number; visible and required if Uses Classes is checked; must be greater than zero)
  * Additional Classes $ (number; 2 decimals; visible if Uses Classes is checked; must be greater than zero)
  * Uses & Requires Liability Coverage (checkbox; defaults to checked)
  * Premium Amount $ (number; 2 decimals; required if the type uses liability coverage; must be greater than zero)
  * Uses <Alternate text for Collision - Long label> Coverage (checkbox; defaults to checked)
  * <Alternate text for Collision - Short label> Entry Fee % (visible if the Solution uses Collision Entry Fee and the "Uses <Collision> Coverage" checkbox is checked for the Vehicle Type; number; two decimals; required if the "Uses <Collision> Coverage" checkbox is checked; must be greater than zero)
  * <Alternate text for Collision - Short label> Premium $ (visible if Solution uses Flat Rate Collision Premiums and the "Uses <Collision> Coverage" checkbox is checked for the Vehicle Type; number; two decimals; required if the "Uses <Collision> Coverage" checkbox is checked; must be greater than zero)
  * <Alternate text for Collision - Short label> Premium % (visible if Solution uses Percentage Collision Premiums and the "Uses <Collision> Coverage" checkbox is checked for the Vehicle Type; number; two decimals; required if the "Uses <Collision> Coverage" checkbox is checked; must be greater than zero)
  * Uses Cargo Coverage (checkbox; defaults to not checked)
  * Cargo Entry Fee % (visible if the Solution uses Cargo Entry Fee and the "Uses Cargo Coverage" checkbox is checked for the Vehicle Type; number; two decimals; required if the type uses cargo coverage; must be greater than zero)
  * Cargo Premium $ (visible if Solution uses Flat Rate Cargo Premiums and the "Uses Cargo Coverage" checkbox is checked for the Vehicle Type; number; two decimals; required if the "Uses Cargo Coverage" checkbox is checked; must be greater than zero)
  * Cargo Premium % (visible if Solution uses Percentage Cargo Premiums and the "Uses Cargo Coverage" checkbox is checked for the Vehicle Type; number; two decimals; required if the "Uses Cargo Coverage" checkbox is checked; must be greater than zero)



  


Subtypes section:

  * Uses Subtypes (checkbox; controls visibility for the rest of the section)
  * Subtypes (embedded spreadsheet with the following:) 
    * Columns: 
      * Subtypes (required; plain text)
      * Max <Alternate text for Collision - Short label> Coverage Amount (number; 2 decimals) 
    * Automatically sorted by: Subtypes (alphabetical)
    * Buttons to append/remove rows: "+" / "-" 
      * Note that the delete button is only visible for rows that are not referenced by an active vehicle and that are not referenced by Silverloom settings
    * Show 10 rows without scrolling 



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Additional Validations:

  * Error on save: if the record is deactivated and is referenced by an active vehicle. "This vehicle type cannot be deactivated because it is referenced by another record."



  


Data Access: Admin

  


Other Notes:

  * N/A



  


Development Specification

Ellis Miller 09/04/2024: 

  


4 Hours. This should be more than extra.

[ ] Add visibility to various fields

[ ] Clear fields in Field Change Expressions if they are not applicable

[ ] We don't expect systems to typically change the system switches after a system is live, so we aren't terrified by edge cases.

  


We are only adding fields here, not changing calculations. That happens elsewhere.
