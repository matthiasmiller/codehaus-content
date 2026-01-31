2.4.1. New Triggered Process

  


Requirements

  * Name: "Add New GemWood PO to Date-Based Buyer Purchase Orders" 
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

_CCI: Please document the Trigger Name, Report Path, and Import Path & let us know, so that we can update the spec accordingly. Thanks!

Niccolas Miller 09/22/2025: Updated spec.
