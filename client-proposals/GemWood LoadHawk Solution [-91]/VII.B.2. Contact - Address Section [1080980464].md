7.2.2. Contact - Address Section

  * Address section: 
    * "(<X> of <Y>)" (visible in the section heading, after "Address", if more than 1 address exists for the Contact; "X" represents the item number of the current address; "Y" represents the total number of addresses) 
    * "🡄" & "🡆" (visible if there are more than one address entered; buttons in the section heading; to cycle through the entered addresses) 
    * Type (optional; visible and editable if there are more than one address entered; drop list of Address Type list items, and the option to add a new item to the list) 
    * Address (optional; for "line 1"; plain text field) 
    * Address 2 (unlabeled field; optional; for "line 2"; plain text field) 
    * City (optional; plain text field) 
    * State (unlabeled field; optional; drop list of US state & territory abbreviations) 
    * Country (optional; drop list of countries) 
    * Zip (unlabeled field; optional; plain text field) 
    * Google Maps (link; visible if at least one of the address-related fields has data entered; opens the entered address in Google Maps) 
    * Export Address (link; visible if at least one of the address-related fields has data entered; opens a prompt screen to export the address (i.e. for printing on an envelope)) 
    * View All (button; opens the "View All Addresses Child Screen" \- see spec below) 
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
      * Automatically sorted by: (e.g. by date, etc, or N/A)
      * Buttons to insert/append/remove rows: "+" / "-" 
      * Show 12 rows without scrolling


