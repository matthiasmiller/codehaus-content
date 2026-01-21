6.2.1. Incident Section

TODO_: Tim Reitz 12/13/2024: Needs standardization. 

  


  


Incident Section: Section heading label is "Incident" at the left corner and **unsaved** (for an unsaved record) at the right end. **unsaved** is replaced by "[[IN0001]]" ID when the record is saved. ID is incremental.  

  


Fields:

  * Title
    * String field.
    * Editable only in detail screen.
    * Shows "Title cannot be empty." if blank while saving the record.



  


  * Status - 
    * Shows list of "To Do|Doing|Done".
    * Required field.
    * Shows "The Assignee is required for incidents with a "Doing" status." while saving the record if the status is set to Doing and Assignee is blank.
    * Check Closed checkbox and set the closed date to Today if the status is set to Done.
    * Added in 



  


  * Status Summary
    * Editable string field.
    * Visible if Custom_IncidentStatusSummaryVisible macro is true.



  


  * Priority 
    * Shows list of priorities.
    * Editable in detail screen only.



  


  * Assignee
    * Shows list of active contacts



  


  * Due Date 
    * Date field.



  


  * Additional Assignees 
    * Multi selection list of active contacts
    * Shows active contact list removing selected Assignee.



  


  * Type -- 
    * User-configurable list of options
    * Shows "Before saving a new incident, set the incident type to an incident type you have permission to edit." error message while saving a new record if type not set and if the current user does not have permission to edit type.



  


  * Workflow



  


  * Contact
    * Shows list of active contacts.
    * Visible if Config_IncidentSupportContacts system switch is true.



  


  * Tags
    * RG field



  


  * Organization
    * Shows list of organizations.
    * Visible if Config_IncidentSupportContacts and Config_IncidentShowOrganization are true.



  


  * Billable
    * Checkbox
    * Adds "to <Contact> with <Organization> if contact and organization are entered.



  


  * Billing Details
    * Child detail screen with below fields
      * Bill to Contact
        * Shows list of contacts.
      * Bill to Organization
        * Shows list of Organizations.
    * View Hours
    * Table with below columns
      * Employee
      * Hourly rate
      * Combined Billable Hours
      * Combined Total
    * Total Worked - shows total work
    * Reset Rates - resets the entered hourly rate



  


  * Start - button
    * Opens an ask prompt
    * Shows "Time Card Category" list options on the ask prompt



  


  


  * Open Time Card
    * Link to open the time card detail screen.



  


  * Archive Notes
    * Button
    * Opens a memo.



  


  * Memo
    * Editable memo.



  


  * Generate PDF
    * Link to open the incident in pdf.



  


  * Export to Word
    * Link to open the incident in word.


