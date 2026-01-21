5.3.7.3. Proposal Itemization Section - Groups Embedded Spreadsheet

  


Requirements

  * Groups (embedded spreadsheet with the following; all fields are set according to corresponding prompt fields in the "New Group for Section" process; note that this includes all Groups for all Sections on the current Proposal: 
    * Columns: 
      * Group Row ID (hidden column; with the following behaviors / details:
        * auto-set and read-only;
        * editable via import;
        * numeric field;
        * unique identifier for the row;
        * note that for any Proposal Groups imported from the existing Power App solution, this will be set to the "Power App Quote Group ID" from the imported data) 
      * Section ID (hidden column; with the following behaviors / details:
        * auto-set and read-only;
        * numeric field;
        * auto-set to the "Section ID" for the selected "Section" entry field on the "New Group for Section" prompt feature, when a new row is added;
        * used for linking between the Group for the row and the corresponding Section from the "Sections" embedded spreadsheet)
      * Section (read-only macro; with the following behaviors / details:
        * plain text;
        * displays the "Section Name" for the selected "Section ID";
        * text displays in bold font for the first/top row for each Section in this embedded spreadsheet; note that if multiple Groups are added for the same Section, the page must be refreshed for this formatting to be displayed properly)
      * Opt / Alt (read-only macro; displays the Option / Alternate information for the selected Section, based on the Section's "Section Inclusion Type", in the following format:
        * if "Section Inclusion Type" = "Standard": this is blank;
        * if "Section Inclusion Type" = "Option": "Opt <Opt / Alt #>";
        * if "Section Inclusion Type" = "Alternate": "Alt <Opt / Alt #>"; 
        * examples: "Opt 1", "Alt 3", etc.)
      * Group Type (column hidden by default, visible if "Show All Columns" is checked; read-only list field ("Group Types" list); auto-set to the selected "Group Type" from the "New Group On-Screen Prompt" when a new row is added)
      * Group Description (read-only macro; this is the text that is displayed in the itemization on the Proposal printout; with the following behaviors / details:
        * if "Group Type" = "Automated":
          * displays the following: "<Group Quantity> <Group UOM> of <Thickness (in)>" <Group Name> @ $<Group Unit Price $> / <Group UOM>"; 
            * the "of <Thickness (in)>" portion is included only if the selected "Automated Proposal Group" has the "Uses & Requires Thickness" checkbox checked (same condition as the requirement and editability for the field, see the corresponding data entry spec and column spec);  
        * if "Group Type" = "Sales Item":
          * displays the following: "<Group Quantity> <Group UOM> of <Group Name> @ $<Group Unit Price $> / <Group UOM>"; 
          * note that this includes the details for the main Sales Item (i.e. the one with "Automatically Added" checkbox checked) for the Group, and if other Sales Items are added to it, their information will not be included here, other than the resulting updated "Group Unit Price $";
        * if "Group Type" = "Manual": displays the "Group Name" for the row)
      * Automated Group (column hidden by default, visible if "Show All Columns" is checked; read-only list field ("Automated Proposal Group" items); with the following behaviors / details:
        * if "Group Type" = "Automated": 
          * required;
          * auto-set to the entry in the "Automated Proposal Group" entry field on the "New Group for Section" prompt feature, when the row is added;
        * if "Group Type" = "Sales Item" or "Manual": N/A (blank and read-only)
      * Group Name (column hidden by default, visible if "Show All Columns" is checked; plain text; editable; with the following behaviors / details:
        * if "Group Type" = "Automated":
          * required;
          * set to the "Name" of the selected Automated Proposal Group in the "Automated Group" entry field on the "New Group for Section" prompt feature, when the row is added; 
        * if "Group Type" = "Sales Item": 
          * required;
          * set to the "Description" of the selected Sales Item in the "Sales Item" entry field on the "New Group for Section" prompt feature, when the row is added;
        * if "Group Type" = "Manual":
          * optional;
          * set to the text of the "Group Description" entry field on the "New Group for Section" prompt feature, when the row is added;
        * for all Group Types, may be edited via the "Group Name" field on the main screen below this embedded spreadsheet) 
      * Group Quantity (column hidden by default, visible if "Show All Columns" is checked; with the following behaviors / details:
        * if "Group Type" = "Automated" or "Sales Item":
          * required ("0" is an accepted value); 
          * number; 2 decimals;
          * validates against negative values - error on the field: "Group Quantity cannot be negative."; 



Austin Priest 11/24/2025: _VA Negative values are currently accepted on the field.

Tim Reitz 11/24/2025: Chasing in [[[IN12338](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12340&)]]. 

  * set to the entry in the "Quantity" entry field on the "New Group for Section" prompt feature; note that this spec should be in sync with the corresponding entry field spec;
  * when this is edited, the "Item Qty" for all linked "Automatically Added" Items for the row with the "Overridden" checkbox not checked are automatically updated as well:
    * for "Automated" Groups: "Item Qty" values update based on the the "Item Qty Formula" on the Automated Proposal Group record;
    * for "Sales Item" Groups: "Item Qty" value updates to match the "Group Quantity"; 
    * this ensures that items that are included on the selected Automated Proposal Group, or the Sales Item that corresponds directly to the selected "Sales Item"-type Group, are updated correctly; 
  * if any non-standard Items (i.e., with "Automatically Added" checkbox not checked and/or "Overridden" checkbox checked) are included in the Group, the "Item Qty" for those is not automatically updated when this is edited, but a warning message is displayed here on the "Group Quantity" field on change: 
    * "The following manually-added / overridden Item(s) for this Group will not be auto-updated: <Item>, <Item>, <Item>."; 
  * may be edited via the "Group Quantity" field on the main screen below this embedded spreadsheet)


  * if "Group Type" = "Manual": N/A (blank and read-only);



Austin Priest 11/24/2025: _VA there is some strange behavior here but it may be as intended. on a sales item row with only one item, if you edit the group Quantity it updates item quantity on the included items sheet but if you edit the Item Qty field on the included items sheet it does not update the Group Quantity . Again I think that this may be as intended, just a little weird.

Tim Reitz 11/25/2025: I think this is actually an issue for the All Items RG (including, but perhaps not limited to the "Overridden" checkbox. 

Tim Reitz 11/26/2025: Chasing it [[[IN12341](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12343&)]] - ZLP - Phase 1 - Proposal Record - Tweaks to All Items RG. 

  * Group UOM (column hidden by default, visible if "Show All Columns" is checked; read-only list field ("Units of Measure" list); with the following behaviors / details:
    * if "Group Type" = "Automated": 
      * auto-set to the "Unit of Measure" for the selected Automated Proposal Group in the "Automated Group" entry field on the "New Group for Section prompt feature, when the row is added; 
      * visible via the "Group UOM" field below this embedded spreadsheet; 
    * if "Group Type" = "Sales Item": 
      * auto-set to the "Unit of Measure" for the selected Sales Item in the "Sales Item" entry field on the "New Group for Section prompt feature, when the row is added; 
      * visible via the "Group UOM" field below this embedded spreadsheet; 
    * if "Group Type" = "Manual": N/A (blank and read-only)) 
  * Thickness (in) (column hidden by default, visible if "Show All Columns" is checked; with the following behaviors / details:
    * if "Group Type" = "Automated":
      * if the selected "Automated Proposal Group" has the "Uses & Requires Thickness" checkbox checked:
        * required; 
        * number; 2 decimals;
        * any number entered here automatically rounds up or down to the nearest .25;
        * set to the entry in the "Sales Item" entry field on the "New Group for Section" prompt feature; 
        * note that this spec should be in sync with the corresponding entry field spec;
        * note that when a "Thickness" value is entered, it is always in inches; 
        * editable via the "Thickness (in)" field below this embedded spreadsheet; 
      * otherwise (if "Used & Requires Thickness" is not checked), N/A (blank and read-only); 
    * if "Group Type" = "Sales Item" or "Manual": N/A (blank and read-only))
  * Included Items (button with "Items for Group" text; opens the "Items for Group" child screen, displaying the items for the Group - see corresponding spec) 
  * Total Item Price $ (column hidden by default, visible if "Show All Columns" is checked; with the following behaviors / details:
    * read-only macro; 
    * number; 2 decimals; 
    * displays the sum of "Item Total $" for all Items linked to the selected Group row; 
    * visible via the "Total Item Price $" field below this embedded spreadsheet; 
    * note that this is the total initial Group price, not displayed on the Proposal Printout; the actual "Group Proposal Price $" is used for the printout and may vary slightly because of the rounding of the "Unit Price $"; 
  * Group Unit Price $ (column hidden by default, visible if "Show All Columns" is checked; with the following behaviors / details: 
    * read-only macro;
    * number; 2 decimals;
    * displays the value of "<"Total Item Price $"> / <"Group Quantity">" for the row, rounded to the nearest 2 decimal places;
    * is blank for "Manual" groups; 
    * visible via the "Group Unit Price $" field below this embedded spreadsheet)
  * Group Proposal Price $ (macro; number; 2 decimals; this is the price that is displayed for the Group on the Proposal record and printout; with the following behaviors / details:
    * if "Group Type" = "Automated" or "Sales Item":
      * read-only macro;
      * displays the value of "<"Group Unit Price"> * <"Group Quantity">" for the row, rounded to the nearest 2 decimal places; 
      * included for correctly handling rounding of calculated unit prices; 
    * if "Group Type" = "Manual":
      * displays the sum of "Item Total $" values for any/all Items linked to the selected Group row;
      * if the "Items for Group" for the row has more than one Item: read-only macro;
      * if the "Items for Group" for the row has only one item:
        * editable macro;
        * if edited, sets the "Stored Total $" field on the single linked ("Automatically Added") Item;
      * maybe be blank or negative - see "Item Total $" spec notes;
    * for all Group Types, visible via the "Group Proposal Price $" field below this embedded spreadsheet)
  * Group Awarded (checkbox; with the following details / behaviors: 
    * editable if "Proposal Result" = "Awarded"; 
    * auto-sets to checked for Groups with "Opt / Alt" = blank when "Proposal Result" is set to "Awarded" \- see spec for "Proposal Result"; 
    * when checked, the row is officially included in the work to be done for the job; 
    * when checked, the following field(s) are immediately affected:
      * "Group Awarded Date" for the row is set to the current date;
      * "Group Target Start" for the row is set to the contents of the "Job Target Start Comments" field (to handle times a Group is marked as Awarded after "Job Target Start Comments" has been set)
    * when this is unchecked, the following field(s) are affected:
      * "Group Awarded Date" for the row is cleared;
      * "Group Target Start" for the row is cleared;
    * editable in limited editing mode)
  * Group Awarded Date (date; with the following details / behaviors: 
    * editable and required if "Group Awarded" checkbox is checked for the row; 
    * auto-sets to the current date when "Group Awarded" is checked or (conditionally) when "Proposal Result" is set to "Awarded" \- see corresponding specs;
    * is cleared when "Group Awarded" is unchecked or when "Proposal Result" is changed from "Awarded" to something else - see corresponding specs;
    * note that individual Groups can be awarded on different dates, even days or weeks after other parts of the Proposal have been marked as Awarded;
    * editable in limited editing mode)
  * Group Target Start (plain text field; with the following details / behaviors: 
    * editable and required if "Group Awarded" is for the same row is checked; 
    * auto-sets to the contents of the "Job Target Start Comments" field when that field is set or when "Group Awarded" for the row is checked, as applicable; 
    * is cleared when "Group Awarded" for the row is unchecked;
    * editable in limited editing mode) 
  * Group Scheduled Start Date (date; with the following details / behaviors:
    * editable if the "Group Awarded" checkbox is checked for the row and "Job Scheduled Start Date" is not blank;
    * warning on Save if editable and blank: "Group Scheduled Start Date is blank for one or more Awarded Groups.";



Austin Priest 11/24/2025: _VA I am seeing this warning when the field is not editable.(When the Job Scheduled field is not checked.)

Tim Reitz 11/24/2025: Chasing in [[[IN12338](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12340&)]]. 

  * if the "Group Awarded" checkbox is checked for the row, auto-sets to the current date when "Job Scheduled Start Date" is set - see corresponding spec;
  *  if the "Group Awarded" checkbox is checked for the row, is cleared when "Job Scheduled Start Date" is cleared - see corresponding spec;
  * editable in limited editing mode) 


  * Automatically sorted by: N/A (unsorted; items remain in the order in which they were entered or moved) 
  * Buttons to add/remove rows: 
    * "New Group for Section" (see corresponding spec) 
    * "Delete Selected Group" (see corresponding spec) 
  * Buttons to move rows up and down: "🡅" / "🡇" (visible if "Ready to Send to Customer" is not checked):
  * Show 12 rows without scrolling 
  * Additional Validations: 
    * Error on Save if there are multiple Groups for a Section and they aren't all together on the embedded spreadsheet: "Not all Groups for Section "<Section Name>" are together. Reorder the Groups before saving."
  * Other Notes: 
    * Selecting a row on this embedded spreadsheet will show the "Additional Details for Selected Group" fields for the selected Group - see corresponding specs.
    * Rows display in gray text if "Result" = "Awarded" for the Proposal and "Group Awarded" checkbox for the row is not checked.)



  


Development Specification

Mockup with main visible columns: On the main detail screen mockup. 

  


Mockup with all columns visible (included in the "Additional Items for Proposal Record" mockup tab): [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=2037082832#gid=2037082832](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=2037082832#gid=2037082832)

  


[ ] Group Row ID

[ ] Section - font formatting if SectionID <> SectionID[p1] I think

[ ] Opt / Alt -- create a SectionOptAltDisplay macro that formats correctly and then a GroupSectionOptAltDisplay that looks this up using the SectionID.

[ ] Group Description - editable macro TODO:

[ ] Add a ProposalGroupAutoGroupDesc( vQuantity, UOM, vThickness, vUnitPrice)  macro that evals on Group RG row.

[ ] Add a ProposalGroupSalesItemDesc macro that evals on Group RG row.

[ ] Add a ProposalGroupDesc macro that returns one of these or the GroupName (for Manual) as appropriate.

BID: 4 DAYS (not counting Items RG or New Groups buttons)
