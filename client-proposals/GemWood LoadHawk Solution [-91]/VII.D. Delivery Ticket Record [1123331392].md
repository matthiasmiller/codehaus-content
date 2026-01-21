7.4. Delivery Ticket Record

  


Requirements

Overview: The Delivery Ticket record is a custom record, and is used to track details about a load of lumber. It is the common thread for an order. 

  


This record is based off of a paper delivery ticket that is filled out on-site at the Member's location when a load of lumber is loaded for shipment. For Phase 1, all Delivery Ticket records are created by GemWood users, but in future phases, the ability could be added for Member users to create them from on-field tablets.

  


The Delivery Ticket Record displays the following categories of information:

  * Member information, on the left side of the screen,
  * Buyer information, on the right side of the screen,
  * Load-specific and GemWood internal information at the top and bottom of the screen. 
  * Note that for narrower device screens, these three categories would fall into line vertically instead.



  


Accessed via: Various reports, such as:

  * Delivery Tickets Reports
  * Delivery Ticket Search
  * Main Menu | Data Entry | New Delivery Ticket (opens a new, blank Delivery Ticket record)
  * etc.



  


Sections and Fields: The sections and fields for this record are specced out in subsections below.

  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility:
    * The main screen is visible to all users.
    * Some section(s) / field(s) are visible only to certain users (based on Permissions - see corresponding specs).
  * Editability:
    * If "Delivery Ticket Status" ≠ "Closed" or "Canceled": 
      * The main screen is editable for users with the "Edit Delivery Tickets interactively" Permission, with some section(s) and/or field(s) further controlled for certain users, based on Permissions - see corresponding section/field specs.
      * Users with the "Edit Delivery Tickets via import" Permission but not the "Edit Delivery Tickets interactively" Permission can edit only via automatic processes (cannot make edits directly on the detail screen).
    * If "Delivery Ticket Status" = "Closed" or "Canceled": Only the following items remain editable (all others become read-only), utilizing the "Limited Editing Mode" feature: 
      * "Buyer Payment Finalized + Delivery Ticket Closed" checkbox (but note that its other editability condition(s) still apply), 
      * "Delivery Ticket Files" embedded spreadsheet (in the "View/Edit Documents" child screen); 
      * "Buyer Grade Report Files" embedded spreadsheet (in the "View/Edit Documents" child screen); 
      * "Delivery Ticket Canceled" checkbox (but note that its other editability condition(s) still apply), 
      * "Buyer Grade Report Sent to Member" checkbox, 
      * All editable fields in the "GemWood Financials" section (but note that some of these have additional editability conditions). 



  


Special Considerations:

  * Copy Record: Disallow (but the copy feature could be considered and added in the future)
  * Delete Record: Allow deletion if "Status" = "Canceled"
  * Merge Record: Disallow



  


Other Notes:

  * Note that various final calculations are not done until the Delivery Ticket is marked as "Closed" (which happens after payment is received from the Buyer, and any negotiations are complete. However, the Solution does calculate and display pending values for these fields, based on the "Buyer Invoice $" amount; these are displayed in gray font with a "(Pending)" suffix.



  


Development Specification

Change Requests: *note changes to specific sections in the Dev Spec for those sections* 

  * Tim Reitz 05/12/2025: [[[IN11326](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11328&)]] - ZGW - Delivery Tickets - Documentation - Allow Upload & Delete if Status = Closed or Canceled
  * Ben Reitz 06/24/2025: [[[IN11532](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11534&)]] - ZGW - Delivery Ticket record - Mark Tickets as "Sent for Approval"
  * Ben Reitz 10/08/2025: [[[IN11594](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11596&)]] - ZGW - Delivery Ticket record - Allow Salesperson to Approve & Deny from detail screen
  * Ben Reitz 10/08/2025: [[[IN11704](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11706&)]] - ZGW - Delivery Ticket record - Remove "n" from the invoice number
  * Ben Reitz 10/08/2025: [[[IN11670](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11672&)]] - ZGW - Add "Internal Fee Payout Sent" and "Sales Commission Paid" emails
  * Ben Reitz 10/08/2025: [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature
  * 


  


Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1659676278#gid=1659676278](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1659676278#gid=1659676278) 

Tim Reitz 01/23/2025: Updated. 

  


Ellis Miller 12/16/2024: 

[ ] Custom DB Level

[ ] NOTE: Let's use Tkt for field prefixes.

BID: 2 HOURS FOR BASIC RECORD

  


Consider coding after the rest of the screen:

[ ] Use the "Limited Editing mode" feature for users with the "Edit Invoice approval fields on Delivery Ticket" Permission but not the "Edit Delivery Tickets" Permission. 

Tim Reitz 01/09/2025: We're not doing this anymore (instead limiting some users to only editing the DT record via import).

[ ] Specify "IsOpenTicket" for all fields except:

  * "Buyer Payment Finalized + Delivery Ticket Closed" checkbox 
  * "Delivery Ticket Canceled" checkbox 
  * All editable fields in the "GemWood Financials" section 



Tim Reitz 01/09/2025: We're now using Limited Editing mode for closed & canceled Delivery Tickets - ask Ellis for updated dev spec.

BID: 4 HOURS FOR SPECIAL EDITING CONTROLS

  


  


_CCI: Tim Reitz 01/16/2025: This likely is stating the obvious, but I wanted to make sure to communicate it: Please note that in places where the spec says to use a % in a calculation (i.e. "GemWood Lumber Brokerage Fee $" in Delivery Ticket Record | Member Financials section: "dynamically displays the rounded value of "GemWood Lumber Brokerage Fee %" * "Ticket Value $""), this assumes that we are using the decimal equivalent of the % rather than the % itself. For example, using "0.04" if the % is set to "4.00".

Jisan Mahmud 02/23/2025: Yes, this was obvious.
