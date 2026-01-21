7.4.4. Delivery Ticket - Buyer Financials Section

  


Requirements

  * Buyer Financials section: 
    * Buyer Paying Freight $ (visible if the "Buyer Paying Freight $" field on the selected Purchase Order "Buyer's PO #" is not zero; read-only macro; number; 2 decimals; with the following behaviors: 
      * displays the value of the "Buyer Paying Freight $" on the selected Purchase Order record; 
      * warning on Save if this ≠ 0 and "Status" ≠ "Closed" or "Canceled" and the "Other Line Items" embedded spreadsheet does not contain a row with "Type" = "Freight": "Make sure "Other Line Items" includes a row for Freight if needed."; 
      * with the main spec for Phase 1, users would always manually add a row to the "Other Line Items" table, but an optional add-on is a feature to automatically add a row when needed - see corresponding spec) 



  


  * No Buyer Invoice (checkbox; defaults to not checked; with the following behaviors:
    * when a Buyer is selected, this updates based on the "No Buyer Invoices" checkbox on the Contact record for the selected Buyer;
    * if the "No Member Grade" checkbox is checked for the Delivery Ticket, this automatically becomes checked and read-only; if "No Member Grade" is later manually unchecked, this becomes editable but remains checked, and can be manually unchecked;
    * if this is checked, various items below are hidden, and the "Invoices Awaiting Approval" notification is not sent - see corresponding specs)



  


  * Buyer Invoice # (read-only macro; displays "<Ticket #>") 
  * Buyer Invoice $ (read-only macro; number; 2 decimals; displays the value of "Total Member Grade $" \+ "Total Other Line Items $"; note that this value is not frozen, but cannot change after "Delivery Ticket Status" = "Closed" or "Canceled", at which point the "+"/"-" buttons are hidden for the corresponding embedded spreadsheets on the Ticket, and the rows become non-editable) 
  * Print Buyer Invoice (visible after the initial save for the record if; link; prompts the user to save the current record, then generates the "Buyer Invoice" printout and opens it in the browser) 



  


  * Send Salesperson Invoice Review Email (visible after the initial save for the record if "No Buyer Invoice" is not checked; link; with the following behaviors:
    * prompts the user to save the current record;
    * sends the email without a preview;
    * if the "Approval Denied checkbox is not checked, sets the "Sent for Approval" field to the current date and time;
    * If the "Approval Denied" checkbox is checked, sets Resent for Approval" field to the current date and time;
    * note that the user must refresh the screen to view the changes) 
  * Sent for Approval (auto-set and read-only; this is the most recent date and time that the "Salesperson Invoice Review Email" was sent while the "Approval Denied" checkbox was not checked) 
  * Resent for Approval (auto-set and read-only; visible if not blank or if the "Approval Denied" checkbox is checked; this is the most recent date and time that the "Salesperson Invoice Review Email" was sent while the "Approval Denied" checkbox was checked; in cases that an invoice is denied multiple times, this field is cleared when the "Approval Denied Comments" field is edited via import)
  * Add'l Notes for Review Email (visible if "No Buyer Invoice" is not checked; button; opens a child screen with an editable memo that can be edited by the user to add custom text to bottom of the standard email body on a per-Ticket basis) 
  * Approve Invoice (visible if the viewing User has the "Edit Delivery Tickets via Import" Permission and if "Status" = "Awaiting Salesperson Approval" or "Status" = "Salesperson Approval Denied"; located above the "Invoice Approved" checkbox; with the following details: 
    * button; 
    * displays as "Approve Invoice"; 
    * opens the "Approve / Deny Invoice Prompt Screen" as a lightbox for the Delivery Ticket, with the following fields set:
      * "Approved?" set to "Yes"; 
      * "Ticket #" set to the corresponding Delivery Ticket;
    * note that the user needs to refresh the screen to see the applied changes) 
  * Deny Invoice (visible if the viewing User has the "Edit Delivery Tickets via Import" Permission and if "Status" = "Awaiting Salesperson Approval"; located above the "Invoice Denied" checkbox; with the following details: 
    * button; 
    * displays as "Deny Invoice"; 
    * opens the "Approve / Deny Invoice Prompt Screen" as a lightbox for the Delivery Ticket, with the following fields set:
      * "Approved?" set to "No"; 
      * "Ticket #" set to the corresponding Delivery Ticket;
    * note that the user needs to refresh the screen to see the applied changes)  



  


  * Invoice Approved (checkbox; with the following behaviors: 
    * visible after the initial save for the record if "No Buyer Invoice" is not checked;
    * defaults to not checked; 
    * if checked, the "Buyer Invoice Email" can be sent) 
  * Approval Denied (checkbox; with the following behaviors: 
    * visible after the initial save for the record if "No Buyer Invoice" is not checked;
    * defaults to not checked; 
    * automatically becomes not checked and read-only if the "Invoice Approved" checkbox is checked)
  * Approval History (link; with the following behaviors;
    * visible if "No Buyer Invoice" is not checked;
    * opens the Modification History for the "Invoice Approved", "Approval Denied", and "Approval Denied Comments" fields) 
  * Approval Denied Comments (editable multi-line plain text field; with the following behaviors: 
    * visible if the "Approval Denied" checkbox is checked;
    * defaults to blank, or set to the comments entered via the "Approve / Deny Invoice" automatic process;
    * when edited via import, clears the "Resent for Approval" field (this is to handle cases where a salesperson denies the invoice multiple times)) 



  


  * Send Buyer Invoice Email (link; with the following behaviors:
    * visible if the selected Buyer Contact has at least one email address and if "Invoice Approved" is checked and if "No Buyer Invoice" is not checked;
    * prompts the user to save the current record, then sends the email without a preview and sets the "Sent to Buyer" field to the current date and time; note that the user must refresh the screen to view the changes; 
    * with the main spec for Phase 1, users would always manually send this email by clicking this link, but an optional add-on is a feature to automatically send the email by clicking a checkbox; this optional feature also includes the ability to track the last Sent date - see corresponding spec)  
  * Sent to Buyer (auto-set and read-only; this is the most recent date and time that the "Buyer Invoice Email" was sent)
  * "No email address for Buyer - invoice must be sent manually." (on-screen message in black text; visible in the location of the "Send Buyer Invoice Email" link if the selected Buyer does not have any email addresses entered on their Contact record and if "No Buyer Invoice" is not checked) 
  * Add'l Notes for Buyer Invoice Email (button; with the following behaviors:
    * visible if the selected Buyer Contact has at least one email address if "No Buyer Invoice" is not checked;
    * opens a child screen with an editable memo that can be edited by the user to add custom text to the bottom of the standard email body on a per-Ticket basis) 



  


  * Buyer Payment Terms (editable and required if there are no linked "Complete" Buyer Payment records for the Delivery Ticket; drop list of "Buyer" Payment Terms items; with the following special behaviors; 
    * defaults to the "Default Buyer Payment Terms" from the selected Buyer's Contact record as of the time that the Buyer is selected on the Delivery Ticket; 
    * the selection here automatically affects the Solution's handling of logic and calculations for due dates, early pay discounts, etc.; 
    * if changed, the following field(s) are affected: 
      * "Buyer Due Date": is updated accordingly, based on the "Ticket Date" and the Due Date settings on the selected Buyer Payment Terms item (i.e. "Payment Due In", "Day Type", and "Date Baseline");
    * note that changes to this spec should be considered for the Member Payment Terms drop list as well)
  * Buyer Due Date (date; optional; with the following details / behaviors: 
    * initially defaults when "Buyer Payment Terms" is set - see corresponding spec; 
    * auto-updated when one of the following changes if "Buyer Payment Terms" is not blank: 
      * "Ticket Date", 
      * "Buyer", or 
      * "Buyer Payment Terms") 



  


  * Est. Buyer Early Pay Due Date (visible if the selected Buyer Payment Terms item has the "Uses Optional Early Payment" checkbox checked; read-only macro; date; displays the estimated due date, based on the "Ticket Date" plus the "Early Pay Window [   ] Days" for the selected "Buyer Payment Terms" item)
  * Est. Buyer Early Pay Discount % (visible if the selected Buyer Payment Terms item has the "Uses Optional Early Payment" checkbox checked; number; 2 decimals; with the following special behaviors: 
    * defaults to the "Early Pay Discount %" on the selected Buyer Payment Terms record as of the time that the Terms was selected on the Delivery Ticket;
    * editable and required for users with the "Manage Financials" Permission; read-only for all other users; 
    * does not automatically update if the default is changed on the Buyer Payment Terms record; 
    * does update if "Buyer Payment Terms" is changed; 
    * displays in gray text with "(Estimate)" suffix; 
    * note that this (and the $ value below) are simply estimates and reference points, and do not affect the actual discount amount, if any, taken by the Buyer; 
    * note that changes to this spec should be considered for the Member side as well) 
  * Est. Buyer Early Pay Discount $ (visible if the selected Buyer Payment Terms item has the "Uses Optional Early Payment" checkbox checked; read-only macro; number; 2 decimals; with the following behaviors: 
    * dynamically displays the rounded value of "Est. Buyer Early Pay Discount %" * "Buyer Invoice $"; 
    * displays in gray text with "(Estimate)" suffix) 



  


Other Notes:

  * Regarding Buyer Early Pay Discount details: GemWood does not include any early pay discount details on the Buyer Invoice. If a Buyer wishes to pay early and take an early pay discount, they do it on their own initiative and do the calculations themselves. As a result, the Estimated Buyer Early Pay Discount items in the Solution are displayed for reference purposes only. They are not included on the Buyer Invoice or in payment calculations. However, if a Buyer takes a discount it is recorded on the Buyer Payment record, and reflected on the Delivery Ticket record, and if it is past the "Est. Buyer Early Pay Due Date" or greater than the "Est. Buyer Early Pay Discount %", the Solution displays a warning for the user to double check and confirm it (see the Buyer Payment record spec).



  


Development Specification

BID: 12 HOURS
