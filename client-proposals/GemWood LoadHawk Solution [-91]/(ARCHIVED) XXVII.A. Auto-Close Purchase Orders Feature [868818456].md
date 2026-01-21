27.1. Auto-Close Purchase Orders Feature

  


Requirements

Tim Reitz 04/29/2025: Moved to [[[IN11417](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11419&)]] - ZGW - Auto-Close Purchase Orders Feature. 

  


The Phase 1 spec originally included automation for closing both Date-Based and Load-Based PO's, but that has been removed in the interest of scope reduction. The design spec has been moved here as an optional add-on that could be implemented in the future if the need would arise. In the meantime, users will manually close out PO's

  


Estimated Cost: $1,500

  


Spec:

  


Automatic Processes | Triggered Processes:

"Close Purchase Order":

  * Overview: Closes a Purchase Order record from a Delivery Ticket or different Purchase Order record. 
  * Prompts: 
    * N/A
  * Initiated:
    * When "Remaining Loads" for a non-Closed, Load-Based Purchase Order = 0 and the user saves a linked Delivery Ticket record. 
    * When a Date-Based Purchase order is selected in the "This PO Replaces" field is on another Date-Based Purchase Order record and the user saves the record. 
  * Action(s): 
    * Takes the PO # / ID from the initiating record and checks the "Closed" checkbox on the corresponding Purchase Order record. 
  * Command(s) for Scheduled Tasks:
    * N/A (not run via Scheduled Task)



  


See additional dev spec. 

  


Purchase Order Record | Closing Details Section: 

  * This PO Replaces (visible and defaulted if "Close Type" = "Date-Based"; with the following behaviors:
    * drop list of Buyer's PO #'s for all Open Date-Based Purchase Order records for the Buyer;
      * if there are none or multiple, defaults to blank;
      * if there is only one, defaults to that one;
    * on the first save after a PO has been selected here, the "Close Purchase Order" automatic process runs to close the selected PO - see corresponding spec (note that closing can happen silently in the background with no notification needed);
    * warning on Save if visible and blank and there is one or more Open Date-Based Purchase Order records for the Buyer: ""This PO Replaces" is blank. Please confirm if this is correct.") 



  


Delivery Ticket Record | Delivery Ticket Overview Section:

Proposal spec: 

  * Remaining Loads (visible if "Close Type" for the selected PO = "Load-Based"; auto-set and read-only; number; 0 decimals; with the following behaviors: 
    * dynamically displays the value of the "Remaining Loads" from the selected PO, i.e. the number of linked non-Canceled Delivery Tickets, taking the current Ticket into account; 
    * if = 0 and the selected PO's Status ≠ "Closed", on the subsequent Save the "Close Purchase Order" automatic process runs to close the selected PO - see corresponding spec (note that closing can happen silently in the background with no notification needed))
  * "The selected PO has reached its target number of <#> delivery tickets and will be closed when this ticket is saved." (on-screen message in red text; 
    * visible if the following are all true for the selected Purchase Order: 
      * "Purchase Order Status" ≠ "Closed" and 
      * "Close Type" = "Load-Based" and 
      * "Remaining Loads" = 0; 
    * the <#> in the message displays the "Target # Loads")



  


See additional dev spec.

  


Development Specification

Automatic Processes | Triggered Processes: "Close Purchase Order" automatic process>

Ellis Miller 12/13/2024: CODED BY USA:

  


Close Purchase Order

[ ] Probably use a field TmpCloseOldPO for each record. 

[ ] Add a database trigger to run on these.

BID: 4 HOURS

  


Delivery Ticket Record | Delivery Ticket Overview Section:

[ ] USA: Red warnings and "Close the PO on Save" \-- use macros to make this clean. 6 hours

[ ] For "The selected PO has reached its target number of <#> delivery tickets..." message: count this record in the counts if it is unsaved. 

[ ] "Close the PO" checkbox: Temporary field with an x30 that runs on Save to modify the selected Purchase Order record.

[ ] Use a trigger report to close it out.
