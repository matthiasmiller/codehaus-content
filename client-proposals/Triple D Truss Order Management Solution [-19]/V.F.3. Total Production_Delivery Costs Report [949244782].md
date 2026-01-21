5.6.3. Total Production/Delivery Costs Report

  


Requirements

TODO_AP: Ben Reitz 11/14/2025: Review and standardize/update as needed.

  


This is a report of Delivery records that have the "Scheduled" or the "Will Call" checkbox checked, showing various costs.

  


Title: 

  * If "Show Delivery Costs" is not checked and "Show Packing List Columns" is not checked: Total Production
  * If "Show Delivery Costs" is checked: Total Production Delivery Cost
  * If "Show Packing List Columns" is checked and "Show Delivery Costs" is not checked: Print Yard Packing List



  


Columns: 

  * Print Yard Packing List (visible only if the "Show Packing List Columns" checkbox is checked; link; opens the "Yard Packing List" printout PDF for that row)
  * Customer
  * Quote / Order (displays the ID of the linked Quote or Order; link to that record)
  * Job
  * Schedule Date
  * Made (Yes/No)
  * Made Date
  * Item (link to record)
  * Board Feet (total type = sum)
  * Will Call (Yes/No)
  * Trucker (visible only if the "Show Packing List Columns" checkbox is checked)
  * Trailer (visible only if the "Show Packing List Columns" checkbox is checked)
  * Big Truck Delivery $ (total type = sum; visible if Show Delivery Costs is checked)
  * Big Trucks Permits $ (total type = sum; visible if Show Delivery Costs is checked)
  * Big Truck Escorts $ (total type = sum; visible if Show Delivery Costs is checked)
  * Big Trucks Overnights $ (total type = sum; visible if Show Delivery Costs is checked)
  * Big Truck Miles (total type = sum; visible if Show Delivery Costs is checked)
  * Small Truck Delivery $ (total type = sum; visible if Show Delivery Costs is checked)
  * Small Truck Permits $ (total type = sum; visible if Show Delivery Costs is checked)
  * Small Truck Escorts $ (total type = sum; visible if Show Delivery Costs is checked)
  * Small Truck Overnights $ (total type = sum; visible if Show Delivery Costs is checked)
  * Small Truck Miles (total type = sum; visible if Show Delivery Costs is checked)



  


Grouped by: Status

  


Sorted by: Schedule date + Customer

  


Filters: 

  * Status (blank = all)  (multi-select drop-list of In Progress, Made, Delivered)
  * Quote / Order # (optional; number field; defaults to blank = all)
  * Start Date (blank = all)
  * End Date (blank = all)
  * Show Delivery Costs (checkbox)
  * Show Packing List Columns (checkbox; visible if the "Quote / Order #" filter is filled)



  


Buttons: 

  * New Delivery



  


Development Specification

Change Requests:

  * Ben Reitz 05/08/2025: [[[IN10789](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10791&)]] - ZTD - Allow for linking Orders and Deliveries
  * Ben Reitz 05/08/2025: [[[IN11280](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11282&)]] - ZTD - Remove unscheduled deliveries from various printouts and reports
  * Ben Reitz 11/26/2025: [[[IN12310](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12312&)]] - ZTD - Add new "Print Yard Packing List" report


