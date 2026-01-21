9.1. Work Order Record

TODO_TR: 

  


Overview: 

  


Accessed via: 

  


  


Sections and Fields: 

  


Work Order section: (for all Work Order types) 

  * Work Order ID (auto-fill and read-only; __



TODO_TR format:  

  * "WO-21-xxxxx
    * WO
    * Current Year (YY format) 
    * Sequential number (based on all work orders) 


  * Status (drop list of the following): 
    * Draft / Active / In Progress / Complete / Canceled)
      * Current:
        * Red - waiting
        * Orange - in progress
        * Green - complete (on the lot ready to sell/delivered)



TODO_TR

  * Work Order Type (drop list of the following:)
    * Manufacturing (used for manufacturing a new building) 
    * Change Order (used for a building that is under construction or a completed building) 



TODO_TR: sometimes these will need to also have a haul request to bring them back to the factory... 

  * Service Call (used for completed buildings) 
  * Repo (
  * Trade-In (



DONE_CH: what should the process be for repos and trade-ins? go back to the original SO and click a button? create a new SO with a Haul Request WO? Or do we even need work orders for these (we could just use a Haul Request to document the move) ?

could these be subtypses of Haul Requests? 

TODO_TR: I think this is a Haul Request. Since we link to an SO, we can determine which subtype from that.

  * Haul Request (used for any time a building is hauled/relocated) 


  * Building (visible and required if not a Misc. Haul Request; list of all buildings; filters down as you type; auto-filled when created from a building)
  * Contact (required; list of all Contacts; filters down as you type; auto-filled when created from a building with a Contact) 
  * Salesperson (auto-filled and read-only; filled from the primary Salesperson for the corresponding Sales Order; blank if there is no corresponding Sales Order) 
  * Dealer (auto-filled and read-only; filled with the current Dealer of the Salesperson; does not update if the Salesperson switches to another Dealer in the future; blank if there is no corresponding Sales Order) 
  * Notes (multi-line text field)
  * Previous Location (auto-filled and read-only; address or coordinates; filled with the most recent Building Location) 
  * Destination (required; address and coordinates:) TODO_TR   
    * For Manufacturing: default to the shop
    * For Change Order: ___ 
    * For Repair/Service Call: default to current Building Location 
    * For Repo: __ 
    * For Haul Request: filled from default to blank 
  * Complete (__ 
  * Completed Date (auto-fill; default to "Today") 
  * Completed By (auto-fill; ____
  * Print Work Order for Shop (link; opens a PDF in a new tab; see corresponding section of this proposal) 
  * Print Work Order for Office (link; opens a PDF in a new tab; see corresponding section of this proposal) 
  * Create Sales Order (link; ___ 



DONE_CH: ???

TODO_TR: I think this is the wrong direction. I'm not sure why we'd ever do this.

  


  


Options section: (for Manufacturing, Change Order, and Service Call types)

TODO_TR:

  * Options on building are source of truth
  * You can't finalize a quote that has different options from the building
  * Change Request SOs put the options on the building and on the Options section on the WO. These options on building/WO are editable by admins on the detail screen.


  * Embedded spreadsheet identical to the one in the Options section on the Building record, except that it defaults to blank (not showing any Standard Options).



  


  


Assembly section: (for Manufacturing, Change Order, Service Call types) 

  * Assembly (read-only embedded spreadsheet of all Materials SKUs for the Options and/or Base Building SKUs included in the Work Order) DONE_CH: how do we link the Options/Base Building SKUs to the WO? 
  * TODO_TR: I think it's just copied over into fields/RG and frozen (editable by admins).
    * Columns: (same as SKUs?) 



  


Tasks section:  (for Manufacturing, Change Order, Repair/Service Call types)

  * Tasks (



DONE_CH: RG or report? 

TODO_TR: Report

  


Special Order Materials section: (for Manufacturing, Change Order, Repair/Service Call types; visible only if the Assembly includes Special Order Materials SKUs)

  * Message in black text: "This Work Order contains one or more Materials SKUs requiring special order. See the Assembly section."
  * All Ordered (checkbox; default to cleared; cannot be cleared if the "Arrived" checkbox is filled)
  * All Arrived (checkbox; default to cleared; cannot be filled if the "Ordered" checkbox is not filled)



  


Special Order-related validation: 

  * Have a warning on Save if the "All Arrived" checkbox is not filled: "This Work Order has one or more Special Order items that have not arrived yet." 
  * Have a warning when work begins (when the first Task is started) on a Work Order that has Special Order item(s) but does not have the "All Arrived" checkbox filled: "This Work Order has one or more Special Order items that have not arrived yet." 



  


Repo Details section: (for Repo type) 

  * New Owner (required; drop list of all RTO Company contacts - if there is only one, auto-fill with that one



DONE_CH: is this auto-fill doable? I want to stick to our plan of being able to handle multiple RTO companies, but also the reality that there normally is only one... 

TODO_TR: This should be on the SO not the WO. Can we have the RTO company be the customer of the SO?

  


Repo notes: 

  * Completing a Repo-type Work Order should change the following on the Building record (in addition to the standard changes made by the Work Order): 
    * Owner from the Customer to the RTO Company
    * Building Status to SRB 



  


  


Haul Request Details section: (for Haul Request type) 

TODO_TR: a building cannot be sold if it has a Haul Request WO associated with it...  (this removes the need for a "In transit" Dealer...

TODO_TR: Maybe have a "Move Building" button on all building records?? 

  * Haul Request Subtype/Category (required; list of the following:) 
    * Inventory Move (used for moving buildings from the factory to lots)
    * Delivery (used for delivering sold buildings to customers)
    * Misc (used for general notes on the calendar, etc.; would not require a )
    * Move Job (used when moving a customer's building at some point after it has been delivered, or for moving buildings for other manufacturers, etc.) 
  * Customer (auto-fill and read-only)
  * Customer Phone Number (auto-fill and read-only)
  * Building Style/Size (auto-fill and read-only)
  * Last 4 of Serial # (auto-fill and read-only)
  * Delivery Date (required; cannot be in the past) 
  * Delivery Notes (multi-line text field) 
  * Delivery Address (link to Google Maps; __
  * Delivery Coordinates (link to Google Maps; __
  * Complete (checkbox; ____
  * Cancel Delivery (checkbox; ____



DONE_CH: how to keep a lot building from being sold while being transported from factory to lot, etc.? 

TODO_TR: Hide the convert to order button when there's an incomplete haul request. Show "In Transit" instead of the button

  


  


Data Access:

  


The Work Order does not need to show the full materials list. It only needs to track the SO materials and alert the purchaser.
