4.3.8. Metal section

Metal section (visible, editable, and at least one row required if the Metal Order checkbox is checked; located below the Lumber section if Lumber section is visible; otherwise located below the Truss Prints section):

  * Central States (checkbox; when checked, unchecks Everlast checkbox; defaults to unchecked)
  * Everlast (checkbox; when checked, unchecks Central States checkbox; defaults to unchecked)
  * Embedded spreadsheet with the following:
    * Columns:
      * Qty (required if an Item is selected; number; no decimals; no commas; error on the field if it not less than 10,000)
      * Feet (number; no decimals; error on the field if it is not less than 100; error on Save if selected Item uses Ft UOM and Feet and Inches are blank: "<Item Desc> requires that feet or inches is defined. (Field: Feet)")
      * Inches (number; cannot be more than eleven if Feet is not blank; if Feet is blank and a value of more than twelve is entered in Inches, the Inches will automatically be converted to Feet and Inches)
      * " (optional; checkbox; when checked, copies Item Description and Color from the row above)
      * Item Description (optional; drop-list of Metal category SKU descriptions)
      * '' (optional; checkbox; when checked, copies Item Description from the row above)
      * More Info (ellipses button if an Item Description is selected; the button opens a read-only memo that displays the Notes for the selected SKU)
      * Addl. Descr. (optional; plain text)
      * Color (optional; drop-list)
      * '' (optional; checkbox; when checked, copies Color from the row above)
      * Unit Wt (optional; Weight per Foot * Length in Feet; wide enough for 99.99)
      * Weight (read-only macro; number; two decimals; product of Qty and Unit Weight for that row; wide enough for 9,999.99)
      * Unit Price (optional; Price per Foot * Length in Feet)
      * Total Price (read-only macro; product of Qty and Unit Price)
    * Buttons:
      * "+" (insert row above selected row)
      * "-" (delete selected row)
      * Up (move selected row up)
      * Down (move selected row down)
      * Append Row (append one row)
      * Append Multiple Rows (append twenty rows)
  * Total Weight (read-only macro; number; two decimals; sum of "Weight" for all rows in the spreadsheet; wide enough for 999,999.99)
  * Total Price (number; two decimals; read-only; sum of Price for all rows in the spreadsheet)


