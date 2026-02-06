4.8.2.2. Device - Warranty Details Section

  * Warranty Details section (visible for all Device Types; note that full warranties are only tracked for devices that are sold by Think Ink; other devices simply have a field for manually entering the warranty terms):
    * Warranty Status (automatic and read-only:)  
      * "Active": if the current date is on or before the Warranty End Date.
      * "Expired": if the current date is after the Warranty End Date.
      * "N/A": if the Device has no Warranty End Date.



  


  * Manual Warranty Terms (months) (visible only if the "Sold by Think Ink" checkbox is not checked; optional; number field with no decimals; defaults to blank; used to manually set the warranty terms in months for Think Ink-owned devices or for Customer devices purchased elsewhere)



  


  * Warranty Terms (months) (visible if the "Sold by Think Ink" checkbox is checked; auto-set and read-only; number field with no decimals; sum of Manufacturer's Warranty months and all selected Extended Warranty months; used to track the total number of months of warranty coverage for the Device; note that this always treats multiple warranties as stacking rather than overlapping) 



  


  * Warranty End Date (date; auto-set and read-only; set based on the following:)
    * If Type = Leased Printer or Leased Other: Based on the TI Purchase Date and the number of months in Manual Warranty Terms
    * If Type = Customer Printer: Based on the Customer Purchase Date and the number of months in Manual Warranty Terms or Warranty Terms, as applicable



  


  * Manufacturer's Warranty End (visible if the "Sold by Think Ink" checkbox is checked; auto-set and read-only; based on the Purchase Date and the Manufacturer's Standard Warranty on the selected Model)
  * Manufacturer's Warranty Details (visible if the "Sold by Think Ink" checkbox is checked; auto-set and read-only; displays the Manufacturer's Warranty Details from the selected Model)



  


  * Extended Warranty Details (visible if the "Sold by Think Ink" checkbox is checked; embedded spreadsheet with the following:) 
    * Columns: 
      * Description (required; drop list of Available Extended Warranties for the selected Model)
      * Terms (Months) (auto-set and read-only; fills from the corresponding field on the selected Warranty)
      * Amount (auto-set and read-only; fills from the corresponding field on the selected Warranty)
      * Invoice # (Phase 3: optional; plain text field; manually filled with an invoice number)
        * Phase 4: To be auto-set when an invoice is linked to the row
      * Invoice Status (Phase 3: blank)
        * Phase 4: auto-set and read-only; displays the Status of the corresponding Invoice 
    * Automatically sorted by: N/A
    * Buttons to add/remove rows ("+" / "-") 
    * Show 4 rows without scrolling



  


  * Warranty Notes (memo; used for documenting any notes about the Device's warranties) 
  * Replace Under Warranty (button; clicking this opens the Replace Device Under Warranty child screen -- see details in the corresponding section of the proposal).


