7.1.9. Knowledge Tree Branch Record

  


Requirements

Overview: This record allows configuring the Knowledge Tree Branches, which are used to categorize Knowledge Tree Entries. These are all stored on a shared underlying list, but each member has their own unique set of branches that they can configure and use.

  


Accessed via: Configure Knowledge Tree Branches report

  


Sections and Fields: 

  * New Knowledge Tree Branch (link; displayed at the top of the screen, near the Save button; opens a blank new Knowledge Tree Branch record with Member defaulted to the same member as the current record, to allow uplines to easily create new records for downlines) 



  


  * Knowledge Tree Branch section: 
    * Active (checkbox; filled by default)
    * Description (automatic and read-only; Branch Name + Contact ID, i.e. "Finances #001"; unique identifier)
    * Branch Name (required; plain text; validate against duplicates)
    * Member (required; editable on new records for all users; record technically visible for all users if no member is selected; for standard Members, drop list displaying only the current user's name, defaulting to the Contact for the current user; for Facilitator, Regional Rep, and Super Admin users, editable, drop list of all downline Members, defaulting to blank)



  


Data Access: See the Data Access Controls section of the proposal for details.

  


Special Considerations: 

  * Copy Record: N/A
  * Delete Record: Prevent deletion if the record is referenced anywhere in the Solution: "This Knowledge Tree Branch cannot be deleted because it is referenced by another record in the database."
  * Merge Record: N/A



  


Other Notes:

  * Each member (or his uplines) will set up their set of branches. 
  * Each member can start out with a pre-set list of Branches that matches the current list of Development Resource Categories. This list can be set via a button on the Knowledge Tree Entry record (see details in that section of the proposal).
  * The member can set up a category for "Uncategorized" if desired.
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1511793566](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1511793566)

  


BID: 1.5 Days 

  


  


  


Change Requests:

  * Tim Reitz 04/08/2024: [[[IN9704](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9706&)]] - ZSB - Knowledge Tree - Fix Permissions Issue Preventing Creation by Non-Admins
  * Tim Reitz 04/08/2024: [[[IN9638](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9640&)]] - ZSB - Various Changes March 2024 (batch 1)


