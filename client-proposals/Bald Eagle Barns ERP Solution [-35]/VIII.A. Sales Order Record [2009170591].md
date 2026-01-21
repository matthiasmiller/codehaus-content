8.1. Sales Order Record

  


Requirements

Sales Order record

  


normally created from a Building record or Work Order record (General SO's would be created separately)

  


also have a menu option for Blank Sales Quote/Order

  


TODO_TR / DONE_JM: which fields should become read-only when status = Sold and beyond? 

Tim Reitz 10/22/2021: probably nearly all locked down - definitely things that affect the items and the price, SP, customer

  


This record will have the following sections, fields, and options:

  


  * Create Work Order (_____



TODO_TR: creating the work order for a new build should assign the serial # on the building

  * Warning on save if the building price has changed since the Quote was created (only for Quotes): The price for the Base Building and/or one or more of the Options has increased and does not match the quote amount."



DONE_CH: Jason wants the price to stay the same for Quotes but increase to match when it's turned into an Order. the salesperson can reconcile it with a line item discount.

TODO_TR: Update the Quote -> Order process to indicate that. The MSRP on the building should just magically work as designed.

DONE_CH: He'd like to keep the original Quote record for reference. Instead, could we automatically add a note to the Notes memo??

TODO_TR: I'd prefer a read-only Quote memo

  


  


Customer Details section:

  * Customer (required; auto-filled if ___; defaults to BEB if SO Type = Trade-In; shows list of RTO copmanies if SO Type = Repo; the contact here becomes the Building Contact on the Building record on Save) 



DONE_CH: For building-related SOs: required/editable OR auto-filled and read-only? again, will a building always track the owner/customer? what about for lot buildings that don't have a customer yet?

TODO_TR: I think this just defaults. The linking is actually the other way -- customer temporarily set on the building until the SO is created. I don't think lot buildings have an SO -- we have a way to generate a WO for them generically.

  * New Customer (visible if Customer is blank; link; opens a blank Contact record of "Customer" type in a new tab; after creating and saving the new Contact, find it in the Customer list)
  * Referring Party (drop list of all contacts; filter down as you type; if the customer already has the "Referring Party" field filled in on a previous Sales Order, have a warning on Save: "This customer has previously been referred."; see corresponding sections of this proposal for more details)
  * Add New (ellipsis link to the right of "Referring Party"; opens a blank Customer-type contact record in a new tab; this new person is added to the Referring Party list when the new contact is saved)
  * Referral Letter Printed (print date; auto-filled and read-only; set from the Customer Referrals Report) 



  


 

Sales Quote / Sales Order Details section: (maybe on the right side?)

  * Status (Quote, Order, Sold-Undelivered, Sold-Delivered, Canceled) 



TODO_TR: 

  * defaults to Quote on creation
  * manually advance it from Quote to Order, BUT do not allow to advance to Order if the building is still in Draft (must click the "Create Work Order" button); (___ 
  * auto-advance from Order to Sold-Delivered when at least the full down payment amount has been applied to it
  * auto-advance from Order or Sold-Undelivered to Sold-Delivered when the building has been Delivered
  * manually advance to Canceled (checkbox) 
    * An Order can be canceled at any point until the building is marked Delivered
    * If an Order with a linked Work Order is canceled, there should be a warning that there is still an open Work Order for the building; the user should have the option to cancel the Work Order as well or to keep it



TODO_TR 

  * Sometimes a customer doesn't pay the full down payment amount, so we should not advance to Sold until the down payment is paid in full. 
  * If the payment type is Purchase Order, the status advances to Sold even if the money hasn't come in
  * Building cannot be built (tasks cannot be started) until the status = Sold. 
  * Don't allow to go back from Order to Quote or Sold to Order/Quote without canceling the Sales Order
  * Don't allow a Sales Order to be canceled if there are uncanceled Payments on the SO



DONE_CH: how should this work? it would be nice to keep the restocking fee connected to the SO

TODO_TR: It has to be a button to prompt what to do wiith the WO. We can prompt for the Restocking Fee. (Add a discount line item for the total, then add the restocking fee as a new line item.) I think the complete status requires a $0.00 balance on the invoice, which means they need to issue a partial refund after cancelling. And this will show up in an AR report with a negative balance.

  * Allow for edits for the rest of the same day after the sales order is advanced to Order OR Sold?? 
  * 

  * Sales Quote ID / Sales Order ID (auto-fill and read-only; see description below)
  * Sales Order Type (required; drop list of the following options 



DONE_CH: which should be conditional on the other - SO Type or Building Category?? 

TODO_TR: I think we should have the Building ID be specified first. This allows us to prefill the other fields. I think we should still store them for simplicity. I think the order that makes sense is Building ID -> Building Category -> SO Type

  * Cash Sale of Building (not available for Existing Customer Building)
  * RTO Sale of Building (not available for Existing Customer Building)
  * Move Job (only available for Existing Customer Building; created from __ TODO_TR)
  * Change Order (not available for a New Building)
  * Service Call (not available for a New Building) 
  * Repo (only available for Existing Customer Building) 
  * Trade-In (only available for Existing Customer Building) 
  * General (used for selling materials, dog houses, etc.; never linked with a Building) 


  * Building Category (visible and required if SO Type = anything except General; drop list of the following options:)



DONE_CH: should this be a drop list or should it be auto-set based on the category of the selected Building? 

And actually - we might not need this if SO Type can determine which Buildings show up on the Building drop list... 

Or maybe - we allow the salesperson to select a building first, and auto-set the SO Type? But what about General sales? Matthias Miller 11/18/2021: This. And have a General Sale checkbox. 

  * New Building (visible if SO Type = Cash Sale or RTO Sale of Building) 
  * Existing Customer Building (visible if SO Type = Move Job, Change Order, Service Call, Repo, or Trade-In) 
  * Existing Lot Building (visible if SO Type = Cash Sale or RTO Sale of Building) 
  * Existing SRB (visible if SO Type = Cash Sale or RTO Sale of Building) 
  * Existing Trade-In (visible if SO Type = Cash Sale or RTO Sale of Building)  


  * Salesperson (required; drop list of names for all Member and Non-member Salespeople; defaults to the user who created the record; editable only by admins) 



  


DONE_CH: Jason wondered if there's a way to split commission for sale of a building between two Member Salespeople... 

TODO_TR: 

  * On the sales order record, have an editable field for salesperson when there's just one. If there are multiple, it should show "(Split)". There should be an ellipsis button beside it that opens an RG of:
    * Salesperson
    * Sale %
  * Validate that the Sale % always adds up to 100.



When we do commission reporting, we need to handle this appropriately.

The salesperson defaults to the user who created the Sales Quote/Order. Only admins can modify this.

  


  * Dealer (auto-filled and read-only; filled with the current Dealer of the Salesperson; does not update if the Salesperson switches to another Dealer in the future) 
  * Approved (checkbox; visible if SO Type = Sale of Building for a New Customer Building or any SO type that makes changes to an existing building (Existing Customer Building, Lot Building, SRB, or Trade-In); default to filled if Salesperson = a Member; default to not filled if Salesperson = a Non-member; can only be filled by an Admin or a Member Salesperson; Tasks for the corresponding Work Order cannot be started until it has been Approved; see corresponding section of this proposal for more details)
  * Approved By (auto-filled and read-only; default to the ___ TODO_TR 
  * Create Work Order (button; visible for if the building is in Draft status; initiates a background process to create the Work Order record and assigns the Serial Number for the building; note that work cannot start on the building until there is a WO associated with it) 



  


Building Details section: (visible for all SO Types except General) 

  * Building (drop list of building serial numbers; auto-filled if SO is created from a Building record; see details:)
    * If Building Category = New Building, list of Draft/Quote buildings for the selected Customer and a "Create New" link to create a new building



TODO_TR: clean this up/update it. only show buildings that haven't been Sold yet. 

  * If Building Category = Existing Customer Building, list of Sold/Built/Completed/__ buildings for the selected Customer
  * If Building Category = Existing Lot Building,
    * For a Non-member Salesperson: All Buildings on the lot(s) of the Salesperson's Dealer that have not been Sold. 
    * For a Member Salesperson: ___ can sell a building that isn't completed yet
  * If Building Category = Existing SRB, list of all __
  * If Building Category = Existing Trade-In, list of all __


  * Serial Number: (read-only; auto-filled from Building Record of the selected Building)
  * SRB (



DONE_CH: we should have a way to show that this building is an SRB. this should appear on the printout - this currently is just a line items in the Options for "Used Building Discount"...

TODO_TR - Show it to the right of the building ID on the detail screen. (Checkbox defaulted to the current value.) They need to tell us how they want it on the SO or we just come up with a reasonable proposal.

  * Building Style: (read-only; auto-filled from Building Record of the selected Building)
  * Size: (<Length>X<Width>; read-only; auto-filled from Building Record of the selected Building)
  * Base Price: (read-only; auto-filled from Building Record of the selected Building)



DONE_CH: will these auto-update if the Building Record is changed? A determining factor is when the building can be edited. And how will they handle generating multiple quotes for the same building. 

  * TODO_TR: No, I think they'll get a message that this is no longer in sync with the building record, and an option to update the quote. (So we need to check more than just pricing. We need to check items, building style, size, etc)


  * Door Faces (list of the following options:)
    * Forward
    * Back
    * Driver
    * Passenger
  * Manufacturing Changes (visible for Sale of Building or Manufacturing Change; embedded spreadsheet to select from Options SKUs



TODO: spec this out

TODO: where to put this, since it's dependent on Type?

  * Additional Materials & Services (embedded spreadsheet of Options and Materials SKUs:) 
    * Description 
    * Qty
    * Note (plain text field)



TODO_TR: use a Custom SKU for general notes, etc. 

TODO_TR: where to put this, since it's dependent on Type?

  * Options 
  * Assembly (all materials for the building and options for this order) 
  * Tasks
    * 


  


RTO section: (visible if SO Type = RTO Sale) 

  * Rental Company (default to Rosewood Rentals) 
  * Due Date (required; this is when the initial monthly payment is due) 
  * Include LDW (required; drop list of Yes, No) 
  * LDW Rate $ (auto-filled and read-only; always show) 
  * Months (required; drop list of 36, 48) 
  * Security Deposit (auto-filled and editable; only admin can set an amount less than the automatic amount) 
  * Down Payment (auto-filled and read-only; sum of Security Deposit and first month's payment) 
  * Contract (link to view/print; opens PDF in new tab) 
  * Customer is Landowner? (required; drop list of Yes, No) 
  * Landowner Name (text field; visible and required if Customer is Landowner = No) 
  * Print Property Owner Release Form (link; visible if Customer is Landowner = No; see corresponding section of this proposal)



  


Delivery Details section: (visible ___ 

  * Schedule Delivery (button; opens a child screen with prompts for ___ TODO_TR
  * View/Edit Delivery Work Order (visible after the WO has been created) 
  * Delivery Date (auto-filled and read-only)
  * Delivery Driver (DONE_JM: do you need this on the SO? 



TODO_TR: not needed

  * Directions & Notes (memo; Salesperson enters )



TODO_TR: these should be pushed to the memo in the Calendar event

copy in lat/long

TODO_TR: on the delivery record, include a link to the SO

  


General Sales section: (visible only if SO Type = General) 

Embedded spreadsheet with the following: TODO_TR 

  * Columns: 
    *   * Sorted by: 
  * Buttons to add and remove rows ("+" and "-") ???
  * Buttons to move rows up and down (up/down arrows) ???
  * Show at least __ rows without scrolling



  


Repo section: (visible only if SO Type = Repo) 

  * 


  


  


Trade-In section: (visible only if SO Type = Trade-In) 

  * 


  


Notes section: (visible for all SO Types) 

  * Notes (Memo)



  


Sale Details section: (visible for all SO Types) 

  * Subtotal ( TODO_TR
    * If SO Type = Cash Sale of Building: auto-filled and read-only; pulled from the MSRP on the Building 
    * If SO Type = RTO Sale of Building: auto-filled and read-only; pulled from the MSRP on the Building 
    * If SO Type = Change Order: __
    * If SO Type = Service Call: __ 
    * If SO Type = Repo or Trade-In: __
    * If SO Type = General: __
  * LDW Amount (if RTO; auto-filled and read-only) 
  * Flat-Rate Discount (optional; number field; deducts a flat rate $ amount from the pre-tax total for the building) 
  * Discount Description (optional; plain text field) 
  * Taxable (checkbox; default to filled) 
  * Sales Tax Code (required if Taxable is filled; drop list of Sales Tax Groups; filters down as you type) 
  * Sales Tax Details (ellipsis button beside the Sales Tax Code field; opens a child screen with an embedded spreadsheet with the following:)
    * Columns:
      * Code (auto-filled and read-only; Sales Tax Items for the selected Sales Tax Group)
      * Rate (auto-filled and read-only; copied from the Sales Tax Item record; does not update if the Item rate changes)
      * Amount (auto-filled and read-only)
  * Tax Amount (auto-filled and read-only; sum of amounts in Sales Tax Details)
    * NOTE: When calculating sales tax for a Sales Tax Group, use each of the individual % rates, then round to 2 decimals, then add them all together. This mirrors how Quickbooks handles this and should eliminate discrepancies. 
  * Total Sale Price (auto-filled and read-only) 
  * Contract Price (visible and auto-filled for RTO sales;



TODO_TR:

  


  * Collect Payment (link; opens a Payment record in a new tab; for a Cash Sale or RTO Sales, cannot collect payment until a Delivery Date/Work Order has been set/created for the building TODO_TR) 
  * Payments & Refunds (auto-filled and read-only



DONE_CH: would this be an RG? or a child screen? or a report?

TODO_TR: My preference is a BottomReport on the detail screen if we don't need it for anything else and it's not too obtrusive. Otherwise, I'm thinking a virtual RG.

  * Payment/Refund (
  * Amount (negative for refunds?
  * Payment Type (
  * link to payment record(s)
  * 

  * Print Sales Quote / Sales Order (button toward/at the bottom of the screen) 
  * Create Work Order (button) 
    * TODO_TR: does this happen automatically? 
    * TODO_TR / DONE_JM: Does the status need to be Sales Order before the work order can be created? Or can we create a work order for a Sales Quote?
      * Tim Reitz 10/22/2021: Wait until the status is Sold for a custom building.
        * TODO_TR: for modifications, they need to be able to do the work before payment, but wiht a commitment from the customer....



  


  


Other Notes:

  * Discounts: 
    * This would be entered manually as desired/needed.
    * They have a Repeat Customer Discount. Jason said that if we have a flat-rate $ amount line item discount, that should be good.
    * Sometimes they knock off something if the customer doesn't want some standard options. 
  * Sales Tax Code: The customer and salesperson, not the software, will determine which Sales Tax Code to use for each order.
  * There will be a limit of one quote per building for Customer Buildings (but not for Lot Buildings). 



DONE_CH: is this still relevant? Jason doesn't want this limitation.

TODO_TR: I can't remember why we imposed this limitation. Make sure you can't turn a quote to an order if the building has been sold, for example.

  * Change Orders: Allow for Sales Orders of the "Change Order" type to be of a negative amount, to handle scenarios where a change order reduces the building price. See also the Order Cancelations and Changes section of this proposal.  
  * 


  


DONE_JM: For warranty work, can they just adjust the amounts to 0.00? 

Tim Reitz 10/22/2021: Most warranty work is from damage on delivery

Tim Reitz 10/22/2021: And yes, would be fine to change amounts to 0.

DONE_CH: can this be done automatically? Jason is fine with manual if needed.

TODO_TR: We could do a SO Type, or have a Warranty checkbox in the RG. Ask Jason whether they mix/match warranty on the same SO.

  


DONE_JM: should there be a separate WO/SO type for warranty work?

TODO_TR: yes.

  


  


TODO_TR: Quotes should be deactivated if not used. Automatically after 60 days. User should be able to search for and view and reactivate quotes that have been deactivated. 

DONE_CH: is this fine?

TODO_TR:

  * Have a setting for Deactivate Quotes After (X)
  * Active Quote checkbox (editable expression) -- sets deactivate on to today if unchecked, to +60 if checked
  * Deactivate Quote On [Date]
  * Reactivate Quote button that sets it to X + 60



  


Development Specification

Mockup: 

  


We'll need to store four internal fields:

  * Sales Quote Year (2-digit year)
  * Sales Quote Number
  * Sales Order Year (2-digit year)
  * Sales Order Number



  


This can be used for two macros:

  * Sales Quote ID
  * Sales Order ID



  


The record name would be based on whether it's a current quote or order. If we have any places where we search by Sales Quote number, it'd be nice if it could pull up the Sales Order number.

  


Taxable: They currently experience an error in the syncing process is a sale is marked not taxable, so they just use a tax rate of 0.00%. Let's make sure the QB sync can handle non-taxable sales.
