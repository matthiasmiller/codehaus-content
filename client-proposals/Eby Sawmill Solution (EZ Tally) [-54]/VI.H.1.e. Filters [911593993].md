6.8.1.5. Filters

  


Requirements

Filters (all filters apply to the left pane; note that the right panes have their own special filters): 

  


  * Search by Payment ID (checkbox; if checked, all filter options except Payment ID are hidden, to allow for simple searching by ID)
  * Payment ID (visible and required if "Search by Payment ID" checkbox is checked; plain text field; defaults to blank; if a payment ID is specified, that specific payment will be displayed and other filters will be ignored; clicking Continue opens the report view based on the Payment's Type)
  * Payments Status (visible and required if "Search by Payment ID" checkbox is not checked; drop list of "Unpaid + Paid Today", "All Paid"; defaults to "Unpaid + Paid Today" for the Payments Due reports; defaults to "All Paid" for the Payments Summary reports)
    * If set to "Unpaid + Paid Today", the report includes all unpaid Payments (Status = "Open Unpaid" or "Locked Unpaid") and Paid Payments with a Payment Date of Today (this is used for the Payments Due Reports)
    * If set to "All Paid", the report includes only Payments with Status = "Paid" (this is used for the Payments Summary reports)
  * Payment Date Start (visible if Payments Status = "All Paid"; defaults to blank = all)
  * Payment Date End (visible if Payments Status = "All Paid"; defaults to blank = all)
  * Payment Type (visible and required if "Search by Payment ID" checkbox is not checked; drop list of Payment Types; defaults to blank or to the menu option selection)
  * Include Negative Payments (visible if Payment Type = Landowner Flat or Landowner %; checkbox; defaults to cleared; if filled, the report includes Payments with a negative Payment Total) 
  * Payee (visible if "Search by Payment ID" checkbox is not checked; drop list of Contacts,  filters down as you type; defaults to blank = all; list filtered according to the Payment Type selection:
    * if Payment Type = blank: show no options; 
    * If Payment Type = Landowner Flat: show all Landowner-type contacts that have one or more Tracts for which Purchase Type = Flat Payments 
    * If Payment Type = Landowner %: show all Landowner-type contacts that have one or more Tracts for which Purchase Type = Adjustable Tiered Percentages
    * If Payment Type = Logger: show all Logger-type contacts
    * If Payment Type = Vendor: show all Vendor-type contacts)
  * Due Date Start (visible if Payment Type = Landowner Flat; defaults to blank = all)
  * Due Date End (visible if Payment Type = Landowner Flat; defaults to blank = all) 
  * Tract (visible if Payment Type = Landowner Flat, Landowner %, or Logger; drop list of Tract Names, filtered according to the Payment Type selection; filters down as you type; defaults to blank = all)
    * If Payment Type = Landowner Flat, show all Tracts for which Purchase Type = Flat Payments
    * If Payment Type = Landowner %, show all Tracts for which Purchase Type = Adjustable Tiered Percentages
    * If Payment Type = Logger, show all Tracts



  


Development Specification

Change Requests:

  * Tim Reitz 08/19/2024: [[[IN10016](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10018&)]] - ZET - Tract Record - Adding More Tiers 
  * Tim Reitz 10/07/2024: [[[IN10236](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10238&)]] - ZET - Rework Payment Linking


