27.12. Sales Commission to be Paid Report Alert

  


Requirements

Sean Miller 04/29/2025: Moved to [[[IN11430](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11432&)]] - ZGW - Sales Commission to be Paid Report Alert

  


  


Estimated Cost: Approximately $500

  


Spec:

  


Overview/Purpose: This is an internal report alert to notify users that it is time to pay Sales Commission (from Delivery Ticket records). 

  


Details: 

  * Title: "Sales Commission to be Paid"
  * Displays: The first Monday of every month
  * Action: Open the "Sales Commission Report" \- see the corresponding spec
  * User(s) to notify: All users with the "View Sales Commission Details" Permission 
  * Dismiss type: Auto-dismiss when all items are resolved



  


Other Notes: 

  * Note that the "User(s) to notify" should be changed if the Solution is enhanced in the future to handle multiple Salespeople.



  


Development Specification

Ellis Miller 12/24/2024: Let's discuss exactly how these are implemented. The "Users to Notify" needs to be baked into the report subset or we need a separate auto-push report.

  


Mockup: N/A 

  


TODO_PRICING: Tim Reitz 12/06/2024: Not included in the HLD.
