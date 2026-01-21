7.8. GA Campaign

Overview: 

  


Accessed via: 

  


Sections and Fields: 

  * Silverloom ID (number; required; autonumber)
  * Campaign ID (list; required; lookup record)
  * Account ID (list of GA Accounts)
  * Name (text)
  * Advertising Channel Type (list; list of GA Channel Types)



  


Indexes:

  * Account ID + Campaign ID
  * Account ID + Advertising Channel Type



  


Data Access: 

TODO_IDD: Document based on Permission, rather than User Groups. 

  


Special Considerations: TODO_IDD: 

  * Copy Record: (think: does it make sense to allow copies? what fields are retained / cleared on copy?) 
  * Delete Record: (think: allow deletion? under what circumstances?)
  * Merge Record: (think: does it make sense for this record to be merged since the initiating one is deleted completely?; if we disallow deletion across the board, probably disallow merging)



  


Other Notes:

  * Note that this record includes a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



TODO_IDD: Yes or no?
