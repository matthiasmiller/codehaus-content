12.3.2. Contract Definition Record

Overview: This is a custom record type, used to create a Contract template that can be used to setup Contract records with certain information filled in already. (Note: RTO Contract language and requirements are specific to each state and Rental Company.)

  


Accessed via:

  * Settings | Configuration | Configure Contract Definitions



  


Sections and Fields: 

  * Contract Definition section
    * Definition ID (auto number internal ID field; hidden)
    * Rental Company (list of Rental Companies; required)
    * State (list of US states; required)
    * Rental Contract Type (required; drop list of Rental Contract Types; i.e. RTO vs. RTR; default to RTO)
    * Active (checkbox)



  


  * Rent-to-Own Contract Types section (only visible if "Rental Contract Type" is set to "RTO")
    * RTO Contract Types (embedded spreadsheet with the following:) 
      * Columns: 
        * Contract Type (required; drop list; allow user additions; includes the following shipped items: 
          * Standard
          * CRA)
        * CRA (checkbox; unchecked and read-only for Standard; checked and read-only for CRA; editable for Custom Contract Types.)
        * Disallow Increased Security Deposit (checkbox; editable if CRA is unchecked; hidden if CRA is checked; Note: this field is cleared on save if CRA is checked)
        * # of Days Same as Cash (number; 2 decimals)
      * Automatically sorted by: RTO Contract Type (alphabetically):
        * Standard first 
        * CRA second
        * Custom items third
      * Buttons to add/remove rows: "✚" / "🞭"
      * Shows 5 rows without scrolling
      * Other Notes: 
        * Has the following validations:
          * Error on save if there isn't at least one row in the RG
          * Error on save if there are are duplicate RTO Contract Type rows 



  


Visual Mockup:

RTO Contract Type| CRA| Disallow Increased Security Deposit*| DWF $| # of Days Same as Cash  
---|---|---|---|---  
Standard   [v]| [ ] | [ ] | 4| 90  
CRA          [v]| [X] | disabled| 4|   
  
  
  


  


  * Rent-to-Own Financials (only visible if "Rental Contract Type" is set to "RTO")
    * Terms section (RG, warning on save if no rows are specified. Sorted with shortest terms on top)
      * Term Length (list of Terms that are listed on the Rental Company; required)
      * Cash Price % (number; 2 decimals; required)
      * Rental Fee % (auto-calculated; 100 - Cash Price %; percentage field; 2 decimals) 
      * Divisor (auto-calculated; Term Length * Cash Price %; 2 decimals)
    * Requires Balloon Payment (checkbox)
      * Minimum Price (list of Balloon Payment Minimum Types list; required if checkbox is checked)
        * % of Product Price (including tax) 
        * % of Product Price (excluding tax) 
        * % of Contract Price (monthly payment * sales tax * term length)
      * % of Price (percentage; 2 decimals; required if checkbox is checked; error if percentage is less than 0 or greater than 100) 



  


  * RG:
    * Minimum Downpayment:
      * Type
        * % of Cash Price (including tax)
        * # of Payments
      * Downpayment % (number; 2 decimals; percentage; visible by type)
      * Downpayment # Payments (number; 0 decimals; visible by type) 
      * Max Price / Error Message (optional)
      * Max Width / Error Message (optional)



  


  * Late Fees (visible for both RTO & RTR)
    * Warn if there are no rows.
    * RG of:
      * Repayment Cycle (required, list of payment terms, only allow one row per repayment cycle) 
      * Grace Period (Days); (number; 0 decimals)
      * Method (list; required)
        * Increment Per Day (requires mins and maxes; only available for Late Fee)
        * Per Payment $ (does not allow mins and maxes; only available for Damage Waiver)
        * Per Payment %  (requires mins and maxes; only available for Damage Waiver)
      * $ or % (number; 2 decimals; required)
      * Min Fee $ (optional; editable for Increment Per Day or Per Payment %)
      * Max Fee $ (optional; editable for Increment Per Day or  Per Payment %)
      * Tax (required); choice of:
        * Non-Taxable
        * Remove from Late Fee
        * Add to Late Fee



  


  * Allow Deferring Late Fees until End of Contract (checkbox) 



  


  * Limit Late Fees (required; list of "Per Account" and "Per Contract")



  


  * Other Fees (section: visible for both RTO & RTR)
    * Other Fees; RG of:
      * Other Fee Type
        * Processing Fee
        * Delivery Fee
        * Redelivery Fee
        * Reinstallation Fee
        * Reposession Fee
        * Damage Waiver Fee (required row)
      * $ (number; 2 decimals)
      * Taxable (checkbox)
        * Require TODO_PERMISSIONS some big permission to edit the fee amount
    * NSF Fee $ (number; 2 decimals; required)



  


  


  * Template section (visible on both RTR and RTO)
    * Contract-level memo (embedded expression; Note: eventually this might be tied to a template, either a fillable PDF or a memo template)



  


  * Notes section 
    * "This record must be saved before creating a linked note." (label, visible for new unsaved records)
    * New Note (opens a new note record; populates the Type + Linked Record, visible if the record has been saved)
    * View Notes (report link; opens the My Notes report)
    * Notes (read-only memo that concats based on record Type + record ID, sorted in order of Note ID; newest first)



  


Modification History: This contains the following standard feature for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: __
  * Editability: __



TODO_PERMISSIONS: Document based on Permission, rather than User Groups. 

  


Special Considerations: TODO_: Spec these out; see a standard record Snippet for the wording format.  

  * Copy Record: __ (think: does it make sense to allow copies? what fields are retained / cleared on copy?) 
  * Delete Record: __ (think: allow deletion? under what circumstances?)
  * Merge Record: __ (think: does it make sense for this record to be merged since the initiating one is deleted completely?; if we disallow deletion across the board, probably disallow merging)



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.


