5.5.2. Invoice - Itemization Section

  


Requirements

*Done. 

  


  * Itemization standard section:
    * Itemization (no label; embedded spreadsheet with the following: 
      * Columns: 
        * Date (optional date field; defaults to blank) 
        * Vehicle Name (drop-list of vehicles for the selected Contacts)
        * Sales Item (drop-list of active sales items)
        * Description (plain text; custom behavior: auto-sets to "Refund" if "Amount" is negative)
        * Amount (number; two decimals)
      * Automatically sorted by: "Date" (earliest at the top) 
      * Buttons to add/remove rows (visible if Invoice "Status" = "Draft"): "✚" / "🞭" 
        * Custom behavior: If a line item is deleted, the "Line Item Dismissal" automatic process is run at Save (see corresponding spec).
      * Shows 10 rows without scrolling
      * Other Notes: 
        * N/A)



  


  * To edit line items, the status must be changed back to 'Draft'. (visible if "Status" ≠ "Draft"; on-screen message in gray font) 
  * Total Amount (read-only macro; displays the sum of "Amount" values for all rows in the Itemization embedded spreadsheet)
  * Total Paid (custom; read-only macro; displays the sum of all "Amount" values for all rows in the Payments embedded spreadsheet)
  * Payments (custom; button; displays a white triangle if there is any data to display; opens a child screen with an embedded spreadsheet with the following: 
    * Columns: 
      * Date (valid date required; defaults to the current date)
      * Check # (optional; plain text)
      * Amount (optional; number; two decimals)
      * Deposit Date (optional; date)
      * Deposited By (optional; drop-list of "In-State Agent"-type Contacts)
      * Notes (optional; plain text)
    * Automatically sorted by: "Date" (latest date at the top)
    * Buttons to add/remove rows (visible if Invoice "Status" = "Paid"): "✚ Add Row" / "🞭 Delete Row"
    * Shows approximately 25 rows without scrolling
    * Other Notes: 
      * N/A)



  


  * Due Amount (custom; read-only macro; displays the difference of "Total Amount" and "Total Paid")



  


Other Notes: 

  * Custom: The "Collision Entry Fee" list item in the drop list for Sales Items is included if Solution uses Collision Entry Fee. 
  * Custom: The "Cargo Entry Fee" list item in the drop list for Sales Items is included if Solution uses Cargo Entry Fee.



  


Development Specification

Change Requests: 

  * Tim Reitz 08/19/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident
  * Tim Reitz 08/23/2025: [[[IN9943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9945&)]] - ZWA - Pre-ZWW - Vehicle Record - Fees & Credits - Add "Dismiss" Option for Fees
  * Tim Reitz 08/26/2025: [[[IN10760](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10762&)]] - ZWA - Pre-ZWW - Processes - Add "Line Item Dismissal" Trigger / Process


