5.2. Changes to the "All Delivery Tickets" Report

Overview: This is a custom report of all Delivery Ticket records in the Solution, with various filters.

  


Accessed from:

  * Main Menu | Members | All Delivery Tickets (opens the report directly, bypassing the filter screen)



  


Title: 

  * If "Member" and "Buyer" filters are blank: "All Delivery Tickets"
  * If "Member" filter is specified: "Delivery Tickets from <Member Name>"
  * If "Buyer" filter is specified: "Delivery Tickets for <Buyer Name>"
  * If both "Member" and "Buyer" filters are specified: "Delivery Tickets from <Member Name> for <Buyer Name>"



  


Columns: 

  * GemWood PO #
  * GemWood PO Status
  * Member
  * Ticket # (link to open record)
  * Ticket Date
  * Buyer
  * Buyer PO # (link to open the corresponding Purchase Order record)
  * Ticket Value $ (total row shows sum) 
  * Load Type (displays the "<Thickness> <Species> <Grade>" (i.e. "4/4 WO Rift") for the first row in the Load Itemization table for the Delivery Ticket)
  * Last Sent for Approval (displays the most recent date and time of the "Sent for Approval" and "Resent for Approval" fields, i.e., the most recent date that the "Salesperson Invoice Review Email" was sent)
  * Sent to Buyer (displays the date and time)
  * Closed Date (displays the Closed Date or Canceled Date, as applicable) 
  * Balance Due to Member $
  * Next Payment Due Date
  * Delivery Location
    * Note: the location of this column is being changed. 



  


Grouped by:

  * If "Group By" = "Delivery Ticket Status": Delivery Ticket Status (standard sequence) 
  * If "Group By" = "GemWood PO Status": GemWood PO Status (standard sequence)



  


Sorted by: Ticket # (alphabetically)

  


Filters: 

  * Ticket # (optional; drop list of Ticket #'s; defaults to blank = all) 
  * Member (optional; drop list of Member-type Contacts; filters down as you type; defaults to blank; defaults to blank = all) 
  * Buyer (optional; drop list of Buyer-type Contacts; filters down as you type; defaults to blank; defaults to blank = all) 
  * Buyer's PO # (optional; drop list of Buyer's PO #s for the selected Buyer in the following format: "<Buyer's PO #> (<PO Date>, <Buyer>)"; filters down as you type; defaults to blank = all)
  * Status (optional; multi-select drop list of the Delivery Ticket Status items; defaults to all items except "Closed" and "Canceled" selected) Ticket Date Start (optional; date; defaults to blank = all; looks at the "Ticket Date") 
  * End (optional; date; defaults to blank = all; looks at the "Ticket Date") 
  * Group By (required; drop list of "Delivery Ticket Status" / "GemWood PO Status"; defaults to "Delivery Ticket Status")



  


Buttons: 

  * New Delivery Ticket (opens a blank new record)



  


Menu Visibility: All users

  


Other Notes:

  * Rows for Tickets with "Delivery Ticket Status" = "Closed" or "Canceled" are displayed in gray font. 
  * This report is used as a "master report", run with various filter configurations for other reports.


