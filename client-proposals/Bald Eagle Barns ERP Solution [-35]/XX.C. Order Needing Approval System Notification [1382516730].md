20.3. Order Needing Approval System Notification

TODO_TR: spec out this report

  


DONE_CH: can we add a permission for "Dealer Approvals & Notifications" or something like that? (checkbox on the Salesperson Type contact details). if this is set to true, the person would get the notification and be able to approve the Sales Orders...

TODO_TR: To clarify, I would only call it a permission if it's on the user profile. Yes, this is fine. I wonder if we could make it a literal permission "Approve Dealer Buildings" and just have the notification be based on that? (Or if it's better to have it a checkbox on the contact , that's fine. As long as the wording is clear.

  


TODO_TR: spec out/clean up

  


Overview/Purpose: When an independent dealer sells a new building (one that needs to be built), it might require approval. 

  


Details: 

  * Title (can be an expression): 
  * Text (can be an expression): 
  * Trigger: When a Sales Order for a __ (custom) building or for a Change Order is marked as Sold by a Dealer who requires approval



TODO_TR: this would also apply to cancelations for custom buildings... 

  * Real-time?: Yes 
  * Action: Open a report of all Sales Orders that require approval TODO_TR: spec out this report
  * User(s) to notify: whoever has the setting set to true
  * Default Preference (alert style): 
  * Urgent? (notification with "!"): 
  * Internal Name (not visible to the user): 



  


Other Notes:
