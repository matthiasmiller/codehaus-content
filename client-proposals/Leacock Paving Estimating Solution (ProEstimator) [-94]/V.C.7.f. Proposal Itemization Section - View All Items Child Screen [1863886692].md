5.3.7.6. Proposal Itemization Section - View All Items Child Screen

  


Requirements

  * "View All Items" Child Screen: 
    * All Items for Proposal (embedded spreadsheet that includes all Items on the Proposal; with the following:) 
      * Columns: 
        * Group ID (hidden column; read-only; required; numeric field; displays the "Group Row ID" for the corresponding "Group"; used to facilitate linking between the "Groups" embedded spreadsheet and the "Items for Group" embedded spreadsheet) 
        * Group (read-only macro; displays the "Group Description" for the row, based on the "Group ID" for the row) 
        * Item Row ID (hidden column; required; numeric; unique identifier for the row; note that for Proposals imported from the existing Power App solution, this will be set to the "Power App Group Item ID" from the imported data) 
        * Sales Item Code (optional; drop list of all active Sales Item records; with the following details / behaviors:  
          * editable for rows with "Automatically Added" not checked; 
          * display details: 
            * when the drop list is open: list items are displayed in the following format: "<Sales Item "Description"> \- <Sales Item "Code">";  
            * when an item is selected: only the Code is displayed; 
          * when an item is selected, the following fields are affected:  
            * "Item Description": sets to the "Description" for the selected Sales Item; 
            * "UOM": sets to the "Unit of Measure" for the selected Sales Item; 
            * "Unit Cost $": sets to the "Unit Cost $" for the selected Sales Item; 
            * "Markup %": sets to the "Markup %" for the selected Sales Item; 
            * "Unit Price $": sets to the "Unit Price $" for the selected Sales Item; 
          * when cleared, the following fields are cleared: 
            * "Item Qty"; 
            * "UOM"; 
            * "Unit Cost $"; 
            * "Markup %"; 
            * "Unit Price $"; 
            * "Item Description" and "Item Total $" are not cleared, to allow for changing a row from a Sales Item to a manual Item; 
          * validation against duplicate Sales Items for the same Group - error message on the field "Duplicate Sales Items (<Sales Code>) are not allowed for this Group (<Group Description>).") 
        * Item Description (plain text field; with the following details / behaviors: 
          * if the row has a "Sales Item Code": 
            * read-only; 
            * auto-set to the "Description" from the Sales Item record at the time that "Sales Item Code" is set; 
          * if the row does not have a "Sales Item Code": editable and required)  
        * Item Qty (with the following details / behaviors:
          * if the row has a "Sales Item Code": 
            * required ("0" is an accepted value);
            * number; 2 decimals; 
            * validates against negative values - error on the field: "Item Qty cannot be negative."; 
            * defaults:
              * if "Automatically Added" for the row is checked, is set based on the following:
                * if the row was added as part of an "Automated"-type Group: sets as determined by the calculations for the Automated Proposal Group, based on the Quantity, Thickness, etc.;
                  * also updates automatically if "Group Quantity" for the linked Group is edited - see corresponding spec;
                * if the row was added as part of a "Sales Item"-type Group: initially sets to the entered "Quantity" from the "New Group for Section" prompt; 
                  * also updates to match "Group Quantity" of the linked Group when that is edited - see corresponding spec; 
                * note that this remains editable to allow it to be manually overridden on a per-row basis on the Proposal; 
              * if "Automatically Added" for the row is not checked: defaults to blank; 
            * when manually edited, the following other field(s) are affected on change: 
              * "Group Quantity" for the linked Group: updates to match if "Group Type" = "Sales Item" and "Automatically Added" for the item is checked;
              * "Overridden" checkbox for the row: is automatically checked if "Group Type" for the linked Group = "Automated" and "Automatically Added" for the item is checked (note that other Item rows are not truly overridden by editing this field); 
              * note that that macros for Group pricing also dynamically update with changes here)
          * if the row does not have a "Sales Item Code": N/A (read-only and blank); 
        * UOM (with the following details / behaviors: 
          * if the row has a "Sales Item Code": 
            * read-only; stored field;
            * sets to the "Unit of Measure" on the Sales Item for the row at the time that the row was added; 
          * if the row does not have a "Sales Item Code": N/A (read-only and blank)) 
        * Unit Cost $ (with the following details / behaviors: 
          * number; 2 decimals;
          * if the row has a "Sales Item Code": 
            * required; 
            * sets to the "Unit Cost $" on the Sales Item for the row at the time that the row was added;
            * editable, to allow it to be manually overridden on a per-row basis on the Proposal; 
            * when manually edited, the following other field(s) are affected: 
              * "Unit Price $" for the row updates based on the following formula: ""Unit Cost $" * (1 + decimal value of the "Markup %")", rounded to the nearest 2 decimal places; 
              * "Overridden" checkbox for the row is automatically checked if "Group Type" for the linked Group = "Automated" and "Automatically Added" for the item is checked (note that other Item rows are not truly overridden by editing this field); 
            * note that this "Unit Cost $" field should never update automatically based on the others; 
          * if the row does not have a "Sales Item Code": N/A (read-only and blank)) 
        * Markup % (with the following details / behaviors: 
          * number; 5 decimals;
          * if the row has a "Sales Item Code": 
            * required; 
            * sets to the "Markup %" on the Sales Item for the row at the time that the row was added;
            * editable, to allow it to be manually overridden on a per-row basis on the Proposal; when manually edited, the following other field(s) are affected: 
              * "Unit Price $" for the row updates based on the following formula: "(1 + decimal value of the "Markup %") * "Unit Cost $"", rounded to the nearest 2 decimal places; 
              * "Overridden" checkbox for the row is automatically checked if "Group Type" for the linked Group = "Automated" and "Automatically Added" for the item is checked (note that other Item rows are not truly overridden by editing this field);  
          * if the row does not have a "Sales Item Code": N/A (read-only and blank)) 
        * Unit Price $ (with the following details / behaviors: 
          * number; 2 decimals;
          * if the row has a "Sales Item Code": 
            * required; 
            * sets to the "Unit Price $" on the Sales Item for the row at the time that the row was added;
            * editable, to allow it to be manually overridden on a per-row basis on the Proposal; when manually edited, the following other field(s) are affected: 
              * "Markup %" for the row updates based on the following formula: "Unit Price $" / "Unit Cost $", rounded to the nearest 5 decimal places; 
              * "Overridden" checkbox for the row is automatically checked if "Group Type" for the linked Group = "Automated" and "Automatically Added" for the item is checked (note that other Item rows are not truly overridden by editing this field); 
          * if the row does not have a "Sales Item Code": N/A (read-only and blank)) 
        * Item Total $ (macro; number; 2 decimals; with the following details / behaviors: 
          * if the row has a "Sales Item Code": 
            * read-only macro;
            * displays the value of "<"Unit Price $"> * <"Item Qty">", rounded to the nearest 2 decimal places; 
          * if the row does not have a "Sales Item Code": 
            * editable macro; 
            * displays the value of "Stored Total $"; 
            * when a value is entered, it is stored in "Stored Total $") 
        * Stored Total $ (hidden column; optional; number, 2 decimals; with the following details / behaviors: 
          * used only for manual items (rows without "Sales Item Code"), to store the value displayed in the "Item Total $" macro; 
          * for the "Automatically Added" Item row for a "Manual"-type Group: 
            * this is initially set from the "Total Group Price $" entry field in the "New Group for Section" prompt, and may be updated from the "Item Total $" on the same row; 
            * if no other Item rows exist for the Group, may be updated from the "Group Proposal Price $" on the linked Group row; 
          * for additional (non-"Automatically Added") Items, it is set/updated from the "Item Total $" on the same row; 
          * note that this may be left blank, for Items / Groups without a price;
          * note that this can be set to a negative number, to allow for entering discounts, etc.) 
        * Automatically Added (checkbox; with the following details / behaviors:
          * auto-set and read-only field;
          * automatically checked when a row is added via the "New Group" on-screen prompt;
          * remains not checked when a row is added manually via the "✚" button;
          * note that this is important, because manually-added "Sales Item"-type Items need to be excluded from the automation that calculates Qty, etc., when "Group Quantity" for an "Automated" or "Sales Item"-type Group is updated, and all included Items need to be updated accordingly; 
          * note with the Phase 1 spec, "Automatically Added" items cannot be deleted from Proposals, to ensure integrity of calculations and of the Items embedded spreadsheet; if one of these Items should not be included in a Proposal, the user can set the "Item Qty" to 0; if needed, additional design & coding work can be done in the future to carefully allow deleting these Items) 
        * Overridden (checkbox; with the following details / behaviors: 
          * this is automatically checked when certain fields for the same row are manually edited (see corresponding specs); note that this means this checkbox is only auto-checked, and never manually checked; 
          * read-only when not checked;
          * when manually unchecked, the following fields in the same row are affected/updated (with the Solution looking up the current values for them from the corresponding Automated Proposal Group or Sales Item record (as applicable), and setting them accordingly):
            * "Item Description" (looks up & sets to the value from the Sales Item); 
            * "Item Qty" (if the row is an "Automatically Added" item for an "Automated"-type Group: looks up & sets based on the "Group Quantity" and the "Item Qty Formula" from the Automated Proposal Group; 
              * note that otherwise (i.e. rows for "Sales Item"-type Groups, etc.), this does not automatically update because it is never checked for other rows); 
            * "Unit Cost $" (looks up & sets to the value from the Sales Item); 
            * "Markup %" (looks up & sets to the value from the Sales Item);  
            * "Unit Price $" (looks up & sets to the value from the Sales Item)) 
        * Order in Group (hidden column; number; 0 decimals; with the following details / behaviors: 
          * auto-set and read-only; 
          * defaults to 1 more than the highest "Order in Group" value for the same Group when the row is added; 
          * this is used to correctly add new rows to the bottom of the list for their Group; 
          * note that this could also be used to facilitate reordering Items in a Group via "🡅" / "🡇" buttons, if that capability is desired in the future -- it would only be available in the All Items screen, not the "Items for Group" screen) 
        * Group Unit Price $ (read-only macro; dynamically displays the "Group Unit Price $" for the linked Group; value is visible on the top row only, to avoid showing multiple rows with the same value)
        * Group Printout Price $ (read-only macro; dynamically displays the "Group Proposal Price $" for the linked Group; value is visible on the top row only, to avoid showing multiple rows with the same value)
      * Automatically sorted by:
        * First by: "Group" (to facilitate proper sorting in the "All Items" embedded spreadsheet, which is the unfiltered table from which this one is drawn);
        * Second by: "Order in Group" 
      * Buttons to add/remove rows:
        * "✚" (visible on the "Items for Group" screen if "Ready to Send to Customer" is not checked)
        * "🞭" (visible on the "Items for Group" screen if "Ready to Send to Customer" is not checked and "Automatically Added" for the selected row is not checked)
      * Space for rows: 
        * On the "Items for Group" screen: Shows about 20 rows without scrolling
        * On the "All Items" screen: Shows about 12 rows without scrolling 
      * Other Notes: 
        * Note on how Items are added for different Group Types:
          * For "Automated"-type Groups: Items are added automatically based on the selected Automated Proposal Group, and additional linked Items can be added manually.
          * For "Sales Item"-type Groups: The initial linked Item is added automatically based on the selected Sales Item, when the button is clicked to add the Group, and additional linked Items can be added manually.
          * For "Manual"-type Groups: No items are added automatically, but linked Items can be added manually. 
        * The same Item may be used by multiple different Groups (though not more than once by the same Group). When the same Item is used by more than one Group, it will appear in separate rows for each Group on the "All Items" embedded spreadsheet. 



  


  


This concludes the spec for the Proposal Itemization Section.

  


Development Specification

Change Requests: 

  * Tim Reitz 11/26/2025: [[[IN12341](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12343&)]] - ZLP - Phase 1 - Proposal Record - All Items RG - Improve Behavior for Setting "Overridden"
  * 


  


  


Mockup (included in the "Additional Items for Proposal Record" mockup tab): [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=2037082832#gid=2037082832](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=2037082832#gid=2037082832)

  


Ellis Miller 06/17/2025: 

Large RG, but not super complicated.

  


[ ] View All Items: Make this an embedded RG on a child screen so that we don't have an "Add Row" button in the UI. Make sure that you have a Add Row button for the linked Items in Group RG. Talk to me with questions.

[ ] Use a helper list on Sales Item Code to format list items as described. 

[ ] If needed for testing, you could temporarily add the Add Row button before the linked functionality is all working.

  


[ ] Add Field Change expressions to delete any Item rows on save where the linked Group no longer exists.

  


BID: 1 DAY
