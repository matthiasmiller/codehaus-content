4.3.1. Changes to the "Delivery Ticket Overview" Section

  * Delivery Ticket Overview section:
    * ...
    * Member (auto-set and read-only list field; with the following details / behaviors:
      * set to the name of the Member-type Contact, based on the Member ID portion of the "Ticket #" field; 
      * auto-updates if the Member ID portion of the "Ticket #" is changed; 
      * link to the corresponding Member-type Contact record) 
    * Ticket Numeric Value (hidden; auto-set and read-only; displays the numeric portion of the Ticket #) 



  


  * Ticket Date (required; date; with the following behaviors:
    * defaults to the current date; 
    * when set or changed, the following are also subsequently set/updated: 
      * "GemWood Early Pay Due Date": defaults to the calculated date;
      * "Buyer Due Date": defaults to the calculated date if "Buyer Payment Terms" is set) 



  


  * GemWood PO # (with the following details / behaviors: 
    * drop list of GemWood PO #'s that meet the following conditions: 
      * GemWood PO "Status" = "Awaiting Delivery Ticket" and 
      * GemWood PO "Member" = "Member" on the current Delivery Ticket; 
    * editable if there are no linked Buyer Payment records (should not be changed if they Buyer has already received payment); 
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
    * required; drop list of active Buyer-type Contacts; filters down as you type; with the following additional behaviors: 
      * defaults to blank; 
      * includes an ellipsis button to open the selected record, or create a new one if the drop list is blank; 
      * when set or changed, the following are also subsequently set/updated: 
        * "Buyer's PO #": cleared if both it and "Buyer" are set, then "Buyer" is cleared or changed; 
        * "Buyer Payment Terms": sets to the "Default Buyer Payment Terms" on the selected Buyer's Contact record; 
        * "Buyer Due Date": sets based on the "Buyer Payment Terms";
        * "Delivery Location" cleared if both it and "Buyer" are set, then "Buyer" is cleared or changed; 
      * warning on the field if changed from non-blank: "Buyer has been changed"; 
      * error on Save if the user attempts to change the Buyer when there are any linked Buyer Payments: "The Buyer cannot be changed if there are any linked Buyer Payments.")
  * Buyer's PO # (auto-calculated and read-only; list macro of Buyer's PO #'s; looks up the Buyer's PO # from the linked Purchase Order record; displays as a link to the corresponding record)
    * optional; drop list of Buyer's PO #'s for Open Purchase Order records for the selected Buyer; with the following additional behaviors: 
      * defaults to blank; 
      * includes an ellipsis button to open the selected record, or create a new (completely blank) one if the drop list is blank; 
      * warning on save if blank: "Buyer's PO # is blank") 
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
  * Delivery Location (optional; wide drop list of all Addresses from the Buyer's Contact record; in the following format: "<Address Type>: <Full Address>, i.e. "Ship To: 1234 Some St, Sometown, VA 11111"; automatically cleared if "Buyer" is changed - see corresponding spec)
  * # of Packs (optional; number; 0 decimals; used to document the number of packs of lumber loaded for the Delivery Ticket; note that this is simply a reference point / cross-check item, and is not connected with any calculations)


