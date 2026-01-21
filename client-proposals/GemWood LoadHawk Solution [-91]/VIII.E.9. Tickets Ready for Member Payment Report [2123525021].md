8.5.9. Tickets Ready for Member Payment Report

  


Requirements

Overview: This is a custom multi-pane "Accounts Payable"-style report of Delivery Tickets that are ready for payment to the Member (left pane), and Member Payments made on the current day (right pane).

  


Accessed from: 

  * Main Menu | Payments | Tickets Ready for Member Payment (bypasses the filter screen to open the report directly)
  * The "Tickets Ready for Member Payment" notification



  


Title: "Tickets Ready for Member Payment" 

  


Left pane: This pane shows all Delivery Tickets that are ready for payment to the Member, i.e. all Tickets for which all of the following are true:

  * "Delivery Ticket Status" ≠ "Canceled" (note that "Closed" Tickets should be included, since some are paid in full after being closed) 
  * "Next $ Due to Member" ≠ zero (note that the report does include Tickets with values that are negative) 
  * "Balance Due to Member $" ≠ zero (but the report does include Tickets with values that are negative) 



  


Preface: "Accounts Payable"

  


Columns: 

  * Member
  * Ticket # (link to open record)
  * Ticket Date
  * Balance Due to Member $ (total row shows sum; displays in red font if negative, which should rarely happen)
  * Next Payment Due Date (displays in red if = current day or in the past) 
  * Days Until Due (displays the number of days until the "Next Payment Due Date", or "0" if due on the current date, or the negative number of days since the Due Date if in the past; displays in red if the Due Date is = the current day or is in the past) 
  * New Member Payment (link; same as the corresponding link on the Delivery Ticket screen)



  


Grouped by: The following special groupings:

  * Overdue (if "Next Payment Due Date" is in the past) 
  * Due Today (if "Next Payment Due Date" = today) 
  * Due This Week (if "Next Payment Due Date" is in the current calendar week) 
  * Due Next Week (if "Next Payment Due Date" is in the next calendar week) 
  * Due in the Future (if "Next Payment Due Date" is after the end of the next calendar week) 



  


Sorted by: Next Payment Due Date (earliest at the top) 

  


Filters: 

  * Due Within # Days (number; 0 decimals; defaults to blank = all; when a number is entered, the report shows only items due within that number of days; report always shows overdue items; applies to the left pane)



  


Right Pane: This pane shows all payments made to Members on the current date, i.e. all Member Payment records for which "Payment Date" = the current date. This is the main "Member Payments Report", with both the "Payment Date Start" and "End" filters set to the current date.

  


Buttons: 

  * N/A



  


Menu Visibility: All users

  


Other Notes:

  * N/A



  


Development Specification

Mockup:[https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=415514229#gid=415514229](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=415514229#gid=415514229)

Tim Reitz 03/12/2025: Updated.

  


  


Change Requests: 

  * Tim Reitz 03/12/2025: [[[IN11201](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11203&)]] - ZGW - Delivery Ticket - Remove "Next $ Due to Member"
  * 


  


  


Ellis Miller 12/18/2024: 

  


BID: 1 DAY
