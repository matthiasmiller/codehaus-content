5.3.8.2. Proposal Details - Fields on Left Side

  


Requirements

  * Proposal Oil Index (no label; plain text macro; with the following details / behaviors:
    * if both the "Override Oil Index" and the "Ready to Send to Customer" checkboxes are not checked:
      * read-only;
      * dynamically displays the "Current PA Oil Index" from Silverloom Settings (see corresponding spec); 
    * if "Override Oil Index" is checked and "Ready to Send to Customer" is not checked:
      * editable; 
      * required;
      * displays the text from the "Stored Proposal Oil Index" field (see corresponding spec); 
      * to be manually edited by the user as needed; 
      * when edited, the entered value is stored in the hidden "Stored Proposal Oil Index" field;
    * if the "Ready to Send to Customer" checkbox is checked:
      * read-only;
      * displays the frozen value of the hidden "Stored Proposal Oil Index" field, to preserve data integrity; 
      * bold font;
    * note that if the Oil Index needs to be changed after the Proposal has been sent to the customer, it normally would warrant a new (Revised) Proposal being created) 
  * Stored Proposal Oil Index (hidden; plain text field; with the following details / behaviors:
    * used to store the overridden Oil Index or the frozen Oil Index when the proposal was sent;
    * set via:
      * the "Override Oil Index" checkbox (see corresponding spec), or 
      * the "Proposal Oil Index" macro (when editable), or
      * automatically when the "Ready to Send to Customer" checkbox is checked -- see corresponding specs) 



  


  * Override Oil Index (checkbox; with the following details / behaviors: 
    * to be used to allow the user to override the default "Proposal Oil Index" if needed, such as for jobs in states other than Pennsylvania, etc.; 
    * when checked, the following field(s) are affected:
      * "Stored Proposal Oil Index": sets to the following: "<Current Month & Year, in MMMM YYYY format> <Job Address State abbreviation> Oil Index: $", i.e. "April 2025 MD Oil Index: $"; note that the user should enter in the dollar value after the dollar sign, and make other changes as needed; 
    * when unchecked, the following field(s): are affected:
      * "Stored Proposal Oil Index": clears; 
    * warning on the first Save after this is checked: "Oil Index overridden. Confirm whether any section or group names need to updated to match.")



  


  * Total Items Price $ (read-only macro; number; 2 decimals; displays the sum of "Total Item Price $" for all Groups on the Proposal; displays in gray text; this is the based on the initial Group prices, not used for the actual Proposal Price to the Customer) 
  * Total Proposal Price $ (read-only macro; number; 2 decimals; with the following details / behaviors:
    * this is the price for the Customer, displayed on the Proposal and the printout;  
    * if "Proposal Result" ≠ "Awarded": displays the sum of "Group Proposal Price $" values for all "Standard" Groups on the Proposal (specifically, all Groups with "Opt / Al" = blank);
    * if "Proposal Result" = "Awarded": displays the sum of "Group Proposal Price $" values for all "Awarded" Groups on the Proposal, regardless of "Section Inclusion Type" (specifically, all Groups with the "Group Awarded" checkbox checked)) 



  


  * Deposit Required (checkbox; with the following details / behaviors: 
    * defaults to not checked; 
    * when checked, "Deposit Amount $" is made visible - see corresponding spec) 
  * Deposit Amount $ (read-only macro; with the following details: 
    * number; 2 decimals;
    * visible if "Deposit Required" checkbox is checked; 
    * displays the following: 
      * if "Ready to Send to Customer" is not checked: displays the estimated calculation (value of the hidden "Calculated Deposit Amount $" macro); 
      * if "Ready to Send to Customer" is checked: displays the finalized calculation (contents of the hidden "Stored Deposit Amount $" field); 



Austin Priest 11/25/2025: _VA So I noticed that If you have a proposal where deposit required was checked, then you mark it ready to send, then change the Proposal Deposit % in sliverloom settings, on the proposal printout you see the updated percentage from the silverloom settings not the percentage that was set when the proposal was marked ready to send. therefore the Deposit Amount $ on the record and the Deposit % on the PDF do not agree.

![](data:image/png;base64,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)

Tim Reitz 11/26/2025: Good catch! Chasing in [[[IN12346](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12348&)]]. 

  * if desired, this could be made editable in the future, with consideration of what validations are needed) 


  * Calculated Deposit Amount $ (hidden; read-only macro; with the following details / behaviors: 
    * number; 2 decimals; 
    * returns the current calculated value for the "Deposit Amount $", based on the following calculation: (<"Total Proposal Price $"> * <the decimal equivalent of "Proposal Deposit %" in Silverloom Settings>), rounded to the nearest 2 decimal places)  
  * Stored Deposit Amount $ (hidden; read-only stored field; number; 2 decimals; automatically set / cleared when "Ready to Send to Customer" is checked or unchecked - see corresponding spec; note that this remains unchanged, and does not update based one which Groups are Awarded) 



  


  * Include Unit Price Details (checkbox; defaults to not checked; if checked, the "Unit Price Details" field becomes visible - see corresponding spec)
  * Unit Price Details (visible if "Include Unit Price Details" checkbox is checked; optional; multi-line plain text field; used for documenting manually-entered notes about unit prices for the Proposal) 



  


  * Add Proposal Notes (with the following details / behaviors: 
    * multi-select drop list of active "Proposal Note" items, sorted by "Sort Order" \+ "Note Text"; 
    * user selects the note(s) that they wish to add to the Proposal, then clicks the "Append to Proposal Notes" button to add the selected items to the memo; this process can be repeated to add additional notes to the bottom of the memo) 
  * Append to Proposal Notes (visible if one or more items are selected in the "Add Proposal Notes" drop list; button; when clicked the following are affected: 
    * all selected "Proposal Note" items in the "Add Proposal Notes" drop list are added to the bottom of the "Proposal Notes" memo below, each in a separate line with a "\- " prefix, to create a type of bulleted list as bulleted list items, in the sequence in which they are displayed on the drop list; 
    * all checked checkboxes in the drop list are cleared) 
  * Proposal Notes (with the following details / behaviors: 
    * editable memo; 
    * as mentioned in the above spec, "Proposal Note" items are added to this memo from the "Add Proposal Notes" multi-select drop list, when the "Append to Proposal Notes" button is clicked;
    * also, users can manually edit this memo (either editing Proposal Note" items that were added, or adding additional text))



  


Development Specification

Change Requests: 

  * Tim Reitz 11/25/2025: [[[IN12304](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12306&)]] - ZLP - Phase 1 - Proposal Record - Improvements to "Deposit Required" / "Deposit Amount $"
  * 


  


  


Ellis Miller 06/19/2025: 

  


[ ] Proposal Oil Index / Overrides - 2 Hours

[ ] On-screen warning: ProposalOilIndexOutOfSyncMsg macro:

[ ] You will need a DollarsFromPAOilIndexString( vString) - That does a RightOf on vString for "PA Oil Index: $" and trims closing parentheses.

[ ] You can then do a ConcatRG through the ItemsRG returning OilIndexDollars that do not match the OilIndexDollars from the ProposalOilIndex macro (may be blank if "Override Oil Index"), then PipeListRemoveDuplicates and finally format the results as noted in spec.

2 Hours

Tim Reitz 09/23/2025: We're removing this (see notes in History and [[PC0181545]]). 

[ ] Misc Fields 4 Hours
