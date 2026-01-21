15.4.1. Page Count Entry

  


Requirements

This is an editable report of active "Asset-Printer"-type devices, grouped by page count status for the current billing period (needed at top, needs review (50% off) in middle, entered at the bottom)...

TODO_TR: update the description 

  


This would be accessed from ___. 

  


Title: Page Count Entry

  


Columns: 

  * Customer
  * Asset ID (link to record)
  * Model
  * Meter Read Date (editable)
  * Billing Date (editable)
  * Last Black Count
  * Black Meter Count (editable)
  * Black Used 
  * Last Color Count
  * Color Meter Count (editable)
  * Color Used 
  * Source (editable) 



  


TODO_CH: any special handling to add rows to the RG from the report? 

  


TODO_CH: can we default values for the editable cells? (e.g. Read Date and Billing Date) 

  


TODO_CH: how much of this would auto-update? (e.g. Black/Color Used, grouping)  

  


TODO_CH: do we need a column for Needs Review checkbox? 

  


Grouped by: Page Count Status

  * Needs Page Count
  * Page Count Needs Review
  * Page Count Complete



  


Sorted by: Customer then Asset ID

  


Filters: 

  * 


  


Buttons: 

  * 


  


Menu Visibility: All users can view and edit

  


Other Notes:

  


Development Specification

Mockup: 

[https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=461442254](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=461442254)

  


Ellis Miller 11/09/2021: I think pane 3 requires special entry macros that will on-save add a row to the print counts RG.

  


IN0001   CustomerName1 Date1IN1010   CustomerName2 Date2| Memo from highlighted incident in Pane 1?| Editable report for all assets for customer from Pane 1  
---|---|---  
  
  


HL Est: 16 Hours?? Lots of questions here
