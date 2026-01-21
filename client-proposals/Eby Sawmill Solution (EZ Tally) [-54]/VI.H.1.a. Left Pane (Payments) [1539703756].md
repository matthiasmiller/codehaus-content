6.8.1.1. Left Pane (Payments)

  


Requirements

Left pane: This pane shows Payment records according to the selected filters, with one row for each Payment.

  


Title: Payments Due

  


Columns:

  * Payment ID (visible for all Payment Types; link to record)
  * Payee (visible for all Payment Types)
  * Tract Name (visible if Payment Type = Landowner Flat, Landowner %, or Logger; link to record)
  * Flat Payment Subtype (visible if Payment Type = Landowner Flat)
  * Flat Payment Due Date (visible if Payment Type = Landowner Flat; editable)
  * Flat Payment Amount (visible if Payment Type = Landowner Flat; looks at the Flat Payment Amount field on the record; editable for Payments with Status = "Open Unpaid" or "Locked Unpaid")
  * Amount Paid (visible if Payment Type = Landowner %; displays the corresponding value from the record; total row shows sum) 
  * Calculated Amount (visible if Payment Type = Landowner %, Logger, or Vendor; displays the corresponding value from the record; total row shows sum)
  * Check # (visible for all Payment Types; editable)
  * Check Amount (visible for all Payment Types; editable; same behaviors as the corresponding field on the Payment record; total row shows sum)  
  * Notes (visible for all Payment Types; plain text; editable)
  * Payment Date (visible for all Payment Types; editable; same behaviors as the corresponding field on the Payment record)
  * PDF (visible if Payment Type = Landowner %, Logger, or Vendor; clicking the button generates the corresponding PDF for that row's Payment; see the corresponding Printout sections of the proposal)
    * If Payment Type = Landowner %: Landowner % Payment Summary Printout PDF
    * If Payment Type = Logger: Logger Payment Summary Printout PDF
    * If Payment Type = Vendor: Yard Tally Summary Printouts PDF (combining all summaries for Yard Tallies linked to the Payment record into one PDF) 
  * Excel visible if Payment Type = Landowner % or Logger; clicking the button generates the corresponding Excel file for that row's Payment and downloads it; see the corresponding Printout sections of the proposal)
    * If Payment Type = Landowner %: Landowner % Payment Summary Printout Excel file
    * If Payment Type = Logger: Logger Payment Summary Printout Excel file



  


Grouped by: Open Unpaid, Locked Unpaid, Paid

  


Sorted by: Payee, then Payment ID

  


Development Specification

Change Requests: 

  * Tim Reitz 10/07/2024: [[[IN10236](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10238&)]] - ZET - Rework Payment Linking 
  * Tim Reitz 10/04/2025: [[[IN11651](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11653&)]] - ZET - Landowner % Payments - Add Down Payment Info
  * 


  


  


Ellis Miller 12/22/2022: 

  


BID: 4 HOUR
