11.1.1. Department Record

Overview: This is a simple configuration record used to track the various Faith Builders Departments using or being referenced in the Solution. User cannot create or delete department records; however, most fields are editable.

  


Accessed via: Advanced | Configuration | Configure Departments

  


Sections and Fields: 

  * FB Department section
    * Name (read-only; displays the department name or acronym; desired changes should be communicated to CodeCrafters) 
    * Active (checkbox)



_TR Austin Priest 02/20/2025: There is an active checkbox on these records in the test system. An active checkbox was not mentioned in the spec. I'm not sure there should be on active checkbox on these records. With brief testing, it looks like making one of these departments inactive does not make any change in the system. Note that if we remove this checkbox, we should update the spec for the shipped records.

TODO_NM: Tim Reitz 02/24/2025: Does this active checkbox do anything for the shipped records?

  * FB Department From Name (editable; required; plain text field; used to track the name use as the "From" for communications sent from the department)
  * FB Department From Email (editable; required; plain text field; used to track the email address used as the "From" for communications sent from the department) 



  


Modification History: This contains the following standard features for modification tracking: 

  * Activity History (link to open the report for the record)



  


Data Access: All users can view and edit

  


Special Considerations:

  * Copy Record: N/A (disallowed)
  * Delete Record: N/A (disallowed)
  * Merge Record: N/A (disallowed)



  


Other Notes:

  * The Solution includes some Department records that are "shipped" \- see the following proposal subsection.


