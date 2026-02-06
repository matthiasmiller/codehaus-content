10.1. Changes to the "Purchase Orders to be Closed" Report Alert

Overview/Purpose: This is an internal report alert to notify users that one or more Purchase Order records need to be closed. 

_CLIENT: Tim Reitz 09/04/2025: Consider / confirm whether this should be for just Buyer PO, or also GemWood POs. Or separate notifications for each. 

Tim Reitz 09/04/2025: If both, then let's make the PO Type filter on the report to be optional (blank in this case). 

_VA: Tim Reitz 09/05/2025: It now seems like no change to closing Buyer POs. 

  


  


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


