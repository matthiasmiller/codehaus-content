7.8. Finished Building Inventory Report

This is a report of all completed buildings (Sold, Lot, SRB, and Trade-In statuses) that haven't been delivered yet. 

TODO_TR

  


This would be accessed from a "Finished Building Inventory" menu option on the Main Menu. 

  


Title: Finished Building Inventory

  


Columns: 

  * Building Category
  * Building Status 
  * Building (serial number; link to record; with total of buildings)
  * Building Style (name)
  * Building Size (WidthXLength)
  * Location 
  * Days on Lot (# of days in current location) 
  * Salesperson (displays for sold buildings) 
  * Siding Color
  * Trim Color
  * Roof Color
  * Value ($) (Total Building Price on the Building record; with total)
  * Notes (from the Notes memo on the Building record; 



DONE_CH: would this show as plain text? or an elipsis button? 

TODO_TR: Can be both rich/plain text. Ellipsis button only if we make it an editable report, so no on that. We can limit it to the 1st paragraph if needed. Images would show up inline in the report, File attachments would show up as a link.

  * 


  


Grouped by: required choice of the following:

  * Location (with totals for Building and for Value ($); locations listed alphabetically) 
  * Building Status (with totals for Building and for Value ($); statuses listed as follows:)
    * Built
    * Sold
    * SRB (includes sold and unsold SRBs)
    * Trade-In (includes sold and unsold Trade-Ins)



  


Sorted by: Style (alphabetically), then by Size (Width then Length)

  


Filters: 

  * Customer (drop list of all Customer contacts; blank = all)
  * Dealer
  * Salesperson (drop list of all Salesperson names for the selected Dealer; blank = all)
  * Serial Number (search by partial) 
  * Building Style (multi-select list of all Building Styles)
  * Building Length (drop list of all building lengths that have been built; blank = all)
  * Building Width (drop list of all building widths that have been built; blank = all)



DONE_CH: is this OK? would this mean 2 more simple lists to track these?

TODO_TR: This is fine. We don't need simple lists, I don't think.

  * Siding Color (drop list of all)
  * Trim Color (drop list of all)
  * Roof Color (drop list of all)
  * Group By (required; choice of Location and Building Status) 
  * Location (list of all locations) 
  * 


  


Buttons: 

  * Print Selected (generates a PDF in a new tab; reflects the report) 
  * Print In Transit for Selected (generates a PDF export of the selected rows in a new tab)



DONE_CH: can we do this? 

TODO_TR: Yes. In the Dev Specs, mention that we can use the "Open Report or Graph by Selected Values"

  * Print Infosheet for Selected (generates a PDF in a new tab with an Infosheet page for each selected building)



  


Color Coding:

 TODO_TR: (SRBs should be color-coded with orange text so the users can see which are SRBs).

  


Data Access: 

  * 


  


Other Notes:

  * There would be some menu options for some pre-set versions of this report:
    * My Inventory (Building Inventory report filtered to show only buildings for the current user's dealer; note that if the Dealer has multiple lots, this will show inventory for all of the Dealer's lots)
    * Cave City Inventory (Building Inventory report filtered to show only buildings at the Cave City location)
  * The AppHosting Favorites feature can be used to set up quick access to other pre-filtered versions of this report



  


  


  


TODO_TR: incorporate above...:

Things to track: 

  * Building (serial #) 
  * Price (
  * Dealer ( 
  * (Dealer Code OR Salesperson Code) 
  * Location (



  


  * Several independent dealers
  * Track by log - keep track of what inventory is at each sales lot
  * Keep track of the home sales lot
  * Jason currently has a separate lot called “in transit”, then adds a note that the building is being moved from Location A to Location B. This works well for Jason and it pulls it from the first lot's inventory



  


Another piece that may play into the finished goods inventory is repo buildings: 

  * The RTO company buys the new building from Bald Eagle Barns
  * When the building comes back, they repo it in the system, which puts it in inventory as an SRB Class (“Sold Repo Building”) 
    * RTO company picks up the repo and delivers it back to BEB
  * It remains property of the RTO company; BEB sells it on consignment for the RTO company
    * BEB collects the payment (to the customer it looks just like a normal sale)
    * Line item discount for Used Building
    * BEB pays the RTO company for the building (the full amount - with or without sales tax?)
    * At the end of the month, BEB invoices the RTO for delivery, sales commission
  * Instead of stock building, it marks it as repo
  * When they sell it again, it does not invoice the rental company for the company -- they can run it through the quote, but it does not invoice the RTO company, or the delivery -- it just makes a generic sales order



  


Tracking Price: 

\- do we use the live/current price? or do we freeze it with the price at the time of completetion?

  


On the Finished Goods inventory report, have a column with a link to view the Info Sheet PDF (then can print from there). TODO_TR
