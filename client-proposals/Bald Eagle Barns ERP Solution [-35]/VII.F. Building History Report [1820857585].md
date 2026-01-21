7.6. Building History Report

  


Requirements

This is a report of changes made to a building over the building's history, looking at both Sales Order records and Work Order records.

  


This would be accessed from the Building record. It would only show one building at a time. 

  


Title: Building History for <Serial Number> 

  


Columns: 

  * Date (Sale Date for SO; Completed Date for WO)
  * Created By (User ID)
  * Event (Sales Order Type or Work Order Type + subtype??)
  * Owner (owner at the completion of the event)
  * Location (Ending Location from the Work Order) 
  * Sales Order / Work Order (ID; link)
  * Salesperson (for SO; Salesperson initials) 
  * WO Completed By (for WO; Member's initials) 
  * SO Completed By (for SO; Salesperson's initials) 



  


Grouped by: N/A

  


Sorted by: Date (most recent at the top) 

TODO_TR: simple to handle actions that happened on the same day (repo, sold same day)? not a big deal to Jason if we don't do it

  


Filters: 

  * Building S/N Sequence # (auto-filled when opened from a Building record) 



  


  


TODO_TR: Can we make this a multipane?

  


Buttons: N/A

  


Development Specification

Note that this is a report on both Sales Orders and Work Orders.

  


Mockup:

  


TODO_CCI: How bad is it to put this into a single report? It becomes a repeat for list based on a list of SO's and WO's, then using local macros to split them apart. Alternatively, we can do a multipane.
