8.2. Converage Deactivation Due / Overdue Report Alert

TODO_VA: report alert

  


Overview/Purpose: The "Coverage Deactivation Due / Overdue" report alert is displayed for agents who have one or more client vehicles with coverage deactivations that are due or overdue.

  


Details: 

  * Title (can include an expression): Coverage Deactivation Due / Overdue
  * Displays within 20 minutes of: The "Deactivation Date" on a Vehicle record being on the current day or in the past without the "Deactivate" button being clicked.
  * Action: Opens the "Coverage Deactivation Dates" report, filtered to the current user's clients.
  * User(s) to notify: 
    * The agent whose client vehicle's "Deactivation Date" is set to the current day or in the past.
  * Dismiss type: 
    * Auto-dismiss when all items are resolved



  


Other Notes: N/A

  


Dev Spec: 

  * If dismissing before items are resolved, specify what should cause this alert to reappear (most likely it should be based on modified fields in Activity History).


