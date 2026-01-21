8.2. Changes to the All Incidents Report

  


Requirements

The All Incidents report is a customized version of the AppHosting standard Incidents report, and it shows all incidents in the Solution with various views and filters. 

  


The Think Ink version would have the following changes: 

Remove the following column(s) (to be done manually to the report configuration in the test & live systems - see accompanying instructions): 

  * Stage
  * Organization
  * Modified By
  * Modified Date



  


Move the following column(s) (to be done manually to the report configuration in the test & live systems):  

  * Workflow to be between Type and Contact



  


Add the following column(s): 

  * Device (between Contact and Priority; shows the contents of the Device field on the incident record)



  


Other Notes: 

  * This would be a user-configurable version of the standard Incidents report. 
  * Note that each user might have to switch from the standard view to the Think Ink view the first time they run the report. After that, the Think Ink view should open by default each time. CCI/CH can assist with this process.



  


Development Specification

Tim Reitz 01/31/2024: Done in [[[IN8658](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8660&)]] - ZTK - Changes to the All Incidents report.
