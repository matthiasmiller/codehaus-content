10\. Tasks

  


Requirements

Tim Reitz 10/04/2021: separate record type, tied out to the Work Order 

  


DONE_CH: let's wait to have the Tasks created until the building goes into the shop (to allow for change requests up until that point). this was we don't have to auto-delete unwanted Tasks (we just don't create them in the first place!). 

TODO_TR: This is fine, as long as somewhere we have an action that gets triggered when it comes into the shop, either through a WSGI or detail button.

  


TODO_: Hourly tasks are "General" tasks (sweeping the shop, etc.). Should have a way to generate individual tasks for these.

  


DONE_JM: tasks would repeat/duplicate on the if there are multiple of the same "by Piece" Options. Correct that they would not for Square Foot and Linear Foot SKUs?

DONE_CH: currently it shows up as one line item with a Qty of 4, but he's fine with having 4 separate tasks, etc.

Tim Reitz 10/12/2021: Matthias is thinking that having a Qty might be easier/make mroe sense. 

TODO_TR: We can do that. We don't allow SF/LF tasks.

Tim Reitz 01/20/2022: We're planning toward doing 1 Task with a Qty of 4 rather than 4 separate Tasks. 

  


  


TODO_TR: Make sure that materials costs get frozen on the Tasks so that Assembly (and other) reporting works properly. (also noted to do the same in WO)

  


TODO_TR: record: 

Fields: 

  * Task ID (numeric; auto-numbered) 
  * Status (To Do, Complete; auto-set and read-only; toggles with the Completed checkbox)
  * Building (automatic based on work order)
  * Sales Order (automatic based on work order)
  * Work Order (__
  * SKU (either based building or option)
  * Task Type (__
  * Quantity TODO_TR
  * Payment Type (__
  * Completed By (if Payment Type =  Piece Work or Fixed)



TODO_TR: finish speccing 

  * RG...
    * Member (
    * Percentage (required; number field with no decimals; default to 100 if there is only one Assignee, default to blank if more than one; sum must equal 100, so error on Save if not: "The sum of the Assignees' percentages must equal 100")


  * Completed (checkbox; marking a Task Complete locks all fields) 
  * Completed Date and Time (auto-filled and read-only; based on the Completed checkbox) 
  * Hours (visible if Payment Type = Hourly; required for Saving if Status = Complete; number field to 1 decimal place)
  * Notes (___
  * 


  


DONE_JM:  can tasks be "un-completed"? 

TODO_TR: yes, but admin only. but not a huge deal.

TImeframe:

DONE_CH: can we track when it was synced to QB and disallow it after the sync? This would be ideal.

If not, allow only for one day.

TODO_TR: Yes, just spec this way.

  


  


TODO_TR: all users can create and edit tasks, but only admins can edit tasks that are assigned to another person.

  


Development Specification

Task ID:

  


Using separate records for Tasks because: 

  * We need to track separate percentages
  * We want to avoid edit collisions (less of an issue)


