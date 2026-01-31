3.2.3. Incident Record

  


Requirements

Overview: The Solution would use Incidents to track sales opportunities, on-site visits, tech support incidents (remote and on-site), and more. This makes it easy to track all customer interactions in a single view, track time and other expenses, and more.

  


This is AppHosting's existing Incidents module, with various customizations. This would allow for incorporating the existing incidents that Think Ink has created while using the base version of the Solution. 

  


Accessed via: 

  * New Incident menu option (opens a new incident with all blank fields)
  * New Sales Opportunity menu option & link on Contact record (see corresponding notes)
  * New Service Incident menu option & link on Contact record (see corresponding notes)
  * New Check-In Incident link on Contact record (see corresponding notes)
  * All Incidents Report
  * My Incidents Report



  


Incident Types: The Incident Type would be a required field on the Incidents. The following types would be used, and each may have one or more custom fields/sections: 

  * Sales Opportunity (standard type; used for documenting and tracking potential sales)
  * Service (used for tracking and documenting service calls, both in-person and remote)
  * Check-In (used for tracking and documenting customer check-ins; part of replacing Badger)
  * Internal (used for Think Ink internal matters such as to-do lists, one-off tasks, etc.) 



Note that these are intentionally limited to only a few types. 

  


The Think Ink incidents would hide the following standard fields:

  * Organization
  * Status Summary



  


Incidents of all Types would have the following Think Ink-specific sections:

  


Customer Details section: (custom section to the right of the standard sections; all fields auto-filled and read-only; based on the selected Contact for the incident)

  * Contact Tags (comma-separated)
  * Primary Address 
  * Primary Phone 
  * Fax 
  * Email (link to open email)



  


Device Details section: (custom section to the right of the standard sections; allows for tracking/linking devices with incidents) 

  * Device (optional; plain text field) 
    * Note that this is a plain text field for the initial phases, until the Device records are designed and developed, at which point this should change to a drop list of Device descriptions for the selected Customer.
  * Serial # (optional and editable if Device is blank; auto-filled and read-only if a Device is selected) 
    * Note that this allows the user to simply document a serial # without creating a Device record if the device is not already in the database.
    * Note that this is the design for the initial phases, until the Device records are designed and developed, at which point this should be auto-filled and read-only if a device is selected from the drop list.
  * New Device (to be added in a later phase; not included in Phase 1)



  


Customized behaviors for standard fields: 

  * Assignee (required; default to blank) 



  


Other customizations: 

  * New Incident (link at the right-hand side of the toolbar at the top of the screen; opens a blank new incident with no fields defaulted) 
  * The name of the Contact should appear after a dash in the section header bar for the "Incident" section. The format would be "Incident - <Contact Name>". 



  


Also include: 

  * Created (user ID, date, and time; auto-filled and read-only) 
  * Last Modified (user ID, date, and time; auto-filled and read-only) 
  * Modification History (link to report)



  


Data Access: All users can view and edit

  


Other Notes:

  * When an incident is closed, fields should remain editable.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=664971991](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=664971991)

  


First Section Title

We will include the Incident type and contact name in the Incident bar at the top. See mockup. We would use a Custom_IncidentFirstSectionTitle macro. 

BID: 1 hour

  


Hidden Fields

[ ] Consider hiding the organization field for non-legacy systems. [[PC0142986]] -- This is module maintenance, not part of this bid.

[ ] Add Config_IncidentShowStatusSummary switch that defaults to true and is overridden for them to false.

BID: 2 hours.

  


Customer Details

Bid: 2 hours

  


Device Details:

[ ] Name the fields IncidentDeviceStr and IncidentSerialNumStr because eventually we will have a IncidentDeviceID list field.

Bid: 1 hour

  


Customized Behavior:

[ ] Make Assignee required: Custom_IncidentRequireAssignee macro that can be overridden. We will override with true to always require.

[ ] Add a Custom_IncidentDetailTitle macro that can be overridden.

Bid: 4 hours 

  


TOTAL BID: 1.5 Days

_____________________________________________________________________

  


[[[IN5886](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-5888&)]] - ZTK - Adding Incident Tracking

BID: 2 CCI days to code [[PC0137494]]. Probably Seth

BID: 4 hours for CH to configure.
