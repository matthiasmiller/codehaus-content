7.3. Purchase Order Record

  


Requirements

Overview: This is a custom record that tracks Purchase Orders ("POs") submitted by Buyers who wish to purchase lumber. A Purchase Order is linked to one or more Delivery Ticket records that fulfill the PO.

  


Accessed via: 

  * Purchase Orders report(s)
  * Main Menu | Data Entry | New Purchase Order (opens a new, blank Purchase Order record) 
  * "New Purchase Order" link on the Buyer-type Contact record



  


Sections and Fields: 

  


  * All Section and Field specs are in the subsequent rows below this one (rows 490-530), except for the Bottom Report, which is specced below.



  


  * Bottom Report: This screen includes a special report across the bottom of the screen, displaying the "Delivery Tickets by PO Report", filtered to this Purchase Order. 



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users
  * Editability: For users with the "Edit Purchase Orders" Permission



  


Special Considerations:

  * Copy Record: Disallow (but the copy feature could be considered and added in the future)
  * Delete Record: Allow deletion if "Status"= "Canceled"
  * Merge Record: Disallow



  


Other Notes:

  * N/A



  


Development Specification

Original PC: [[PC0174496]] - ZGW - Add functionality to purchase order record

  


Change Requests: *note changes to specific sections in the Dev Spec for those sections* 

  * Tim Reitz 05/12/2025: [[[IN11254](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11256&)]] - ZGW - Clean up Linking Between Purchase Orders & Delivery Tickets
  * Ben Reitz 10/08/2025: [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature
    * Ben Reitz 10/08/2025: Note that I split the 5 main sections (excluding the bottom report) into new proposal sections, to reduce the size of this section.



  


Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=569310505#gid=569310505](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=569310505#gid=569310505)

  


Ellis Miller 12/16/2024:

[ ] Custom DB Level

[ ] PurchaseOrderStatus macro

[ ] Buyer - Use ActiveContactsByType.ndx (create a wrapper macro called ActiveContactsByType(vType))

[ ] Buyers PO - OnChange and validation

  


[ ] Trigger to close old PO.

Tim Reitz 01/06/2025: This has been deferred as an optional add-on item. 

  


BID: 2.5 Days

  


TODO_PRICING: Tim Reitz 11/08/2024: Include an index of Buyer ListNum +Buyer's PO # text + binary PO date + Internal ID. This is used for the ask prompt drop list on the PO's report, etc. 

  


TODO_PRICING: Tim Reitz 10/23/2024: Not included in official HLD estimate (we were expecting to completely do away with Purchase Orders).
