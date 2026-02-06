4.8.1.1. Device Tags

  


Requirements

Overview: These tags can be used for all Device Types, to be able to tag devices and filter out all devices of a certain tag (i.e. to send a list to Canon of the printers that are on Canon's MPS program). 

  


Accessed via: Configure Device Tags Report

  


Sections and Fields: 

  * Active (checkbox; defaults to checked) 
  * Tag Name (required; plain text; validate against duplicates)
  * Device Type (required; multi-select drop list of all Device Types; designates which Type(s) the Tag can be applied to) 



  


Data Access:

  * View: All users (but non-admin users will not have easy access to the record itself by virtue of the menu option being disabled)
  * Edit: Admin-only



  


Special Considerations:

  * Copy Record: N/A
  * Delete Record: Prevent deletion if the record is referenced anywhere in the Solution: "This Tag cannot be deleted because it is referenced by another record in the database."
  * Merge Record: N/A



  


Other Notes:

  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard). 
  * These configuration records should be set up at deployment by Think Ink, with help from CCI/CH as needed. 
  * Examples of the device tags include: 
    * Canon MPS
    * Brother MPS
    * Think Ink Warranty
    * Mfg Service Plan



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1807567785](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1807567785)

  


TODO_CCI: Include a note in the testing job to set up the following in the test system: 

  * Canon MPS
  * Brother MPS
  * Think Ink Warranty
  * Mfg Service Plan



  


TODO_IDD: Include a note in the deployment incident to set up the following in the live system: 

  * Canon MPS
  * Brother MPS
  * Think Ink Warranty
  * Mfg Service Plan


