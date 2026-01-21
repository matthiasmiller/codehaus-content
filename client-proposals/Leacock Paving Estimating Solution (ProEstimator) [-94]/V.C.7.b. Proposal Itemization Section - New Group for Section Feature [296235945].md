5.3.7.2. Proposal Itemization Section - New Group for Section Feature

  


Requirements

  * New Group for Section (checkbox; gray background behind the checkbox and the label; with the following details / behaviors:
    * visible if both of the following conditions are true:
      * there is at least one row in the "Sections" embedded spreadsheet and 
      * "Ready to Send to Customer" is not checked (i.e. hidden in limited editing mode);
    * when checked, the "New Group On-Screen Prompt" opens;
    * when unchecked, the prompt is hidden and the included entry fields are cleared; 
    * note that at some point in the future, the checkbox could be changed to a button, as additional capabilities are added to the software platform;
  * "Add at least one Section before adding Groups." (on-screen message in gray font; visible if there are no rows in the "Sections" embedded spreadsheet, located in the same the location as "New Group for Section")



  


  * New Group On-Screen Prompt (no label; visible with a gray background when the "New Group for Section" checkbox is checked; with the following items)
    * Section (required; drop list of "Section Name" items included on the "Sections" embedded spreadsheet on the current Proposal; defaults to the currently-selected row on the embedded spreadsheet)
    * Group Type (required; drop list of "Group Type" list items)
    * Automated Group (visible and required if "Group Type" = "Automated"; drop list of "Names" for all active Automated Proposal Group records)
    * Sales Item (visible and required if "Group Type" = "Sales Item"; drop list of all active Sales Items records, in the following format: "<Sales Item Description> \- <Sales Item Code>")
    * Quantity (visible and required if "Group Type" = "Automated" or "Sales Item"; number; 2 decimals)
    * UOM (visible if "Group Type" = "Automated" or "Sales Item"; auto-set and read-only; sets to the "Unit of Measure" from the selected "Automated Proposal Group" or "Sales Item")
    * Thickness (in) (visible and required if "Group Type" = "Automated" and if the selected "Automated Proposal Group" has the "Uses & Requires Thickness" checkbox checked; number; 2 decimals; any number entered here automatically rounds up or down to the nearest .25 (i.e. ".00", ".25", ".50", or ".75")) 
    * Group Description (visible and optional if "Group Type" = "Manual"; single-line plain text field)
    * Total Group Price $ (visible and optional if "Group Type" = "Manual"; number; 2 decimals)



  


  * Add Group (button; visible if the "New Group for Section" checkbox is checked; located below the gray area; with the following details / behaviors:
    * validations for the required prompt fields appear on this button when it is clicked with one or more fields blank;
    * clicking this button with all required entry fields filled adds the new row to the Groups embedded spreadsheet with the relevant / corresponding fields set there; 
      * note that "Group Name" on the embedded spreadsheet is set to one of the following: 
        * if "Group Type" = "Automated": the selected Automated Group "Name"; 
        * if "Group Type" = "Manual": the manually-entered "Group Description";  
        * if "Group Type" = "Sales Item": the Sales Item "Description"; 
    * also, when the new row is added to the Groups embedded spreadsheet, corresponding rows are added to the "All Items" embedded spreadsheet for the new Group:
      * if "Group Type" = "Automated Group": rows are added, one for each Sales Item in the Automated Group, with the following set: 
        * "Item Description": sets to the "Description" for the selected Sales Item (same as when "Sales Item Code" is manually set - see corresponding spec in the "All Items" embedded spreadsheet spec); 
        * "Item Qty": set based on the entered "Quantity" and the "Item Qty Formula" on the Automated Proposal Group record;
        * "UOM": sets to the "Unit of Measure" for the selected Sales Item (same as when "Sales Item Code" is manually set - see corresponding spec); 
        * "Unit Cost $": sets to the "Unit Cost $" for the selected Sales Item (same as when "Sales Item Code" is manually set - see corresponding spec); 
        * "Markup %": sets to the "Markup %" for the selected Sales Item (same as when "Sales Item Code" is manually set - see corresponding spec); 
        * "Unit Price $": sets to the "Unit Price $" for the selected Sales Item (same as when "Sales Item Code" is manually set - see corresponding spec); 
      * if "Group Type" = "Sales Item Group": a single row is added for the selected "Sales Item" with "Item Qty" set based on the entered "Quantity"; 
      * if "Group Type" = "Manual Group" and "Total Group Price $" is not blank: a single row is added, with the following details set: 
        * "Sales Item Code" = blank; 
        * "Item Description": 
          * if "Group Description" entry field text is not blank: sets to that text;  
          * if "Group Description" entry field text is blank: sets to "Manual"; 
        * "Stored Total $": set to the "Total Group Price $" entry field value; 
        * note that no Item rows are added for Manual Groups if the "Total Group Price $" is blank (in that case, all that happens is that the "Group Description" entry is set on the new Group row); 
      * for all "Group Type" selections: the "Automatically Added" checkbox is checked for each new Item row)



  


Development Specification

TODO_: Tim Reitz 10/07/2025: Consider whether to include the Sales Item Code in the entry field. 

  


Mockups of all 3 different possibilities, based on the selected "Group Type" (included in the "Additional Items for Proposal Record" mockup tab): [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=2037082832#gid=2037082832](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=2037082832#gid=2037082832)

  


Ellis Miller 06/18/2025:

  


FOR NICCOLAS 

[ ] We are going to use normal fields for this, but we have Field Change on save to clear them out so that they are never saved.

Niccolas Miller 09/15/2025: Using ClearIfHidden instead.

  


[ ] "New Group for Section" is an MRG editable checkbox field:

Niccolas Miller 09/15/2025: I changed the spec from MRG editable checkbox macro to MRG editable checkbox field.

[ ] Returns true if ProposalNewGroupSectionID is non-blank

[ ] When checked, it sets the hidden NewGroupSectionID Detail Variable to the current ProposalSectionID.

[ ] When checked, it clears the field for all other rows.

[ ] When unchecked, it clears the Detail Variable and all New Group variables.

[ ] "New Group Section" is an editable string expression that returns the Section Name for NewGroupSectionID, OnChange it sets it.. Uses helper list of section names from this proposal.

[ ] Rest of fields are simple items as described.

  


[ ] Validation needs to happen via Validation on the Add Group button OR display a label "Please fill in all fields to add group." and as soon as all are filled in, the Add Group button becomes visible.

  


[ ] Add Group button is an OnChange button that appends a new Group row, filling in:

[ ] GroupSectionID - From NewGroupSectionID

[ ] GroupID - maybe set this to a new random number that you store in a detail variable (NewGroupID) so that you can easily use it when adding items.

[ ] All of the NewGroup fields that the user filled in are copied to the RG row

[ ] If it's a Sales Item Group, add the Sales Item Group to the Items RG.

[ ] Can probably just do a NewRG then set the necessary fields (including the new Group ID)

[ ] Set ItemAutomaticallyAdded for the new row

[ ] If it's an Auto Group, add all of the Auto Groups items to the Items RG.

[ ] Will probably need to do a FillRGFromPipeList -- maybe have a string detail variable NewItemIDs that is a pipe-delimited list of random item IDs for however many rows you want to add to the Items RG. You would concatenate all existing ItemRowIDs with this list of random ones for your FillRGFromPipeList.

[ ] For the new Item RG rows, you need to fill in the Sales Item fields for all of the items in the Auto Group.

[ ] Set ItemAutomaticallyAdded for the new rows

[ ] Make sure that quantities are correctly updated. I think if you set GroupQuantity last, it will automatically update the quantities for the linked auto items.

2 DAYS

  


\-------------------
