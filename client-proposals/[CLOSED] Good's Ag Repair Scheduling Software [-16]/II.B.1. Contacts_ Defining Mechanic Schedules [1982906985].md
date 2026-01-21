2.2.1. Contacts: Defining Mechanic Schedules

  


Requirements

If the contact is an incident assignee, show a weekly shop schedule for that contact. This schedule would define how many shop hours are available per weekday: For example:

  


Weekday| Available Hours  
---|---  
Monday| 8  
Tuesday| 8  
Wednesday| 4  
Thursday| 8  
Friday| 8  
  
  


This schedule would be used for estimating the completion time for a given project.

  


Development Specification

I propose that we genericize Sales Pipelines and Stages to be general incident tools;

  * Rename "Sales Pipeline" to "Incident Workflow".
  * Rename "Sales Stage" to "Incident Stage".
  * Add a "Incident Type" to Workflow. If left blank, the workflow is available for all incidents. Otherwise, it's available only for the selected incident.



  


On the Stage, we will add the following fields:

  * Update Status to <todo/doing/done>
  * Update Assignee to <assignee>
  * Update Priority to <priority>



Add OnChange expressions to the Incident for this.

  


Add an Incident Report by Stage, which groups by workflow and sorts by stage. Also add a filter to the Incidents ask prompt.

  


For Goods, we will:

  * Ship a "Work Order" incident type.
  * Ship a "Work Order" workflow with the following stages:
    * Pending
    * Scheduled
    * Started
    * Finished
    * Billed



  


These should be Investortools-owned, but should be editable in the client system.

  


We will also add custom validation to Good's Ag that warns if the assignee is out-of-sync.
