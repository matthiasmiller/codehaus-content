5.8.2. Triggered Processes

  


Requirements

Triggered Processes: The Solution contains the following automatic processes that are initiated via a trigger in the Solution:

  


1\. "Close Delivery Ticket from Buyer Payment":

  * Overview: Checks the "Buyer Payment Finalized + Delivery Ticket Closed" checkbox field on a Delivery Ticket record. 
  * Initiated:
    * On the first Save after the "Complete" checkbox is checked on a Buyer Payment record. 
  * Prompts:
    * N/A 
  * Action(s): 
    * If the following is true for any linked Delivery Tickets when the above mentioned Save happens: "Total Buyer Pmt. (Pre-Discount) $" for the Ticket is not zero and is equal to "Buyer Invoice $": Checks the "Buyer Payment Finalized + Delivery Ticket Closed" checkbox. 
  * Command(s) for Scheduled Tasks:
    * N/A (not run via Scheduled Task)
  * Database Trigger to be Enabled: 
    * "CloseDeliveryTicket"



  


2.  "Add New GemWood PO to Date-Based Buyer Purchase Orders" 

  * Description: This process automatically adds a new GemWood Purchase Order to a Buyer Purchase Order (by adding a new row to the "GemWood Purchase Orders" embedded spreadsheet). 
  * Action(s): 
    * Adds a new row to the "GemWood Purchase Orders" embedded spreadsheet, with fields according to the defaults specced in the spec for that embedded spreadsheet.  
  * Trigger Name (to be enabled at deployment): AddNewGWPOToBuyerPO
  * Report Path: Std Trigger Add New GemWood PO to Date-Based Buyer Purchase Order.r20
  * Initiated:
    * When the "Send Email" link is clicked for a row on the "GemWood Purchase Order" embedded spreadsheet on a Purchase Order record and the following conditions are met: 
      * "Close Type" for the Purchase Order = "Date Based" and 
      * there are no rows on the "GemWood Purchase Order" embedded spreadsheet with "Sent to Member" = blank (other than the row for which the email is being sent).
  * Priority: N/A 
  * Run as User: "Administrator" 
  * Import Path: Std Add New GemWood PO to Date-Based Buyer Purchase Order.x30



  


Development Specification

Change Requests: 

  * Tim Reitz 02/28/2025: [[[IN11186](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11188&)]] - ZGW - Delivery Ticket - Clarifications for Auto-Closing Delivery Tickets
  * Ben Reitz 10/08/2025: [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature


