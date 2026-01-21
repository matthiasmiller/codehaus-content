8.6.3. Sales Commission Report

  


Requirements

Overview: This is a custom editable multi-pane report of Sales Commission for a selected Salesperson, based on Delivery Ticket records with "Delivery Ticket Status" of anything other than "Canceled", with various filters.

  * The left pane is editable and includes a row for each applicable Delivery Ticket and its corresponding Commission details.
  * The right pane shows the total of all unpaid rows selected in the left pane.



Users with the "Manage Financials" Permission can mark Commission as paid directly from this report via the "Pay Selected Unpaid" button.

  


Accessed from: Main Menu | Financials | Sales Commission

  


Title: Sales Commission for <Salesperson Name>

  


Left Pane: This pane is editable and includes one row per Delivery Ticket and its corresponding Commission details

Preface: N/A 

  


Columns: 

  * Ticket Date
  * Ticket # (link to record) 
  * Member 
  * Buyer 
  * Buyer's PO # 
  * Total Buyer Payment $ (total row shows sum) 
  * Commission % 
  * Commission $ (total row shows sum) 
  * Commission Paid Date (editable; displays the Commission Paid Date, when applicable) 



  


Grouped by: 

  * First by: Commission Status ("Pending / Unpaid / Paid")
  * Second by: Commission Paid Month & Year (looking at the "Commission Paid" date for Paid items; displays the month and year in the following format: "MMMM YYYY"; current month at the top; note that "Pending" and "Unpaid" do not display these sub-groupings because they do not include any Paid items) 



  


Sorted by: Ticket Date 

  


Right Pane: This pane shows the total Commission $ of all unpaid rows selected in the left pane.

  


Preface: "Payment amount (sum of selected unpaid rows from left pane):"

  


Columns: 

  * Total Commission $ (displays the sum of "Commission $" for all selected unpaid rows from the left pane) 



  


Grouped by: N/A

  


Sorted by: N/A

  


Filters: 

  * Salesperson (required; drop list of Internal-type Contacts; defaults to the Default Salesperson)
  * Commission Status (multi-select drop list of "Pending / Unpaid / Paid" list items; none selected = all; defaults to only "Unpaid") 
  * Commission Paid Date Start (date; looks at the Commission Paid Date; defaults to blank = all)
  * End (date; looks at the Commission Paid Date; defaults to blank = all)



  


Buttons: 

  * Pay Selected Unpaid (visible to users with the "Manage Financials" Permission; 
    * clicking this button opens a prompt with the following: 
      * Close (button; closes the child screen to cancel the payment process); 
      * Payment Date (editable; defaults to the current date) 
      * Confirm that "Total Commission $" matches the full payment amount. (message)
      * Continue (button) 
    * clicking "Continue" does the following directly (no automatic process): 
      * checks the "Commission Paid" checkbox for the selected "Unpaid" Delivery Tickets (ignoring "Pending" and "Paid" rows); 
      * sets the Commission Paid Date to the selected "Payment Date"; 
      * automatically refreshes the report screen to display the updated information)
    * Send Email(s) Today (visible to users with the "Manage Financials" Permission; opens a child screen with the following:
      * Send email(s) for payments made on (date field; defaults to the current date);
      * Continue (button; clicking this button sends the "Commission Payment Issued" email for all Delivery Tickets for the Salesperson selected in the report ask prompt that have "Commission Paid" = the selected date);
      * note that clicking this button multiple times will send the email multiple times)



  


Menu Visibility: Visible to users with the "View Sales Commission Details" Permission

  


Save Type: Save Button

  


Other Notes: 

  * Rows for Tickets with "Delivery Ticket Status" = "Closed" are displayed in gray font.



  


Development Specification

Change Requests: 

  * Tim Reitz 05/12/2025: [[[IN11467](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11469&)]] - ZGW - Sales Commission Report - Misc. Improvements
  * Ben Reitz 10/08/2025: [[[IN11670](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11672&)]] - ZGW - Add "Internal Fee Payout Sent" and "Sales Commission Paid" emails
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=64265082#gid=64265082](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=64265082#gid=64265082)

Tim Reitz 12/12/2024: Updated yesterday(?). 

  


  


TODO_CCI: Tim Reitz 11/20/2024: "Pay Selected Unpaid" button is a modify button, rather than an x30.

TODO_CCI: For the Pending and Unpaid groupings, hide the second level of totals (like the mockups).
