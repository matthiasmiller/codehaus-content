5.1.3. Client Deactivation Reason Record

  


Requirements

*Done. 

  


Overview: This is a custom record type, used to store information that is used when deactivating a client's last vehicle.

  


Accessed via: Advanced | Configuration | Configure Client Deactivation Reasons

  


Sections and Fields: 

  * Reason (plain text; required; validate against duplicates - error message on save: "Duplicate Client Deactivation Reason names are not allowed: <Reason>)
  * Active (checkbox; defaults to checked; error on save: if the current record is not active and the Reason is is referenced on a Vehicle record. "This client deactivation reason cannot be deactivated because it is referenced by another record. (Field: Active))
  * Reportable (checkbox; defaults to checked)
  * Requires Clarification (checkbox)



  


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
  * Some example Deactivation Reasons include:
    * Death (reportable)
    * Left Plan (reportable)
    * Obtained Other Coverage (reportable)
    * Member Without Vehicles (not reportable)
    * Other Reportable (requires clarification; reportable)
    * Other Non-reportable (requires clarification; not reportable)



  


Development Specification

Tim Reitz 08/19/2020: Are these reasons pre-entered, or customizable?

Matthias Miller 08/20/2020: Probably just hand-entered. You'll want to test with a Reportable, Non-reportable, Other Reportable, and Other Non-reportable for testing.

 

Ellis Miller 08/12/2020: Simple lookup record and assoc report that shows fields (0.5 days)
