4.3.7. Lumber section

Lumber section (visible, editable, and at least one row required if the Lumber Order checkbox is checked; located below the Truss Prints section)

  * Embedded spreadsheet with the following:
    * Columns:
      * Unsold Inventory (read-only number; no decimals; this is the remaining SKU Lot amount for the selected SKU; defaults to gray text, but is red if zero or negative; warning on Save is zero or negative: "Some Lumber items will run out of inventory)
      * Qty (required if an Item is selected; number; no decimals; no commas; error on the field if it not less than 10,000)
      * Feet (number; no decimals; error on the field if it is not less than 100; error on Save if selected Item uses Ft UOM and Feet and Inches are blank: "<Item Desc> requires that feet or inches is defined. (Field: Feet)")
      * Inches (number; error on the field if the number is more than 11 and if Feet is not blank; if Feet is blank and a value of more than twelve is entered in Inches, the Inches will automatically be converted to Feet and Inches)
      * Item Description (optional; drop-list of Lumber category SKU descriptions)
      * More Info (ellipses button if an Item Description is selected; the button opens a read-only memo that displays the Notes for the selected SKU)
      * Addl. Descr. (optional; plain text)
      * Load # (number; no decimals; visible and required if Multiple Loads is checked; error on the field if the number is not between one and five)
        * The color of the Price column varies according to Load #:



Load 1 - violet

Load 2 - green

Load 3 - blue

Load 4 - pink

Load 5 - brown

  * Unit Weight (optional; number; two decimals; wide enough for 999.99)
  * Weight (read-only macro; number; two decimals; product of Qty and Unit Weight for that row; wide enough for 99,999.99)
  * Unit Price (optional; number; two decimals)
  * Price (read-only macro; product of Qty and Unit Price)


  * Buttons:
    * "+" (insert row above selected row)
    * "-" (delete selected row)
    * Up (move selected row up)
    * Down (move selected row down)
    * Append Row (append one row)
    * Append Multiple Rows (append twenty rows)
  * Show __ rows without scrolling


  * Total Weight (read-only macro; number; two decimals; sum of "Weight" for all rows in the spreadsheet; wide enough for 999,999.99)
  * Total Price (number; two decimals; read-only; sum of Price for all rows in the spreadsheet)


