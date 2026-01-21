3.6.1. Triggered Processes

  


Requirements

Triggered Processes: The Solution contains the following automatic processes that are initiated via a trigger in the Solution:

  


  * Dismiss Vehicle Rows From Deleted Invoice Rows:
    * Description: This process sets the "Billing Action" on the Fees & Credits table (on the Vehicle record) to "Dismiss" for deleted Invoice line items.
    * Action(s): 
      * Takes an input file with all of the line items that were deleted from the Invoice (specifically needs the "VehicleFeesRowID")  
      * Sets the "Billing Action" field to "Dismiss" for the corresponding row on the Fees & Credits table (on the Vehicle record).
    * Trigger Name (to be enabled at deployment): DismissVehicleRowsFromDeletedInvoiceRows
    * Report Path: Std Trigger Sales Form Deleted Items.r20
    * Initiated:
      * On the first Save after a line item on an Invoice is deleted.
    * Priority: N/A 
    * Run as User: "Administrator" 
    * Import Path: Std Update Vehicle Fees Rows Dismissed.x30



  


Development Specification

Change Requests: 

  * Tim Reitz 08/26/2025: [[[IN10760](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10762&)]] - ZWA - Pre-ZWW - Processes - Add "Line Item Dismissal" Trigger / Process


