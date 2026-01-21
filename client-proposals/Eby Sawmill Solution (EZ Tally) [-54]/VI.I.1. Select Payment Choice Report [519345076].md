6.9.1. Select Payment Choice Report

  


Requirements

Overview: This is report of Payment records with Status = "Open Unpaid" and "Locked Unpaid", and based on the selected filters. One row is included at the top of the report for "(none)", to allow the user to completely unlink an item from a Payment. Note that this report normally is accessed via the "Select Payment Choice Report" that opens up on the Yard Tally or Pulpwood Load record.

  


Accessed from: N/A (none - always runs on an individual record) 

  


Title: Select Payment 

  


Columns: 

  * Status
  * Payment ID (link to open the record; displays the Payment ID)
  * Notes (displays the text entered in the Notes field of the Payment record, if any)
  * Amount 
  * Type 
  * Tract 
  * Payee 



  


Grouped by: N/A

  


Sorted by: Payment ID (in reverse, so that "Open Unpaid" items are at the top) 

  


Filters: 

  * Payment Type (required; drop list of Payment Types) 
  * Payee (required; drop list of Contacts, filters down as you type; defaults to blank = all; list filtered according to the Payment Type selection: 
    * if Payment Type = blank: show no options; 
    * If Payment Type = Landowner Flat: show all Landowner-type contacts that have one or more Tracts for which Purchase Type = Flat Payments 
    * If Payment Type = Landowner %: show all Landowner-type contacts that have one or more Tracts for which Purchase Type = Adjustable Tiered Percentages
    * If Payment Type = Logger: show all Logger-type contacts
    * If Payment Type = Vendor: show all Vendor-type contacts)
  * Tract (visible and required if Payment Type = Landowner Flat, Landowner %, or Logger; drop list of Tract Names, filtered according to the Payment Type selection; filters down as you type; defaults to blank = all)
    * If Payment Type = Landowner Flat, show all Tracts for which Purchase Type = Flat Payments
    * If Payment Type = Landowner %, show all Tracts for which Purchase Type = Adjustable Tiered Percentages
    * If Payment Type = Logger, show all Tracts; 
    * Note that this is basically the same as the Tract filter on the Master Payments Report, so changes here could be reflected there and vice versa)



  


Buttons: 

  * New Payment (opens a new Payment record with Payment Type, Tract (where applicable), and Payee automatically filled, based on the selections in the filters)



  


Menu Visibility: N/A 

  


Other Notes: 

  * N/A



  


Development Specification

Change Requests:

  * Tim Reitz 10/07/2024: Added in [[[IN10236](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10238&)]] - ZET - Rework Payment Linking


