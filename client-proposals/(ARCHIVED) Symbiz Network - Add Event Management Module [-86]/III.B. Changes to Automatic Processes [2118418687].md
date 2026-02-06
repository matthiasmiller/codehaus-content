3.2. Changes to Automatic Processes

  


Requirements

*Documented 

  


Make the following changes to Automatic Processes (changes indicated with blue / strike-through):

  


Send Info Meeting Follow-up Emails (Primary & Secondary):

  * Overview: Used to automatically send the following User Notification emails:
    * Info Meeting Follow-up (Primary)
    * Info Meeting Follow-up (Secondary)
  * Schedule: Every day at 7:00 am ET.
  * Actions:
    * Checks Info Meeting-type Event records, and send the "Info Meeting Follow-up (Primary)" email notification for all records with a Status other than Canceled that have the Event Date 14 calendar days in the past. 
    * Checks Info Meeting-type Event records, and send the "Info Meeting Follow-up (Secondary)" email notification for all records with a Status other than Canceled that have the Event Date 3 weeks (21 calendar days) in the past, if there is at least one linked Event Registration record with the "Lead Follow-up Completed" checkbox not checked.
  * Scheduled Task Commands:
    * Line 1: "< email "Standard\Std Email Notification - Info Meeting Follow-up (Primary).r20" >"
    * Line 2: "< email "Standard\Std Email Notification - Info Meeting Follow-up (Secondary).r20"" >"



  


Send Review Launch Meeting Registrations Email:

  * Overview: Used to automatically send the "Review Launch Meeting Registrations" User Notification email:
  * Schedule: Every day at 7:00 am ET.
  * Actions:
    * Checks Launch Meeting-type Event records, and send the "Review Launch Meeting Registrations" email notification for all records with a Status of Tentative or Scheduled that have the Event Date 14 days in the future. 
  * Scheduled Task Command: "< email "Standard\Std Email Notification - Review Launch Meeting Registrations.r20" >"



  


These are configured in the Solution at deployment by CCI.

  


Development Specification

Dev Spec notes for the designers: 

  * General info: [[[W0457](https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages&NumberID=-458&)]] - 170. Scheduled Tasks 
  * Wiki page for setting up Scheduled Tasks: [[[W0552](https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages&NumberID=-553&)]] - Setting Up Scheduled Tasks 
  * [ ] Add a note to the deployment incident to set up the Scheduled Tasks 



  


Ellis Miller 06/20/2024: 

NO BID: We'll include in the email section
