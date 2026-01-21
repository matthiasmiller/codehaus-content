7.11. HS Disposition

Overview: 

  


Accessed via: 

  


Sections and Fields: 

  * Silverloom ID (number; autonumber; required)
  * Disposition ID (list of HS Dispositions; required; lookup type)
  * Hub ID (list of HS Hubs)
  * Label (string)
  * Deleted (boolean)



  


Indexes:

  * Hub ID + Disposition ID



  


Data Access: 

TODO_IDD: Document based on Permission, rather than User Groups. 

  


Special Considerations: TODO_IDD: 

  * Copy Record: (think: does it make sense to allow copies? what fields are retained / cleared on copy?) 
  * Delete Record: (think: allow deletion? under what circumstances?)
  * Merge Record: (think: does it make sense for this record to be merged since the initiating one is deleted completely?; if we disallow deletion across the board, probably disallow merging)



  


Other Notes:

  * Note that this record includes a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



TODO_IDD: Yes or no?
