5.3.2.1. Down Payments Fields

  


Requirements

Overview: The Down Payments section tracks down payments made to landowners for Adjustable Tiered % tracts. The user will manually enter a check number and a date (the date that the down payment was made). The user will also enter the date that the amount should be applied (linked) to a payment record for the landowner. The Solution automatically ties out the down payment to the Payment record on or after that date. Note that the Payment record tracks these amounts as negative ( * -1) so as to cancel out an equal amount of Yard Tallies and Pulpwood Loads (see the "Processing Down Payments and Expenses Withholdings" section of the proposal for more details). 

  


  * Down Payments (visible if Purchase Type = Adjustable Tiered Percentages; editable only for Admins; embedded spreadsheet with the following:) 
    * Columns: 
      * Down Payment Date (required; editable until Down Payment Check # is set for the row; default to the current date) 
      * Down Payment Amount (required; editable until the corresponding Payment record is marked Paid; number field to 2 decimals; may be entered as a negative amount to cancel out part or all of an previous Down Payment amount)
      * Down Payment Check # (required; editable until Payment ID is set for the row; number field; wide enough to show 6 digits)
      * Apply Date (required; editable until Payment ID is set for the row; default to the current date; on this date, the Amount is linked to a Payment for the Landowner - see below)
      * Payment ID (auto-set and read-only; when the Apply Date for the row = the current date or a past date, this sets to the earliest unpaid Payment record for the Primary Landowner Contact + Tract; automatically set/linked on Save, or via the "Create and Link All Payments" background process, which runs daily at 3:00am, if it hasn't been set already; if no such unpaid Payment record exists at that time, the Solution will automatically create one when the background process is run and apply that Payment ID here; Payment is unlinked on Save after a row is removed) 
      * Pmt. Settled (checkbox; auto-set and read-only; filled if the corresponding Payment record is marked Paid)
      * View (link; displays as "Link"; opens the corresponding Payment record)
    * Automatically sorted by: first by Down Payment Date and then by Apply Date
    * Buttons to add and remove rows ("+"/"-")
      * Note that the "-" button is hidden for rows with Paid Payments. 
    * Show 4 rows without scrolling
    * Other Notes: 
      * Note that the user can enter a negative Amount to enter a positive $ amount on the Payment (e.g. if too much Down Payment has been added and Paid). 
      * See Processing Section below for more details about how Down Payments work
  * Total Down Payment Remaining (auto-calculated and read-only; shows the total amount of any unapplied Down Payment Amounts and any applied Down Payment Amounts that have not been canceled out by harvest income from Yard Tallies / Pulpwood Loads; sum of the following:)
    * Total of Down Payment Amounts for any rows on the table not linked to a Payment record.
    * Total of the absolute values of any non-canceled Down Payment Amounts on any individual linked Payment records.
      * If a Payment record contains amounts for both Down Payment and Expenses Withholding, the system first pays off the full applied Down Payment Amount, and then pays off the full applied Expenses Withholding Amount.



  


  * Other Notes:
    * See the "Processing Down Payments and Expense Withholdings" section for more details and example(s).



  


Development Specification

\- To hide the "-" button for Paid rows" Have an index of Paid Payments and look at whether the referenced Payment record is Paid.

  


\- For linking Down Payment and Expenses Withholding RG rows with Payments: Have an .x30 that runs at or around 3:00am every day to find all rows with an Apply Date on or before today that do not have a Payment ID, and assign them them Payment ID as described (consider using a hidden field that can trigger field change expressions that automatically populate the Payment IDs).

  


Ellis Miller 01/19/2023: TractDownpaymentRemaining (For Nic) Sum:

  * Down Payment Amount for rows not tied to a payment record
  * Sum of negative balances on all referenced Payment records (use a sorted pipe-list of PaymentIDs so that if two rows point to the same payment, we only examine the payment record once). If Payment Total is less than 0, use the absolute value of the Total for that Payment record; otherwise use 0 for that Payment record.
    * Amount remaining: if (PaymentTotal < 0, Abs(PaymentTotal), 0)
    * NOTE: Talk to me bofore coding. This became more complex with the spec above in situations where we have both downpayment and expense withholding
  * Think through Payment records that cover both Down Payment and Expenses Withholding items



  


  


Ellis Miller 12/16/2022: 

CCI BID: 3 HOUR

[ ] Add basic RG with behaviors as specified.

[ ] Payment ID: Editable InImport. No coding here. Niccolas will provide in Processing section.

[ ] Settled: Macro Lookup if Payment is Paid

[ ] View: Autopush to open payment

[ ] Downpayment Remaining: Display macro that Niccolas provides

  


NIC: 

[ ] Downpayment Remaining macro: 4 HOUR
