3.3. Add Feature for Filling Multiple Descriptions on Metal Orders

  


Requirements

If a Metal order has a lot of the same of rows with the same Item or Color (but different lengths), Triple D would like to have a way to quickly fill in a bunch of the rows/cells with that value. They have done copy and paste at times. This isn't a huge deal, but it would be a cool feature to have.

Add an option to fill Description and/or Color for a row based on the row above:

  * Add 3 columns with checkboxes to the embedded spreadsheet: 
    * One between "Inches" and "Item Description": This should copy both Description and Color from above. 
    * One between "Item Description" and "More Info": This should copy just Description from above. 
    * One between "Color" and "Unit Weight": This should copy just Color from above. 
  * For all 3 of these, use ditto marks for the column heading, to not make the columns (and thus the embedded spreadsheet) too wide. Use one set of marks per column ( " ). 
    * John doesn't want these new columns to take up too much space. 
  * Default the checkboxes to unchecked. 
  * If a checkbox is checked, fill the corresponding cell with the information that is in the cell(s) in the row directly above it, then clear the checkbox. 
  * For the top row, hide the checkboxes if possible (since there is nothing above that row to copy down).



  


Additional Feature (if desired): 

  * Checkboxes would not immediately clear after checking them. They would remain checked as long as the rows match, and be clear if the rows do not match. 
  * If the cell above a cell with copied data is changed, clear the corresponding checkbox. 
  * Unchecking a box would clear the description for the corresponding cell(s). 
  * If adjacent cells match, the corresponding checkbox would be filled.



  


Time Estimate: 1 day

  


Development Specification

Tim Reitz 07/15/2021: From [[[IN4612](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-4614&)]] - ZTD - Changes to the Quote/Order Detail & Related Printouts:

  


Metal Order - Filling Multiple Descriptions: If an order has a lot of the same of rows with the same Item or Color (but different lengths), Triple D would like to have a way to quickly fill in a bunch of the rows/cells with that value. They have done copy and paste at times. This isn't a huge deal, but it would be a cool feature to have. Let's look at giving them the option to fill Description and/or Color for a row based on the row above. 

  * Add 3 columns with checkboxes to the embedded spreadsheet: 
    * One between "Inches" and "Item Description": This should copy both Description and Color from above. 
    * One between "Item Description" and "More Info": This should copy just Description from above. 
    * One between "Color" and "Unit Weight": This should copy just Color from above. 
  * For all 3 of these, use ditto marks for the column heading, to not make the columns (and thus the embedded spreadsheet) too wide. Use one set of marks per column ( " ). 
    * John doesn't want these new columns to take up too much space. 
  * Default the checkboxes to unchecked. 
  * If a checkbox is checked, fill the corresponding cell with the information that is in the cell(s) in the row directly above it, then clear the checkbox. 
  * For the top row, hide the checkboxes if possible (since there is nothing above that row to copy down).



Additional Feature: 

Tim Reitz 07/15/2021: Would this be additional work, or is it included in the 1 day estimate? Would removing the following items reduce the estimate to 1/2 day?

  * Checkboxes would not immediately clear after checking them. They would remain checked as long as the rows match, and be clear if the rows do not match. 
  * If the cell above a cell with copied data is changed, clear the corresponding checkbox. 
  * Unchecking a box would clear the description for the corresponding cell(s). 
  * If adjacent cells match, the corresponding checkbox would be filled.  



Ellis Miller 06/11/2021: Yes, included in subscription.

Tim Reitz 06/29/2021: Per Ellis: 

  * Use editable macros for these columns:
    * * OrderMetalMatchPriorDesc
    * * OrderMetalMatchPriorColor
    * * OrderMetalMatchPriorDescAndColor
  * The macro returns true if the items match the prior row. The editable macro is visible except for the first row.
  * OnChange, when checking we copy the prior rows values using [p1] or something like that. When unchecking, we blank it out.



Estimate: 1 day.
