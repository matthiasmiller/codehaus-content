27.10. Buyer Payments Lacking Grade Reports Report Alert

  


Requirements

Sean Miller 04/29/2025: Moved to [[[IN11428](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11430&)]] - ZGW - Buyer Payments Lacking Grade Reports Report Alert

  


  


Estimated Cost: Approximately $500

  


Spec:

  


Overview/Purpose: This is an internal report alert that notifies users that one or more Buyer Payments have been entered for a Delivery Ticket that is lacking Buyer Grade Report information.

  


Details: 

  * Title: "<#> Buyer Payment(s) Lacking Grade Reports" (with "#" = the number of corresponding records)
  * Displays within 20 minutes of: Creation of / Saving a "Closed" Buyer Payment record that is linked to a non-Closed Delivery Ticket record that has no attachments in the "Buyer Grade Report Files" embedded spreadsheet. 
  * Action: Opens the "Buyer Payments Lacking Grade Reports" report
  * User(s) to notify: All users with the "Edit Payments" Permission
  * Dismiss type: Auto-dismiss when all items are resolved



  


Other Notes:

  * N/A



  


Development Specification

Mockup: N/A 

  


TODO_PRICING: Tim Reitz 12/06/2024: Not included in the HLD.
