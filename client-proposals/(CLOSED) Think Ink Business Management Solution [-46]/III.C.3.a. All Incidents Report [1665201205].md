3.3.3.1. All Incidents Report

  


Requirements

The All Incidents report is a customized version of the AppHosting standard Incidents report, and it shows all incidents in the Solution with various views and filters. 

  


The Think Ink version would have the following changes: 

Remove the following column(s): 

  * Stage
  * Organization
  * Modified By
  * Modified Date



  


Move the following column(s): 

  * Workflow to be between Type and Contact



  


Add the following column(s): 

  * Device (between Contact and Priority; shows the contents of the Device field on the incident record)



  


Other Notes: 

  * This would be a user-configurable version of the standard Incidents report. 
  * Note that each user might have to switch from the standard view to the Think Ink view the first time they run the report. After that, the Think Ink view should open by default each time. CCI/CH can assist with this process.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1513492533](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1513492533)

  


DONE_EM: Tim Reitz 08/23/2023: It appears that these changes were not done: [https://testthink.apphosting.zone/Reports/Standard/Std_Incidents?Asks=...](https://testthink.apphosting.zone/Reports/Standard/Std_Incidents?Asks=...). 

Tim Reitz 09/05/2023: TODO_IDD: write up a CR and pass it along to Ellis for comments on how to implement it. 

  


Does it make sense to handle this with a user-configurable report, with the exception of the new Device column?

Ellis Miller 06/13/2022: Sure!

  


  


Make this a configurable report (play around with how to share the same configuration sets between "All Incidents" which is a multi-pane and "My Incidents" which pops out a pane. I think we can use a Canonical Path on the subpane so that configurations are shared in both cases. Talk to Ellis if you run into any problems or have questions. 

  


Otherwise, it is just adding column ID's to each column and adding a client-specific column for devices.

  


BID: 1 Day
