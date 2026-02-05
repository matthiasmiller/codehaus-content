12.3.4. Asset Record

Overview: This is a custom record type, used to hold information about individual products (e.g. a building etc.)

  


If the same building is owned multiple times (bought/sold/bought/sold from the manufacturer), we will then have multiple product records with duplicate serial numbers.

  


Accessed via: 

  * "Building" link in "Contracts" record
  * Accounting | Products | Search Products



  


Sections and Fields: 

  * Asset section
    * (Description text in the header label; in the following format:
      * If Type is "Structure": <Primary ID> \- <Dimensions (ft)> <Model / Series> \- <Internal ID> (e.g. S25081169 - 12x16 Shed - 00003)
      * If Type is "Other": <Description> \- <Internal ID> (e.g. "My Custom Building Structure - 00006")
    * Rental Company (required; non-editable drop list of active Rental Companies; default to active Rental Company if there’s only one) 
    * Manufacturer (drop-list of active Manufacturer type contacts linked to the RTO Company)
    * Dealer (drop list of active dealers for Manufacturer) 
    * Salesperson (drop list of active salespeople for Rental Company) 
    * Tags (multi-select drop list of Product Tags; populates an underlying RG of ProductTag)
    * Type 
      * required
      * list of Product Types: Rentable Structure, Rentable Other, Non-Rentable; 
      * defaults to "Rentable Structure"
      * clears description if Type is not set to "Rentable Other"
    * Description (visible and required if Type = "Rentable Other"; plain text field)



  


  


  * Purchase Financials section
    * Purchase Date (date field; date that ownership moves from Manufacturer to the Rental Company; marks the start of depreciation)
    * Purchase Amount (number; two decimals) 
    * Premium Paid (auto-calculated; number, 2 decimals; sum of Bill itemization rows for the product with a type of Asset Premium)
    * Expenses Paid (auto-calculated; number, 2 decimals; sum of Bill itemization rows for the product with a type of Asset Expense)
    * Details (child screen)
      * Purchase section 
        * Purchase Amount (number; 2 decimals; uneditable; value from the Purchase Amount field on the main screen)
        * Purchase Amount Paid (auto-calculated; number; 2 decimals; sum of Bill itemization rows for the product with a type of Asset Purchase)
        * Balance (auto-calculated; number; 2 decimals; Purchase Amount - Purchase Amount Paid)
      * Premium section 
        * Premium % (auto-calculated; percent with 2 decimals)
          * if Override is not checked then this is premium % from manufacturer settings
          * if Override is checked then it is the Owed Amount / Purchase Amount
        * Premium Owed (number field; two decimals; with the following behaviors: 
          * if Override is not checked: read only; PurchaseAmount * MfgPremium% / 100 from the Manufacturer record for MfgPremium% effective on the product Purchase Date
          * if Override is checked: editable and required)
        * Override (checkbox; makes "Premium Owed" editable)
        * Premium Paid (number; includes a link to view paid premiums) 
        * Premium Balance (read-only; Premium Owed - Premium Paid)
    * Linked Bills (report showing bill itemization rows linked to this product)
    * TODO_DB: Review RTO Pro fields to make sure that we have all the variables



  


  * Structure section
    * Primary ID (plain text field; validates against duplicates; functions as a Serial Number)
    * Secondary ID (plain text field; validates against duplicates)
    * Invoice Number (plain text field) 
    * Build Date (date) 
    * Model / Series (drop list of Product Models; user-editable; sorted alphabetically; comes with two shipped items: "Barn" and "Shed.")
    * Dimensions (ft) (length field [ProductLength]; number; 0 decimals)
    * x (width field [ProductWidth]; number; 0 decimals) 
    * Roof Style (drop list of Product Roof Styles; user-editable)
    * Roof Color (list of Product Colors; user-editable)
    * Siding Type (drop-list of Product Siding Types; user-editable)
    * Siding Color (list of Product Colors; user-editable)
    * Trim Style (drop-list of Product Siding Types; user-editable)
    * Trim Color (list of Product Colors; user-editable)
    * Last Condition (drop-list of Product Conditions)



  


  * Contracts Section (visible if the type is Rentable Structure or Rentable Other)
    * Virtual RG of all contracts linked to the product; read-only columns:
      * Contract ID
      * View Contract (link to the contract record)
      * Primary Customer
      * View Customer
      * Contract Status
      * Contract Start Date
      * Rent Collected
      * DWF Collected
      * Late Fees Collected
      * Other Fees Collected



  


  * Resell/Buyback Section (label based on Method; visible if the type is Rentable Structure or Rentable Other)
    * Sold On (date; other items visible based on this)
    * Method (required; Buyback or Resell)
    * Sale Amount (number, required)
    * Invoiced Amount (calculated amount from invoices linked to this product)
    * View Invoice(s)
    * New Invoice (only visible if Sale Amount is not equal to the Invoiced Amount)



  


  * Depreciation Section (visible if the user has permission to View Full Asset Details)
    * Start Date (read-only and auto-calculated as earliest contract start date unless Override Depreciation Start Date is checked; then, editable and required; error on save if not after the earliest contract start date)
    * Override Depreciation Start Date (checkbox)
    * Book Schedule (editable if there are no past depreciation dates; displays "<Method> \- <Type> \- <Term Year>", sets underlying fields)
      * Method (hidden; list of Depreciation Methods; set by Book Schedule)
      * Type (hidden; list of Depreciation Useful Lives; set by Book Schedule)
      * Term Year (number; set by Book Schedule)
    * Useful Life (Years) (if Type is "Contract Length"; auto-calculated and read-only, contract term / 12 for the contract with the earliest start date; if Type is "Fixed Length"; editable; drop-list of Available Terms [in years] from the Rental Company)
    * Virtual RG of depreciation rows with a date that is less than or equal to the current date
      * Columns:
        * Book Depreciation Date
        * Depreciation $ (number; two decimals)



  


  * Notes section 
    * "This record must be saved before creating a linked note." (label, visible for new unsaved records)
    * New Note (opens a new note record; populates the Type + Linked Record, visible if the record has been saved)
    * View Notes (report link; opens the My Notes report)
    * Notes (read-only memo that concats based on record Type + record ID, sorted in order of Note ID; newest first)



  


  * Helpful Macros 
    * ProductActiveContractField(...)
    * ProductLatestContractField(...)
    * ProductContractsToArray(...)



  


Modification History: This contains the following standard feature for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access: 

  * View record: All users
  *  Edit record: Has "Edit Products" permission



  


Special Considerations:  Sean Miller 07/14/2025: TODO_PERMISSIONS: Please confirm.

  * Copy Record: Allow copying; clear "Primary Identification Number " and "Secondary Identification Number" on copy (retaining all other fields). 
  * Delete Record: Allow deletion until the record has been referenced by another record, then disallow.  
  * Merge Record: Allow merging (one record is completely replaced by the other)



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.


