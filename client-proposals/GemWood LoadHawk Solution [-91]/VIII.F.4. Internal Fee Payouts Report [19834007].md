8.6.4. Internal Fee Payouts Report

  


Requirements

Overview: This is a custom report of Internal Fee Payouts, based on Closed Delivery Ticket records, with various filters.

  


Accessed from: Main Menu | Financials | Internal Fee Payouts

  


Title: 

  * Basic title: "Internal Fee Payouts" 
  * If "Payee" filter is not blank: Includes a "for <Payee>" suffix
  * If "Division" filter is not blank: Includes a "for <Division>" suffix (after the Payee suffix, if both are applicable)



  


Left Pane: This pane is a totals-only report that displays values from rows from the "Internal Fee Payouts Breakdown" embedded spreadsheet on Delivery Records, grouped by the Fee Payout Status, with one row per Division, per "Paid Date" (when applicable), per Payout Status.

  


Columns: 

  * Division
  * Fee Payout $ (total row shows sum)
  * Paid Date



  


Grouped by: 

  * First by: Internal Fee Payout Status ("Pending / Unpaid / Paid")
  * Second by: Division (alphabetically)



  


Sorted by:

  * First by: Division (alphabetically)
  * Second by: Paid Date (latest at the top)



  


Right Pane: This pane shows a simple breakdown for each selected unpaid row from the left pane, with one row per Division per Delivery Ticket represented in the corresponding row in the left pane.

  


Preface: "Details for selected unpaid row(s) from left pane):"

  


Columns: 

  * Delivery Ticket # (link to record)
  * Total Payout $ (total row shows sum) 



  


Grouped by: Division

  


Sorted by: Delivery Ticket #

  


Filters: 

  * Division (optional; drop list of GemWood Divisions list items; defaults to blank = all) 
  * Internal Fee Payout Status (multi-select drop list of "Pending / Unpaid / Paid" list items; none selected = all; defaults to only "Unpaid") 
  * Paid Date Start (date; looks at the "Paid Date" from rows on the "Internal Fee Payouts Breakdown" embedded spreadsheet; defaults to blank = all) 
  * End (date; looks at the "Paid Date" from rows on the "Internal Fee Payouts Breakdown" embedded spreadsheet; defaults to blank = all) 
  * Payee (hidden; optional; drop list of all Contacts and blank; defaults to blank = all) 



  


Buttons: 

  * Pay Selected Unpaid (visible to users with the "Manage Financials" Permission; 
    * clicking this button opens a prompt with the following: 
      * Close (button; closes the child screen to cancel the payment process); 
      * Payment Date (editable; defaults to the current date) 
      * Confirm that "Total Payout $" matches the full payment amount(s). (message)
      * Continue (button) 
    * clicking "Continue" does the following directly (no automatic process): 
      * takes all of the rows on "Internal Fee Payouts Breakdown" embedded spreadsheets on Delivery Tickets for the selected Division(s) on the left pane;
      * checks the "Paid" checkbox for the embedded spreadsheet rows; 
      * sets the "Paid Date" for those embedded spreadsheet rows to the selected "Payment Date"; 
      * automatically refreshes the report screen to display the updated information)
  * Send Email(s) Today (visible to users with the "Manage Financials" Permission; opens a child screen with the following:
    * Send email(s) for payments made on (date field; defaults to the current date);
    * Continue (button; clicking this button sends the "Internal Fee Payout Issued" email for all Internal Fee Payout embedded spreadsheet rows that have "Paid Date" = the selected date);
    * note that going through these steps multiple times will send the email multiple times)



  


Menu Visibility: Visible to users with the "Manage Financials" Permission

  


Other Notes:

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1264753268#gid=1264753268](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1264753268#gid=1264753268)

Tim Reitz 02/17/2025: Updated.

  


Change Requests:

  * Ben Reitz 10/08/2025: [[[IN11670](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11672&)]] - ZGW - Add "Internal Fee Payout Sent" and "Sales Commission Paid" emails
  * 


  


TODO_CCI: Tim Reitz 12/09/2024: "Pay Selected Unpaid" button is a modify button, rather than an x30. Additionally, it is on the right pane, and is a "modify all" button, even though it's labeled as a "selected" button in the UI.
