16.5. Order Record

  


Requirements

Overview: This record is used to track all of the different types of orders.

  


The record includes the following sections and fields:

  


  * Order Overview section
    * Order # (auto-set)
    * Order Notes (red notes to the right of the Order #. Used for important things that should be documented.)
    * Buyer (droplist of all customers)
    * Special Request (checkbox + requested date)
    * Order Type (drop list of the following:)
      * Animal (Oak Hill's animals)
      * Transport (animals transported for others)
      * Protocol (for housing animals for others)
      * Feed (for selling feed items)
    * Cancelled (checkbox)



  


  * Special Request section (visible if Special Request checkbox is filled)
    * Assigned To
    * # Males
    * # Females
    * # Either Sex
    * Requested Weight
    * Notes
    * Request Approved (checkbox with Date and Approved By; if checked, other order fields become required)



  


  * Shipping Details section:
    * Ship To (droplist)
    * Add Ship To (button)
    * Unload Order (single line plain text field)
    * Departure Date (date)
    * Departure Time (single line plain text field)
    * Ship Date (date)
    * Ship Date End (date)
    * Status (droplist of order statuses)
    * Driver (droplist)
    * Facility (editable droplist of all Oak Hill buildings)
    * Delivery Date (date)
    * Delivery Time (single line plain text field)
    * ID # (single line plain text field)
    * Location (droplist)
    * Quote # (single line plain text field)
    * Truck Size (droplist of large / small)
    * Vehicle (single line plain text field)



  


  * Animal Order Details section (visible if Type = Animal):
    * Embedded spreadsheet with the following:
      * Columns:
        * PI (list of PIs)
        * PO# (text)
        * Gender 
        * Order Weight (text)
        * ID# (visible for dog orders; list of IDs, filtered based on order type then by male/female order weight)
        * DOB (visible for dog orders; automatic and read-only)
        * Age (automatic and read-only; ___ decimals; as of __ date)
        * Shipped Weight (number; __ decimals)
        * Color (visible for dog orders; automatic and read-only)
        * Comments
        * Price 
        * Received Weight
      * Buttons:
        * Delete (button on every row)
        * Copy (button on every row; copies data from above row)
        * Insert
    * Note that there might be a "Quick Entry" feature, but the need for this would be assessed in the in-depth design, as it might not be necessary in AppHosting.



  


  * Feed Order Details section (visible if Type = Feed):
    * Details to be determined in in-depth design.



  


  * Protocol Order Details section (visible if Type = Protocol):
    * Details to be determined in in-depth design.



  


  * Transport Order Details section (visible if Type = Transport):
    * Details to be determined in in-depth design.



  


  * Documents section (visible for all order types) 
    * Attachments (used to add attachments to the order; memo or embedded spreadsheet of)
      * Name
      * Download Link
      * Date
      * Time
      * Delete Link (confirm)
    * View Order PDF (link to template)
    * Create QuickBooks Invoice (button)
    * Email Confirmation (link to new email)
      * This prepares the email with attachment(s) and a pre-filled TO and body. Pretty much all you have to do is hit Send. Based on things defined in Options section (looks like an email template/record). 
    * New Paperwork Packet (previously called "Create Disposition"; link to new blank Paperwork Packet record)



  


Other Notes:

  * Animal vs. Transport: The two companies coexist and the orders coexist. 
  * Transport order has less info pulled from the database. More manual entry. 
  * Orders can be shipped in multiple shipments.



  


Development Specification

TODO_IDD: Consider whether vehicle should be a list and if truck size should be fielded on the vehicle. We could then filter vehicle based on the selected size.

  


Gender (TODO_IDD - does this filter the ID#? If not, make it read-only)

  


Price (defaulted - TODO_IDD - should this be editable?)

  


  


Matthias Miller 03/22/2023: TODO_IDD: - would be looking to add each city and the delivery price

  * Price list is based on City - they have their prices set on a per-city basis
  * But there's still a little variability -- there are Small Truck and Large Truck flat fee


