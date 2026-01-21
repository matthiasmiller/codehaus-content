5.2.2. Contact - Address Section

*Done. 

  


  * Address section (standard section):
    * "<" & ">" (visible if there are more than one address entered; buttons in the section heading; to cycle through the entered addresses) 
    * Type (drop list of Address Type list items, and the option to add a new item to the list; with the following details / behaviors: 
      * optional, with the following custom exception: there must be one address with have "Type" = "Primary" \- error messages on Save: "At least one address should be primary address." / "Only one address should be primary address."; 
      * custom: always visible and editable) 
    * Address (required; for "line 1"; plain text field) 
    * Address 2 (unlabeled field; optional; for "line 2"; plain text field) 
    * City (plain text field; warning on Save if blank and "Address" is not blank) 
    * State (no label; drop list of US state & territory abbreviations; warning on Save if blank and "Address" is not blank) 
    * Zip (no label; plain text field; warning on Save if blank and "Address" is not blank) 
    * Google Maps (link; visible if at least one of the address-related fields has data entered; opens the entered address in Google Maps) 
    * Export Address (link; visible if at least one of the address-related fields has data entered; opens a prompt screen to export the address (i.e. for printing on an envelope)) 
    * View All (button; opens the "View All Addresses Child Screen" - see spec below) 
    * New (button; adds a new address item)  
    * Delete (visible if there are more than one address entered; button; deletes the currently-visible address) 



  


  


  * View All Addresses Child Screen: 
    * Embedded spreadsheet with the following: 
      * Columns: 
        * Type (column always visible; otherwise the same as the corresponding field on the main screen) 
        * Address (same as the corresponding field on the main screen)
        * Address2 (same as the corresponding field on the main screen)
        * City (same as the corresponding field on the main screen) 
        * State (same as the corresponding field on the main screen) 
        * Zip (same as the corresponding field on the main screen) 
        * Country (same as the corresponding field on the main screen)
        * Export (link; displays as "Link"; same behavior as the "Export Address" link on the main screen) 
      * Automatically sorted by: 
        * First by (custom): Primary (at the top) 
        * Second by: N/A (additional rows remain in the order in which they were entered) 
      * Buttons to insert/append/remove rows: "+" / "-" 
      * Show 12 rows without scrolling 
      * Other Notes: 
        * Custom: The "Primary" address may be located anywhere on the list (since this Solution uses a dedicated "Primary" Address Type, rather than considering the first / top address to be the "Primary" address)


