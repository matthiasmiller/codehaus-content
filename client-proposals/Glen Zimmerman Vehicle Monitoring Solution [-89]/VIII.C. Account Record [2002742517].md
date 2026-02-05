7.3. Account Record

  


Requirements

*Done. 

  


Overview: This is a custom record type, used to track Accounts and their related details.

  


Accessed via:

  * Accounts reports
  * Providers | Accounts | New Account (opens a new Account record) 



  


Sections and Fields: The sections and fields for this record are specced out in sub-sections below.

  


Data Access: 

  * Visibility: Visible to all users, with some sections / fields are hidden:
    * All users with the "Full Access" Permission can view everything; 
    * For Group Admins:
      * "Group Admin" users for the selected "Account Group" and "Upline Group(s)": can view everything;
      * Other "Group Admin" users: some sections / fields may be hidden; 
    * For Account Resellers:
      * Linked "Account Reseller" / corresponding "Reseller Reps": can view everything;
      * Other Resellers: some sections / fields may be hidden; 
  * Editability:
    * For new, unsaved records: Editable for all users; 
    * For saved records: 
      * Editable interactively for "Upline Provider Roles" users for the Account.
        * Note that this could be changed in Phase 2 or at some other point in the future, to allow other providers some limited editing. 
      * Editable via import (automatic process) for all users (this allows other Resellers / Reps to request a Reseller transfer, and to approve transfers in progress).



  


Special Considerations: 

  * Copy Record: Disallow copying. 
  * Delete Record: Allowed for the selected "Account Reseller" and all users with the "Full Access" Permission if the following are true: "Account Status" = "In Setup" or "Closed" and the "Devices" embedded spreadsheet is empty.
  * Merge Record: Disallow merging. 



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.  
  * Unless otherwise noted, all fields that become hidden for any reason retain their values. If they should be cleared, that is noted specifically in the field specs.
  * Heading color (custom): This record type uses a light yellow color for section headings.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1369316398#gid=1369316398](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1369316398#gid=1369316398)

  


  


TODO_REVIEW / TODO_DEV: Tim Reitz 12/22/2025: Per Nic, editability for this record can be based on a can edit expression (doesn't need to be restricted data). Of course, this could change if requirements change.
