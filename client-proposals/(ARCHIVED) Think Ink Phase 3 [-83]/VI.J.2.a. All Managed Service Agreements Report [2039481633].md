6.10.2.1. All Managed Service Agreements Report

  


Requirements

TODO_IDD: clean up

  


This is a two-pane report of all Managed Service Agreement records and their included Devices, with various filtering options. Note that filtered versions of this report can be used for other reports.

  


This would be accessed from Home | Managed Service Agreements | All Managed Service Agreements.

  


Title: 

  * If Customer filter is blank = all, then the title is "Managed Service Agreements"
  * If a Customer is selected, then the title is "Agreements for <Customer Name>"



  


Left Pane:

  * Columns: 
    * Customer
    * Agreement Name (link to record)
    * Black Meter Type (required; drop list of Per Group, Per Device) 
    * Color Meter Type (required; drop list of Per Group, Per Device) 
    * Billing Frequency (required; drop list of Monthly, Quarterly; applies only to base charges since page counts will all be billed quarterly)
    * Billing Address (__
    * Location Address (__
    * Devices (list all __ 



  


Right Pane: TODO_IDD: included devices

  * Columns:
    * 


  


Grouped by: Agreement Sales Rep

  


Sorted by: Customer

  


Filters: 

  * Customer (drop list of Customer-type contacts; filters down as you type; defaults to blank = all) 
  * Status (multi-select drop list of Agreement Statuses; defaults to blank = all)
  * Agreement Sales Rep (drop list of all Employee contacts; defaults to blank = all) 
  * TODO_JM: others filters? 



  


Buttons: 

  * New Agreement (opens a blank new record)



  


Menu Visibility: All users

  


Other Notes:

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1649178932](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1649178932)
