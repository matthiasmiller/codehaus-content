7.3.4. Closing Details Section

  


Requirements

  * Closing Details section (left-hand side; located beneath the "Itemization" section): 
    * Close Type (required; with the following details / behaviors: 
      * drop list of "Date-Based" / "Load-Based"; 
      * defaults to "Load-Based"; 
      * when selecting "Date-Based", if there is a single date-based PO, "This PO Replaces" will be set to that PO; 
      * warning on the field if changed: "Changing the Close Type affects the related fields below.";
      * on the first Save after this is set to "Date-Based", a row is added to the "GemWood Purchase Orders" embedded spreadsheet) 
    * This PO Replaces (visible and defaulted if "Close Type" = "Date-Based"; with the following behaviors:
      * drop list of Buyer's PO #'s for all Open Date-Based Purchase Order records for the Buyer with "Replaced By" = blank (i.e. all that have not already been replaced by another PO); 
        * if there are none or multiple, defaults to blank; 
        * if there is only one, defaults to that one; 
      * warning on Save if visible and blank and there is one or more Open Date-Based Purchase Order records for the Buyer: ""This PO Replaces" is blank. Please confirm if this is correct."; 
      * becomes read-only if "Replaced By" for this Purchase Order is not blank, to prevent a replaced PO from being used to replace other PO's) 
    * Old PO Status (visible if a PO is selected in "This PO Replaces"; read-only macro; dynamically displays the current Status of the selected PO, in gray text) 
    * View/Edit (link; visible if a PO is selected in "This PO Replaces"; opens the selected Purchase Order record is selected) 
    * Target # Loads (visible and required if "Close Type" = "Load-Based"; with the following details / behaviors: 
      * number; 0 decimals;
      * defaults to blank;
      * when set, the following field(s) are affected:
        * "GemWood Purchase Orders" embedded spreadsheet: rows are added to match the number entered here, not counting canceled rows; 
      * error on the field if set to a number than is less than the current number of uncanceled rows in the "GemWood Purchase Orders" embedded spreadsheet: "This cannot be set to <#> because it is less than the number of GW POs". Cancel a GW PO if needed."; 
      * once the PO reaches the set number of linked Delivery Ticket records, a warning displays on linked Delivery Tickets - see corresponding spec; 
      * note that a future enhancement could be an alert when the set number of loads is approaching and/or passed)
    * Remaining Loads (visible if "Close Type" = "Load-Based"; read-only macro; displays the value of <"Target # Loads"> \- <the number of linked non-Canceled Delivery Tickets>)
    * Closed (editable if the "Canceled" checkbox is not checked; checkbox + date, which toggle; date defaults to the current date when the checkbox is checked; note that the Purchase Order can be marked as "Closed" even if there are open Delivery Tickets linked to it) 
    * Replaced By (visible if the current PO is selected in the "This PO Replaces" field on another Purchase Order record; read-only macro; displays the PO # for the corresponding Purchase Order; link to open the corresponding record)
    * Canceled (with the following details / behaviors: 
      * editable if the "Closed" checkbox is not checked; 
      * checkbox + date, which toggle; 
      * date defaults to the current date when the checkbox is checked; 
      * validation error on the field if there are any non-Canceled Delivery Tickets linked to the Purchase Order: "PO cannot be canceled because there is at least one non-Canceled Delivery Ticket linked to it." (note that an error is used instead of making this read-only so that the user can have an explanation for why it cannot be canceled in this situation))



  


Development Specification

Change Requests:

  * [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature


