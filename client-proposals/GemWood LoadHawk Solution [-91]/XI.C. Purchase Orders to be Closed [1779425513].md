11.3. Purchase Orders to be Closed

  


Requirements

Overview/Purpose: This is an internal report alert to notify users that one or more Purchase Order records need to be closed. 

  


Details: 

  * Title: "<#> Purchase Order(s) to be Closed" (with "#" = the number of corresponding records)
  * Displays within 20 minutes of: 
    * For "Load-Based" Purchase Orders: "Remaining Loads" on a Purchase Order record changes to "0" or negative and "Status" remains = "Open"; or  
    * For "Date-Based" Purchase Orders: "Replaced By" is set to non-blank and "Status" remains = "Open". 
  * Action: Open the "Purchase Orders to be Closed" report - see the corresponding spec.
  * User(s) to notify: All users with the "Edit Purchase Orders" Permission 
  * Dismiss type: Auto-dismiss when all items are resolved



  


Other Notes: 

  * N/A



  


Development Specification

Mockup: N/A 

  


_DD: Tim Reitz 01/04/2025: Let's keep this one, to help keep track of POs. 

Tim Reitz 01/07/2025: Client is fine with keeping this. 

  


TODO_PRICING: Tim Reitz 10/29/2024: Not included in official HLD estimate (we were expecting to completely do away with Purchase Orders [and we weren't planning to do any alerts].
