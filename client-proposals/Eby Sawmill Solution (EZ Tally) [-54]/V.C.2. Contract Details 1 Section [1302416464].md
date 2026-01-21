5.3.2. Contract Details 1 Section

  


Requirements

Contract Details 1 section:

  * Landowner (embedded spreadsheet with the following:) 
    * Column(s): 
      * Landowner (required; drop list of active Landowner-type Contacts; filters down as you type; validate against multiple rows for the same Landowner - error message on the field: "This landowner has already been added to this Tract.")
      * Primary (checkbox; auto-set and read-only; sets to filled for the top row)
    * Automatically sorted by: Order of entry (unsorted)
    * Buttons to add and remove rows ("+"/"-"). New rows are added to the bottom.
    * Show 3 rows without scrolling
    * Other notes:
      * At least one Landowner is required for each tract - error on Save validation message: "At least one Landowner must be specified for this Tract."
      * All Landowner Payments for a Tract are linked to the Primary Landowner (the first Contact entered for the Tract)
      * A Landowner with one or more Payments for this Tract cannot not be deleted from the Tract record - error on Save validation message: "This Tract has payments for one or more Landowners not listed on the Tract: <A>, <B>, <C>. Please add the Landowner(s) to the Tract or change the Payee on the Payment records." 
  * New Landowner (link, creates a new Contact record, defaulting Contact Type to Landowner; after the new contact has been saved, the new name will show up as an option in the Landowners drop lists)
  * Eby's Timber Freight Rate ($/mbf; no decimals; used for tracking freight expenses for the tract) 
  * Purchase Type (required; drop list; read-only if there is one or more Paid Payments for a landowner for the Tract; choice of:) 
    * Adjustable Tiered Percentages
    * Flat Payments
  * Set up Payment (visible if Purchase Type = Flat Payments; link; opens a new Payment record in a new tab, with the following fields defaulted: Payment Type = Landowner Flat, Tract = current Tract; Payee = Primary Landowner)
  * Adjustable Tiered Percentages (visible for respective Purchase Type; embedded spreadsheet of:)
    * Columns: 
      * Min Price $/MBF (required; number with no decimals; editable if the "Harvest Started" checkbox is not checked; defaults to 0 for the initial row)
      * Max Price $/MBF (number with no decimals; auto-calculated and read-only; $1 less than the next higher row; highest/top row would be blank = infinity) 
      * Payment % (required; number; no decimals; editable if the "Harvest Started" checkbox is not checked)
      * Tier (auto-set and read-only; "1st" for the top row or if there is only one row, "2nd" for the second row, "3rd" for the third row, "4th" for the fourth row, "5th" for the fifth row)
    * Automatically sorted by: Min Price $/MBF (highest at the top)
    * Buttons to insert and delete rows, visible if the "Harvest Started" checkbox is not checked ("+"/"-")
    * Show 5 rows without scrolling 
    * Other Notes:
      * This is limited to 5 tiers for reporting purposes. However, the software can be expanded to additional tiers in the future if needed. If a user attempts to add a fourth row, the following validation message displays on the "+" button: "Only 5 tiers can be specified."
      * The bottom row must always have a Min Price of 0 - error on Save if non-zero: "The Min Price for the lowest row must be $0."
      * The Min Price cannot be duplicated on multiple rows - error on Save if duplicates exist: "Min Price cannot be the same on more than one row."
      * The Payment % cannot be duplicated on multiple rows - error on Save if duplicates exist: "Payment % cannot be the same on more than one row." 
  * Landowner Pulpwood Rate (visible and required if Purchase Type = Adjustable Tiered Percentages; $/ton; two decimals; used for tracking expenses for the Tract; warning on Save if changed when there is at least one Pulpwood Load record linked to the Tract: "There already is at least one load of pulpwood recorded for this Tract. Changing the Landowner Pulpwood Rate will result in data discrepancies.")



  


Development Specification

Change Requests: 

  * Tim Reitz 08/19/2024: [[[IN10016](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10018&)]] - ZET - Tract Record - Adding More Tiers 
  * 


  


  


_TR: Make sure that income/expenses are handled the way the clients want (see recording from call with clients on 10/21/22, about 15 min in).

Tim Reitz 08/19/2024: I think this probably can be considered resolved. 

  


Ellis Miller 12/15/2022:

DESIGN:

[ ] Basic initial fields (4 HOURS)

[ ] LandOwner Primary is just a readonly macro that returns true for first RG Row.

[ ] Two report links to create records

[ ] Need to add validation to not delete a paid Landowner.

[ ] Adjustable Tiered Percentages (4 HOURS)

[ ] When sorting, make sure that blank sorts to the top so that new rows are always at the top.

[ ] CCI: please let Tim know if you have questions on the Down Payment/Expense Withholding features. Also, please make a note in the testing job(s) for those features to ask the client for input/approval after the job(s) have been tested, so that we can make sure that things are working as desired.=
