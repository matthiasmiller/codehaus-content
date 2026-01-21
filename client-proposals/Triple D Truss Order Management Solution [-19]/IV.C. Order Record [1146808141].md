4.3. Order Record

  


Requirements

TODO_AP: Ben Reitz 11/14/2025: Standardize the entire spec for this record as needed. This would include making sure that all fields that are affected by other fields are specced correctly.

  


Overview: The Order record is a custom record, and is used to track all the necessary details for an order that is called in by a customer.

  


Accessed via: 

  * Quotes & Orders reports



  


Special Links / Buttons: This screen contains the following special links / buttons at the top right-hand corner, between the "Document Archive" option and the "advanced" drop-down menu arrow: 

  * Print Quote / Order (opens the Quote / Order Printout as a PDF in a new tab)
  * Print Packing List (drop list; displays the following buttons:
    * Standard Packing List (opens the Standard Packing List Printout as a PDF in a new tab);
    * Yard Packing List (opens the Standard Packing List + Yard Packing List Printout as a PDF in a new tab))



  


Sections and Fields: The sections and fields for this record are specced out in subsections below.

  


Data Access: 

  * Visibility: Visible to all users
  * Editability: Editable for all users



  


Special Considerations:

  * Copy Record: Allowed; no fields are cleared
  * Delete Record: Allowed
  * Merge Record: Allowed



  


Other Notes:

  * Edits made to an Order record are conditionally pushed to the linked Delivery record(s). See the "Create & Link Delivery" Automatic Process.



  


Development Specification

Change Requests:

  * Tim Reitz 07/20/2024: [[[IN9998](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10000&)]] - ZTD - Contact & Quote/Order Records - Add "Customer Notes" Read-Only Memo
  * Ben Reitz 05/08/2025: [[[IN10789](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10791&)]] - ZTD - Allow for linking Orders and Deliveries
  * Ben Reitz 05/08/2025: [[[IN10787](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10789&)]] - ZTD - Add Yard Packing List Printout (prev. Changes to Lumber Order RG)
  * Ben Reitz 05/08/2025: [[[IN10786](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10788&)]] - ZTD - Order Record - Enter deposits on Quotes / Orders
  * Ben Reitz 05/08/2025: [[[IN11262](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11264&)]] - ZTD - Order record - Allow all users to use "New Delivery" link (prev. "Automatic linking to Delivery records")
  * Ben Reitz 05/08/2025: [[[IN11311](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11313&)]] - ZTD - Order record - Add "Create Delivery" checkbox (prev. Add "Order/Schedule" status)
  * Ben Reitz 09/17/2025: [[[IN11482](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11484&)]] - ZTD - Order record - Add "Weight" columns and fields
  * 


  


  


Matthias Miller 04/11/2020:

[ ] Per discussion with Josh, we'll see if we can use the conditional scheduled tasks to run the inventory tracking.

  


[ ] Send Josh info about inventory tracking when we're done w/ it

  


  


Matthias Miller 04/23/2020: Notes:

  * Text as a fraction is "4 1/2". Matthias Miller 04/23/2020: What kind of formatting would you like?



  


TECHNICAL DETAILS: John would like to have something like QuickBooks, where you can start typing and it autocompletes.

  


We need a smart list in RGs.

  


Also, we should store an underlying SalesItem field.
