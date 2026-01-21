5.1.2. Congregration Record

  


Requirements

*Done. 

  


Overview: This is a custom record type, used to stores congregation names for reference.

  


Accessed via: Advanced | Configuration | Configure Congregations

  


Sections and Fields: 

  * Name (required; plain text; validate against duplicates - error message on save: "Duplicate Congregation names are not allowed: <Name>")
  * Active (checkbox; defaults to checked; error on Save if selected on an active Contact record. "This congregation cannot be deactivated because it is referenced by one or more active Contact records. See the "Congregation" column on the All Clients report.")



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (User ID, date, and time stamp) 
  * Last Modified: (User ID, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: 

  * View, edit and delete: Admin



  


Special Considerations: 

  * Copy Record: Allowed
  * Delete Record: Allowed when not active
  * Merge Record: Allowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Change Requests: 

  * Tim Reitz 08/23/2025: [[[IN11238](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11240&)]] - ZWA - Pre-ZWW - Clean up various validations


