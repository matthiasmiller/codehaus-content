5.5. QR Code Record

  


Requirements

Overview: This is a custom record type, used to create and track QR Codes. This record tracks individual furniture pieces from check-in through loading, ensuring complete orders (like all 9 pieces of a bedroom set) make it onto the correct truck. Each code stores the piece's warehouse zone and block location, preventing the "wrong truck" errors that currently happen with paper-based tracking.

  


Accessed via: QR Codes report

  


Sections and Fields: 

  * General section:
    * Active (checkbox)
    * Internal ID (number; auto-set and read-only; possibly hidden - TBD)
    * Order # (drop list of Orders)
    * Item (drop list of Items from the selected Order)
    * Qty (number field without decimals)
    * Notes (standard memo)
    * Warehouse Zone (drop list of Warehouse Zones)
    * Warehouse Block
    * Print (checkbox; when checked, prints the QR code from the printer)



  


  * Scans section:
    * Unlabeled and read-only embedded spreadsheet with the following:
      * Date
      * Time
      * User



  


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



  


Additional Design Notes:

  * Checkin Process
    * Allow creating QR Codes for pieces at the point of checkin.
      * Filter by Builders, show orders grouped by Builders + Date + Order ID
      * If multiple items are combined in a single box, we will simply print multiple QR codes.
      * Allow selecting an item and Generate & Print QR Code
      * Advanced option to generate a QR code with a custom quantity
    * Admin tools
      * Re-print an QR Code
      * Deactivate a QR code, etc



  


  * Pulling/Loading/Delivering:
    * Scanning the QR prompts for a login
    * Top of Screen - 
      * BOL # + Drop # + Left/Right Buttons to move through stops
      * High-level view of current item
    * Middle/Bottom of Screen:
      * Button to toggle Pulled / Loaded / Delivered (depending on current role AND based on whether a future action has been completed)
    * Bottom of Screen
      * List of current customer's orders, with the scanned item highlighted in the list



  


  * NOTE: Require pullers to move through customers in sequence. The warehouse manager can optionally defer items and/or override items as completed (with notes)



  


  * QR Details:
    * Should the QR contain any descriptive information?
      * Builder + Customer + PO + Item + Code + Qty (if overridden)?
    * Links to something like [https://vvt.wsgi.silverloom.io/qr/12345/ABCD](https://vvt.wsgi.silverloom.io/qr/12345/ABCD) (where 12345 = Silverloom's internal order ID, ABCD = a unique ID for the QR code)



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=834393728#gid=834393728](https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=834393728#gid=834393728)

  


TODO_HLD - will they use a laptop for checkin?
