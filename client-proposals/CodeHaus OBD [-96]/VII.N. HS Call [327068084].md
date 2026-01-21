7.14. HS Call

Overview: 

  


Accessed via: 

  


Sections and Fields: 

  * Silverloom ID (autonumber)
  * Hub (list of Hubs; required)
  * Object ID (number; required)
  * Disposition (HS Dispositions)
  * Timestamp (string)
  * Call Duration (Number)
  * Owner ID (number)
  * Contact ID (number)
  * Deals RG
    * ID (number; required)



  


  * Hub + Object ID (using BinStringBigNum for the object ID)
  * Hub ID + Deal ID (using BinStringBigNum for the object ID)
  * Hub ID + Contact ID (using BinStringBigNum for the object ID)



  


Data Access: 

TODO_IDD: Document based on Permission, rather than User Groups. 

  


Special Considerations: TODO_IDD: 

  * Copy Record: (think: does it make sense to allow copies? what fields are retained / cleared on copy?) 
  * Delete Record: (think: allow deletion? under what circumstances?)
  * Merge Record: (think: does it make sense for this record to be merged since the initiating one is deleted completely?; if we disallow deletion across the board, probably disallow merging)



  


Other Notes:

  * Note that this record includes a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



TODO_IDD: Yes or no?
