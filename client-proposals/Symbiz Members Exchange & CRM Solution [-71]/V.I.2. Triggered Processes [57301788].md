5.9.2. Triggered Processes

Triggered Processes: The Solution contains the following automatic processes that are initiated via a trigger in the Solution:

  


__. Create Tentative Growth Ring Meeting:

  * Description: Used to schedule a new Growth Ring Meeting.
  * Prompts: 
    * __ 



TODO_VA: Tim Reitz 06/04/2025: Ask Jonathan about prompt details for this one. 

  * Initiated:
    * When the "Schedule Meeting" button on the Growth Ring Meeting record is clicked, if there are no future Scheduled or Tentative Meeting records for the selected Growth Ring Group.
  * Action(s): 
    * Creates a new Meeting record with the Growth Ring Group defaulted, Status = Tentative, and the Meeting Date set to 1 month from the current date.
  * Database Trigger to be Enabled: 
    * CreateTentativeGrowthRingMeeting



  


TODO_VA: Tim Reitz 06/04/2025: Ask Jonathan for details about the other triggers on the report (that have an Email Notification .r20 listed in them): [https://symbiz.silverloom.io/Reports/Standard/Std_Triggers?State=ctLVLwm53iQ&](https://symbiz.silverloom.io/Reports/Standard/Std_Triggers?State=ctLVLwm53iQ&).
