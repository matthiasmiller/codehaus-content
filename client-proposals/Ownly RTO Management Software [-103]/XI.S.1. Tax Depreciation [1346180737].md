11.19.1. Tax Depreciation

Proposal:

  * Straight-Line
  * MACRS GDS 150DB HY Convention - Mid-Quarter Convention
  * MACRS GDS 150DB HY Convention - Half-Year Convention
  * MACRS GDS 200DB HY Convention - Mid-Quarter Convention
  * MACRS GDS 200DB HY Convention - Half-Year Convention



  


NOTE:

  * Mid-Quarter Convention - 15th of the middle month of the quarter
  * Multi



  


  * Tax Schedule (drop-list of all depreciation schedules for the linked RTO Company? in the following format: "<Depreciation Method> \- <Useful Life> <Length (Years)> Years"; note that Length (Years) value and "Years" text is only included if Useful Life is "Fixed Length") 
    * Tax Schedule Method (hidden list field; list of Depreciation Methods; set when Book Schedule is set)
    * Tax Schedule Type (hidden list field; list of Useful Life; set when Book Schedule is set)
    * Tax Schedule Term Year (hidden number field; set when Book Schedule is set if Useful Life is Fixed Length)
  * Book Depreciation (dated RG; editable for users with the "Edit Depreciation Settings" permission)
    * Embedded Spreadsheet with the following:
      * Columns:
        * Date (required if there is a row in the RG; date field; validates against duplicates)
        * Depreciation $ (number string; editable __)
      * Automatically sorted by: Date (current/latest at the top)
      * Buttons to add/remove rows: "✚" / "🞭"
  * Tax Depreciation (editable for users with the "Edit Depreciation Settings" permission)
    * Embedded Spreadsheet with the following:
      * Columns:
        * Tax Year (required if there is a row in the RG; number field; 0 decimals;  error on save if not a valid year)
        * Depreciation $ (number field; 2 decimals)
      * Automatically sorted by: Tax Year (current/latest at the top)
      * Buttons to add/remove rows: "✚" / "🞭"



  


TODO:

  * Type (choice of "Book" vs. "Tax"; required)



  


  


NOTE:

[ ] We will populate
