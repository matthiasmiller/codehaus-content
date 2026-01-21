6.8.1.2. Top Right Pane (Yard Tallies & Misc)

  


Requirements

Top right pane: This pane shows details for Yard Tallies and other items linked to the selected Payment on the left pane. There is one row for each Yard Tally and a totals row.

  


The non-Yard Tally items are the following: Eby Freight, Down Payment Amount, and Expense Withholding Amount. These items are shown only in the totals row.

  


Note that this pane is blank if the Payment Type is Landowner Flat.

  


Title: Yard Tallies & Misc for Payments Report

Displayed Title: Yard Tallies & Misc

  


Columns: 

  * Yard Tally ID (visible if Payment Type = Landowner %, Logger, or Vendor; link to the record)
  * Tally Confirmed Date (visible if Payment Type = Landowner %, Logger, or Vendor) 
  * Total Board Feet (visible if Payment Type = Landowner %, Logger, or Vendor; number with no decimal places; total row shows sum)
  * 1st Tier Board Footage (visible if Payment Type = Landowner %; column heading displays the following from the corresponding tier from the Payment % table on the Tract record: "<Min Price> & greater - BF"; row shows the total BF for all logs on the Yard Tally within the 1st Tier; auto-calculated and read-only; number with no decimal places; total row shows sum) 
  * 1st Tier Log Value (visible if Payment Type = Landowner %; column heading displays the following from the corresponding tier from the Payment % table on the Tract record: "<Min Price> & greater - $"; row shows the 1st Tier Log Value for the Yard Tally; auto-calculated and read-only; number to 2 decimal places; total row shows sum) 
  * 1st Tier Landowner Share (visible if Payment Type = Landowner %; column heading displays the percentage for the corresponding tier from the Payment % table on the Tract record, e.g. "60%"; row shows the corresponding % of the 1st Tier Log Value for the Yard Tally; auto-calculated and read-only; number to 2 decimal places; total row shows sum) 
  * 2nd Tier Board Footage (visible if Payment Type = Landowner %; column heading displays the following from the corresponding tier from the Payment % table on the Tract record: "<Min Price> \- <Max Price> \- BF"; row shows the total BF for all logs on the Yard Tally within the 2nd Tier; auto-calculated and read-only; number with no decimal places; total row shows sum) 
  * 2nd Tier Log Value (visible if Payment Type = Landowner %; column heading displays the following from the corresponding tier from the Payment % table on the Tract record: "<Min Price> \- <Max Price> \- $"; row shows the 2nd Tier Log Value for the Yard Tally; auto-calculated and read-only; number to 2 decimal places; total row shows sum) 
  * 2nd Tier Landowner Share (visible if Payment Type = Landowner %; column heading displays the percentage for the corresponding tier from the Payment % table on the Tract record, e.g. "40%"; row shows the corresponding % of the 2nd Tier Log Value for the Yard Tally; auto-calculated and read-only; number to 2 decimal places; total row shows sum) 
  * 3rd Tier Board Footage (visible if Payment Type = Landowner %; column heading displays the following from the corresponding tier from the Payment % table on the Tract record: "<Min Price> to <Max Price> \- $"; row shows the total BF for all logs on the Yard Tally within the 3rd Tier; auto-calculated and read-only; number with no decimal places; total row shows sum) 
  * 3rd Tier Log Value (visible if Payment Type = Landowner %; column heading displays the following from the corresponding tier from the Payment % table on the Tract record: "<Min Price> to <Max Price> \- $" ; row shows the 3rd Tier Log Value for the Yard Tally; auto-calculated and read-only; number to 2 decimal places; total row shows sum) 
  * 3rd Tier Landowner Share (visible if Payment Type = Landowner %; column heading displays the percentage for the corresponding tier from the Payment % table on the Tract record, e.g. "30%"; row shows the corresponding % of the 3rd Tier Log Value for the Yard Tally; auto-calculated and read-only; number to 2 decimal places; total row shows sum) 
  * 4th Tier Board Footage (visible if Payment Type = Landowner % and if the Search by Payment ID checkbox is checked and if the selected Payment is for a Tract that has a 4th Tier; column heading displays the following from the corresponding tier from the Payment % table on the Tract record: "<Min Price> to <Max Price> \- $"; row shows the total BF for all logs on the Yard Tally within the 4th Tier; auto-calculated and read-only; number with no decimal places; total row shows sum) 
  * 4th Tier Log Value (visible if Payment Type = Landowner % and if the Search by Payment ID checkbox is checked and if the selected Payment is for a Tract that has a 4th Tier; column heading displays the following from the corresponding tier from the Payment % table on the Tract record: "<Min Price> to <Max Price> \- $"; row shows the 4th Tier Log Value for the Yard Tally; auto-calculated and read-only; number to 2 decimal places; total row shows sum) 
  * 4th Tier Landowner Share (visible if Payment Type = Landowner % and if the Search by Payment ID checkbox is checked and if the selected Payment is for a Tract that has a 4th Tier; column heading displays the percentage for the corresponding tier from the Payment % table on the Tract record, e.g. "20%"; row shows the corresponding % of the 4th Tier Log Value for the Yard Tally; auto-calculated and read-only; number to 2 decimal places; total row shows sum) 
  * 5th Tier Board Footage (visible if Payment Type = Landowner % and if the Search by Payment ID checkbox is checked and if the selected Payment is for a Tract that has a 5th Tier; column heading displays the following from the corresponding tier from the Payment % table on the Tract record: "<Max Price> & less - BF"; row shows the total BF for all logs on the Yard Tally within the 5th Tier; auto-calculated and read-only; number with no decimal places; total row shows sum) 
  * 5th Tier Log Value (visible if Payment Type = Landowner % and if the Search by Payment ID checkbox is checked and if the selected Payment is for a Tract that has a 5th Tier; column heading displays the following from the corresponding tier from the Payment % table on the Tract record: "<Max Price> & less - $"; row shows the 5th Tier Log Value for the Yard Tally; auto-calculated and read-only; number to 2 decimal places; total row shows sum) 
  * 5th Tier Landowner Share (visible if Payment Type = Landowner % and if the Search by Payment ID checkbox is checked and if the selected Payment is for a Tract that has a 5th Tier; column heading displays the percentage for the corresponding tier from the Payment % table on the Tract record, e.g. "10%"; row shows the corresponding % of the 5th Tier Log Value for the Yard Tally; auto-calculated and read-only; number to 2 decimal places; total row shows sum) 
  * Tally Amount Due (visible if Payment Type = Landowner %, Logger, or Vendor; total row shows sum)
    * If Payment Type = Landowner %, this is the Yard Tally Landowner Amount
    * If Payment Type = Logger, this is the Yard Tally Logger Amount
    * If Payment Type = Vendor, this is the Yard Tally Total Value
  * Eby Freight (visible if Payment Type = Vendor; displays Yes/No)
  * Down Payment Amount (visible if Payment Type = Landowner %; total row only; displays the sum of all Down Payment amounts for this Payment; displays as a negative number; to view all amounts, the user can open the corresponding Tract from the left pane) 
  * Expense Withholding Amount (visible if Payment Type = Landowner %; total row only; displays the sum of all Expense Withholding amounts for this Payment; displays as a negative number; to view all amounts, the user can open the corresponding Tract from the left pane)



  


Grouped by: N/A

  


Sorted by: Yard Tally ID

  


Special Filters (applying only to this top right pane): 

  * Payment (drop list of all Payment IDs; defaulted according to the selected Payment row in the left pane) 
  * Payment Type (drop list of Payment Types; defaulted according to the selection in the Payment Type filter of the left pane) 
  * Show Yard Tally Breakdowns (checkbox; defaults to checked; if checked, includes all yard tally-related columns) 
  * Show All Totals (checkbox; defaults to checked; if checked, includes Tally Amount Due and the other columns to the right; only shows grand totals for all, hiding groupings) 



  


Other Notes: 

  * As mentioned in the Columns above, the Down Payment Amount and Expense Withholding Amount columns only are filled in on the total row for a specific payment, rather than on a per-row basis, since these values are tracked on a per-Tract basis, rather than on individual Yard Tallies.



  


Development Specification

Change Requests: 

  * Tim Reitz 08/19/2024: [[[IN10016](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10018&)]] - ZET - Tract Record - Adding More Tiers 
  * 


  


  


Ellis Miller 12/22/2022:

[ ] Hide this pane for Landowner Flat.

[ ] Ask prompt of Payment ID.

[ ] Column like Yard Tally ID (visible if Payment Type = Landowner %, Logger, or Vendor) can simply always be visible since the report is not shown for Landowner Flat.

[ ] locTract is derived from PaymentID.

[ ] this is used for column headings like 1st Tier Log Value.

[ ] For Tier columns, use  YardTallyLogValue( vTierNum) and  YardTallyLandownerShare (vTierNum) from "Tally Summary Section"

[ ] For the final 4 columns, just use an NA Column Contents with an Expression Total that does a Lookup on locTract, with a SumRG on the relevant RG.

  


BID: 4 HOUR
