7.3.5. GemWood Purchase Orders Section

  


Requirements

  * GemWood Purchase Orders section (spans both columns; located beneath the "Closing Details" section)
    * GemWood Purchase Orders (no label; embedded spreadsheet with the following:)
      * if "Close Type" = "Load-Based", rows are added based on the value of the "Target # Loads" field - see corresponding spec;
      * if "Close Type" = "Date-Based", the first row is added on the first Save after "Close Type" is set, and a new row is automatically added each time a row is marked as "Sent" and the Buyer Purchase Order "Status" = "Open")
      * Columns:
        * Status (auto-set and read-only; with the following behaviors:
          * displays "GemWood Purchase Order Statuses" list items, with the following logic:
            * "Unassigned" if "Member" for the row is blank;
            * "Ready to Send" if "Member" for the row is not blank and if "Sent to Member" for the row is blank;
            * "Awaiting Delivery Ticket" if "Member" and "Sent to Member" for the row are not blank and if "Delivery Ticket" for the row is blank;
            * "Closed" if "Member", "Sent to Member", and "Delivery Ticket" for the row are not blank
            * "Canceled" if the "Canceled" checkbox for the row is checked) 
        * Canceled (checkbox; editable if checked or if "Delivery Ticket" for the row is blank or if "Delivery Ticket" is set to an item with "Delivery Ticket Status" = "Canceled")
        * GW PO # (auto-set and read-only; unique identifier for the GemWood Purchase Orders; with the following details:
          * displays in the following format: "<Buyer's Contact ID>-<Sequential GW PO ID>", i.e. "12-000051" or "1-000052";
            * If new rows have been added because Target # of Loads has been set or changed for a "Load-Based" PO, the IDs are displayed in the following format: TEMP-(-1). The number increments negatively for the number of new rows. The temporary ID is replaced on save.
          * the "Sequential GW PO ID" is a number, starting at "50")
        * PO Date (auto-set and read-only; defaults to the "PO Date" for the Buyer Purchase Order when the row is added) 
        * Member (optional; drop list of all active Member-type Contacts; filters down as you type; with the following details / behaviors:
          * defaults to blank;
          * editable if "Delivery Ticket" is blank (i.e. becomes read-only once a Delivery Ticket is linked with the GemWood PO); 
          * warning on the field if changed from non-blank: "Changing the Member will require a new email to be sent.";
          * if a GemWood PO needs to be reassigned after it has been linked to a Delivery Ticket, the Delivery Ticket needs to be unlinked;
          * if set or cleared, "Sent to Member" for the row is cleared) 
        * Email PO (link; visible if "Member" for the row is not blank; displays as "Link"; with the following details / behaviors:
          * when clicked, prompts the user to save, then the following happen:
            * the "GemWood Purchase Order" email (see corresponding spec) is sent for the row without a preview;
            * "Sent to Member" for the row is set the the current date and time;
            * the "Add New GemWood PO to Date-Based Buyer Purchase Orders" automatic process is run to add a new GemWood Purchase Order row - see corresponding spec;
            * note that the user must refresh the page to see the applied changes and to continue editing)  
        * Sent to Member (auto-set and read-only; displays the last date and time that the "Email PO" link for that row was clicked)
        * View PDF (link; when clicked, prompts the user to save, then opens the "GemWood Purchase Order" printout for that row)
        * Delivery Ticket (read-only macro; displays the "Ticket #" from the linked Delivery Ticket)
      * Automatically sorted by: N/A (no sorting, rows remain in the sequence they were entered, unless manually moved up or down)
      * Buttons to add/remove rows: N/A (rows are always added automatically, and are marked as "Canceled" rather than deleted)
      * Buttons to move rows up and down (up/down arrows)
      * Show 8 rows without scrolling
    * "GW PO #'s are assigned on save." (label in italics, visible if temporary IDs are displayed in the row)



  


Development Specification

Change Requests:

  * Added in [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature
  * Ben Reitz 01/06/2026: [[[IN12262](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12264&)]] - ZGW - GemWood Purchase Orders - Remove 0's in #


