5.3.2. Proposal - Copy Proposal Section

  


Requirements

  * Copy Proposal section (visible above the Customer & Job Information Section until the first Save for new copied records (specifically, visible until the first save if the "Is Copied Record" checkbox is checked))



  


  * "This is a copied Proposal. Please select from the following copy types:" (visible if the proposal is copied and no copy button has been selected (based on a hidden detail variable); on-screen message in red font) 
  * "Please save this new Proposal record to continue, or refresh the page to change your copy type selection." (visible if the proposal is copied and a copy button has been selected; this provides instruction for the user)



  


  * Revised Proposal (button; with the following details: 
    * always visible if the proposal is copied and no copy button has been selected (based on the hidden detail variable); (note that this button is visible regardless of the "Proposal Type" for the Source Proposal); 
    * if clicked, various fields on the Proposal are affected -- see the "Copy Action Details" spec for "When "Revised Proposal" Button is Clicked")



  


  * Change Order (button; with the following details: 
    * visible if the proposal is copied and no copy button has been selected (based on the hidden detail variable) and "Proposal Type" for the Source Proposal ≠ "Change Order" (note that Change Orders are never created from other Change Orders); 
    * if clicked, various fields on the Proposal are affected -- see the "Copy Action Details" spec for "When "Change Order" Button is Clicked")



  


  * Duplicate Proposal (button; with the following details: 
    * visible if the proposal is copied and no copy button has been selected (based on the hidden detail variable) and "Proposal Type" for the Source Proposal ≠ "Change Order" (note that Duplicate Proposals are never created from Change Orders); 
    * if clicked, various fields on the Proposal are affected -- see the "Copy Action Details" spec for "When "Duplicate Proposal" Button is Clicked")



  


  * Is Copied Record (hidden field; checkbox; with the following details / behaviors:
    * defaults to checked if the Proposal record was created via the Copy feature; 
    * user note: this checkbox causes the red message and buttons to be visible, and lets the software know that the current Proposal was created via copy from another Proposal;
    * error on Save if this checkbox is checked and the record has not been saved and none of the copy type buttons have been clicked: "Please select the desired copy type button."; based on a hidden detail variable; this ensures that a copied record has one of the buttons clicked before being saved); 
    * note that other fields depend on this one) 
  * Is Revised (hidden field; checkbox; sets to checked when the "Revised Proposal" copy type button is clicked)  
  * Is Change Order (hidden field; checkbox; sets to checked when the "Change Order" copy type button is clicked; is not cleared when "Revised Proposal" is clicked on a copy of a Change Order)
  * Is Duplicate (hidden field; checkbox; sets to checked when the "Duplicate Proposal" copy type button is clicked)  



  


  * Copied from Proposal # (hidden plain text field; auto-set and read-only; auto-sets to the "Proposal #" from the "Source Proposal" when a record is created via the Copy feature) 



  


  * "One or more Sales Items in this Proposal were manually set / overridden in the Source Proposal. Open View All Items and click-sort the Overridden column to review. Uncheck the Overridden checkbox to reset rows as needed. Also review rows with no Sales Item Code. Click the Dismiss button if no further change is needed." (on-screen message in orange font; with the following details / behaviors:
    * visible if all of the following conditions are met:
      * either "Is Revised" or "Is Duplicate" checkbox is checked and "Is Change Order" is not checked and 
      * the current Proposal includes one or more Items with the "Overridden" checkbox checked and/or with "Sales Item Code" = blank and 
      * the "Dismiss Items Message" checkbox is not checked;
    * this alerts the user that one or more Items have been copied over directly from the Source Proposal and not automatically updated to the current default pricing;
    * note that this is the cheaper, simpler approach to alerting the user of these situations; there is an optional add-on that could add a feature to review and confirm/clear the manually-overridden items - see corresponding spec)
  * Dismiss (button; with the following details / behaviors:
    * visible in edit mode if all of the following conditions are met:
      * either "Is Revised" or "Is Duplicate" checkbox is checked and "Is Change Order" is not checked and
      * the current Proposal includes one or more Items with the "Overridden" checkbox checked and/or with "Sales Item Code" = blank and 
      * the "Dismiss Items Message" checkbox is not checked;
    * when clicked, the "Dismiss Items Message" checkbox is checked, hiding the above on-screen message)
  * Dismiss Items Message (hidden; checkbox; editable in Limited Editing Mode; checked via the "Dismiss" button; note that this is automatically unchecked when a Proposal is copied, to ensure that it starts new each time)



  


Development Specification

Change Requests: 

  * Tim Reitz 11/25/2025: [[[IN12308](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12310&)]] - ZLP - Phase 1 - Proposal Record - Copy Proposal Issues
  * 


  


  


Mockup (included in the "Additional Items for Proposal Record" mockup tab): [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=2037082832#gid=2037082832](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=2037082832#gid=2037082832)

  


  


Ellis Miller 06/18/2025: 

  


FOR NICCOLAS TO CODE

[ ] Use an OnCopy action to set a Copied boolean field

[ ] Validate on save against having a Copied record without a CopyType specified: "

  


[ ] For each button:

[ ] Sets copy type

[ ] Sets the CopiedFromProposalNum string field to ProposalNum

[ ] Clears ProposalNum

[ ] Clears fields

  


BID: 3 DAYS
