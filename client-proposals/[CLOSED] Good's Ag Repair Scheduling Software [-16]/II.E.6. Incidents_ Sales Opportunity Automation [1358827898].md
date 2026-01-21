2.5.6. Incidents: Sales Opportunity Automation

  


Requirements

The checkboxes will be the primary way to move an incident through the workflow.

  


When you mark a job as "In Progress", the status will automatically update to Doing. When you mark a job as "Completed", the assignee will automatically update to Stephen and the follow-up date will update to today's date.

  


Development Specification

[[[IN7564](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-7566&)]] - ZGA - Remove SMS Feature

  


For the SMS:

  * Add a checkbox to Contacts called "Send real-time text alerts"
  * When checked, require that a mobile phone number is specified
  * Add a hidden field called "Sales Opportunity Last SMS Alert Date" with an index.
  * Create an x30


