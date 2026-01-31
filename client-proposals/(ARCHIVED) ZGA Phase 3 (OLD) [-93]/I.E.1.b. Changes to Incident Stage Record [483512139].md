1.5.1.2. Changes to Incident Stage Record

  


Requirements

The following changes are to be made to Incident Stages (blue font represents changes to existing design / implementation): 

  


  * Assignee: If this field is blank for a Stage, incidents will retain their existing Assignee(s) when advanced to that Stage.



  


The following Stages are hard-coded for Good's Ag Repair and included in the Solution, linked to Service Locations and with non-editable Stage names:

  * Pending (for all Service Locations; default Status when a new Incident is created; not included on the Schedule report; Status = To Do) 
  * Work Schedule (for all Service Locations; when Scheduled checkbox is initially checked; included on the Schedule report; Status = To Do) (replaces the existing "Scheduled" Stage) 
  * Assigned to Tech (for all Service Locations; when Scheduled checkbox is checked and Assignee is set and the Finished checkbox is not checked; included on the Schedule report; Status = Doing) (replaces the existing "Started" Stage) 
  * Quality Control (only for Incidents with a Service Location with "Uses Quality Control" checked; when Finished checkbox is checked and the QC Passed checkbox is not checked; included on the Schedule report; Status = Doing) 
  * Ready to Invoice (for all Service Locations; if Service Location = Shop: when the QC Passed checkbox is checked and the Billed checkbox is not checked; if Service Location is anything other than Shop: when Finished checkbox is checked and the Billed checkbox is not checked; included on the Schedule report; Status = Doing) (replaces the existing "Ready to Bill" Stage) 
  * Complete (for all Service Locations; when the Billed checkbox is checked; not included on the Schedule report; Status = Done) (replaces the existing "Billed" Stage) 



  


The following details and behaviors are to be set on the above Stage records as part of deployment (to be done by CCI/CH):  

  * Workflow: set to "Work Order".
  * Sort Order: set according to the sequence in which they are listed above.
  * Assignee: left blank.
  * Status: set as mentioned above.



  


Note: Child incidents always show the stage of their parent incident.

  


Development Specification

Mockup: N/A 

  


Tim Reitz 10/24/2023: Basic list of stages: 

  * Pending
  * Work Schedule
  * Assigned to Tech
  * Quality Control
  * Ready to Invoice
  * Complete



  


[ ] [[[IN8700](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8702&)]] - CORE - Not clearing Assignee on Incidents

 BID: 2 Hours

  


[ ] May be shipping these so that we can control 

  


[ ] Change IncidentStage to reflect above description

  


[ ] Change IncidentNextStageHint to use an ifs statement instead of ListSubstitute

BID: 1 Day
