8.3.4. Purchase Order Attachments Report

  


Requirements

Overview: This is a custom report of attached files in the "Purchase Order PDF" embedded spreadsheet of a selected Purchase Order record.

  


Accessed from:

  * "View Purchase Order Attachment(s)" link on the Delivery Ticket record



  


Title: Purchase Order Attachments for PO # <Buyer's PO #>

  


Columns: 

  * Attachment (link; displays the file name from the embedded spreadsheet)



  


Grouped by: N/A 

  


Sorted by: Attachment (alphabetically)

  


Filters: 

  * Buyer's PO # (required; drop list of Buyer's PO #s in the following format "<Buyer's PO #> (<PO Date>, <Buyer>)"; filters down as you type; defaults to blank; sets to the Purchase Order for the Delivery Ticket from which the report is opened)



  


Buttons: 

  * N/A



  


Menu Visibility: 

  * N/A (not included on any menus)



  


Other Notes: 

  * N/A



  


Development Specification

TODO_: Tim Reitz 09/04/2025: Do we need to update spec / logic for the items on this [filter] drop list? 

Tim Reitz 09/05/2025: I think it should be something like: 

  * Buyer's PO # (required; drop list of __[all? all active?] Buyer's PO #s for the selected Buyer in the following format "<Buyer's PO #> (<PO Date>, <Buyer>)"; filters down as you type; defaults to blank; sets to the Purchase Order for the Delivery Ticket from which the report is opened)



  


  


Mockup:[https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=410641560#gid=410641560](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=410641560#gid=410641560)

  


Ellis Miller 12/18/2024: 

[ ] Auto-push report

[ ] URL link action on first column

3 HOURS

  


TODO_PRICING: Tim Reitz 12/06/2024: Not included in official HLD estimate (we were expecting to completely do away with Purchase Orders).
