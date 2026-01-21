5.3.3. Contract Details 2 Section

  


Requirements

Contract Details 2 section:

  * Misc Expenses (embedded spreadsheet with the following:)
    * Columns: 
      * To (required; plain text)
      * Description (optional; plain text)
      * Amount (required; number; 2 decimals)
      * Check # (optional; number; wide enough to show 6 digits; entering a Check # automatically sets Payment Date to today and clearing it clears Payment Date)
      * Payment Date (editable)
      * Paid (checkbox; editable; auto-filled if a Payment Date is entered for the row and clears if Payment Date is cleared; filling this box sets Payment Date to today and clearing it clears Payment Date; can be manually filled if no Check # is entered)
    * Automatically sorted by: Payment Date
    * Buttons to add and remove rows ("+"/"-")
    * Show 6 rows without scrolling
    * Note that Misc Expenses is used for documentation and Tract Profitability, and is not tied out to Payment records
  * Pulpwood Prices (embedded spreadsheet with the following:) 
    * Columns: 
      * Location (required; drop list of all Pulpwood Locations, with option to add new item; validate against multiple rows for the same Location - error message on the field: "This location has already been added to this Tract.")
      * Price/Ton (required; number to two decimal places; the price that the Location is paying, used for tracking income for the tract; note that if the Price changes for a Location during harvest, the user can enter an average here to help the P&L reporting be more accurate)
      * Freight/Ton (required; number to two decimal places; used to tracking freight expenses for the tract; warning on Save if changed when the "Harvest Started" checkbox is checked: "Editing Freight/Ton can result in data discrepancies") 
      * Total Tons (auto-calculated and read-only; sum of Tons from Pulpwood Load records for the corresponding Location and Tract) 
      * Total Amount (auto-calculated and read-only; "Price/Ton" * "Total Tons")
      * Total Pulpwood Freight (auto-calculated and read-only; "Freight/Ton" * "Total Tons") 
    * Automatically sorted by: order entered (unsorted) 
    * Buttons to add and remove rows ("+"/"-") 
    * Show 3 rows without scrolling
      * Confirm that this still is the case after making the other changes. 
    * Other Notes: 
      * This embedded spreadsheet uses 2-line column headings.



  


Development Specification

CCI BID: 2 hours

  


Change Requests:

  * Ben Reitz 05/01/2025: [[[IN10943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10945&)]] - ZET - Fix Timber Freight Calculations (prev. Tract Profitability Report - Incorrect formula)


