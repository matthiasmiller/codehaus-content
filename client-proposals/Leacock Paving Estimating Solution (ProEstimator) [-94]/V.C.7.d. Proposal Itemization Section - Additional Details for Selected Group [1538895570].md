5.3.7.4. Proposal Itemization Section - Additional Details for Selected Group

  


Requirements

  * "Additional Details for Selected Group:" (on-screen label, refers to the following items) 
  * Group Quantity (editable; on-screen version of the "Group Quantity" field for the selected Group row - see corresponding spec)
  * Group UOM (read-only field; on-screen version of the "Group UOM" field for the selected Group row - see corresponding spec) 
  * Thickness (in) (editable; on-screen version of the "Thickness (in)" field for the selected Group row - see corresponding spec)
  * Group Name (editable; on-screen version of the "Group Name" field for the selected Group row - see corresponding spec) 
  * Total Item Price $ (read-only macro; on-screen version of the "Total Item Price $" for the selected Group row - see corresponding spec) 
  * Group Unit Price $ (read-only macro; on-screen version of the "Group Unit Price $" for the selected Group row - see corresponding spec) 
  * Group Proposal Price $ (read-only macro; on-screen version of the "Group Proposal Price $" for the selected Group row - see corresponding spec)



  


  * Section Total $ (read-only macro; number; 2 decimals; with the following details / behaviors: 
    * this is the Section price for the Customer, displayed on the Proposal and the printout;  
    * if "Proposal Result" ≠ "Awarded": displays the sum of "Group Proposal Price $" values for all Groups in the "Section" for the currently-selected Group; 
    * if "Proposal Result" = "Awarded": displays the sum of "Group Proposal Price $" values for all "Awarded" Groups in the "Section" for the currently-selected Group (specifically, all with the "Group Awarded" checkbox checked)) 



  


  * Delete Selected Group (visible if "Ready to Send to Customer" is not checked; button; deletes the currently-selected Group line from the Groups embedded spreadsheet; associated Sales Items for the Group also are deleted on Save)



  


Development Specification

Ellis Miller 06/17/2025:

[ ] The editable fields are always visible MRG versions of the conditionally visible RG columns.

[ ] I'd recommend naming these:

[ ] ProposalGroupMrgQuantity

[ ] ProposalGroupMrgUOM

[ ] ProposalGroupMrgThickness

[ ] ProposalGroupMrgName

[ ] We'll need to clone behavior and validation. Please cross-link with comments:

{ NOTE: CLONED BETWEEN RG AND MRG }

  


[ ] The readonly macros can just be expression controls that have the same expressions as the conditionally visible columns.

  


[ ] Delete Selected Group -- simple delete button. The spec for deleting the linked items is in the "View All Items" section.

  


4 HOURS
