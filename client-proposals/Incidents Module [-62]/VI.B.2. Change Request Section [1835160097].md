6.2.2. Change Request Section

  


Requirements

Change Request section (visible if Type = Change Request): 

  * Change Request Status (no label; displayed in the section heading; displays the current CR status from the ChangeRequestsWorkflows list - see corresponding section of the spec) 



  


  * Left-hand column: 
    * Status Notes (plain text)  
    * Deploy Target (optional date + plain text field; to be used to document a target deployment date and/or related notes)
    * Design Started (checkbox + date + optional plain text field; with the following details / behaviors: 
      * checkbox and date field toggle; 
      * defaults to checked; 
      * if checkbox is checked, CR Status = "In Design" until a subsequent status is triggered; 
      * note that this defaults to checked to assume that a new CR will start out in the "In Design" status, but the checkbox can be manually unchecked to send it to "Awaiting Design")
    * Draft Complete (checkbox + date + optional plain text field; with the following details / behaviors: 
      * checkbox and date field toggle; 
      * if checkbox is checked, CR Status = "Awaiting Vendor Approval" until a subsequent status is triggered)
    * Vendor Approval (drop-list + optional editable date field; with the following details / behaviors: 
      * drop list and date field toggle; defaults to blank;  
      * drop-list contains the following items: blank / "Approved" / "Declined" / "Deferred"; 
      * if "Approved" is selected, CR Status = "Send to Client" until a subsequent status is triggered; 
      * if "Declined is selected, CR Status = "Declined by Vendor"; 
      * if "Deferred" is selected, CR Status = "Deferred by Vendor") 
    * Sent To Client (checkbox + date + optional plain text field; with the following details / behaviors: 
      * checkbox and date field toggle; 
      * if checkbox is checked, CR Status = "Awaiting Client Approval" until a subsequent status is triggered)
    * Client Approval (drop-list + optional editable date field; with the following details / behaviors: 
      * drop list and date field toggle; 
      * defaults to blank; 
      * drop-list contains the following items: blank / "Approved" / "Declined" / "Deferred"; 
      * if "Approved" is selected, CR Status = "Coding" until a subsequent status is triggered; 
      * if "Declined is selected, CR Status = "Declined by Client"; 
      * if "Deferred" is selected, CR Status = "Deferred by Client") 
    * CLS Job ID (plain text field; for entering a CLS Product Change ID) 
    * IN (visible if a CLS Job ID is entered for a job that has a corresponding Incident in ZCH; link to open to open the corresponding Incident) 
    * PC (visible if a CLS Job ID is entered; link to open to open the corresponding Product Change)



Tim Reitz 09/25/2025: We recently did a CR to get rid of "IN" and update "PC" to "View PC"

  * Create PC (link; redirects to CLS to create a new blank Product Change with various fields defaulted) 
  * Coded (checkbox + date + optional plain text field; with the following details / behaviors: 
    * checkbox and date field toggle; 
    * if checkbox is checked, CR Status = "Testing" until a subsequent status is triggered)
  * Tested (checkbox + date + optional plain text field; with the following details / behaviors: 
    * checkbox and date field toggle; 
    * if checkbox is checked, CR Status = "Needs Documentation" until a subsequent status is triggered)
  * Documented (checkbox + date + optional plain text field;  with the following details / behaviors: 
    * checkbox and date field toggle; 
    * if checkbox is checked, CR Status = "Ready to Deploy" until a subsequent status is triggered)
  * Deployed (checkbox + date + optional plain text field; with the following details / behaviors: 
    * checkbox and date field toggle; 
    * if checkbox is checked, CR Status depends on the following: 
      * if Billing Type = blank, "Fixed Price", or "Time & Materials", CR Status = "Needs Billing" until a subsequent status is triggered; 
      * if Billing Type = any other item, CR Status = "Complete")
  * Billed (checkbox + date + optional plain text field; with the following details / behaviors:  
    * visible if Billing Type = blank, "Fixed Price", or "Time & Materials"; 
    * checkbox and date field toggle; 
    * if checkbox is checked, CR Status = "Complete")
  * Invoice Line (optional plain text field) 



  


  * Right-hand column: 
    * Client Code (drop list of Client Codes; with the following details / behaviors: 
      * defaults to blank; 
      * when selected, the following are auto-set: 
        * "Contact", 
        * "Organization", 
        * "Solution Provider"; 
      * includes an ellipsis button to open the selected record, or open a new record if blank) 
    * Solution Provider (drop list of Solution Providers; defaults to blank; auto-sets based on the "Client Code" when one is selected) 
    * Billing Type (optional; drop list of Billing Types; defaults to blank)
    * Est. Hours (visible if "Billing Type" = blank or does not start with "No Charge"; number field allowing 2 decimals)
    * Est. Min Price (visible if "Billing Type" = blank or does not start with "No Charge"; number field allowing 2 decimals) 
    * Est. Max Price (visible if "Billing Type" = blank or does not start with "No Charge"; number field allowing 2 decimals) 
    * Actual Price (number field allowing 2 decimals)
    * PS Notes (visible if Billing Type = "No Charge - Premium Subscription"; number field allowing 2 decimals)
    * Pricing Notes (button; opens a child screen containing an unlabeled editable memo; text from the memo is displayed as read-only and clipped text to the right of the button)
    * Attention Needed (checkbox; defaults to unchecked)
    * Assignees (button; visible if Attention Needed checkbox is checked; opens a child screen containing the following:
      * Unlabeled RG of:
        * Attention Needed Assignees (drop list of all Incident Assignees)
      * Insert Row (button; inserts a row into the RG)
      * Append Row (button; appends a row into the RG)
      * Delete Row (button; deletes the selected row(s) from the RG)
    * Assignee Entry (multi-select drop list of Incident Assignees; if rows are added to the Assignees RG, those Assignees are displayed here)
  * Client Requirements (memo; warning on Save if blank and "Vendor Approval" = "Approved") 
  * Dev Spec (memo)



  


Development Specification

Change Requests: 

  * Tim Reitz 12/13/2024: [[[IN10311](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10313&)]] - CORE - Change Requests - Improvements for Managing Projects


