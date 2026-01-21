4.3.2. Changes to the "Load Itemization" Section

  


Requirements

Load Itemization section: 

  


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



  


Development Specification

Ellis Miller 09/10/2025: 

[ ] POItemRowDescription macro that formats it

[ ] POLookupRowIDFromRowDesc that returns the matching Row ID

[ ] Copy across fields with that row ID
