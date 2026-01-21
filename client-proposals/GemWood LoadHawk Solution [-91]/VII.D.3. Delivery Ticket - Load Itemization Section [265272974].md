7.4.3. Delivery Ticket - Load Itemization Section

  


Requirements

  * Load Itemization section:
    * Fill from PO (data entry drop list macro; with the following details / behaviors: 
      * drop list displays rows from the "Itemization" embedded spreadsheet on the linked Buyer Purchase Order, in the following format: "<Thickness> <Species> <Grade> (<Short Notes>)"; 
      * the user can select an item here to automatically add it to the Load Itemization for the Delivery Ticket) 
    * Add Line Item (button; visible if "Fill from PO" is not blank; with the following details / behaviors:
      *  clicking this button added a new row to the "Load Itemization" embedded spreadsheet with the following set from the selected row: 
        * Thickness 
        * Species 
        * Grade 
        * Short Notes > Notes 
        * $/BF; 
      * note that "BF Qty." is not set, to require the user to enter that data manually; 
      * after this button is clicked, the "Fill from PO" data entry drop list is cleared, to allow the user to easily select and add another row) 



  


  * Load Itemization (no label; embedded spreadsheet with the following; used for documenting the information from the paper Delivery Ticket that comes from the Member:) 
    * Columns: 
      * Thickness (optional; drop list of Lumber Thicknesses list items; filters down as you type; defaults to blank) 
      * Species (required; drop list of Species list items; filters down as you type; defaults to blank)
      * Grade (required; drop list of Lumber Grades list items; filters down as you type; defaults to blank; entering a Grade here defaults "Thickness" and/or "Species" to the prior row's value if those fields are still blank in the current row)
      * Notes (optional; plain text)
      * BF Qty. (required; number; 0 decimals; defaults to blank) 
      * $/BF (required; number; 3 decimals; defaults to blank) 
      * Member Grade $ (auto-calculated and read-only; number; 2 decimals; displays the value of "$/BF" * "Member BF Qty.", rounded to the nearest 2 decimal places)
    * Automatically sorted by: N/A (no sorting; rows remain in the sequence in which they were entered, unless manually moved up or down) 
    * Buttons to add/remove rows: "+" / "-" (hidden if "Delivery Ticket Status" = "Closed" or "Canceled") 
    * Buttons to move rows up and down (up/down arrows)
    * Show 10 rows without scrolling
    * Other Notes:
      * This embedded spreadsheet includes a blank/empty row with "Add new row..." text, for easy adding of new rows. This row disappears when the embedded spreadsheet becomes read-only.
      * Changes to columns here should be considered for the Delivery Ticket Printout and the Buyer Invoice Printout as well.)
  * Total BF Qty. (auto-calculated and read-only; displays the sum of all "BF Qty." values from the embedded spreadsheet) 
  * Total Member Grade $ (auto-calculated and read-only; displays the sum of all "Member Grade $" values from the embedded spreadsheet) 
  * No Member Grade (checkbox; defaults to not checked; if checked, "Member Payment Terms" must = "After Buyer Settlement" and the "No Buyer Invoice" checkbox is auto-checked - see corresponding specs) 



  


  * Other Line Items (embedded spreadsheet with the following: 
    * Columns: 
      * Date (required; date; defaults to the current date)
      * Type (required; drop list of "Other Line Item Types" list items; defaults to blank)
      * Description (optional; plain text; defaults to blank)
      * Amount (required; number; 2 decimals; defaults to blank)
    * Automatically sorted by: Date (most recent at the top)
    * Buttons to add/remove rows: "+" / "-" (hidden if "Delivery Ticket Status" = "Closed" or "Canceled") 
    * Show 4 rows without scrolling
    * Other Notes:
      * This embedded spreadsheet includes a blank/empty row with "Add new row..." text, for easy adding of new rows. This row disappears when the embedded spreadsheet becomes read-only.
      * Changes to columns here should be considered for the Delivery Ticket Printout as well.)
  * Total Other Line Items $ (auto-calculated and read-only; number; 2 decimals; displays the sum of the "Amount" fields from the "Other Line Items" embedded spreadsheet)



  


Development Specification

Change Requests: 

  * Tim Reitz 05/12/2025: [[[IN11460](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11462&)]] - ZGW - Delivery Ticket - Various Improvements / Bug Fixes
  * [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature
  * 


  


  


  


Ellis Miller 12/17/2024: BID 6 HOURS
