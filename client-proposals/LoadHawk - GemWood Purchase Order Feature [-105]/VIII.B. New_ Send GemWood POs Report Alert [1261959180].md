8.2. New: Send GemWood POs Report Alert

  


Requirements

Overview/Purpose: This is a custom report alert notification that alerts users with the "Receive Notifications: Assigned PO to Send" permission that one or more GemWood Purchase Orders are ready to be sent to their assigned Members.

  


Details: 

  * Title (can include an expression): "<#> Assigned PO(s) need to be sent"
  * Display within 20 minutes of: When one or more rows on "GemWood Purchase Orders" embedded spreadsheet have "Status" = "Ready to Send". 
  * Action: Opens the "Send GemWood POs Report"
  * User(s) to notify: All users with the "Receive Notifications: Assigned PO to Send" permission (must be manually set for each user) 
  * Dismiss type: Auto-dismiss when all items are resolved



  


Other Notes: 

  * To receive this alert, users must have the "Receive Notifications: Assigned PO to Send" permission.



  


Development Specification

_EM: Tim Reitz 09/11/2025: Could you give a specific $ estimate for this, in case the client wishes to do only one of the notifications for now?

Ellis Miller 09/10/2025: Roughly $200 each to code.
