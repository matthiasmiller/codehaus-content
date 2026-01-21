7.4.9. Delivery Ticket - GemWood Financials Section

  


Requirements

  * GemWood Financials section (visibility for most of these fields is limited based on Permissions, per specs below; editability for all fields in this section is only for users with the "Manage Financials" Permission):
    * Salesperson (read-only macro; with the following details / behaviors: 
      * displays the following: 
        * if "Legacy Stored Salesperson" is blank: displays the "Salesperson" on the linked Purchase Order record; 
        * otherwise: displays the contents of "Legacy Stored Salesperson" (this ensures that the Salesperson is displayed correctly for Delivery Tickets created prior to the "Salesperson" field being added to the Purchase Order record; 
        * displays as a link to the corresponding Salesperson's Contact record) 
    * Legacy Stored Salesperson (hidden; list field of all Internal-type Contacts; this retains the selected Salesperson for Delivery Tickets created prior to the "Salesperson" field being added to the Purchase Order record) 
    * Sales Commission % (read-only stored field; number; 2 decimals; with the following behaviors:
      * visible to users with the "View Sales Commission Details" Permission;
      * dynamically displays the "Sales Commission %" from the selected Member's Contact record as of the time that the Member was selected on the Delivery Ticket and does not automatically change if the setting is updated)
    * Sales Commission $ (read-only macro; number; 2 decimals; with the following behaviors:
      * visible to users with the "View Sales Commission Details" Permission;
      * dynamically displays the rounded value of <decimal value of "Sales Commission %"> * <"Total Buyer Payment $">;
      * auto-updates based on changes to the fields from which it is calculated; displays in gray text with "(Pending)" suffix until Delivery Ticket Status = "Closed", at which point it displays in standard black text)
    * Commission Paid (editable only via Editable reports; checkbox + date, which toggle; with the following behaviors: 
      * visible to users with the "View Sales Commission Details" Permission;
      * checkbox defaults to not checked; 
      * date is set by the "Pay Selected Unpaid" feature on the Sales Commission report) 
    * Commission Status (read-only macro; visible to users with the "View Sales Commission Details" Permission; dynamically displays the corresponding item from the "Pending / Unpaid / Paid" list:
      * "Pending": if "Delivery Ticket Status" ≠ "Closed";
      * "Unpaid": if "Delivery Ticket Status" = "Closed" and the "Commission Paid" checkbox is not checked;
      * "Paid": if "Delivery Ticket Status" = "Closed" and the "Commission Paid" checkbox is checked)



  


  * Total Internal Fee Payouts $ (read-only macro; number; 2 decimals; with the following behaviors: 
    * visible to users with the "Manage Financials" Permission; 
    * displays the value of the sum of all "Payout $" values from the "Internal Fee Payouts Breakdown" embedded spreadsheet; 
    * displays in gray text with "(Pending)" suffix until "Delivery Ticket Status" = "Closed", at which point it displays in standard black text)
  * Internal Fee Payouts Breakdown (embedded spreadsheet with the following; visible to users with the "Manage Financials" Permission: 
    * Columns: 
      * Payee (required; drop list of Contacts included in the "Internal Fee Payouts Configuration" embedded spreadsheet in Silverloom Settings; with the following behaviors: 
        * validate against duplicates for the same Delivery Ticket - error message on the field: "Duplicate Payees are not allowed."; 
        * for manually-added rows, this defaults to blank; 
        * when the Delivery Ticket record is created, a row is automatically added for each active "Payee" on the "Internal Fee Payouts Configuration" table in Silverloom Settings) 
      * Division (auto-set and read-only; displays the "GemWood Division" from the selected Payee's Contact record as of the time that the Delivery Ticket record was created)
      * Payout % (editable and required if "Paid" checkbox for the row is not checked; number; 2 decimals; with the following details / behaviors:
        * defaults to the corresponding "Fee Payout %" value from Silverloom Settings as of the time that the Delivery Ticket record was created; 
        * note that a user can adjust this value if needed, to adjust the Payout $ for a Payee, and/or to adjust the "Total Internal Fee Payouts $") 
      * Payout $ (read-only macro; number; 2 decimals; with the following details / behaviors: 
        * dynamically displays the rounded value of "Payout %" for the row * "GemWood Lumber Brokerage Fee $" for the Delivery Ticket;  
        * displays in gray text with "(Pending)" suffix until Delivery Ticket Status = "Closed", at which point it displays in standard black text)
      * Paid (editable only via Editable reports; checkbox; with the following behaviors:
        * defaults to not checked;
        * toggles with the "Paid Date" for the row) 
      * Paid Date (editable only via Editable reports; date; defaults to blank; with the following behaviors: 
        * toggles with the "Paid" checkbox for the row; 
        * sets according to the date set via the "Pay Selected Unpaid" button on the Internal Fee Payouts report)
      * Status (read-only macro; this is the "Internal Fee Payout Status"; dynamically displays the corresponding item from the "Pending / Unpaid / Paid" list:
        * "Pending": if "Delivery Ticket Status" ≠ "Closed" and the "Paid" checkbox is not checked;
        * "Unpaid": if "Delivery Ticket Status" = "Closed" and the "Paid" checkbox is not checked;
        * "Paid": if the "Paid" checkbox is checked)
    * Automatically sorted by: Payee (alphabetically)
    * Buttons to add/remove rows: "+" / "-" 
    * Show 4 rows without scrolling 
    * Other Notes: 
      * N/A



  


  * GemWood Income $ (read-only macro; number; 2 decimals; with the following behaviors: 
    * displays the value of "GemWood Lumber Brokerage Fee $" \+ "GemWood Discount $"; 
    * displays in gray text with "(Pending)" suffix until Delivery Ticket Status = "Closed", at which point it displays in standard black text; 
    * visible to users with the "Manage Financials" Permission)
  * GemWood Expenses $ (read-only macro; number; 2 decimals; with the following behaviors: 
    * displays the value of "Sales Commission $" \+ "Total Internal Fee Payouts $"; 
    * displays in gray text with "(Pending)" suffix until Delivery Ticket Status = "Closed", at which point it displays in standard black text; 
    * visible to users with the "Manage Financials" Permission)
  * GemWood Gross Profit (read-only macro; number; 2 decimals; with the following behaviors: 
    * displays the value of "GemWood Income $" \- "GemWood Expenses $"; 
    * displays in gray text with "(Pending)" suffix until both the "Commission Paid" and at least one of the "Paid" checkboxes for the "Internal Fee Payouts Breakdown" embedded spreadsheet are checked, at which point it displays in standard black text; 
    * visible to users with the "Manage Financials" Permission)



  


Development Specification

Change Requests: 

  * Tim Reitz 06/27/2025: [[[IN11591](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11593&)]] - ZGW - Round more macros to 2 decimal places
  * [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature


