4.8.1.2. Device Types

  


Requirements

Overview: This record is used to track each Device Type that Think Ink sells. These records will be hard-coded and non-editable in the solution because a lot of other information is dependent on them. New records cannot be created interactively in the solution. 

  


Accessed via: 

  * Configure Device Types report



  


Sections and Fields: 

  * Type (required; plain text; validate against duplicates)
  * Active (checkbox; default to checked; prevent deactivation if the Type is used by any active Devices in the Solution - error message on Save: "This Type cannot be deactivated because it is being used by at least one active Device.") 
  * Always Managed (checkbox; defaults to unchecked)



  


Data Access: 

  * View: All users (but non-admin users will not have easy access to the record itself by virtue of the menu option being disabled)
  * Edit: N/A



  


Special Considerations: 

  * Copy Record: Prevent copying.
  * Delete Record: Prevent deletion if the record is referenced anywhere in the Solution: "This Device Type cannot be deleted because it is referenced by another record in the database."
  * Merge Record: Prevent merging.



  


Other Notes:

  * These will be the initial types:
    * Customer Printer ("Always Managed" checkbox unchecked)
    * Leased Printer ("Always Managed" checkbox checked)
    * Leased Other ("Always Managed" checkbox checked)
  * The initial types will be set up by CCI, as mentioned above.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=72084077](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=72084077)
