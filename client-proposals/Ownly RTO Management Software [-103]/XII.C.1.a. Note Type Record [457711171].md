12.3.1.1. Note Type Record

Seth Miller 09/03/2025: TODO_Permissions: should we add a specific permission for the "Confidential" notes? Currently we are showing them for admins.

  


Overview: This is a custom record type, used to __.

  


Accessed via: __

  


Sections and Fields: 

  * Note Type section: 
    * Name (string field; Note: not directly editable if it is a shipped record)
    * Active (checkbox; default to true)
    * Omit Contents on Linked Record (checkbox;)



  


  * Record History section: 
    * Modification History (link to open the report for the record)



  


  


Note Types to Ship:

  * Customer task
  * Payment Task
  * Contract Task
  * Personal Task
  * URGENT!
  * Letter Template
  * Invoice Template
  * Email Template
  * Call Script
  * Confidential 



Seth Miller 10/16/2025: TODO_Backlog: Are these for sure the note types we want?

  


  


Data Access: Sean Miller 11/13/2025:  TODO_Permissions

  * Visibility: __
  * Editability: __



  


  


Special Considerations: Sean Miller 11/13/2025: TODO_IDD

  * Copy Record: __ (think: does it make sense to allow copies? what fields are retained / cleared on copy?) 
  * Delete Record: __ (think: allow deletion? under what circumstances?)
  * Merge Record: __ (think: does it make sense for this record to be merged since the initiating one is deleted completely?; if we disallow deletion across the board, probably disallow merging)



  


  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.


