21.0.2. New Sales Opportunity Prompt and Report

  


Requirements

Tim Reitz 07/05/2022: Deferred from Phase 1. See [[[IN6415](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-6417&)]] - ZTK - Incidents - New Sales Opportunity Prompt & Report. 

  


Prompt Details: 

Clicking the "New Sales Opportunity" menu option would open a prompt page with the following fields:

  * Lead Source (optional; drop list of the following:) 
    * Website
    * Phone Call
    * Email
    * Other 
  * Due Date (optional; fills the standard Due Date field on the Incident) 
  * First Name (optional; fills the Prospect First Name field on the Incident)
  * Last Name (optional; fills the Prospect Last Name field on the Incident)
  * Business Name (optional; fills the Prospect Business field on the Incident)
  * Phone (optional; fills the Prospect Phone field on the Incident)
  * Email (optional; fills the Prospect Email field on the Incident)
  * Tags (optional; multi-select drop list of Contact Tags; fills Prospect Contact Tags field on the Incident) 
  * Print Volume (optional; text field)
  * Notes (optional; multi-line plain text field; fills the standard Notes field on the Incident OR fills the existing Incident Notes memo - TBD; this field might be to the right of the other fields in a second column - TBD) 



TODO_TR

  


Clicking Continue would open a report that shows three panes (see below).

  


Report Details: 

Title: New Sales Opportunity

  


Left Pane: (shows Contacts in the Solution who are potential matches to the information entered in the prompt) 

Title: Matching Contacts for Prospect

  


Columns: 

  * Contact Name (link to record) 
  * Contact Phone (shows the phone number that matches the filter; otherwise, shows the primary number)
  * Contact Email (same as phone, but for email)



  


Grouped by: N/A 

  


Sorted by: The best match as follows:

  * 3 points for matching primary or secondary email
  * 3 points for matching primary or secondary phone
  * 1 point for matching first name
  * 1 point for matching last name



  


Top Right Pane: (shows existing Sales Opportunity Incidents for the selected contact in the left pane) 

Title: Sales Opportunities for Contact

  


Columns: 

  * ID 
  * Sales Opportunity (title; link to record)
  * Followup On 
  * Status Summary



  


Grouped by: Active (show at top), Inactive 

  


Sorted by: Sales Opportunity title

  


Bottom Right Pane: (shows existing Sales Opportunity Incidents with Prospect fields that match the information entered in the prompt)

  


Title: Matching Sales Opportunities for Prospect

  


Columns: 

  * ID 
  * Sales Opportunity (title; link to record)
  * Prospect First Name
  * Prospect Last Name
  * Prospect Business Name
  * Prospect Phone
  * Prospect Email



  


Grouped by: Active (show at top), Inactive 

  


Sorted by: The best match as follows:

  * 3 points for matching prospect email
  * 3 points for matching prospect phone
  * 1 point for matching prospect first name
  * 1 point for matching prospect last name



  


Menu Visibility: All users 

  


Buttons: 

  * New Prospect Opportunity (opens a new Sales Opportunity-type incident with the sales opportunity's fields filled in on the incident) 
  * New Customer Opportunity (works the same as "New Prospect Opportunity", except that it also links the selected Contact to the incident) 



  


Other Notes: N/A

  


Development Specification

Mockup (prompt): [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=135459352](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=135459352)

Mockup (report):  [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=2130002708](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=2130002708)

  


CCI: I'm thinking the New Customer Opportunity would be a button on the opportunities subpane.

  


DONE_CCI: Tim Reitz 07/01/2022: Client wishes to defer the New Sales Opp Prompt & Report for now. I'm planning to create a Change Request to save it for future reference. Also, the  Client wishes to remove the Location checkboxes, so I've updated the Requirements & mockup accordingly.

Ellis, could you update the Phase 1 price accordingly? Also, should I set the CR as T&M or Fixed Price (and what estimate/quote should I give it)?

DONE_TR: Pull out of proposal, create CR (with link to mockup)

Ellis Miller 07/02/2022: Pulled. Fixed Price for the next 6 months. $1450.

  


BID: 2 Days
