7.6. FB Insight

Overview: 

  


Accessed via: 

  


Sections and Fields: 

  * Silverloom ID (automatic & autonumber)
  * Account ID (list of FB Accounts)
  * Campaign ID (list of FB Campaign IDs)
  * Ad Set ID (list of FB Ad Set IDs)
  * Ad ID (list of FB Ad IDs)
  * Impressions (number)
  * Clicks (number)
  * Actions; embedded spreadsheet of:
    * Action Type (list of FB Ad Action Types)
    * Actual Value (string)
  * Date (required; date)
  * Conversions (number)
  * Add "Spend" (number; 0 decimals)



  


Indexes:

  * Account ID + Ad Set ID + Ad ID + Date



  


Data Access: 

TODO_IDD: Document based on Permission, rather than User Groups. 

  


Special Considerations: TODO_IDD: 

  * Copy Record: (think: does it make sense to allow copies? what fields are retained / cleared on copy?) 
  * Delete Record: (think: allow deletion? under what circumstances?)
  * Merge Record: (think: does it make sense for this record to be merged since the initiating one is deleted completely?; if we disallow deletion across the board, probably disallow merging)



  


Other Notes:

  * Note that this record includes a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



TODO_IDD: Yes or no?
