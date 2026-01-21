11.1. Send GemWood POs Real-Time Notificaiton

  


Requirements

Overview/Purpose: This is a custom real-time notification that alerts users with "Receive Notifications: Assigned PO to Send" permission that one or more GemWood Purchase Orders are ready to be sent to their assigned Members. 

  


Details: 

  * Description: Assigned PO to Send
  * Title (can include an expression): "<# POs ready to send> Assigned PO<"s" if more than one> to send: <GemWood PO #1>, <GemWood PO #2>, and <GemWood PO #3>"
  * Text (can include an expression): N/A
  * Display when: 
    * Record type: Purchase Order
    * Transaction Type: Create, Update
    * Condition: a GemWood PO's "Status" changes to "Read to Send" 
  * Notification preference: On (play sound, show banner)
  * Urgent? (notification includes "!"): Yes 
  * Action: Opens the "Send GemWood POs Report"
  * User(s) to notify: All users with the "Receive Notifications: Assigned PO to Send" Permission (must be manually set for each user) 



  


Other Notes:

  * To receive this alert, users must have the "Receive Notifications: Assigned PO to Send" permission.
  * The alert disappears automatically when clicked. 
  * Each user that receives the alert must click on it to dismiss it.



  


Development Specification

Change Requests:

  * Ben Reitz 10/09/2025: [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature


