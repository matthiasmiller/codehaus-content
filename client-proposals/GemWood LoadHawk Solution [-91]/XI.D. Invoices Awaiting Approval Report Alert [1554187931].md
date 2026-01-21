11.4. Invoices Awaiting Approval Report Alert

  


Requirements

Overview/Purpose: This is an internal report alert to notify users that one or more Buyer Invoices (from Delivery Ticket records) with the status of "Awaiting Salesperson Approval" (see details in the status spec).

  


Details: 

  * Title: "<#> Invoice(s) Awaiting Approval" (with "#" = the number of corresponding records)
  * Displays:Within 15 minutes of the following being true for at least one Delivery Ticket: 
    * "Delivery Ticket Status" = "Awaiting Salesperson Approval". 
  * Action: Open the "Invoices Awaiting Approval" report (see the corresponding spec)
  * User(s) to notify: Users in the following User Group(s): 
    * "Full Access" User Group
    * "Salespeople" User Group
  * Dismiss type: Auto-dismiss when all items are resolved



  


Other Notes: 

  * N/A



  


Development Specification

Change Requests: 

  * Tim Reitz 10/04/2025: [[[IN11560](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11562&)]] - ZGW - Improve Approval / Denial Process
  * 


  


  


  


Mockup: N/A
