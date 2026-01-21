8.5.1. All Delivery Tickets Report

  


Requirements

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
  * View Invoice PDF (visible if the viewing User has the "Edit Delivery Tickets via Import" Permission and the "Status" filter = only "Awaiting Salesperson Approval"; link; with the following details: 
    * displays as "View Invoice PDF"; 
    * opens the "Buyer Invoice Printout" for the Delivery Ticket for the row; note that the user can use "Ctrl+Click" or something similar to open in a new tab) 
  * Approve Invoice (visible if the viewing User has the "Edit Delivery Tickets via Import" Permission and the "Status" filter = only "Awaiting Salesperson Approval"; link; with the following details: 
    * displays as "Approve Invoice"; 
    * opens the "Approve / Deny Invoice Prompt Screen" for the Delivery Ticket for the row, with "Approved?" set to "Yes"; 
    * note that the user can use "Ctrl+Click" or something similar to open in a new tab) 
  * Deny Invoice (visible if the viewing User has the "Edit Delivery Tickets via Import" Permission and the "Status" filter = only "Awaiting Salesperson Approval"; link; with the following details: 
    * displays as "Deny Invoice"; 
    * opens the "Approve / Deny Invoice Prompt Screen" for the Delivery Ticket for the row, with "Approved?" set to "No"; 
    * note that the user can use "Ctrl+Click" or something similar to open in a new tab) 
  * Sent to Buyer (displays the date and time)
  * Closed Date (displays the Closed Date or Canceled Date, as applicable) 
  * Balance Due to Member $
  * Next Payment Due Date
  * Delivery Location



  


Grouped by:

  * If "Group By" = "Delivery Ticket Status": Delivery Ticket Status (standard sequence) 
  * If "Group By" = "GemWood PO Status": GemWood PO Status (standard sequence)



  


Sorted by: Ticket # (alphabetically)

  


Filters: 

  * Ticket # (optional; drop list of Ticket #'s; defaults to blank = all) 
  * Member (optional; drop list of Member-type Contacts; filters down as you type; defaults to blank; defaults to blank = all) 
  * Buyer (optional; drop list of Buyer-type Contacts; filters down as you type; defaults to blank; defaults to blank = all) 
  * Buyer's PO # (optional; drop list of Buyer's PO #s for the selected Buyer in the following format: "<Buyer's PO #> (<PO Date>, <Buyer>)"; filters down as you type; defaults to blank = all)
  * Status (optional; multi-select drop list of the Delivery Ticket Status items; defaults to all items except "Closed" and "Canceled" selected) Ticket Date Start (optional; date; defaults to blank = all; looks at the "Ticket Date") 
  * End (optional; date; defaults to blank = all; looks at the "Ticket Date") 
  * Group By (required; drop list of "Delivery Ticket Status" / "GemWood PO Status"; defaults to "Delivery Ticket Status")



  


  


Buttons: 

  * New Delivery Ticket (opens a blank new record)



  


Menu Visibility: All users

  


Other Notes:

  * Rows for Tickets with "Delivery Ticket Status" = "Closed" or "Canceled" are displayed in gray font. 
  * This report is used as a "master report", run with various filter configurations for other reports.



  


Development Specification

Change Requests:

  * Ben Reitz 06/24/2025: [[[IN11532](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11534&)]] - ZGW - Delivery Ticket record - Mark Tickets as "Sent for Approval"
  * Tim Reitz 10/04/2025: [[[IN11560](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11562&)]] - ZGW - Improve Approval / Denial Process
  * Ben Reitz 10/09/2025: [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1993127426#gid=1993127426](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1993127426#gid=1993127426) 

Tim Reitz 02/17/2025: Updated

  


Tim Reitz 12/05/2024: Load Type column: Catalog macro to pull together the values from the RG columns. 

  


Ellis Miller 12/18/2024: BID: 8 HOURS
