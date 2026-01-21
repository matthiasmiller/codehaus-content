5.1.4. Sales Item Record

  


Requirements

Overview: Sales Items are configured on Sales Item records and viewed on the Sales Items report (both Silverloom standard features). Note that any customizations are noted as such in the spec.  

  


In the ProEstimator Solution, these Sales Items are used in Automated Proposal Groups and in Proposals. 

  


Accessed via: 

  * Configure Sales Items Report



  


Sections and Fields: 

  *   Product / Sales Item section: 
    * Is Active (checkbox; defaults to checked) 
    * Code (required; plain text; validate against duplicate Codes: error on the field and on Save: "Duplicate Product / Sales Item names are not allowed: <Code>"; unique identifier for the record) 
      * Custom note: For imported data, this might be set directly or it might be set via a "Power App Base Item ID" field -- TBD. 
    * Description (required, based on the "Sales Item Require Description" System Switch; plain text) 
    * Category (required; drop list of "Sales Item Categories" list items) 
    * Unit of Measure (visible, based on the "Sales Item Show UOM" System Switch; required; drop list of Units of Measure list items, with an option to add a new item)
    * Unit Cost $ (visible, based on the "Sales Item Show Cost & Markup" System Switch; required; number; 2 decimals; with the following behaviors / details: 
      * when manually set, the following other field(s) are affected: 
        * Unit Price $: updates based on the following formula: "Unit Cost $" * (1 + decimal value of the "Markup %"), rounded to the nearest 2 decimal places; 
        * Markup %: If Markup % is blank when Unit Cost $ is entered, the Markup % should be set to (UnitPrice$ / UnitCost$ - 1) * 100
      * note that Unit Cost $ should never update automatically based on "Markup %" or "Unit Price $") 
    * Markup % (visible, based on the "Sales Item Show Cost & Markup" System Switch; optional; number; 5 decimals; with the following behaviors / details: 
      * blank is treated like "0"; 
      * when manually set, the following other field(s) are affected: 
        * Unit Price $: updates based on the following formula: (1 + decimal value of the "Markup %") * "Unit Cost $", rounded to the nearest 2 decimal places; 
      * note that this is a true markup (percent of the Cost), rather than margin (percent of the Price))
    * Unit Price $ (required; number; 2 decimals; with the following additional behaviors / details: 
      * if the "Sales Item Show Cost & Markup" System Switch is set: 
        * sets based on "Unit Cost $" and "Markup %" when they are set; 
        * when set, the following other field(s) are affected:  
          * Markup %: updates based on the following formula: "Unit Price $" / "Unit Cost $", rounded to the nearest 5 decimal places) 
    * Notes (optional; memo) 



  


  * Customized for Leacock Paving custom section: 
    * Display Name (custom; read-only macro; displays "<Description> #<Code> (Oil Index: $<PA Oil Index $>)", i.e. "Sample #1234 (Oil Index: $637.00)"; note that the "(Oil Index: $<PA Oil Index $>)" portion is conditionally included if the "Include PA Oil Index" checkbox is checked; when set to not checked, the "PA Oil Index $" is cleared) 
    * Include PA Oil Index (custom; checkbox; defaults to not checked)
    * PA Oil Index $ (custom; visible if "Include PA Oil Index" is checked; with the following details / behaviors: 
      * required when visible; 
      * number; 2 decimals; 
      * sets to the current value of the "PA Oil Index $" value from the top row of the "PA Oil Index Details" embedded spreadsheet in Silverloom Settings, at the following points: 
        * initially set when made visible via checking the "Include PA Oil Index" checkbox; 
        * set via when the "Update to Current Oil Index" button is clicked - see corresponding spec; 
      * note that this is included as a reference point, and does not impact the Sales Item pricing directly in the Solution; 
      * this is not a dynamic macro because sometimes the user responsible for updating the main PA Oil Index and the pricing does not make all of the changes at the same time, so this should flag when out of sync with the main "PA Oil Index $" value in Silverloom Settings) 
    * "Oil Index is out of date." (custom; on-screen message in red font; visible if "Include PA Oil Index" is checked and "PA Oil Index $" does not match the "PA Oil Index $" value from the top row of the "PA Oil Index Details" embedded spreadsheet in Silverloom Settings) 
    * Update to Current Oil Index (custom; visible if "Include PA Oil Index" is checked and "PA Oil Index $" value does not match the "PA Oil Index $" value from the top row of the "PA Oil Index Details" embedded spreadsheet in Silverloom Settings; button; with the following details: 
      * when clicked, the current value from Silverloom settings is copied immediately into the "Current PA Oil Index" field) 
    * Update to Current (custom; hidden editable macro; drop list of blank / "Yes" / "No"; with the following details / behaviors: 
      * editable only in editable reports if the "Include PA Oil Index" checkbox is checked and Oil Index is not current (i.e. if this = "No"); used to update the "PA Oil Index $" from the Sales Items report; 
      * blank if "Include PA Oil Index" is set to not checked; 
      * otherwise, displays "No" if "PA Oil Index $" value does not match the "PA Oil Index $" value from the top row of the "PA Oil Index Details" embedded spreadsheet in Silverloom Settings; 
      * when set to "Yes", the current value from Silverloom settings is copied immediately into the "Current PA Oil Index" field) 
    * Power App Base Item ID (custom; hidden; number; 0 decimals; used for data migration / imported items from the Power App solution)



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users
  * Editability: Editable for users with the "Edit Sales Items" Permission 



  


Special Considerations:

  * Copy Record: Allowed; "Code" is cleared (retaining all other fields) (standard).
  * Delete Record: Allowed until the record has been referenced by another record, then disallowed (standard). 
  * Merge Record: Allowed without restrictions; the record from which the merge is initiated is completely replaced by the other (all data is deleted) (standard). 



  


Other Notes:

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * Examples of unit price calculations: 
    * Example 1 (editing Unit Cost $): 
      * Unit Price $ = 72.50
      * Unit Cost $ is changed / set to 56.00 
      * Markup % is calculated to 29.46429 
      * Calculation: 72.50 / 56.00 = 1.294642857142857 ≈ 1.2946429
    * Example 2 (editing Markup %): 
      * Unit Cost $ = 55.39
      * Markup % is changed / set to 30.00000
      * Unit Price $ is calculated to 72.01
      * Calculation: 55.39 * 1.3000000 = 72.007 ≈ 72.01 
    * Example 3 (editing Unit Price $): 
      * Unit Cost $ = 55.39
      * Unit Price $ is changed / set to 73.00
      * Markup % is calculated to 31.9274
      * Calculation: 73.00 / 55.39 = 1.317927423722694 ≈ 1.3179274 
  * The following field(s) are hidden (custom) in this Solution:
    * Show in Sales Report  
    * Taxable 
    * Income Account



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1330298279#gid=1330298279](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1330298279#gid=1330298279)

  


Standard Sales Item Changes - USA (Assign to Nic)

[ ] Make Description optionally required -- new Config_SalesItemDescrRequired system switch, defaults to false for others and overridden as true in this catalog.

[ ] Add Unit of Measure field, visible based on new Config_SalesItemUOMVisible

[ ] Add Unit Cost $ and Markup % fields, conditionally visible based on Config_SalesItemShowCostAndMarkup switch.

[ ] Handle behaviors as described. Think through to make sure we got them all.

[ ]  Add the standard System Switches to the Sales Item catalog (wherever that is). See "System Switches" section

[ ] Note that we are changing the "Unit Price" label to "Unit Price $"

[ ] Note that we are changing the "Prevent Delete If Referenced" setting to: Allow deletion until the record has been referenced by another record, then disallow. 

[ ] Change Sales Items to be based on a new "Edit Sales Items" permission in core catalog (enabled by default)

BID: 1 DAY

  


Customized for Leacock Paving

[ ] Create SalesItemDisplay_ZLP macro - note that this uses the SalesItemOilIndex

[ ] SalesItemIncludeOilIndex

[ ] SalesItemOilIndex - simple field here

[ ] Oil Index warning - shown if this is different than CurrentPAOilIndex (a none-level macro that gets current value from Silverloom settings).

[ ] Update button - simple OnChange button to copy the current value into the SalesItemOilIndex.

  


[ ] Make sure switches are set so that:

  * The following field(s) are hidden (custom) in this Solution:
    * Show in Sales Report  
    * Taxable 
    * Income Account



BID: 4 HOURS
