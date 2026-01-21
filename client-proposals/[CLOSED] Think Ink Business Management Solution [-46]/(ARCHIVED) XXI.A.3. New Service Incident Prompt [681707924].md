21.0.3. New Service Incident Prompt

  


Requirements

Tim Reitz 07/05/2022: Deferred from Phase 1. See [[[IN6416](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-6418&)]] - ZTK - Incidents - New Service Incident Prompt. 

  


Clicking the "New Service Incident" menu option would open a prompt page with the following fields:

  * Customer (required; drop list of Customer-type contacts; filters down as you type; fills the Contact field on the Incident if a new Incident is created)
  * Open Incidents (visible if a Customer is selected; optional drop list of open Incidents for the selected Customer; display "<Title>" \- <Creation Date>"; reverse sort by Creation Date) 



  


If an incident is selected from the list of Open Incidents: 

Clicking Continue would open the corresponding incident.

  


If no incident is selected from the list of Open Incidents:

The following fields would be visible under a "NEW INCIDENT" heading:

  * Assignee (optional; drop list of Employee type contacts)
  * Request Source (required; drop list of Email, Fax, Phone)
  * Device (optional; plain text field) 
    * Note that for the initial phases, this will simply be a plain text field, until the Device records are designed and developed, at which point this should change. 
  * Workflow (required; drop list of Workflows for Service-type incidents)
  * Notes (optional; plain text field) 



  


Clicking Continue on the prompt would create a new Service-type Incident with the corresponding fields filled in. The title of the new incident should default to "<first 20 characters of Contact Name>: <Workflow> <Device>". Note that any colons will be automatically removed from the Contact Name, Workflow, and Device when added to the title.

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=2085996154](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=2085996154)

  


Ellis Miller 06/20/2022: We will want to make Open Incidents a conditional list:

  * For every customer, check a OpenSvcIncidentByCustomer.ndx index. Almost always, this will be an empty hit.
  * For any customer with an open incident, we have to do one more disk read to get the title



Make sure this is fast.

  


DONE_CCI: Tim Reitz 07/01/2022: Client wishes to defer the New Sales Opp Prompt & Report for now. Would keep the New Service Incident menu option, which would simply open a blank new Service Incident with assignee defaulted. I'm planning to create a Change Request to save it for future reference.

Ellis, could you update the Phase 1 price accordingly? Also, should I set the CR as T&M or Fixed Price (and what estimate/quote should I give it)?

DONE_TR: Pull out of proposal, create CR (with link to mockup)

Ellis Miller 07/02/2022: Pulled. Fixed Price for the next 6 months. $1450.

  


BID: 2 Days
