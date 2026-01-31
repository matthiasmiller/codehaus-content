3.2.1. Quickbooks

Invoice information to QuickBooks: 

  * Could we integrate Quickbooks to push all the Customers Statement, Techs Story, Shop supplies used and billable hours for multiple jobs into a single invoice for each individual incident? This means we would have multiple lines of billed labor with a description containing the above information for each line. As well as the shop supplies itemized for each job. Our goal is an itemized invoice with all the parts separated out into each job as well as the above information to clarify things for our customers.



  


  * Will AppHosting be the source of truth for contact records? Yes
  * Do we need to sync Quickbooks contacts with AppHosting contacts? Yes
  * What triggers an invoice to be sent to QB?



Can create the invoice as they close the incident.

NOTE: We would have to create a warning about tracking time or adding supplies to an incident that’s been invoiced.

  


Quickbooks Customer:

  * Add a custom field to QB Customer for the AppHosting Contact ID
  * Create a database level in AppHosting to mirror QB contacts – AHZ Customer ID, Quickbooks Name, Contact (list of Contacts)
  * T/B: make sure that Transaction Pro can import and export custom fields



See also [https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages&NumberID=-519&](https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages&NumberID=-519&)

  * T/B: See if we can get Customer record IDs (more than just name)
  * Also for T/B: list out QB fields that need to be synced across and how they map across to AppHosting fields



  


Sync Process:

  * TODO_MM - Depending on whether we can export record IDs – Export contacts from QB and import into AHZ’s QB Contacts, linking based on AH ID. This is required because we need to use the “Name” from Quickbooks to push AH contacts across
  * T/B: Spec out an export of contact information linked to QB
  * Push that into QB
  * Export sales items from QB
  * T/B spec out an import to push into AH
  * Deactivate any items in AH that are not in QB
  * Export of all invoices that need to be pushed across, along with the AH ID and in whatever format that it needs to be in to be pushed across



  


Desktop Integration Definition:

  * This would be editable by Admins only.
  * Should have a name, active checkbox, expression field for Version, an RG with: Type (web service or command line), path or URL, Input Path, Output Path
  * Add report/import to query and update desktop integration versions



  


Desktop Integration Result:

  * This would be created by the sync utility.
  * Definition field
  * Start date and time
  * End date and time
  * Was it successful?
  * Memo with results



  


Sync Utility:

  * It’s installed on one of Good’s Ag’s computers
  * It’s configured via a configuration file that specifies local address, local port, AH URL, AH username and password, optional query interval, HMAC secret
  * Web interface would be a “force sync” and “sync if needed”



  


TODO_CH: Tim Reitz 10/10/2023: From Matthias, via Audra: 

  * need to either figure out how to do billing for parts or get on a call w/ client for billing for parts
  * once we know that, should take a transaction pro template and just do a mockup of an invoice that has all of the hours, shop supplies, service calls - this is something Tim or Ben could do
  * once we have the mockup, the workflow, how and when do they want these things getting pushed to QB
  * and then once we get that figured out, Matthias can come in and figure out the technical side of tying into transaction pro



  


TODO_LG: 

[ ] sample invoice of everything you would like included from the software

[ ] shop supplies list - are you fine with no automatic syncing of shop supplies from QB to AHZ? (basically need to add new items to AHZ whenever you add them in QB) 

  


Ben Reitz 10/19/2023: Notes doc from Thursday 10/19 call: [https://docs.google.com/document/d/1KZDS3poAXHSgurrlyjP7GusqbWyL4LP7Wclo1pp1INo/edit](https://docs.google.com/document/d/1KZDS3poAXHSgurrlyjP7GusqbWyL4LP7Wclo1pp1INo/edit)

  


TODO_CH: 

[ ] Tim Reitz 10/19/2023: Work on items in the doc above

[ ] Tim Reitz 10/19/2023: Communicate with Ellis & client about splitting the QB sync stuff off of the main Phase 3.

  


Matthias Miller 01/04/2024: Notes from Client:

  


Had a meeting with our team here discussing the options we have for dealing with parts and how to sort them to fit in our invoice format. We discussed the options we had came up with on the call and took some time to brainstorm about what would really serve the purpose for us.

We came up with an idea for a third option I would like to present and see how it would look from your perspective.

 

For parts ordered specific to an incident we would like to do that inside each child incident.This would be a field similar to Shop Supplies. We would need an editable list of items to select from. A quantity field, An editable price field (price would be attached to item and would auto fill but be changeable), and a field to select the vendor. Matthias Miller 01/04/2024: T/B can handle this. We should use Inventory Management w/ SKUs.

 

To order parts we would open the incident, select part from the list(create a new item if needed), enter quantity, update price, and select vendor

 

That would put the parts directly in the incident for invoicing sorting.

 

Could we then have App hosting create a PO from all parts entered in incidents since the last PO was created for each vendor whenever we are ready to place the order? (We would need a place to select which vendor or vendors we are ready to create a PO for) Matthias Miller 01/04/2024: We should use the standard PO module, with a custom report to generate POs.

  


We would then send that PO to our vendor as our order. We would also need to receive the vendors bill against the PO in App Hosting since Quick Books knows nothing of the PO. Matthias Miller 01/04/2024: We should then use the standard VI module.

  


This would put all the invoice data in App Hosting. When we are ready to create an invoice we would push the invoice into Quick books. Matthias Miller 01/04/2024: The incident line items would like to a PO - and it would calculate the prices based on the VI invoice + Vendor

  


Another feature to add would be pricing rules per vendor, to set the markup percentage from entered prices Matthias Miller 01/04/2024: Fields on the Vendor contact type for Markup %.

 

We would also need to push the bills into Quick books for accounting at some point.   Matthias Miller 01/04/2024: Exporting Vendor Invoices into a format that can be imported.

 

This is an overview of what we dreamed up! Hopefully it makes at least a bit of sense. Let me know what for questions this generates! Thanks!

  


Ben Reitz 01/04/2024: We will be adding the standard inventory module to ZGA. It includes the following:

  


  * QuickBooks Items
    * Name
    * Item Type; list of:
      * Inventory Part
      * Service
      * Non-inventory Part
      * Other Charge
    * Active



  


  * AppHosting Settings
    * QuickBooks Invoicing section
      * Default Parts Item (list of active QuickBooks items)
      * Default Hours Item (list of active QuickBooks items)
      * Default Shop Supplies Items (list of active QuickBooks items)



  


  * SKUs (record with customizations)
    * QuickBooks Item for Invoicing (list of active QuickBooks Items)



  


  * Incidents (with customizations):
    * RG of a list of SKUs, Quantity, Vendor Price (defaults to SKU price but editable), Vendor (drop list filtered to Vendors for the SKU), Vendor Markup % (defaults to Markup % on Vendor - TBD regarding editability), Retail Price (Vendor Price * (100% + Vendor Markup %)), Purchase Order ID
      * Consider warning when making changes to a row that is linked to a PO
    * Macro for retail price
      * Finds the first vendor invoice for that SKU and PO, get the price, and mark it up by the Vendor percentage



  


Note that this is per incident, regardless of hierarchy

  


  * Purchase Orders (with customizations):
    * Add an Incident ID column to the RG
    * To create POs:
      * Create an import that uses a helper report
      * Helper report should show Vendor, SKU, Quantity, Price, and Incident ID for all rows that are not linked to a PO
      * Follow up with an import to backfill PO IDs on these incident rows



  


  * Vendor Invoices (no customizations)



  


  * QuickBooks Invoice export:
    * All invoices ready to bill, all items based on the quantity received, mapped to the appropriate QuickBooks Item.



_LG: Ben Reitz 01/04/2024: How do we want to handle situations where not all parts were received? 

_MM: Ben Reitz 01/11/2024: If we are exporting an invoice and parts are not received, the parts that are not received do not get exported in the invoice.

_LG: Ben Reitz 01/04/2024: How do you do your sales items? What do you use for parts, hours, services codes, etc.? 

_MM: Ben Reitz 01/11/2024: Parts are sold as Non inventory parts. All parts are currently sold under one item Labeled Parts, Description is edited each time, It would be good I believe to have each part entered as a separate item.    Hours, and all services (A/C machine hookup, Laptop diagnostic hookup, Etc.) Is sold as individual service items.

TODO_LG: Matthias Miller 01/11/2024:

  * Are you wanting us to push these service items onto the invoice?
  * If so, presumably we'll need another place to enter these?
  * Do service items have any hours associated with them, or are they fixed rate? If the former, how do we split hours from the main hours line item to this one?



TODO_MM: Ben Reitz 01/11/2024: 

  * Yes, We need to push these items onto the invoice.
  * Currently these items are bunched in along with the shop supply items and are being entered there. It should work on our end to let that continue
  * These services are fixed rate


  * Client wants the option to do this individually (per-job) or in batch
  * For each incident (parent and each child): 
    * One line for hours tracked (with the Incident Title + Work Requested + Work Performed as the description) 
    * One line for each Shop Supply row (with the Incident Title as the description) 
    * One line for total number of Service Calls (for Service Truck jobs) 
    * Populate the Amount column on the Invoice for the Qty of Shop Supplies. 



Do not populate the Amount column on the Invoice for the number of hours tracked. 

  * Macro that indicates quantity received
    * Consider how to handle SKUs that share a PO ID (probably require them to be a unique Incident + PO ID combination)
  * Billing Hours
  * Add custom field to QB Invoices for AH ID (Incident ID)



  


  * QuickBooks Bills export:
    * Export of Vendor invoices with validation against double exporting invoices



_LG: Ben Reitz 01/04/2024: Do you want an automated export or are you fine with having something on your end that's slightly manual? I.e., exporting from our system and importing into QB?

TODO_MM: Ben Reitz 01/11/2024: Automation is best! Having a manual process would be okay depending mostly on ease and cost differences

  


  * Contact record:
    * Contacts will start including a Vendor Contact-type


