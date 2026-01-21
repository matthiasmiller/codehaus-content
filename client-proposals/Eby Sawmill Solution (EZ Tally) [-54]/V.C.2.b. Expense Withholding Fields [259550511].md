5.3.2.2. Expense Withholding Fields

  


Requirements

Overview: The Expenses Withholding section tracks agreed-upon expenses that Eby's incurs (e.g. for building a road) on behalf of the landowner for an Adjustable Tiered % tract. These are deducted from the landowner Payment records like the Down Payments. Note that the Payment record tracks these amounts as negative ( * -1) so as to cancel out an equal amount of Yard Tallies and Pulpwood Loads (see the "Processing Down Payments and Expenses Withholdings" section of the proposal for more details). 

  


  * Expenses Withholding (visible if Purchase Type = Adjustable Tiered Percentages; editable only for admins; embedded spreadsheet with the following:) 
    * Columns: 
      * Expense Withholding Date (required; editable until Payment ID is set for the row; default to the current date)
      * Amount (required; editable until the corresponding Payment record is marked Paid; number field to 2 decimals; may be entered as a negative amount to cancel out part or all of an previous Expense Withholding amount)
      * Expense Withholding Notes (required; plain text field) 
      * Apply Date (required; editable until Payment ID is set for the row; default to the current date; on this date, the Amount is linked to a Payment for the Landowner)
      * Payment ID (auto-set and read-only, like the Payment ID on Down Payments) 
      * Select Payment (no column heading; ellipsis button; visible in Edit Mode if the Status of the linked Payment is not "Paid"; opens the "Select Payment Choice Report" as a child screen -- see corresponding details in the Yard Tally section of the proposal / living spec) 
      * Pmt. Settled (checkbox; auto-set and read-only; filled if the corresponding Payment record is Paid) 
      * View (link; displays as "Link"; opens the corresponding Payment record) 
    * Automatically sorted by: first by Expense Withholding Date and then by Apply Date
    * Buttons to add and remove rows ("+"/"-")
      * Note that the "-" button is hidden for rows with Paid Payments. 
    * Show 4 rows without scrolling
    * Other Notes: 
      * Note that the user can enter a negative Amount to enter a positive $ amount on the Payment (e.g. if too much has been withheld and Paid). 
    * See the Processing section below for details about how Expenses Withholdings work
    * Total Expenses Withholding Remaining (auto-calculated and read-only; shows the total amount of any unapplied Expense Withholding Amounts and any applied Expense Withholding Amounts that have not been canceled out by harvest income from Yard Tallies / Pulpwood Loads; sum of the following:)
      * Total of Expense Withholding Amounts for any rows on the table not linked to a Payment record.
      * Total of the absolute values of any non-canceled Expense Withholding Amounts on any individual linked Payment records.
        * See the Down Payments section for details about how the system handles Payment records that include both Down Payment and Expense Withholding amounts.



  


  * Other Notes:
    * See the "Processing Down Payments and Expense Withholdings" section for more details and example(s).



  


Development Specification

Change Requests: 

  * Tim Reitz 10/07/2024: [[[IN10236](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10238&)]] - ZET - Rework Payment Linking
  * 


  


  


\- To hide the "-" button for Paid rows" Have an index of Paid Payments and look at whether the referenced Payment record is Paid.

  


Ellis Miller 12/16/2022:

CCI BID: 2 HOURS

[ ] Simple RG very much like the Down Payments

[ ] Payment ID should be editable InImport.

[ ] Use Niccolas's ExpenseWithholdingRemaining macro

  


NIC BID: Included with DP

[ ] ExpenseWithholdingRemaining
