3\. Scheduling

  


Requirements

Customers

On the customer record, add a checkbox called, "Show weekly production totals".

  


Production/Inventory Locations

We need to be able to define multiple production/inventory locations. These would specify:

  * Location Name
  * Location Capacity (board feet per week)



  


Finished Goods (e.g. jobs)

The Finished Goods (one-to-one correspondence with a job) would also have the following fields:

  * Location
  * Production Required?
    * Materials Pulled Date
    * Production Start Date
    * Production Complete checkbox and date
  * Delivery Required? (true if production is required)
    * Delivery Start Date
    * Delivery Complete checkbox and date



  


Drivers

You would be able to set up and configure a list of drivers for deliveries. It would have the following fields:

  * Driver Name



  


Deliveries

Deliveries are completely independent of the truss management software. The Finished Good (job) would have an embedded spreadsheet of deliveries, that would include:

  


  * Scheduled Date
  * Hold Delivery checkbox
  * Driver
  * Delivery Notes
  * Delivered Date
  * Hidden: Load Number - used to specify which load this should go on
  * Hidden: Load Sequence - used to specify which spot it should be on the load



  


When adding or modifying a schedule date for a future date, it should clear the hold checkbox. Show a warning when modifying a schedule date from a future to a past date.

  


If a delivery does not have a future delivery date and is incomplete, it will show up for re-scheduling. See "Jobs Needing Delivery" report.

  


Deliveries can be scheduled directly from the Job record detail.

  


Delivery Checkoff

We will have a Recent Deliveries report that shows deliveries in the past week. Every day, the secretary will open that report and mark all the pending deliveries as complete. This will allow closing out multiple deliveries at a time, prompting for a delivery completion date (defaulting to previous business day).

  


Jobs Needing Delivery

This report would show all deliveries that are either on hold or are marked needing delivery without a scheduled delivery. The report will be grouped by:

  * Deliveries on Hold
  * Production Complete
  * Production Started
  * Production Required



  


You can remove jobs from hold or reschedule delivery by opening the job record itself or by opening the delivery calendar.

  


Production Calendar

The production calendar is a full screen calendar view, with a Week/Month view toggle.

  


Each Job/Finished Good would appear on the calendar on the production start date. The description would be the job name and the total board feet, and it would link to the record detail for that job. These would show up in different colors based on the production location, with an option to show only a single location or all locations. To reschedule production, you would simply drag the event to a new date.

  


Each production location's weekly total board feet would be displayed on an event on the Sunday of each week. In addition, the calendar would show the weekly total for all customers with that setting enabled on the customer record.

  


Production by Customer

We will provide a Production by Customer report. It will prompt for the customer, start date, and optional end date. If production has already been started, filter jobs based on whether production overlaps with the requested date range. If production has not been started, filter jobs based on the scheduled production date.

  


This report will be grouped by:

  * Production Scheduled
  * Production Started
  * Production Complete
  * Delivery on Hold
  * Delivery Complete



  


The report will show:

  * Job ID
  * Job Name
  * Customer PO
  * Scheduled Production Date
  * Actual Production Date (if started)
  * Delivery Date (scheduled delivery date, or the delivery completion date)



  


Delivery Scheduling

The delivery scheduling calendar will be a weekly calendar showing 5 columns for each day of the week. If a delivery is scheduled on the weekend, those days would appear as well.

  


The Delivery would show the job name and delivery address.

  


Jobs can be dragged and dropped between days, drivers, and loads.

  


Monday, Feb 10| Tuesday, Feb 11| Wednesday, Feb 12| Thursday, Feb 13| Friday, Feb 14  
---|---|---|---|---  
  
  * Driver 1
    * Load 1
      * Delivery 1
      * Delivery 2
      * (New Delivery)
    * Load 2
      * Delivery 3
      * Delivery 4
      * (New Delivery)
    * (New Load)
  * Driver 2
    * Load 1
      * Delivery 5
      * Delivery 6
      * (New Delivery)
    * Load 2
      * Delivery 7
      * Delivery 8
      * (New Delivery)
    * (New Load)
  * Driver 3
    * (New Load)

| 

  * Driver 1
    * (New Load)
  * Driver 2
    * (New Load)
  * Driver 3
    * (New Load)

| 

  * Driver 1
    * (New Load)
  * Driver 2
    * (New Load)
  * Driver 3
    * (New Load)

  
| 

  * Driver 1
    * (New Load)
  * Driver 2
    * (New Load)
  * Driver 3
    * (New Load)

  
| 

  * Driver 1
    * (New Load)
  * Driver 2
    * (New Load)
  * Driver 3
    * (New Load)

  
  
  
  


It will show dates two months into the past and four months into the future. We would have an option to view All Drivers or just a specific driver.

  


Today's schedule will be visually distinguished from the rest of the calendar.

  


Each load will have a New Delivery link. This will prompt for a Job ID. If the job has one or more deliveries on hold, it will remove them from hold and assign them to that date, driver, and load. Otherwise, it will create a new delivery for that date, driver, and load.

  


Shop Delivery Monitor

The delivery calendar will be read-only if the user does not have permission to modify schedules or jobs. This calendar will be displayed on a monitor in the shop.

  


Development Specification

Matthias Miller 02/22/2020: Is this the right terminology? What's the right relationship to the production start date/etc?

  


Matthias Miller 02/04/2020:

For calendars, could we have a JSON report that pulls data for the calendar -- how to add data if you want to? Ask prompts for current Year + Month?

We can explore this...
