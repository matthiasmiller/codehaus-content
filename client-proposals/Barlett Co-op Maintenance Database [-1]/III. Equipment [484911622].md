3\. Equipment

  


Requirements

The software will track active and inactive equipment. It will support searching, viewing, and editing equipment lists. Pertinent maintenance records and upcoming deadlines will be shown.

  


Equipment Report

The View Equipment report will display a criteria scan to allow you to search for equipment. If no criteria is specified, all equipment will be displayed. Options include:

  * Equipment Type -- one or more types of equipment can be selected (e.g. show all "Bulk Tank" and "Anhydrous Tank" equipment).
  * Location -- one or more locations can be specified
  * Name -- text field to type in the name of the equipment (e.g. "Liner" or "Semi" to find the Truck labeled "1997 Freightliner Semi Tractor")
  * Active status -- options to view Active, Inactive, or All equipment. Defaults to Active.
  * Group by -- options for (Default), (None), Type, and Location. If "Default", we will group by Type unless only one type is selected, then we will group by location. Users can also choose to group specifically by Type or Location.



  


Once criteria is selected, the report is displayed:

  * There will be columns for Type, Location, Name, and Inactive Date (if inactive equipment is displayed), Next Deadline (includes both inspections and other deadlines, yellow if within 30 days, red if overdue), # Open Work Orders (link to report), current mileage/hours for relevant equipment (90,000  Miles as-of  4/12017  or  1,425  Hours as-of  3/16/2016)
  * Equipment will be grouped by the specified Group By, then sorted by the other value + name (if grouped by "Type", within each type, we first by location and then by name).
  * Clicking on an equipment name will display the equipment record detail.
  * If both active and inactive equipment is shown, the inactive items will be displayed in gray at the bottom of the report.
  * There will be an option to create a new equipment record.



  


Equipment Record

Users with the "Manage equipment list" permission can create equipment and mark equipment as active or inactive. Only administrators can delete equipment.

  


The equipment record will contain:

  * Equipment name ("1997 Freightliner Semi Tractor") -- this name must be unique across locations. It can include the location name if needed to make it unique.
  * Equipment type
  * Location - list of locations
  * If equipment type tracks hours or miles, there will be "Tracking hours" or "Tracking miles" checkbox changeable by users with "Manage equipment list" permission. This can be unchecked for equipment without working odometer / hour meter.
  * Hours -- visible if type tracks hours and "Tracking hours" is checked. has link to history and an as of date. Users can update the miles whenever they wish. This will enter a new value and update the as-of date.
  * Hours -- visible if type tracks hours and "Tracking hours" is checked. has link to history and an as of date. Users can update the hours whenever they wish. This will enter a new value and update the as-of date.
  * Active checkbox -- if unchecked the "Inactive date" is automatically filled in, but can be modified. This field requires the "Manage equipment list" permission.
  * Notes - rich text field for any extra information about the equipment
  * A Create Work Order link
  * List of Open Work Orders.
  * A 8 Closed Work Orders link that displays the closed work orders.
  * A View Inspections link to show both upcoming inspections and completed inspections. Show a "(Next due 04/10/2018)" label beside the link. Show it in Yellow if < 30 days, red if overdue.
  * List of Upcoming Deadlines -- more details in following section



  


Development Specification

Report

Use three columns for hours/miles:

  


Equip| Reading| Date  
---|---|---  
90,000| Miles as-of| 04/01/2017  
1,425| Hours as-of| 03/16/2016  
  
  

