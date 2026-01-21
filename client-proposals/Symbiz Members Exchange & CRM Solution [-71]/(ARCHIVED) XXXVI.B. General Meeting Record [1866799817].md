36.2. General Meeting Record

  


Requirements

_VA: Tim Reitz 07/10/2025: This needs to be removed now, along with all other references.

  


Tim Reitz 07/10/2025: Removed in [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)

  


\----------

  


Note: This is being replaced by the Events record / feature, to accommodate the Annual Summit, Industry Summits, Info Meetings, and Launch Meetings.  

  


Overview: This record can be used to set up and track details for meetings (not Growth Ring-specific). 

  


Accessed via: 

  * General Meetings Report
  * Admin | General Meeting Management | New General Meeting



  


Sections and Fields: 

  * General Meeting Overview section: 
    * Meeting Status (read-only; displays in the section header; options are Scheduled, Complete, Canceled:)
      * Scheduled: if the Meeting Date = the current date or in the future.
      * Complete: if the Meeting Date is in the past.
      * Canceled: if the Meeting Canceled checkbox is filled.
    * Meeting ID (auto-set and read-only; unique identifier for the record)
    * Meeting Canceled (checkbox; defaults to cleared; if filled, Meeting Status is set to Canceled; note that fields on the record will still be editable)
    * Meeting Description (required; plain text field)
    * Industry-Specific (checkbox)
    * Industry (visible and required if Industry-Specific; multi-select drop list of Industries) 
    * Meeting Date (required; date)
    * Meeting Type (required; drop list of In-Person / Virtual / Hybrid; defaults to blank) 
    * Meeting Recording (optional; field for pasting in a recording link stored on another platform; for users who can edit the record, this becomes a clickable link that opens the recording if the user clicks the Stop Editing button; for users who cannot edit the record, this displays as a clickable link) 



  


  * In-Person Meeting Details section (visible if Meeting Type = In-Person or Hybrid): 
    * Location (optional; plain text; can be used to track the name of the location)
    * Street Address (required)
    * City (required) 
    * State/Province (required)
    * Zip (required)



  


  * Virtual Meeting Details section (visible if Meeting Type = Virtual or Hybrid): 
    * Meeting Link (required; field for pasting in a meeting link; for users who can edit the record, this becomes a clickable link to open the meeting if the user clicks the Stop Editing button; for users who cannot edit the record, this displays as a clickable link) 



  


Data Access: See the Data Access Controls section of the proposal for details.

  


Special Considerations:

  * Copy Record: Clear the Meeting ID
  * Delete Record: Prevent deletion if Status is not Canceled (error message: "This General Meeting record cannot be deleted because its Status is not Canceled.")
  * Merge Record: Only can be merged by Super Admins.



  


Other Notes:

  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

TODO_VA: Deactivate this section when we bring in the Events feature. See the separate new proposal: [https://zch.apphosting.zone/Detail/Edit/2?RecordType=ClientProposals&NumberID=-86&StateID=p6ekG6ZUTH9U&ShowTitleBar=true&State=ISwSvCyE0ts&#](https://zch.apphosting.zone/Detail/Edit/2?RecordType=ClientProposals&NumberID=-86&StateID=p6ekG6ZUTH9U&ShowTitleBar=true&State=ISwSvCyE0ts&#)

  


  


Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1812568055](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1812568055)

  


For reference, view: [https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=795%3A4797&node-id=882%3A6546&viewport=-1359%2C-478%2C0.26&scaling=min-zoom&starting-point-node-id=806%3A4917](https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=795%3A4797&node-id=882%3A6546&viewport=-1359%2C-478%2C0.26&scaling=min-zoom&starting-point-node-id=806%3A4917)
