7.5. FB Ad Set

Overview: 

  


Accessed via: 

  


Sections and Fields: 

  * Silverloom ID (number; required; autonumber)
  * Ad Set ID (list of FB Ad Set IDs; required)
  * Account ID (list of FB Account IDs; required)
  * Name
  * Optimization Goal (user-configurable list of FB Optimization Goals)
  * Promoted Pixel ID (user-configurable list of FB Pixel IDs)
  * Promoted Custom Event Type (user-configurable list of FB Custom Event Types)[



  


Indexes:

  * Account ID + Ad Set ID



  


Data Access: 

TODO_IDD: Document based on Permission, rather than User Groups. 

  


Special Considerations: TODO_IDD: 

  * Copy Record: (think: does it make sense to allow copies? what fields are retained / cleared on copy?) 
  * Delete Record: (think: allow deletion? under what circumstances?)
  * Merge Record: (think: does it make sense for this record to be merged since the initiating one is deleted completely?; if we disallow deletion across the board, probably disallow merging)



  


Other Notes:

  * Note that this record includes a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



TODO_IDD: Yes or no?
