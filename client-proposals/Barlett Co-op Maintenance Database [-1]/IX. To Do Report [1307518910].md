9\. To Do Report

  


Requirements

Menu

There will be two links on the menu:

  * My Tasks -- the tasks for the current user, plus any tasks for their location. 
  * Other Tasks -- Prompts for one or more users and/or one or more locations. If left blank, all tasks are listed. If both users and locations are specified, it will show tasks for all selected users AND all tasks for the selected locations.



  


Reports

The To Do Reports that combines all of the upcoming issues:

  * Equipment deadlines -- any upcoming deadlines within the time range
  * Work orders -- any open work orders
  * Upcoming Inspections -- any upcoming inspections within the time range
  * Open inspections -- all open inspections



  


They will default to show one month in the future, but this range can be modified.

  


The report will show separate lists for deadlines, work orders, and inspections. During the development phase, we will work with Bartlett Co-op to determine the exact order and contents of these reports.

  


Record Integration

The Inspection and Work Order records will be changed to show if there are other tasks listed on the equipment record:

  


Equipment:  2009 Ford Truck

      (5 Other Tasks)

  


Equipment:  2009 Ford Truck

      (0 Other Tasks)

  


This will include any upcoming inspections in next 30 days, any open inspections, any open work orders, and any equip deadlines in the next 30 days. Need to subtract out this inspection/work order if it’s open.

  


Development Specification

Need to calculate # of tasks, subtracting out ourselves. Use macro: EquipmentTasksString( vSubtractOne)

  


If location is blank and one user is specified, then use that user's location.
