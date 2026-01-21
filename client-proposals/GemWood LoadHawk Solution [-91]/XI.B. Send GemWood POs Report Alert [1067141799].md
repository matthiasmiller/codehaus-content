11.2. Send GemWood POs Report Alert

  


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

Change Requests:

  * Ben Reitz 10/09/2025: [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature


