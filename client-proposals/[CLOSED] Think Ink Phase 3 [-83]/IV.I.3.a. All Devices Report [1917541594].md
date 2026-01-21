4.9.3.1. All Devices Report

  


Requirements

This is a report of all Devices in the database, with various filtering options. Note that this full report includes both managed and non-managed Devices.

  


Also note that in the future this could be a multi-pane report with the left pane showing all Devices in the Solution, and the right pane showing all parts/accessories in the Solution for that device.

  


This would be accessed from Home | Devices | All Devices. 

  


Title: All Devices

  


Columns: 

  * Description (link to record)
  * Device Nickname
  * Device Type
  * Device Tags (comma separated; wrapping text)
  * Serial #
  * Device ID 
  * Status
  * Customer
  * Monthly Service Plan 
  * Average Black Usage 
  * Average Color Usage
  * Needs Review (Yes/No)
  * Special Instructions (wrapping text) 
  * Agreement (link to record)
  * Prepay End Date (show in red if in the past; blank if N/A)



 

Grouped by: Status (Active, Available, End of Life)

  


Sorted by: Description 

  


Filters: 

  * Managed Devices Only (checkbox; defaults to unchecked)
  * Include Historical Managed Devices (checkbox; visible if Managed Devices Only is checked; if checked, the report will include historical devices in gray, and devices that have been deployed to multiple Customers will appear on the report once for each Customer) 
  * Prepay Only (checkbox; visible if Managed Devices Only is checked; if checked, the report will include only Devices with the Prepay checkbox checked) 
  * Needs Review Only (checkbox; defaults to unchecked; if checked, the report shows only Devices needing review)
  * Device Type (drop list of Device Types; defaults to blank = all)
  * Customer (drop list of all Customer contacts; filters down as you type; defaults to blank = all)
  * Managed Service Agreement (drop list of Agreement Names for the selected Customer; filters down as you type; defaults to blank = all) 
  * Model (drop list of Device Models; defaults to blank = all)
  * Serial # (text field; matches on partial)
  * Device Nickname (text field; matches on partial)
  * Device Tags (multi-select drop list of all Device Tag items; defaults to blank = all)
  * Status (multi-select drop list of Device Statuses; defaults to Active)



  


Buttons: 

  * New Device (opens a new blank Device record) 



  


Menu Visibility: All users 

  


Other Notes: 

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=104380110](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=104380110)
