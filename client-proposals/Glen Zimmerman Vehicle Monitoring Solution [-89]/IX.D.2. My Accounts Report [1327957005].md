8.4.2. My Accounts Report

  


Requirements

TODO_VA: Tim Reitz 10/06/2025: Is this a filtered version of the Master Account Report, with conditional title, etc. 

Tim Reitz 10/06/2025: Yes, if the Master report is not an autopush for some reason. 

  


Overview: This is a custom report of Account records for which the current user is an Account Manager and/or Driver, with various filters. 

  


Accessed from: 

  * My <Service Name> | Account Details | My Account (opens the report directly, bypassing the filter screen; if only one matching Account exists, opens that Account directly, bypassing the report entirely) 



_NM: Tim Reitz 10/06/2025: Can the menu option be "My Account" if only 1 record exists / "My Accounts" if multiple? 

TODO_VA: Tim Reitz 10/06/2025: Yes, we can do that. 

  


Title: "My Accounts" 

  


Preface: N/A

  


Columns: 

  * Account Status
  * Account # (link to open the record) 
  * Account Name 



  


Row-Specific Buttons:

  * N/A



  


Grouped by: "Account Status" (in the standard list sequence) 

  


Sorted by: Account # (lowest number at the top)

  


Filters: N/A

  


Buttons: N/A

  


Menu Visibility: All users (disabled for users who are not an Account Manager or Driver for any Accounts) 

  


Other Notes:

  * This is an "auto-push" report, allowing it to open a record directly (bypassing the report entirely) if only one matching record exists.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=380097686#gid=380097686](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=380097686#gid=380097686)
