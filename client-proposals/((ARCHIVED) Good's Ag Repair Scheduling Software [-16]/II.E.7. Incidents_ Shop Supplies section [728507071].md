2.5.7. Incidents: Shop Supplies section

Austin Priest 01/20/2023: [[[IN5224](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-5226&)]] - ZGA - Incidents - Add Tracking for Shop Supplies (T&M)

  


Design: 

[[PC0147955]] - ZGA - Changes to Incidents (T&M)

Changes to Incidents: 

  * Change the Incidents to use a 2-column layout
  * Add a "Shop Supplies" section at the top of the right-hand side of the screen: 
    * Embedded table with the following: 
      * Columns: 
        * Description (required; drop list of all Shop Supplies items; filters down as you type; includes the option to add a new item to the list) 
        * Total Qty (editable number field; required; number to 2 decimal places) 
        * Qty Adjustment (number entry that adjusts the Total Qty for the same row; supports  "+17" or "17" to add, and "-17" to subtract; after the number is entered and user tabs or clicks away the Total field auto-updates and the Adjustment field auto-clears)
      * Sorted: Alphabetically by Description (numbers listed before letters) 
      * Buttons to add and remove rows below the left end of table ("Add" and "Remove") 
      * Always show a new (empty) row for easy data entry
      * Show at least 5 rows without scrolling 
      * Validations: 
        * Validate against multiple rows with same Description on the same incident (the user should update the Qty in the existing row if more of a certain supply is used). Show an error when a user selects a duplicate Description: "This item has already been used for this incident. Remove the new row and update the Qty on the existing row." 
        * Show a warning when deleting rows: "Are you sure you want to delete the selected row(s)?"
    * If the incident is a parent incident, the section will be titled "Shop Supplies (Including Child Jobs): 
      * The embedded spreadsheet will be read-only and the items, and quantities from the the parent incident and all child incidents will be combined there to show the totals. 
      * Include a checkbox for "View/Edit Shop Supplies for This Job". Filling this checkbox will show an editable embedded spreadsheet for the parent incident. 
        * If there are any supplies entered for the parent incident, show "(<X> items)" in the checkbox label.


