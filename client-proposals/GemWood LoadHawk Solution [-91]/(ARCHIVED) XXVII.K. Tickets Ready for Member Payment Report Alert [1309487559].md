27.11. Tickets Ready for Member Payment Report Alert

  


Requirements

Sean Miller 04/29/2025: Moved to [[[IN11429](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11431&)]] - ZGW - Tickets Ready for Member Payment Report Alert

  


  


Estimated Cost: Approximately $500

  


Spec:

  


Overview/Purpose: This is an internal report alert to notify users that one or more Delivery Tickets are ready for payment to the Member.

  


Details: 

  * Title: "<#> Ticket(s) Ready for Member Payment" (with "#" = the number of corresponding records)
  * Displays within 20 minutes of one of the following conditions being true for a Delivery Ticket: 
    * Delivery Ticket "Status" = "Closed" and "Balance Due to Member $" ≠ 0 and "Next Payment Due Date" is within 3 days of the current date.
    * Delivery Ticket has a "Next Payment Due Date" in the past or on the current date.
  * Action: Open the "Tickets Ready for Member Payment" report, with the "Due with # Days" filter set to "3" \- see corresponding report spec for more details
  * User(s) to notify: All users with the "Edit Payments" Permission
  * Dismiss type: Auto-dismiss when all items are resolved



  


Other Notes:

  * N/A



  


Development Specification

Mockup: N/A 

  


TODO_PRICING: Tim Reitz 12/06/2024: Not included in the HLD.
