7.1. Configure Email Communications

  


Requirements

AppHosting will provide a template system to set up these email communications.

  


Each template will define:

  * Type, which is a choice of:
    * Contact
    * Member Applications
    * PDF Document (for tax information)
    * SPE Approvals
  * Subset (expression based on type, as well as the following checkboxes)
    * [ ]  Prompt for Contact Group (available for Contact and Member Application types)
    * [ ]  Respect Hold Solicitations Until Date (available for Contact and Member Application types)
    * [ ]  Prompt for Check Received Date (available for Member Applications only)
  * Reminder Date (expression based on type)
  * From (choice of contacts, filtered by those with login access)
  * Subject (template based on type)
  * Body (template based on type)
  * Attachments
    * PDF Attachments (memo)
    * [ ] Attach Redacted Tax Documents (visible for PDF Document)



  


All communications will be previewed before being sent.

  


Each record will track a history of past communications. This avoids sending duplicate communications. For example:

Communication Type| Sent On  
---|---  
  
|   
  
  
  


It will also show all relevant, unsent communications. For example:

Communication Type| Send On| Send Now  
---|---|---  
  
|   
| (Link)  
  
  


Some communications will not have a specific date or reminder. For those, the Send On column will be blank.

  


Development Specification

Ellis Miller 02/14/2021:

[ ] Expression Requirement fields don't support a dynamic target level (for validation or for evaluation). We have two options -- we can have clone fields (separate set of fields for each type) or we can pass the record ID into each of these as a string (if a numeric ID, it will just be the number as a string). There will be no validation that this is a valid record ID. The caller will need to do lookups with the ID for any field access.

Example:

Field: CommDefSubset

Level: None

DataType: Boolean

Parameter Name: vRecordID

Parameter Type: String

  


Sample expression:

LookupLevelField(vRecordID, ContactIsActive, Contacts)

  


[ ] The purpose of the date is to trigger a system reminder. It won't auto-send. This cannot reference record-specific information (e.g. we don't show different dates for different contacts)

  


[ ] I don't think we have a way to dynamically email attached documents, but we have talked about doing so for Triple-D, but never did. Bidding this at 5 days of C++ [[PC0030811]].  Also needed for the Attach redacted tax forms.

  


[ ] TODO_CH: The mockups don't include the two tables showed in the spec above. These will be at the bottom of each of the detail screens.

3 days.

  


[ ] Basic Communication Definition:

[ ] 4 Expression Field Requirements, including body. 3 Days

[ ] Other fields and detail screen: 3 Days

  


[ ] Email Template:

[ ] Repeat for List report on a Communication Definition

[ ] Repeat for List is a list of matching record ID's by applying subset and prompts and respect checkboxes. 3 days.

[ ] email templates are simple Evaluate calls on various fields. 2 days.

[ ] Attachments will take special attention using the C++ above. 2 days

  


[ ] Uncertainty: 4 Days
