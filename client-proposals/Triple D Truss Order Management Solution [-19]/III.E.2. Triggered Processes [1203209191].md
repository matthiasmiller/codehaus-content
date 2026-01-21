3.5.2. Triggered Processes

  


Requirements

The Solution contains the following automatic processes that are initiated via a trigger in the Solution:

  


1. Create & Link Delivery:

  * Overview: This process creates and links a Delivery record to an Order record, and updates as appropriate.
  * Prompts: 
    * Quote / Order # (required; numeric; passed in automatically)
  * Initiated:
    * When the "Save" button is clicked on the Order record 
  * Action(s): 
    * If there is no linked Delivery for the Order: creates a Delivery record and sets the "Quote / Order #" field if the "Create Delivery" checkbox is visible and checked;
    * Updates the linked Delivery record(s) to match the fields copied from the Order record "if "Status" = "Quote" or if it is the first Save after "Status" has been set to "Order" (from "Quote" or blank) and the "Scheduled" checkbox is not checked on the Delivery record. 
  * Command(s) for Scheduled Tasks: 
    * N/A (not run via Scheduled Task)
  * Other Notes:
    * This Database Trigger needs to be turned on manually.



  


Development Specification

Change Requests:

  * Ben Reitz 05/08/2025: [[[IN10789](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10791&)]] - ZTD - Allow for linking Orders and Deliveries
  * Ben Reitz 05/08/2025: [[[IN11311](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11313&)]] - ZTD - Order record - Add "Create Delivery" checkbox (prev. Add "Order/Schedule" status)
  * Ben Reitz 05/08/2025: [[[IN11274](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11276&)]] - ZTD - Order / Delivery linking - Change behavior based on "Scheduled" checkbox


