7.4.1. Delivery Ticket - Delivery Ticket Overview Section

  


Requirements

  * Top of the screen, above the "Delivery Ticket Overview" section:
    * "This Delivery Ticket is closed. Edits may result in data discrepancies." (on-screen warning message in red font; visible in edit mode if the "Closed" checkbox is checked)
    * "This Delivery Ticket is canceled. Edits may result in data discrepancies." (on-screen warning message in red font; visible in edit mode if the "Canceled" checkbox is checked) 



  


  * Delivery Ticket Overview section:
    * Delivery Ticket Internal ID (hidden; auto-set and read-only; numeric; unique identifier for the record) 
    * Delivery Ticket Status (located in the header bar for this section; no label; read-only macro; displays the status (items correspond to the "Delivery Ticket Statuses" simple list - see corresponding spec): 
      * "Send for Salesperson Approval": if the "No Buyer Invoice" checkbox is not checked and the "Sent for Approval" field is not set and the "Invoice Approved" checkbox is not checked;
      * "Awaiting Salesperson Approval": if one of the following is true:
        * if the "No Buyer Invoice" checkbox is not checked and the "Sent for Approval" field is set and the "Invoice Approved" checkbox is not checked and the "Approval Denied" checkbox is not checked; or
        * if the "Approval Denied" checkbox is checked and the "Resent for Approval" field is set;
      * "Salesperson Approval Denied": if the "Approval Denied" checkbox is checked and the "Resent for Approval" field is not set; 
      * "Send Invoice to Buyer": if the "Invoice Approved" checkbox is checked and the "Sent to Buyer" field is not set and "Total Buyer Payment $" = zero (i.e. no Buyer Payment amount has been applied to the Ticket); 
      * "Awaiting Buyer Payment": if one of the following is true: 
        * if the "Invoice Approved" checkbox is checked and the "Sent to Buyer" field is set and "Total Buyer Payment $" = zero (i.e. no Buyer Payment amount has been applied to the Ticket), or 
        * if the "No Buyer Invoice" checkbox is checked and Total Buyer Payment $" = zero (i.e. no Buyer Payment amount has been applied to the Ticket); 
      * "Awaiting Grade Report / Settlement": if there is some Buyer Payment applied to the Ticket, but either the payment is not enough, or GemWood is waiting for a Buyer Grade Report, or negotiations are in process; i.e., the following is true:
        * "Total Buyer Pmt. (Pre-Discount) $" is not zero but does not equal "Buyer Invoice $", and neither "Closed" nor "Canceled" is checked;  
      * "Closed": if the "Closed" checkbox is checked (which is dependent upon the Buyer Payment being settled - see checkbox spec); note that this happens before Member Payments, Sales Commission, and Internal Fee Payouts are settled; 
      * "Canceled": if the "Canceled" checkbox is checked)



  


  * Ticket # (required; editable alphanumeric field; manually entered based on the corresponding ticket number printed on the paper tickets that Members use to document loads that are shipped, identifying both the Member and a per-Member unique sequential ticket number; serves as the visual identifier for the Delivery Ticket throughout the Solution, and also as the base for Invoice #'s, Payment ID's, etc.; has the following behaviors:
    * must be in the following format: "<Member ID (2-4 letters)><numeric portion (4-5 digits)>", i.e. "DHW0123" \- warning on the field: "Must consist of only the Member ID and 4-5 numeric digits.";
    * for the Member ID prefix portion: 
      * setting or changing the Member ID prefix in this field auto-sets / auto-updates the Member field below - see details (note that this validation only applies when the prefix is edited;
      * when setting/changing this field, validate that the "Member ID" portion is a valid Member ID for an active Member-type Contact - error on the field: "The Member ID portion of this Ticket # is not valid."; 
      * this field does not automatically change if the Member ID is changed on a Member's Contact record; 
    * for the numeric portion: 
      * the numeric portion can be edited without an error even if the Member ID prefix is not a currently-valid ID (i.e. in the case of a Member's ID being changed on their Contact record); 
      * validate that the numeric portion is unique for the Member - error on the field: "The numeric portion of this Ticket # has already been used for this Member."; 
    * when set, the following are also subsequently set:
      * "Member": based on the Member ID portion of the Ticket #;
      * "Member Payment Terms": defaults to the "Default Member Payment Terms" from the selected Member's Contact record;
    * error on the field if the user attempts to change the Member ID portion of the ID where there are any linked Member Payments: "The Member cannot be changed if there are any linked Member Payments.")
  * Print Delivery Ticket Printout (visible after the initial save for the record; link; prompts the user to save the current record, then generates the "Delivery Ticket" printout and opens it in the browser) 



  


  * Member (auto-set and read-only list field; with the following details / behaviors:
    * set to the name of the Member-type Contact, based on the Member ID portion of the "Ticket #" field; 
    * auto-updates if the Member ID portion of the "Ticket #" is changed; 
    * link to the corresponding Member-type Contact record) 
  * Ticket Numeric Value (hidden; auto-set and read-only; displays the numeric portion of the Ticket #) 



  


  * Ticket Date (required; date; with the following behaviors:
    * defaults to the current date; 
    * when set or changed, the following are also subsequently set/updated: 
      * "GemWood Early Pay Due Date": defaults to the calculated date, based on "Ticket Date" plus the "Early Pay Window [ ] Calendar Days from Ticket Date" for the selected Member Payment Terms item;
      * "Buyer Due Date": defaults to the calculated date if "Buyer Payment Terms" is set) 



  


  * Buyer (required; drop list of active Buyer-type Contacts; filters down as you type; with the following additional behaviors: 
    * defaults to blank; 
    * includes an ellipsis button to open the selected record, or create a new one if the drop list is blank; 
    * when set or changed, the following are also subsequently set/updated: 
      * "Buyer's PO #": cleared if both it and "Buyer" are set, then "Buyer" is cleared or changed; 
      * "Buyer Payment Terms": sets to the "Default Buyer Payment Terms" on the selected Buyer's Contact record; 
      * "Buyer Due Date": sets based on the "Buyer Payment Terms";
      * "Delivery Location" cleared if both it and "Buyer" are set, then "Buyer" is cleared or changed; 
    * warning on the field if changed from non-blank: "Buyer has been changed"; 
    * error on Save if the user attempts to change the Buyer when there are any linked Buyer Payments: "The Buyer cannot be changed if there are any linked Buyer Payments.")



  


  


  * GemWood PO # (with the following details / behaviors: 
    * drop list of GemWood PO #'s that meet the following conditions: 
      * GemWood PO "Status" = "Awaiting Delivery Ticket" and 
      * GemWood PO "Member" = "Member" on the current Delivery Ticket; 
    * editable if there are no linked Buyer Payment records (should not be changed if the Buyer has already received payment); 
    * required for all Delivery Ticket records created after the date specified in the "Ticket GemWood PO required date" System Switch (see corresponding spec; note that this is to ensure that a GemWood PO # is not required for Delivery Tickets created before the GemWood PO feature was added); 
    * when set, the following field(s) are affected: 
      * "Buyer": sets to the "Buyer" from the Purchase Order; 
      * "Buyer's PO #": sets to the "Buyer's PO #" from the Purchase Order;
      * "Buyer Payment Terms": sets to the "Default Buyer Payment Terms" on the selected Buyer's Contact record; 
      * "Buyer Due Date": sets based on the "Buyer Payment Terms"; 
      * "Salesperson": sets to the "Salesperson" on the  linked Purchase Order record;
    * warning on the field if changed from non-blank: "GemWood PO # has been changed") 
  * GemWood PO Status (read-only macro; displays the "Status" for the selected GemWood PO; located to the right of "GemWood PO #")



  


  * Buyer (auto-set and read-only; list field of active Buyer-type Contacts; when "GemWood PO #" is set, this auto-sets to the "Buyer" on the linked Purchase Order record; displays as a link to the corresponding record) 
  * Buyer's PO # (auto-calculated and read-only; list macro of Buyer's PO #'s; looks up the Buyer's PO # from the linked Purchase Order record; displays as a link to the corresponding record) 
  * Create New PO (visible if "Buyer's PO # is blank; link; opens a new Purchase Order record with "Buyer" defaulted) 
  * Remaining Loads (visible if "Close Type" for the selected PO = "Load-Based"; read-only macro; number; 0 decimals; with the following behaviors: 
    * dynamically displays the value of the "Remaining Loads" from the selected PO, i.e. the number of linked non-Canceled Delivery Tickets, taking the current Ticket into account)
  * "The selected PO has reached its target number of <#> delivery tickets and needs to be closed. Go to the PO record to close it there." (on-screen message in red text; with the following behaviors: 
    * visible if the following are all true for the selected Purchase Order: 
      * "Purchase Order Status" ≠ "Closed" and 
      * "Close Type" = "Load-Based" and 
      * "Remaining Loads" = 0; 
    * the <#> in the message displays the "Target # Loads")
  * View Purchase Order Attachment(s) (visible if "Buyer's PO #" is not blank; link; with the following behaviors: 
    * if the selected Purchase Order has more than 1 attached file, this opens the "Purchase Order Attachments" report, filtered to the selected Purchase Order -- see corresponding spec; 
    * if just 1 file, this bypasses the report screen to open that file directly; 
    * if no files, this opens the blank report) 
  * Delivery Location (read-only macro; displays the "Delivery Location" from the "Buyer's PO")
  * # of Packs (optional; number; 0 decimals; used to document the number of packs of lumber loaded for the Delivery Ticket; note that this is simply a reference point / cross-check item, and is not connected with any calculations)



  


Development Specification

Change Requests: 

  * Tim Reitz 03/28/2025: [[[IN11254](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11256&)]] - ZGW - Clean up Linking Between Purchase Orders & Delivery Tickets
  * Tim Reitz 10/09/2025: [[[IN11542](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11544&)]] - ZGW - Delivery Ticket record - "GemWood Early Pay Due Date" blanking out
  * Ben Reitz 10/09/2025: [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature
  * 


  


  


Delivery Ticket Status: 

Ellis Miller 12/16/2024: TODO_PRICING:  Review after we've done everything else

  


  


Ellis Miller 12/16/2024:

[ ] BD Main section without Ticket # Entry and warnings/trigger: 6 Hours

[ ] Status Macro: TODO_PRICING

[ ] Member field (Readonly, but for testing could make it editable until US codes the Ticket # entry below)

[ ] Delivery Location TODO_PRICING: Str field with helper list of the ConcatRG. We're literally just storing the displayed text in a string field. I think you can use something like: 

Concat(": ", ContactType, Assign vDisplay = AddressRecordDisplay( AddressRecord, false, false); Replace( vDisplay, NewLine, ", ") 

  


  


[ ] USA: Ticket # entry: 1 Day

[ ] Create macro MemberIDFromTicketNum(vTicketNum) that returns "" if the trimmed vTicketNum has any non-alphanumeric characters,. then call KeepOnlyLetters to get the member ID. Return "" if the letters are not all at the beginning (NOT HasPrefix).

[ ] Create macro NumericValueFromTicketNum(vTicketNum). It calls KeepOnlyNumbers and returns NA if the numbers aren't all at the end (NOT HasSuffix). It should also return NA if there are non alphanumeric characters.

[ ] Use an OnChange to trim. We store the full ticket number as a string and then also update the Member list and hidden TicketNumValue number field.

[ ] Give validation errors if text is entered and these macros don't return valid values.

[ ] If the MemberID changes, we validate that the new memberID is legit and use OnChange to update the Member field. Don't validate or OnChange if only the number changes. It could be that the ID was previously valid.

[ ] On all changes, update the hidden TicketNumValue numeric value.
