7.4. All Buildings Report

  


Requirements

This is a report of all buildings in the database. Draft buildings would be hidden by default.

  


This would be accessed from the All Buildings option on the Main Menu. 

  


TODO_TR: look at their list from recording. pretty much everything on there now is stuff they use.

  


Title: All Buildings 

  


Columns: 

  * Building Category (if grouped by Building Status)
  * Building Status (if grouped by Building Category)
  * Building (serial number; link to record)
  * Building Style (name)
  * Building Size (WidthXLength)
  * Siding Color 
  * Trim Color 
  * Roof Color 
  * Built Date
  * Current Building Contact
  * Last Sale Date
  * Last Sale Type
  * Last Sale Price (Total Amount from the most recent Sale-type Sales Order) 
  * Last Delivery Date
  * Salesperson (initials) 
  * Approved By (__; show “Pending” if pending approval) 
    * TODO_TR: this is set on the Sales Order... probably not show here? or add a macro to the building record? maybe we actually need the macro to keep the WO from starting without approval?
    * Matthias Miller 10/27/2021: Add macro to building and work order



  


Grouped by: Building Category or Building Status

  


Sorted by: 

  


Filters: (note: all of these look at the current/most recent data on the building, e.g. if the building has been sold more than once)

  * Serial Number (search by partial) 
  * Group By (choice of Building Category and Building Status; default to Building Status)
  * Building Category (multi-select of Building Categories; default to include ___
  * Building Status (multi-select of Building Statuses; default to include all but Drafts) 
  * Building Style (multi-select list of all Building Styles, active and inactive)
  * Building Width (drop list of all building widths on all SKUs; blank = all)
  * Building Length (drop list of all building lengths on all SKUs; blank = all)
  * Siding Color (drop list of all, active and inactive)
  * Trim Color (drop list of all, active and inactive)
  * Roof Color (drop list of all, active and inactive)
  * Built Date (drop list of date options, see details below; defaults to Year to Date)
  * Sale Date (drop list of date options, see details below; defaults to Year to Date)
  * Delivery Date (drop list of date options, see details below; defaults to Year to Date; include future/scheduled Delivery Dates)
  * Repo Date (drop list of date options, see details below; defaults to Year to Date)
  * Sale Type (drop list of Cash, RTO; defaults to blank = all)
  * Current Building Contact (drop list of all Customer contacts, active and inactive; filters down as you type; blank = all)
  * Dealer (drop list of all Dealer names, active and inactive; blank = all)
  * Salesperson (drop list of all Salesperson names for the selected Dealer, active and inactive; blank = all)



  


All of the Date filters for this report would use the following:

TODO_TR: change to "Current Year", etc. 

  * Week to Date (starts on Monday of the current week)
  * Month to Date (starts on the 1st of the current month)
  * Year to Date (starts on January 1st of the current year)
  * Custom (shows a Start Date and End Date; default both to blank)



  


Buttons:

  * New Building (opens a new blank building record in a new tab) 



  


Color Coding: Text colors for building rows on the report should be based on various criteria: 

TODO_TR: how helpful are colors? should we encourage them to use grouping instead (at least for phase 1)?

TODO_TR: move around, spec out 

TODO_TR:

  * Could we create a list of 101 statuses for all the color coding options, then make them lookup types that let them customize the foreground and background color? We can use the Colors list. They can add to that list if needed. Show a preview label on the detail screen.
  * If we can merge this into Building Status, all the better, but not a deal breaker if we can't. It could be the logic for this status could depend on the logic for that one. (If BuildingStatus = X, then ThisNewStatus should be Y)
  * We should maybe just map out current Statuses and see how much difference there is here.


  * WO - Customer Buildings in Progress: Black text on green background 
  * WO, SO - Buildings Needing Approval: Black text on blue background 
  * WO - Completed Buildings Needing Modifications: White text on dark red background 
  * Inventory - Lot Building in Stock: Black text on white background 
  * Inventory - Lot Buildings in Stock for 24+ months: Black text on purple background
  * Buildings - Sold & not delivered: 
  * Buildings - Sold & Delivered Buildings: Hunter Green 
  * Inventory - SRB: Black text with yellow background
  * Buildings - Sold SRB: Yellow text with dark green background 
  * Buildings - Canceled Buildings: Red (sales orders that were canceled)



  


  


  


Data Access:

  


Other Notes:

  


Development Specification

Mockup: 

  


  


Tim Reitz 10/20/2021: Per Matthias, on reports we can do text and background color by row or by cell...
