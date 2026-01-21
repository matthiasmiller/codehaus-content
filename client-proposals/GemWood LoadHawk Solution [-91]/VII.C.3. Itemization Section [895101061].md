7.3.3. Itemization Section

  


Requirements

  * Itemization section (spans both columns; located beneath the "Purchase Order Overview" and "Documentation" sections):
    * Itemization (no label; embedded spreadsheet with the following:)
      * Columns:
        * Thickness (optional; drop list of Lumber Thicknesses list items; filters down as you type; defaults to blank)
        * Species (required; drop list of Species list items; filters down as you type; defaults to blank)
        * Grade (required; drop list of Lumber Grades list items; filters down as you type; defaults to blank; entering a Grade here defaults "Thickness" and/or "Species" to the prior row's value if those fields are still blank in the current row)
        * Short Notes (optional; plain text)
        * Buyer Notes (ellipsis button; opens a child screen with a memo) 
        * BF Qty. (number; 0 decimals; defaults to blank; with the following behaviors:
          * if "Close Type" = "Load-Based", editable and required;
          * if "Close Type" = "Date-Based", blank and read-only)  
        * $/BF (required; number; 3 decimals; defaults to blank)
        * Itemization Row ID (hidden column; auto-set and read-only; number; unique identifier for the row)
      * Automatically sorted by: N/A (no sorting, rows remain in the sequence they were entered, unless manually moved up or down)
      * Buttons to add/remove rows: "✚" / "🞭" (hidden if "Status" = "Closed" or "Canceled")
      * Buttons to move rows up and down (up/down arrows)
      * Show 6 rows without scrolling
    * Special Instructions (optional; memo; defaults to the text from the "Special Instructions for Purchase Orders" memo from the selected Buyer's Contact record)



  


Development Specification

Change Requests: 

  * Added in [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature


