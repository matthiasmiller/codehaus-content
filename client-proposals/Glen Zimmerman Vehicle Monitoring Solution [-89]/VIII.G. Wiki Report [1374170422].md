8.7. Wiki Report

  


Requirements

Overview: The Solution includes the standard Silverloom Wiki report. This is a two-pane editable report of the Wiki pages in the Solution. By default it only shows active items. Note that any customizations are noted as such in the spec. 

  


Accessed from: __ | Wiki | Wiki. 

TODO_VA: tbd, based at least in part on the client's preference for visibility for the Wiki feature

  


Title: Wiki

  


Left Pane: 

Columns: 

  * Category (list of Wiki Categories) 



  


Grouped by: 

  * (All Categories) 
  * (Recent Unread)
  * (Recent)
  * List of categories with hierarchies



  


Sorted by: N/A

  


Right Pane: 

Columns: 

  * Read/Unread (displays as a blue dot if unread, or blank if read; clicking on the cell checks or unchecks an editable checkbox to mark the Wiki page as read or unread)
  * Category 
  * Title (link to record)
  * ID 



  


Grouped by: 

  * Uncategorized at the top
  * Then alphabetically by Category



  


Sorted by: Title

  


Filters: 

  * Search for (plain text field; searches the Wiki page body memos; defaults to blank) 
  * Unread only (checkbox; defaults to not checked; if checked, the report displays only pages that are unread for the current user) 



  


Buttons: 

  * New Page (opens a blank new Wiki page) 



  


Menu Visibility: 

_GZ: Tim Reitz 09/17/2025: Explain the standard Wiki feature [[https://demo.silverloom.io/?State=ctLVLwm53iQ&_=IkpbS&](https://demo.silverloom.io/?State=ctLVLwm53iQ&_=IkpbS&)]. Who should have access to the Wiki? 

TODO_VA: Tim Reitz 10/16/2025: Glen sees value in it. Content would need to be created (which would take time). 

Glens sees value for both end users and administrative users. 

[ ] Restricted Data Policies: 

  * Master Administrators: view and edit all
  * Group Admins: view (and maybe edit) "Group Admins" and "End Users" Categories
  * Resellers: view (and maybe edit) "Account Resellers" and "End Users" Categories



_NM: Tim Reitz 10/16/2025: With the complex roles, how hard / easy is it to allow these users to view and edit a category (since the Restricted Data Policy is set on the User Profile / User Group record)? 

TODO_ EM : Tim Reitz 10/16/2025: Talk about Restricted Data Policies. 

  * Account Managers: view "End Users" Category 
  * Drivers: view "End Users" Category 



[ ] Wiki Categories: 

  * Master Administrators 
  * Groups Admins 
  * Account Resellers 
  * End Users 



TODO_ EM : Tim Reitz 10/16/2025: Should we ship these? 

TODO_ EM : Tim Reitz 10/16/2025: What happens Restricted Data Policies if a new Category is set up? Is the new category fully available to everyone by default? 

TODO_VA: Tim Reitz 10/16/2025: Wiki record: Maybe make "Category" required? 

  


  


Other Notes: 

  * The Read/Unread checkbox saves automatically when edited.



  


Development Specification

Mockup: N/A
