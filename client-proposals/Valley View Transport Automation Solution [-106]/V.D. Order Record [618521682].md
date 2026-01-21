5.4. Order Record

  


Requirements

Overview: This is a custom record type, used to track Orders. This record is the central hub that connects builder, customer, items, pricing calculations, and fulfillment status throughout VVT's entire workflow. Manages the complex rate calculations (combining customer region base rates, builder region markups, product-specific adjustments, and custom overrides), tracks the order through six status stages (Ordered > Picked Up > Pulled > Loaded > In Transit > Delivered), and generates both bills of lading and customer invoices--eliminating the current triple-entry problem where orders get typed into QuickBooks three separate times.

  


Accessed via: Orders report

  


Sections and Fields: 

  * Order Details section:
    * Order # (displayed in the section header; auto-set and read-only number)
    * Order Date (date field; defaults to the current date)
    * Builder (drop list of active builders)
    * Builder Full Address (auto-set and read-only)
    * Customer (drop list of active customers)
    * Bill To (address field in standard format; defaults to Customer's address)
    * Ship To (drop list of standard shipping locations + option to add one-off)
    * Automatic PO (checkbox)
    * PO Number (with the following behaviors:
      * if "Automatic PO" checkbox is checked, read-only and set to a unique PO such as YYMMDD-1234 where 1234 is our internal ID;
      * editable and required if Customer-Assigned)
    * Rate % (read-only with ellipsis to modify individual factors)
      * Override Rate (checkbox)
        * Override Reason (plain text field; visible and required if the "Override Rate" checkbox is checked)
      * Customer Region Base Rate % (number field; visible and required if the "Override Rate" checkbox is checked)
      * Builder Region Markup % (number field; visible and required if the "Override Rate" checkbox is checked)
      * Builder Product Markup (drop list of builder markups; visible and required if the "Override Rate" checkbox is checked)
      * Builder Product Markup % (number field; visible and required if the "Override Rate" checkbox is checked)
      * Builder Markup % Adjustment (number field; visible and required if the "Override Rate" checkbox is checked)
      * Combined Rate % (auto-calculated)
    * Status (drop list of Order Statuses; note: this may just show an "In Transit" status if it's loaded + past the ship date; note: this may be auto-set - TBD)



  


  * Items section:
    * Items (embedded spreadsheet of the following:
      * Item (drop list of list of items)
      * Qty (number field without decimals)
      * Cubes (number field; 3 decimals TBD)
      * Builder Cost (number field;  2 decimals)
      * Finisher Cost (number field; 2 decimals)
      * Total Cost (read-only & auto-calculated; displays the sum of the Builder Cost and Finisher Cost for that row)
      * Rate $ (auto-calculated and read-only; displays Order Markup % x Total Cost)
      * Total $ (auto-calculated and read-only; displays Rate $ x Qty)



  


  * Pieces section (used for barcoding)
    * Pieces (embedded spreadsheet with the following:
      * Unique ID (auto-set; random number)
      * Item (drop list of Items from the "Items" embedded spreadsheet)
      * Qty (number field without decimals)
      * Notes (plain text)
      * Warehouse Zone (drop list of Warehouse Zones)
      * Warehouse Block (drop list of Warehouse Blocks)



  


  * Status section:
    * Picked Up (checkbox; when checked, displays date + user)
    * Pulled (checkbox; when checked, displays date + time + user)
    * Loaded (checkbox; when checked, displays date + time + user)
      * Defer Loading (checkbox; when checked, allows other orders on BOL to be loaded before this one)
    * Delivered (checkbox; when checked, displays date + time + user)
  * Print Bill of Lading
  * Print/Send Invoice
    * Process for this (print/email) and/or process to export to QuickBooks will be determined with further design



  


  * Record History section: 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: TBD
  * Editability: TBD



  


Special Considerations: 

  * Copy Record: TBD
  * Delete Record: TBD
  * Merge Record: TBD



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.  
  * Unless otherwise noted, all fields that become hidden for any reason (based on other fields, user permissions, etc.) retain their values. If they should be cleared, that is noted specifically in the field specs, with a "clear if hidden" or similar note.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=655293171#gid=655293171](https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=655293171#gid=655293171)

  


TODO_: Tim Reitz 10/22/2025: "Warehouse Blocks" are mentioned here, but not specced as a list or record. Let's dig into that (just a simple list?).

  


TODO_: Tim Reitz 10/22/2025: Note that the HLD spec for Invoices is very sparse. If we end up doing something complex with that, it could greatly increase the project cost -- maybe note it as an optional add-on if it gets large.
