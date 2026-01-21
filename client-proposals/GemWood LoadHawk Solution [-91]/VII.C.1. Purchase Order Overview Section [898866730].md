7.3.1. Purchase Order Overview Section

  


Requirements

  * Purchase Order Overview section (left-hand side): 
    * Status (located in the header bar for this section; no label; read-only macro; displays the status (items correspond to the "Open / Closed / Canceled" simple list):
      * "Open": if the Closed checkbox is not checked;
      * "Closed": if the Closed checkbox is checked;
      * "Canceled": if the Canceled checkbox is checked)
    * Internal ID (hidden; auto-set and read-only; unique identifier for the record)
    * Salesperson (with the following behaviors and details: 
      * required for all Purchase Orders records created after the date specified in the "Ticket GemWood PO required date" System Switch;
      * editable if "Status" = "Open"; 
      * drop list of all Internal-type Contacts; 
      * defaults to the "Default Salesperson" from Silverloom Settings at the time that the record is created; 
      * warning on the field if changed from non-blank and there are one or more linked Delivery Ticket records: "Changing the Salesperson will also change the Salesperson on the linked Delivery Tickets.") 
    * Buyer (required; drop list of active Buyer-type Contacts; with the following details / behaviors: 
      * defaults to blank; 
      * editable if there are no Delivery Tickets linked to the Purchase Order (read-only if there is at least one Delivery Ticket); 
      * when set or changed, the following are also subsequently set/updated: 
        * "Delivery Location" set if only 1 item is included on the list; otherwise cleared when "Buyer" is cleared or changed) 
        * "Special Instructions" set to the "Special Instructions for Purchase Orders" memo on Buyer's contact record. If there is already content in the memo, the new content is appended to the existing content.
    * Buyer's PO # (required; plain text field; with the following details / behaviors: 
      * any letters are automatically converted to upper case; 
      * maximum length of 20 to allow for indexing -- error message on Save: "Buyer's PO # must not exceed 20 characters."; 
      * defaults to blank; 
      * editable if there are no linked Delivery Tickets (read-only if there is at least one Delivery Ticket); 
      * validation against duplicate PO #'s for the same Buyer - error message on the field: "Duplicate PO #'s are not allowed for the same Buyer."; 
      * note that if for some reason a Buyer would have the same PO # more than once, the user would need to enter something to distinguish them; 
      * warning on the field if changed after having been saved: "Buyer's PO # has been changed.")
    * PO Date (required; date; defaults to the current date) 
    * Description (optional; plain text; defaults to blank; may be used to document additional details about the PO) 
    * Delivery Location (optional; editable if PO is not closed or canceled; wide drop list of all Addresses from the Buyer's Contact record; with the following details / behaviors: 
      * items display in the following format: "<Address Type>: <Full Address>, i.e. "Ship To: 1234 Some St, Sometown, VA 11111"; 
      * automatically set when "Buyer" is set if only 1 item is included on the list & automatically cleared if "Buyer" is changed - see corresponding spec)
    * Buyer Paying Freight $ [   ] Per Load (required; number; 2 decimals; with the following details / behaviors: 
      * must equal 0 or a positive number -- error message on Save: "Buyer Paying Freight $ must be 0 or a positive number."; 
      * defaults to 0.00; 
      * used for documenting the amount per load that the Buyer is paying for freight costs)



  


Development Specification

Change Requests: 

  * [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature


