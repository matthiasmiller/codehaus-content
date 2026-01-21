3.9.2. QuickBooks Integration

  


Requirements

The following fields will be pushed from QuickBooks into the line of business software:

  * Item Code
  * Item Description
  * Item Price
  * Item Active



  


This will be done with the assumption that Item Codes never change. For now, this will be set up with TransactionPro using a batch file that:

  * Uses TransactionPro to export those values from QuickBooks
  * Uses curl/wget to import these items into the software



  


Development Specification

[https://www.zed-systems.com/](https://www.zed-systems.com/) OR  [[[W0518](https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages&NumberID=-519&)]] - AppHosting QuickBooks Integrations

  


  


Basic Process:

  * Import from QB into read-only AHZ records, storing the record ID
  * Link AHZ contacts to QB using QB Customer ID
  * Create an export that exports the last known Customer Name from QB, with all the other current information



  


  


OR

  * Import from QB into read-only AHZ records, storing the record ID  **AND** a custom field
  * Store the Record ID of the newly-created customer record on the AHZ Contact record



  


TODO_IDD: Design out the custom QB fields.
