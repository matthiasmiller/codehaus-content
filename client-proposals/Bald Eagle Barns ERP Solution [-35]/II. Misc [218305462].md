2\. Misc

  


Requirements

Deleting Records: All records can only be deleted by admins. Some records have further restrictions on deleting. However, in general deleting records is not recommended, as doing so can cause issues with linking and reporting. Deactivating the record is usually the right choice. 

  


Record History: All records should include a "Modification History" link to allow the user to view historical changes to the record. All records will also have "Created By" and "Last Modified By" fields. 

  


Menus: The system should have the following main menus: 

  * Home (used for the most common/general features; accessible for all Member users)
  * Financial (used for finance-related features such as customer/member/entity payments, etc.; used by and accessible for Admins and Office Workers) 
  * Admin (accessible only for Full Admin users; used for Full Admin-level reporting and features)
  * Advanced (accessible to all users except Non-member Salespeople; with limited capabilities depending on permissions; used for settings, configuration, and other various features) 
  * Dealer (used for Non-member Salespeople; accessible for Non-member Salespeople and Full Admins; this would be similar to the Home menu, but without some features such as Time Tracking)



Note that within a given menu, some menu options may be hidden for certain user groups or disabled for certain user groups. 

  


Abbreviations/Terminology: 

  * SRB = Sold Repo Building 
  * RTO = Rent to Own 
  * Repo = A building that has been repossessed from from an RTO customer before it has been paid in full
  * Trade-In / Buy-Back = A building that has been sold back to BEB from a customer



  


Development Specification

Record Types: 

Existing: 

  * Contacts
  * Contact Types (with customizations)
  * SKUs (+inventory management; with customizations)



New: 

  * Building Styles 
  * Manufacturing Departments
  * Manufacturing Task Types
  * Building Diagrams 
  * Diagram Shapes 
  * Sales Tax Codes
  * Buildings 
  * Sales Orders
  * Work Orders
  * Tasks
  * Weekly Time Sheets
  * Locations 
  * Customer Payments
  * Customer Refunds??



NOTE: 

  * All records should include the "Modification History" link at the bottom
  * 


  


Existing Modules/Features: 

\- Inventory Management (Josh) 

- 

  


  


  


TODO_TR/other: 

[ ] Remove all "*Done." references before finalizing the proposal 

[ ] Make sure we are using "Base Building" consistently in the proposal/system. Search and replace in proposal.  

[ ] "Item Code" \- find other terms like "Base Building Code" and replace

[ ]
