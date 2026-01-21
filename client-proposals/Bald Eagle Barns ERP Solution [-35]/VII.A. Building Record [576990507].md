7.1. Building Record

  


Requirements

Overview: The Building record is the source of truth for buildings in the database, storing current and historical information about the buildings built by BEB/Benchmark Buildings. The building record for a new building is created before a Work Order or Sales Order is created for a building.

  


Accessed via: 

  * New Building menu option on the Main Menu
  * New Building button on the Customer record
  * New Building button on various buildings-related reports
  * Building links in various locations



  


Sections and Fields: 

Customer section: 

  * Building Contact (see details:)  
    * If there is no Sales Order of any status except Canceled for the building (e.g. a Lot Building or when a Customer Building is being designed), this is an editable drop list of all Customer contacts; filters down as you type; auto-filled if the building record is created from a Contact record or from a report where the Contact is specified
    * If there is at least one non-canceled Sales Order record for the building, this is a read-only contact name from the most recent non-canceled Sales Order record for the building (thus is can change if the building is sold/changes hands)
    * If a building is repo'd, the Building Contact should change to the RTO company, via the Repo Sales Order.
    * If a building is traded in, the Building Contact should change to Bald Eagle Barns via the Trade-In Sales Order.
  * New Customer (if Building Contact is blank; link; opens a blank Contact record of "Customer" type in a new tab; after creating and saving the new Contact, find it in the Building Contact list) 
  * View (if there is a Building Contact; link; opens the Contact's record in a new tab)



  


Building Details section: 

  * Active (checkbox; defaults to filled; editable only for admin; clearing it changes the Building Status to "Inactive" and locks all fields; refilling it activates the building again, restores the previous Building Status, and retains all other information)
  * Deactivation Reason (visible and required if the Active checkbox is cleared; text field) 
  * Building ID (hidden; internal system ID; auto-numbered)
  * Serial Number Counter (hidden; auto-number and read-only; all-time building count; note that at deployment this should start on the next sequential number after the last imported building) 
  * Assign Serial Number (hidden and auto-set; when set, the SN is assigned and displayed on the Serial Number field on Save) 
  * Serial Number (auto-generated & read-only; see corresponding section of this proposal)
  * Repo Date (hidden field with the date of the latest Repo work order; used to support data access permissions on a per-dealer basis)
  * Trade-In Date (hidden field with the date of the latest Trade-In work order; used to support data permissions on a per-dealer basis)
  * Building Category (auto-set and read-only; list of the following:)
    * New Customer Building (if the building has a Building Contact when the status is Draft) 
    * Lot Building (if the building does not have a Building Contact set when the status is Draft) 
    * Existing Customer Building (if the building has been Sold but not repo'd or traded in) 
    * SRB (if the building has at least one completed Repo-type Work Order)
    * Trade-In (if the building has at least one completed Trade-In-type Work Order)
  * Building Status (auto-generated and read-only:)
    * Draft (default for new building records; if building has no Serial #) 
    * Sold (if building has a Sales Order with Sold status; can be overridden by the SRB status, and can override the SRB status)
    * Scheduled (if the building has a Serial # but no started Tasks)
    * In Progress (if at least one Task has been started)
    * Built (if all Manufacturing-type Tasks for the building have been completed)
    * Delivered - Cash Sale (if the Delivery WO is complete; based on the SO type)
    * Delivered - RTO Sale (if the Delivery WO is complete; based on the SO type)
    * SRB (if the building the building's most recent Work Order is of Repo type) 
    * Trade-In (if the building's most recent Work Order is of Trade-In type)
    * Inactive (if the Active checkbox is cleared) 
  * Status Date (auto-filled and read-only; date of the Sales Order or Work Order that most recently changed the Building Status)
  * Building Item Code (required; drop list of all Base Building SKUs, e.g. "10X12W"; filters down as you type; selecting this auto-populates the Options list, Assembly list, and Tasks accordingly; becomes read-only as soon as an item is selected - see "Clear Building Details" button for how to edit it)
  * Clear Building Details (button to the right of the Building Item Code field; when clicked, this will show a label on the record that says, "Changing the Building Item will reset all building details and options.", with a "Confirm" button. When the confirmation button is clicked, it will blank out the building item code, making it editable, and blank out all other fields in the Building Details section) 
  * New Building Item (link near the Building Item Code field; opens a new Base Building SKU in a new tab; as mentioned in the Base Buildings SKU section of this proposal, if the user is a non-admin, they could only create a Fully Custom Building; once that new SKU is saved, it will appear on the list on the Building Record)
  * Building Style (read-only; full Style name; auto-filled from the selected Item Code)
  * Size ("WidthXLength"; read-only; auto-filled from the selected Item Code)
  * Square Feet (read-only; auto-filled from the selected Item Code)
  * Siding Color (required; drop list of Building Siding Colors; default to blank; editable in Draft or Scheduled status)
  * Trim Color (required; drop list of Building Trim Colors; default to blank; default to blank; editable in Draft or Scheduled status)
  * Roof Color (required; drop list of Building Roof Colors; default to blank; default to blank; editable in Draft or Scheduled status)
  * Built Date (auto-filled and read-only; the date that the Building reached "Built" status)
  * Current Location (auto-filled and read-only; the location from the most recent Work Order) 
  * Days in Current Location (auto-filled and read-only; number of days since the last Haul Request, Repo, or Trade-In, not including the day the Work Order was completed; if a building arrives on a lot and is sold and delivered all in the same day, it should count as 0 days; use the hidden Repo Date and Trade-In Date if necessary)
  * Create Work Order (button; visible if Building Status = Draft; initiates a background process to create the Work Order record and assigns the Serial # for the building; note that work cannot start on the building until there is a WO associated with it) 



  


Reports and Printouts section: 

  * Print Infosheet (link; opens the infosheet PDF in a new tab; see corresponding section of the proposal)
  * View Building History (link; opens the Building History Report, filtered to the current building, in a new tab; see corresponding section of the proposal)
  * View Assembly (link; opens the Building Assembly report, filtered to the current building, in a new tab; see corresponding section of the proposal)
  * View Tasks (link; opens the Tasks by Building Report, filtered to the current building, in a new tab; see corresponding section of the proposal)
  * View All Sales Orders (link; opens the Sales Orders Report, filtered to the current building, in a new tab; see corresponding section of the proposal) 
  * View All Work Orders (link; opens the Work Orders Report, filtered to the current building, in a new tab; see corresponding section of the proposal) 



  


Options section:

  * Options (embedded spreadsheet with the following:)
    * Columns:
      * Item Description (required; drop list of all Options Descriptions; filters down as you type; read-only for Standard Options; note that not all options are available for all buildings, so the salesperson/approval process should catch things that aren't allowed) 
      * SKU Code (auto-filled and read-only) 
      * Standard? (checkbox; read-only; auto-filled if the option for the corresponding row is a Standard Option) 
      * UOM (unit of measure; auto-filled and read-only)
      * Qty (required; number field with up to 2 decimals; for Standard Options, pulled from Base Building SKU; for non-Standard Options, default to blank)
      * Unit Price (auto-filled and read-only; this is the PWBP from the Option SKU; should always show 0.00 for Standard Options) 
      * Total Price (auto-filled and read-only; Qty * Unit Price; rounds to 2 decimals) 
    * Buttons to add and remove rows ("+" and "-"; the "-" does not apply to Standard Options) 
    * If Qty = 0.00, the row should be in gray text.
    * Buttons to move rows up and down (up/down arrows) 



  


Layout section:

  * Create/Edit Layout (link that opens up Layout Editor with the current building's diagram, in a new tab; see corresponding section of this proposal)
  * Memo (read-only view of the most recently saved version of the layout diagram)
  * Copied Diagram (hidden; used for copied buildings)



  


Notes section: 

  * Notes (memo)



  


Sale Details section:

  * Salesperson (auto-filled and read-only; pulls the Salesperson from the most recent Cash Sale or RTO Sale-type Sales Order for the building)
  * Dealer (auto-filled and read-only; filled with the name of the current Dealer of the Salesperson for the building OR the Dealer that has the building on their lot, as applicable. This gets automatically updated on transfer, sale, repo, and trade-in. If a Salesperson changes Dealers, the Dealer here would not update accordingly. The current/latest dealer would be shown on the detail screen, and a list of historical dealers would be shown behind an ellipsis button. This list of historical dealers is used to control visibility of the building, and is a list of all dealers who have sold this building in the past, as well as the current dealer who has it on their lot.)
  * Dealer ellipsis button (opens a child screen with a 1-column embedded spreadsheet of historical dealers, most recent at the top; see explanation above)
  * Generate Sales Quote (button; hidden if there is a Sales Order record with status of Order or Sold; runs a background process to create a Sales Order record with Quote status, defaulting the information to the current Customer and Building - see corresponding section of this proposal; if an active Quote already exists for this building, that existing Quote's status will be changed to Canceled)
  * Print Sales Quote/Order (link; visible if there is a Sales Order record with status of Quote, Order, or Sold; opens PDF printout of the Sales Order record in new tab) 
  * Open Sales Quote/Order(s) (link; visible if there is a Sales Order record with status of Quote, Order, or Sold; opens the Sales Order record in a new tab; if there are multiple Sales Orders for the building, it opens the Sales Orders report, filtered to the current Building) 
  * Building Price (auto-filled and read-only; number to 2 decimals; see notes below)
    * This is calculated from the current Building Base Price + current prices for additional Options; it does not include Sales Tax.
    * This is auto-updated if prices change until the Building Status = Sold or beyond, after which it it frozen; used for reporting).
    * If the price for the Base Building or any of the Options changes after the Building has a Sales Order with status of Quote, the price should not automatically update on the Quote record (but it still will update automatically on the Building record). In this case, the Quote should have a red message saying, "The quoted price is out of sync with the current building price", and an "Update Price" button. If one or more of these prices change when the Building has a Sales Order of a status other than Quote, the message and button should not appear. 



  


Data Access: See separate section. 

  


Other Notes:

  * Buildings with status of Draft should not show up in the to-do lists, etc.
  * Notes about Options: 
    * Note that Standard Options should be auto-filled from the Base Building. 
    * If a customer wishes to remove one or more Standard Options from the Building the salesperson should adjust the "Qty" column of this list accordingly (changing it to "0" or the desired number). The Standard Options should not be removed completely from this embedded spreadsheet (the "-" button will not work for them), but they would show in gray when the Qty is set to 0. 
    * If a Standard Option is removed from a Building during the sales or design process, associated Tasks should also be removed from the Building/Work Order. For example, if there are 4 windows, each window will have its own tasks, so if you remove 2 windows it would remove the associated tasks. However, removing Standard Options from a Building will not automatically affect the sales price of the building (the salesperson can add a line item discount if needed/desired).



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=458594875](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=458594875)

  


  


Building Contact: 

  * Matthias is thinking of an editable macro using an underlying field that is used when no quotes or invoices exist in the system for the building. This way, customer information can easily track with the bulding until the first quote or invoice is created.
  * Matthias Miller 10/25/2021: Let's have Investortools-owned elements, but wrap it in a macro to make it easy to turn into a configuration setting in the future if we want to.



  


TODO_CCI: We'd like to maintain the ID coming from the old system. How would you like to handle this?

  


Let's index the Building Serial # for faster searching in the thousands of records. 

NOTE: we're using a numbered record ID since the serial # isn't assigned right away and can be changed...

  


We should have 2 fields for the Diagram: The actual diagram for the building and the diagram that was copied from another record (in the event that the building was copied).

  


TODO_CH / TODO_CCI: Tim Reitz 03/08/2022: How should the Building Price be frozen? Here are notes from a while ago:

"We will need to have a button to create the delivery work order (and possibly the manufacturing work order). We can stomp the MSRP on the building record at the same time. (This is necessary because the building may return to a dealer different from the original dealer, so the new dealer will not have access to the original SO to calculate the MSRP.)."

But the "Create Work Order" button would be clicked before the building price should be frozen. So can we have an x30 or something to freeze the price when the SO is advanced to "Sold"?

TODO_CH: Something to consider further: What happens if the SO status is changed/reversed from Sold to something else??

  


  


TODO_JM: At what point should the costs/prices be frozen for a building/WO (so that they don't keep updating indefinitely after the building has been built)? When work starts?

TODO_: Document accordingly in [ ] Buildings, [ ] WO, [ ] Tasks(?)
