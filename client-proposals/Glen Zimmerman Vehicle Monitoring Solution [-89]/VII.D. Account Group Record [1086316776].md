7.4. Account Group Record

  


Requirements

*Done. 

  


Overview: This is a custom record type, used to track Account Groups. This allows for grouping of Accounts for support and supervision, and allows the Group Admins to manage the Accounts in their Group.

  


Account Groups can be "nested", creating a series of "upline" and "downline" Groups. An Account Group can have only one direct upline, but may have multiple downlines.

  


The Solution include ones or more general or "catch-all" Account Group records, administered by Master Administrators, for Accounts that do not correspond to any of the main Account Groups. Note that an initial "catch-all" Account Group would be set up by CodeCrafters at deployment.

  


Accessed via: 

  * "Account Groups" reports
  * "Account Group" field on the Account record 
  * Providers | Account Groups | New Group (opens a new Account Group record) 



  


Sections and Fields: The sections and fields for this record are specced out in sub-sections below.

  


Data Access: 

  * Visibility: Can be viewed by: 
    * Users with the "Full Access" Permission can view the screen & all included items.  
    * All other users can view, but some sections / fields may be hidden.
  * Editability: Can be edited by (with some additional conditions specced on individual items): 
    * Users with the "Full Access" Permission (one or more items limited to only these users). 
    * The linked "Account Group Admin" users for the Group and "Upline Group(s)" 



  


Special Considerations:

  * Copy Record: Allowed for users who can edit the record; the following field(s) are cleared on the new record:
    * Group Name
  * Delete Record: Allowed for users with the "Full Access" Permission if the Group is not active and does not have any linked Accounts.
  * Merge Record: Allowed for users with the "Full Access" Permission. Note that the record from which the merge is initiated is completely replaced by the other (deleting all data for the first record).



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * Unless otherwise noted, all fields that become hidden for any reason retain their values. If they should be cleared, that is noted specifically in the field specs. 
  * Heading color (custom): This record type uses a light orange color for section headings.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=757234751#gid=757234751](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=757234751#gid=757234751)

  


  


  


  


Tim Reitz 10/30/2025: It would probably be an extra $500-700 to send it conditionally, choosing who to send it to (would include an extra RG to track who could receive it, with options to change). Probably extra $200-300 if we simply choose whether or not to send it at all ("Send Email on Next Save" checkbox). Is it worth it to you? 

Tim Reitz 11/06/2025: Glen likes the option of choosing who to send the email to. 

Tim Reitz 12/30/2025: Retaining these notes for reference during pricing, etc. 

  


  


_EM - Does CCI care about liability of having this much tracking information, and what happens from a publicity/legal standpoint if something goes awry?

Tim Reitz 08/21/2025: This is a note from before the IDD.

TODO_EM: Tim Reitz 10/30/2025: Per Ellis, some of this could depend on how much of the Traccar data is pulled into Silverloom. 

TODO_GZ: Tim Reitz 10/30/2025: We should also discuss the liability aspect with Glen before pricing (data leaked, lawsuit, etc.). And clearly note that with agreement text, etc.
