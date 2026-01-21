4.3.3. Truss section

Truss section (visible, editable, and at least one row required if the Truss Order checkbox is checked; located below the Customer section)

  * Embedded spreadsheet with the following:
    * Columns:
      * Qty (required; number; no decimals; error on the field if it is not less than 10,000)
      * Span Ft (optional; number; no decimals; no commas; error on the field if it is not less than 1,000)
      * Span In (optional; plain text)
      * Pitch (optional; plain text; auto-fills with /12 if a valid number is entered [e.g. 4 turns into 4/12])
      * Left O.H. (optional; editable drop-list)
      * Right O.H. (optional; editable drop-list))
      * Left Cant. (optional; editable drop-list)
      * Right Cant. (optional; editable drop-list)
      * Description (optional; plain text)
      * Unit Price (optional; number; two decimals)
      * Price (optional; number; two decimals; read-only; product of Qty and Unit Price)
    * Buttons:
      * "+" (insert row above selected row)
      * "-" (delete selected row)
      * Up (move selected row up)
      * Down (move selected row down)
      * Append Row (append one row)
      * Append Multiple Rows (append twenty rows)
  * Total Price (number; two decimals; auto-set and read-only; sum of Price for all rows in the spreadsheet)


