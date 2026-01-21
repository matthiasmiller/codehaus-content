20.3. Feature for Reviewing Overridden Items on Copied Proposals

  


Requirements

_SM: Tim Reitz 07/07/2025: Let's write this up as a "future" CR.

Sean Miller 07/07/2025: [[[IN11678](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11680&)]] - ZLP -  Feature for Reviewing Overridden Items on Copied Proposals

  


The following feature could be added to facilitate easier reviewing / updating of "Overridden" Items on copied Proposals (the basic approach included in the main spec includes an on-screen message, telling the users to go to the All Sales Items to review them)

  


Estimated Cost: TBD

  


Initial Spec: 

  


Changes to Proposal - Copy Feature: 

  * "One or more Sales Items in this Proposal were manually set / overridden in the Source Proposal. Review this list and uncheck "Overridden" checkboxes (or click "Reset All Overridden") to reset items as needed.  Select the "All Sales Items" button and click-sort the "Overridden" column to review these." (on-screen message in orange font; with the following details:
    * visible until the initial save if the "Copied Record" checkbox is checked and "Copy Type" = "Revised" or "Duplicate" and the Proposal includes one or more items with the "Manual / Overridden" checkbox checked;
    * this alerts the user that one or more items have been copied over directly and not automatically updated to the current default pricing;
    * note that this is the cheaper, simpler approach to alerting the user of these situations; there is an optional add-on that could add a feature to review and confirm/clear the manually-overridden items - see corresponding spec)



  


  * Review Overridden Items (visible until the initial save if the "Copied Record" checkbox is checked and "Copy Type" = "Revised" or "Duplicate" and the Proposal includes one or more items with the "Manual / Overridden" checkbox checked; embedded spreadsheet with the following: 
    * Columns: 
      * Includes all the same columns as the "All Sales Items" embedded spreadsheet -- see corresponding spec.
    * Automatically sorted by: N/A (none) 
    * Buttons to add/remove rows: N/A (rows are automatically included)
    * Buttons to move rows up and down: N/A (rows not movable)
    * Shows 10 rows without scrolling 
    * Other Notes: 
      * This embedded spreadsheet includes one row for each row in the "All Items" embedded spreadsheet that has the "Overridden" checkbox checked)
  * Reset All Overridden Items (button; clicking this unchecks all "Overridden" checkboxes for Items on the "Review Overridden Items" embedded spreadsheet)



  


Development Specification

Tim Reitz 06/26/2025: We're not moving forward with this item now. Let's wait to see how the basic approach that's included works.
