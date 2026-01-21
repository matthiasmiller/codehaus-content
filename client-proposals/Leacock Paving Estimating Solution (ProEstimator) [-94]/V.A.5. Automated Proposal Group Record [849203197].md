5.1.5. Automated Proposal Group Record

  


Requirements

Overview: The Automated Proposal Group record is a custom configuration record, and is used to track Groups that are pre-configured and used in the automated process of adding Groups to a Proposal. This record tracks the various details and calculations that are needed to set up a new Group in a Proposal.

  


Accessed via: Configure Automated Proposal Groups Report

  


Sections and Fields: 

  * Automated Proposal Group Overview section:
    * Active (checkbox; defaults to checked)
    * Name (required; plain text field; validate against duplicates) 
    * Unit of Measure (required; drop list of Units of Measure list items) 
    * Uses and Requires Thickness (checkbox; defaults to checked; if checked, the Group has a required field for Thickness on the Proposal record - see corresponding spec) 



  


  


  * Included Sales Items section: 
    * Included Sales Items (embedded spreadsheet with the following; used to configure the included Sales Items and their corresponding quantities / formulas for the Group): 
      * Columns:  
        * Sales Item (required; drop list of "Display Names" for all active Sales Item records; validate against duplicates for the same Automated Proposal Group - error message on the field: "This Sales Item has already been used for this Automated Proposal Group.") 
        * Item Category (read-only macro; displays the "Category" for the selected Sales Item) 
        * Item UOM (read-only macro; displays the "Unit of Measure" for the selected Sales Item) 
        * Item Unit Cost $ (read-only macro; displays the "Unit Cost $" for the selected Sales Item) 
        * Item Markup % (read-only macro; displays the "Markup %" for the selected Sales Item) 
        * Item Unit Price $ (read-only macro; displays the "Unit Price $" for the selected Sales Item) 
        * View / Edit Sales Item (link; displays as "Link"; opens the selected Sales Item record)
        * Item Qty Formula (required; plain text expression field; with the following details / behaviors: 
          * this is used to configure the Item-specific formula, specifying the quantity of the Item that should be included from the Baseline amount, accounting for waste, etc.; 
          * note that the specific formulas may be determined as part of configuring the software; 
          * a report alert is shown to all users if the field contains an invalid expression; 
          * Technical Note: The formulas have a parameter of vGroupAmount and access to the associated Sales Item. All formulas will be based on these two inputs.) 
      * Automatically sorted by: N/A
      * Buttons to add/remove rows: "✚" / "🞭"
      * Buttons to move rows up and down (up/down arrows) 
      * Show 10 rows without scrolling 



  


  


  * Group Calculations Preview Section: 
    * Unit of Measure (read-only macro; displays the selection in the "Unit of Measure" field above; as a reference point for users viewing / using this Preview section) 
    * Preview Min Quantity (required; number; 0 decimals; defaults to "100"; this sets the lowest Group Quantity to be displayed on the "Preview Table" below) 
    * Preview Increment (required; number; 0 decimals; with the following details / behaviors: 
      * defaults to "100"; 
      * error on Save if set to zero or a negative number; 
      * this sets the increment at which the "Preview Table" below displays values between the "Min" and "Max" values) 
    * Preview Max Quantity (required; number; 0 decimals; defaults to "3,500"; this sets the highest Group Quantity to be displayed on the "Preview Table" below; this is defaulted to be higher than the current square yard pricing "plateau" that occurs at 3,000 SY, with the idea of giving a clear visual of where the pricing plateaus) 



  


  * "The calculated number of preview rows is <Calculated number of rows>, which exceeds the maximum allowed number of rows. The number of rows will be capped at <Max Number of Rows>." (on-screen message in red text; visible if the resulting rows in the "Preview Table" would exceed the maximum number of allowed rows, which is initially set at 100) 
  * Preview Table (read-only memo; displays a table based on calculations from the selected row in the "Included Sales Items" embedded spreadsheet, with the following: 
    * Rows: One row for each "Group Quantity" increment, starting with the "Preview Min Quantity" through the "Preview Max Quantity", incremented according to the absolute value of the "Preview Increment", with the smallest number at the top) 
    * Columns: 
      * Group Quantity (number; 0 decimals; displays the "Group Quantity" value, as specified above in the "Rows" spec for this table, in bold font) 
      * Group Price (number; 2 decimals; displays the sum of price amounts for all rows on the "Included Sales Items" embedded spreadsheet, for the corresponding "Group Quantity", preceded by "$")
      * Group Unit Price (number; 2 decimals; displays the unit price for the group, preceded by "$", based on the following formula: <"Group Price $"> / <"Group Quantity">, rounded to the nearest 2 decimal places)
      * Included Item Qty: "<"Display Name" for the selected Sales Item>" (number; 2 decimals; displays the quantity of the selected Item in the "Included Sales Items" embedded spreadsheet that should be included in the corresponding "Group Quantity", rounded to the nearest 0.25, based on the "Item Formula")
      * Graph for Included Item Qty (displays a horizontal bar for the "Included Item Qty" for the corresponding "Group Quantity") 



  


  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users
  * Editability: Editable for users with the "Create/Edit Automated Proposal Groups" Permission



  


Special Considerations:  

  * Copy Record: Allow copying; clear the following field(s) on copied records: 
    * Name
  * Delete Record: Allow deletion until the record has been referenced by another record, then disallow. 
  * Merge Record: N/A (disallowed)



  


Other Notes:

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * The full list of Automated Proposal Groups is available for Proposals of all Job Types. 
  * Changes made to an Automated Proposal Group record do not apply to existing Proposals that use that Automated Proposal Group.
  * If in the future, there is a desire/need for including fully manual items on Automated Proposal Groups (like the "Manual Items" on the "Items for Group" embedded spreadsheet on the Proposals), this probably could be done. Work would be needed to ensure that all needed fields are included on the Automated Proposal Group records, and to determine the correct logic.



  


Development Specification

Change Requests: 

  * Tim Reitz 11/25/2025: [[[IN12315](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12317&)]] - ZLP - Phase 1 - Misc. Changes Job #1
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1065955969#gid=1065955969](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1065955969#gid=1065955969) 

  


BD: Define Core Detail Screen

[ ] Simple fields at top

[ ] Simple RG (overall)

[ ] AutoGroupItemQtyFormula is an expression field

[ ] evaluated on a Sales Item taking vAutoGroupQuantity as a parameter, returning a number.

[ ] Let's do the extra work to give report alerts to everyone if these don't parse.

Nic will do the Preview section with the calcs.

[ ] Modification Links etc

BID: Detail Screen: 4 HOURS + Expression Field/report alert: 4 HOURS

  


  


NICCOLAS: Formulas

[ ] AutoGroupCalcItemQty( vAutoGroupQuantity) calculates the quantity of an item based on the group quantity

[ ] An AutoGroupTotalPrice( vAutoGroupQuantity) macro takes a quantity and does a SumRG, evaluating the quantity for each item multiplying by the Sales Item Price.

  


Preview Section (note that the last two columns are MRG-specific, showing the value for the highlighted RG row, the first 3 columns are the same for all RG rows):

[ ] Use a RichTextExpression with columns. 

[ ] PreviewNumberRows macro: (MaxQuantity-MinQuantity)/Increment + 1

[ ] PreviewRowNumbers: NumericPipeList(0, PreviewNumberRows-1)

[ ] Row Quantity is: Value(RepeatListItem) * PreviewIncrement + PreviewMinQuantity

[ ] Group Price is AutoGroupTotalPrice with the row quantity.

[ ] Group Unit Price is the calc'd price / Quantity

[ ] Included Item Quantity is the AutoGroupCalcItemQty for the row

[ ] Column heading includes the Sales Item Name

[ ] Use a variable-width Table Cell for the bar image. Clever....

BID: 8 HOURS

Tim Reitz 07/26/2025: Here is an incident and linked PC for this: 

  * [[[IN11855](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11857&)]] - ZLP - Phase 1 - Determine Calculations/Formulas
  * [[PC0181482]] - ZLP - Phase 1 - Determine Calculations/Formulas



  


  


  


  


Ellis Miller 06/18/2025: You can largely ignore the below:

Tim Reitz 05/21/2025: Data from client's current tiered pricing structure: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=273157564#gid=273157564](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=273157564#gid=273157564). 

  


\----------------------

Calculations / Formulas: 

  


Tim Reitz 05/21/2025: Per Ellis, the graph bars on the Preview table could use expression like this (try it out in Expression Evaluator): 

FormattedCell("100", 50, "Right") + FormattedCell("20.0", 50, "Right") + FormattedCell("", 20, "", "blue")+ NewLine +

  


FormattedCell("1500", 50, "Right") + FormattedCell("60.0", 50, "Right") + FormattedCell("", 60, "", "blue")+ NewLine +

  


FormattedCell("3000", 50, "Right") + FormattedCell("72.0", 50, "Right") + FormattedCell("", 72, "", "blue")

  


  


Tim Reitz 02/24/2025: We should have the calculator round results: 

[ ] Tons to the nearest whole number or to the nearest quarter if that makes it easier and still gives clean numbers (client is fine with that). 

[ ] Hours to the nearest quarter (Labor & trucking) 

Ellis Miller 05/06/2025: _VA: Formulas can easily round using RoundToIncrement:

Assign vRounded = RoundToIncrement(17.34, 0.25); 

String(vRounded, 0, 2)

  


\----------------------

  


Tim Reitz 05/21/2025: I'm not sure if these are relevant at this point, but keeping them around for now: 

  * Example / sample formulas: 
    * Materials with Thickness: 
      * Description: Calculated material + calculated anticipated waste, rounded to the nearest 0.25 
      * Formula: (SY * Thickness * 0.058) + waste 
      * Example: (2,048 * 4.00 * 0.058) * 1.007 = 478.461952 ≈ 478.50
    * Materials without Thickness: 
      * Description: Calculated material + calculated anticipated waste, rounded to the nearest 0.25 
      * Formula: (__) + waste 
      * Example: __
    * Labor: 
      * Description: Calculated hours + calculated anticipated waste, rounded to the nearest 0.25 
      * Formula: (__) + waste 
      * Example: __


