22.3.4. Classic Accounting Sales Item Record (Read-Only)

  


Requirements

_EM: Tim Reitz 07/25/2023: Do we want to keep pursuing this as part of Phase 3 if we're looking at switching to apphosting accounting soon? 

DONE_IDD: Tim Reitz 07/25/2023: Not needed at this point. 

  


Overview: This is a hidden record type that mirrors the sales items in Classic Accounting and is used for syncing between the two CA and the Solution.

  


Accessed via: The Classic Accounting Sales Items report (see corresponding section of this proposal)

  


DONE_CH: Add SKUs to the Demo system? 

Tim Reitz 04/19/2022: This is in conversation. 

Tim Reitz 08/16/2022: Ellis was fine with looking at it. But I think the first question actually should be: 

DONE_CH: Should we use SKUs or Sales Items? 

DONE_TR: Yes, SKUs.

DONE_NM: Add Inventory Management to E00/Demo and tell Tim

DONE_TR: update the demo system

  


TODO_JM - via Zoom, once we get SKUs in the demo system?: What fields need to be brought in from Classic Accounting? 

  


Sections and Fields (listed here as the field description and the field name): 

TODO_CH: Tim Reitz 09/06/2022: Matthias, what needs to be specced out here? 

  * AppHosting ID (auto-set)



TODO_CH: do we need this or do we use the CA ID? 

  * Item Type Code (itemtypecode; 
  * Item ID (itemid; unique identifier; number)
  * Active (active; checkbox; 
  * Cost (cost; 
  * Create Date (createdate; 
  * Item Code (item_code; 
  * Item Location (itemlocation; text field) 
  * Item Name (itemname; 
  * Item Number (itemnumber; equivalent to SKU ID; can be changed in CA; 
  * Modification Date (moddate; 
  * Notes (notes; 
  * Order Minimum (ordermin; 
  * Order Maximum (ordermax
  * Price (price; number to 2 decimals; 
  * Price Type (pricetype; "Fixed" or "Percentage"; sales items are Fixed, discounts and tax are Percentage; 
  * Purchase Description (purchasedesc; used on vendor documents; 
  * Sales Description (salesdesc; used on customer documents; 
  * Vendor Part Number (vendor_part_number; 
  * Weight (weight; 
  * Inventory Group ID (inventory_group_id; 
    * Tim Reitz 05/10/2022: Not sure if this is needed. 
  * Vendor Name (org; 
  * Purchase Account (purchaseaccountid; for General Ledger; 
  * Sales Account (salesaccountid; for General Ledger; 
  * Alert Note on Purchases (alert_note_purchases; 
  * Alert Note on Sales (alert_note_sales; 
  *   *   * AppHosting SKU (list of SKUs)



TODO_CH: Do we need this on this record? 

  * 


  


Data Access: Admin Only

  


Other Notes:

  


Development Specification

Mockup: None needed (can use auto-generated detail screens)

  


  


Syncing:

  * NOTE: The sync should flag CA items as inactive and run the sync before deleting them (I think)
  * The AppHosting SKU will be automatically set to the Classic Accounting Item if it's non-blank. Validate that multiple CA Items do not link to the same SKU.
  * Create an X30 that runs on all SKUs, copying information from the associated CA Item (adding an index)
  * Make that part of an x30list that will be triggered by the CA sync


