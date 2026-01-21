7.8. Knowledge Tree Entry Record

  


Requirements

Overview: This is a piece of knowledge that is captured from a resource or conversation, which a member wishes to retain for personal reference. These entries may be associated with a Development Resource, but sometimes are not. These entries are associated with the member's Knowledge Tree.

  


Members may create/add these entries throughout the month without associating a Knowledge Tree Branch. At a later point, they may review/sort the entries to categorize or deactivate them.

  


Accessed via: 

  * Knowledge Tree Entry report(s)



  


Sections and Fields: 

  * Knowledge Tree Entry ID (automatic and read-only; unique identifier)
  * Active (checkbox) 
  * Member (required; editable on new records for all users; record technically visible for all users if no member is selected; for standard Members, drop list displaying only the current user's name, defaulting to current user; for Facilitators and uplines, drop list of all downlines with active memberships, defaulting to blank, filters down as you type)
  * Resource (optional; drop list of Development Resource records)
  * View Resource Review (visible if a Resource is selected; link; opens the member's Review of the selected Resource)
  * Page Number (optional; plain text field)
  * Knowledge Tree Branch (optional; drop list of Knowledge Tree Branch items for the selected Member)
  * View/Edit Branches (link; opens the Configure Knowledge Tree Branches report, filtered to the selected Member)
  * New Branch (link; opens a new Knowledge Tree Branch record, with the selected Member defaulted; once saved, the new item will be included on the drop list)
  * Add Default Branches (button; visible if the selected Member does not already have all of the default branches; clicking the button runs the Add Default Branches background process to create a Branch for each of the active Development Resource Categories in the Solution, giving a new member an initial list of items to choose from)
  * Knowledge Tree Entry Text (required; multi-line plain text)



  


Data Access: See the Data Access Controls section of the proposal for details.

  


Special Considerations:

  * Copy Record: N/A
  * Delete Record: N/A
  * Merge Record: Only can be merged by Super Admins. All other users would get a message to contact an Admin to resolve a duplicate. 



  


Other Notes: 

  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockups: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1398340691](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1398340691)

  


  


Change Requests:

  * Tim Reitz 04/08/2024: [[[IN9704](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9706&)]] - ZSB - Knowledge Tree - Fix Permissions Issue Preventing Creation by Non-Admins
  * Tim Reitz 04/08/2024: [[[IN9638](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9640&)]] - ZSB - Various Changes March 2024 (batch 1)


