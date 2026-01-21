9.1.2. Change Orders

TODO_TR:

  


  


  


  


[ ] Who can make these changes? 

Tim Reitz 10/26/2021: same as standard approval process

[ ] When can they happen?

Tim Reitz 10/26/2021: can be done at any point. would create a separate SO and WO.

TODO_CH: how should we handle this for buildings that are currently in production? group WO's by Building? update the original WO so there's no confusion? 

Shop Workers look at both the WO and Tasks...

  


TODO_TR: From a technical perspective, I prefer creating a new one. However, we have to think through how to display this in the Shop interface. One option is to indicate that there are additional WOs, or have the shop interface show all tasks from all open WOs for the building.

  


  


Scenarios:

  * Has not started stage with modifications - doesn't matter what we do
  * Has started stage but we're adding things - doesn't matter what we do
  * Has started stage but need to remove things not yet added - should probably remove from original to avoid confusion
  * Has started stage but need to remove things already added -
    * Pay the shop guys for adding the original thing
    * How do we compensate them for removing the old? TODO_JM



  


When cancelling an item:

  * Prefix incomplete items with a "CANCELLED/SKIP:"
  * Prefix complete items with a  "CANCELLED/UNDO:" and market it incomplete
  * This doesn't address compensation for this.



  


  


\-----

Tim Reitz 01/20/2022: This seems like the simplest solution: 

Assuming 1 Task with a Qty of 4 (rather than 4 separate Tasks):

  * If the Task has not been started/completed yet: Increase or reduce the Qty of the incomplete Task
  * If the Task has been started/completed and something needs to be added: Add a new Task with the additional Qty 
  * If the Task has been started/completed and something needs to be removed: Add a new Task with a negative Qty (there would need to be user training so that the Shop Workers know that this means to undo the work that they've done)
    * TODO_CH / TODO_JM: How does compensation work for this? Ideally, the negative (removal) Task would have the same rate per piece / per hour


