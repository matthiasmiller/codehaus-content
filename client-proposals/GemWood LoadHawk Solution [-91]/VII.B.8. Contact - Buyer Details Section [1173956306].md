7.2.8. Contact - Buyer Details Section

  


Requirements

The Contact record also includes the following custom section and fields: 

  


  * Buyer Details section (visible if Contact Type = Buyer):
    * Buyer ID (required; plain text field; used as an informational reference to clarify Purchase Orders)
    * Default Buyer Payment Terms (required; drop list of active Buyer Payment Terms items; used to set the default "Buyer Payment Terms" for Delivery Tickets for this Buyer; defaults to blank; editable for all users) 
    * No Buyer Invoices (checkbox; defaults to not checked; used to default the "No Buyer Invoice" checkbox for Delivery Tickets for this Buyer; editable for all users) 
    * Purchase Orders by Buyer (link; opens the Purchase Orders by Buyer report, filtered to this Buyer) 
    * New Purchase Order (link; opens a new Purchase Order record, with "Buyer" defaulted)
    * Delivery Tickets by Buyer (link; opens the "Delivery Tickets by Member" report, filtered to this Buyer)
    * Buyer Invoices (link; opens the Buyer Invoices report, filtered to this Buyer) 
    * Buyer Payments (link; opens the Buyer Payments by Buyer report, filtered to this Buyer)
    * Special Instructions for Purchase Orders (memo)



  


Development Specification

Change Requests:

  * [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature
  * Ben Reitz 01/06/2026: [[[IN12230](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12232&)]] - ZGW - Contact record - Add "Buyer ID" field



  


  


Ellis Miller 12/16/2024: 

[ ] Add Payment Terms field. Clear on save if type is not Buyer.

[ ] Add links (may need to be separate job waiting until we add the reports).

2 HOURS
