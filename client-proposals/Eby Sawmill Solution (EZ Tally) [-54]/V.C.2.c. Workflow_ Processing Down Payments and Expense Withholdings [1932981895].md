5.3.2.3. Workflow: Processing Down Payments and Expense Withholdings

  


Requirements

Processing Down Payments and Expense Withholdings: 

  


Process in the EZ Tally Solution:

  * The user adds rows to the corresponding table.
  * When the Apply Date for a row arrives, the "Create and Link All Payments" background process runs before the start of the workday and the row is automatically linked to an unpaid Payment record as a negative amount.
    * Note that if the Apply Date is set to on or before the current date, the row will be linked to the Payment record the next time the "Create and Link All Payments" background process is run (either automatically the next morning or manually). 
  * Yard Tallies and Pulpwood Loads are applied to the Payment record as positive amounts until the Calculated Amount for the Payment is positive, at which point it can be paid to the Landowner. 
    * Note that Payments with a negative Calculated Amount would normally be excluded from the Payments reports, but can optionally be shown so that Payment Summaries can be generated for these payments if needed.
  * If a user wishes to break a Down Payment into multiple smaller payments, this can be done before the linked Payment record has been marked as Paid. The user can add one or more new rows to the table, and set the Amounts and Apply Dates for all of them as desired.



  


  


Example 1: 

  * For a Tract, a user sets up the following: 
    * Down Payment row with Amount = $2,000 and Apply Date = 10/31/2023. 
    * Down Payment row with Amount = $1,000 and Apply Date = 11/30/2023. 
    * Expense Withholding row with Amount = $500 and Apply Date = 10/30/2023. 
  * On the Tract: 
    * Down Payment Remaining = $3,000 
    * Expense Withholding Remaining = $500
  * On 10/31/2023, the background process runs to link the appropriate rows to a new Payment record. 
    * On the Payment, the Calculated Amount = -$2,500 ($2,000 applied DP Amount + $500 applied EW Amount) 
    * On the Tract: 
      * Down Payment Remaining still = $3,000 (the $1,000 that has not been applied to a Payment record, plus the absolute value of the $2,000 that has been applied) 
      * Expense Withholding Remaining still = $500 (the absolute value of the amount that has been applied to a Payment record) 
  * On 11/1/2023, a Pulpwood Load is recorded with Landowner Amount = $900
    * On the Payment, the Calculated Amount = -$1,600 (-$2,500 + $900) 
    * On the Tract: 
      * Down Payment Remaining = $2,100 (all of the Landowner Amount from the Pulpwood Load is entered against the applied DP Amount) 
      * Expense Withholding Remaining still = $500
  * On 11/2/2023, a Yard Tally is recorded with Landowner Amount = $1,200
    * On the Payment, the Calculated Amount = -$400 (-$1,600 + $1,200) 
    * On the Tract: 
      * Down Payment Remaining = $1,000 ($1,100 of the Landowner Amount from the Yard Tally is entered against the applied DP Amount, and now only the unapplied Amount is remaining) 
      * Expense Withholding Remaining still = $400 (the remaining $100 of the Landowner Amount from the Yard Tally is entered against the applied EW Amount) 
  * On 11/3/2023, another Yard Tally is recorded with Landowner Amount = $800
    * On the Payment, the Calculated Amount = $400 (-$400 + $800) 
    * On the Tract: 
      * Down Payment Remaining = $1,000 (none of the Landowner Amount from the Yard Tally is entered against the applied DP Amount, since only the unapplied Amount is remaining) 
      * Expense Withholding Remaining still = $0 (the $400 of the Landowner Amount from the Yard Tally is entered against the applied EW Amount, canceling it out, and since there are no more EW rows, this is $0) 
  * And so on.



  


Development Specification

TODO_CH: Tim Reitz 11/03/2023: Let's give some "real-life" examples here.

  


Std Tract Update Payment IDs.x30list

Tim Reitz 12/11/2023: Note: Renamed to "Std Service Update Payment IDs"

Tim Reitz 06/10/2024: Renamed to "Create and Link All Payments"

[ ] Add UnpaidPaymentsByTractAndPaymentType.ndx -- BinStrings for ListNum(TractID) + ListNum(PaymentType) + ListNum(PaymentID).

[ ] Create a "Std Needed Tract Payments.r20" \-- columns for Tract ID and Payment Type, can run on all Tracts checking for blank Payment ID's for the 3 RG's. Use Repeat for List with Payment Type options:

\- Landowner Percent: Include row if we don't have an unpaid payment for this type AND we need it: if any Down Payments within date range, Expenses within range, or Pulpwood Loads, or Yard Tallies for this tract don't have a Payment ID

\- Logger: Include row if we don't have an unpaid payment for this type AND we need it: if any Pulpwood Loads or Yard Tallies don't have a logger Payment ID

[ ] An x30 uses this r20 to create the Unpaid Payment records for Tract and Type so that we have all needed Payment records.

[ ] Then have an Tract x30 that goes through the various RG's and fills in the Payment ID's as needed.

[ ] Then have an Yard Tallies x30 that goes through and fills in the Payment ID's as needed.

  


BID: 2 Days
