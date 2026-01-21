7.7. GA Account

Overview: 

  


Accessed via: 

  


Sections and Fields: 

  * GA Account ID (list; required; lookup record)
  * Name
  * Timezone (list; GA Time Zones; user-configurable)
  * Sync Cursor (string)



  


Indexes:

  * NA



  


Data Access: 

TODO_IDD: Document based on Permission, rather than User Groups. 

  


Special Considerations: TODO_IDD: 

  * Copy Record: (think: does it make sense to allow copies? what fields are retained / cleared on copy?) 
  * Delete Record: (think: allow deletion? under what circumstances?)
  * Merge Record: (think: does it make sense for this record to be merged since the initiating one is deleted completely?; if we disallow deletion across the board, probably disallow merging)



  


Other Notes:

  * Note that this record includes a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



TODO_IDD: Yes or no?
