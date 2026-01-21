1.5.2.1. Incident Section

  


Requirements

New / updated spec for the existing Incident section (blue font represents changes to existing design / implementation): 

  * Top left column: 
    * Title (standard field) 
    * Status (standard field) 
    * Priority (standard field) 
    * Due Date (custom field)
      * Customizations:
        * If there is a child incident then the Due Date of the child is displayed in the parent incident (read-only) and the parent's Due Date field is hidden. If there are multiple child incidents, the largest of the the child incidents' Due Dates is displayed.
    * Type (standard field; optional; user-editable drop list)
    * Contact (standard field) 
    * Organization (standard field) 
    * Billable (standard field) 



  


  * Top right column: 
    * Status Summary (standard field) 
    * Assignee (standard field; optional; drop list of employees)
    * Shadow Assignee (custom field; optional; drop list of all employees)
    * Service Location (custom field; visible if Type = Work Order; user-editable drop list of Service Location; defaults to "Shop"; warning on Save if blank: "Service Location is blank."; if changed, field changes are handled by the individual fields)
    * Workflow (standard field; optional; drop list varies according to Type)
    * Stage (standard field with custom behaviors; auto-set and read-only;
      * for a non-child incident:
        * set according to the behaviors defined in the Incident Stage Record section of the proposal
      * for a child incident:
        * dynamically displays the Stage from the Parent Incident )
      * Note: Remove the note about tracking time that is displayed when Stage = Scheduled, since the stages are not dependent on time tracking anymore. 
    * Message in gray text:
      * For Parent and Independent incidents:
        * If Stage = "Pending": "Check Scheduled and fill in Target Start Date."
        * If Stage = "Work Schedule": "Assign this incident to a tech."
        * If Stage = "Assigned to Tech": "Check Finished when all the work for this project is done."
        * If Stage = "Quality Control": "Check QC Passed when all the work for this project is ready."
        * If Stage = "Ready to Invoice": "Check Billed when done."
      * For Child incidents:
        * If Stage = "Pending": "Go to the parent incident to check Scheduled and fill in Target Start Date."
        * If Stage = "Work Schedule": "Assign the parent incident to a tech."
        * If Stage = "Assigned to Tech": "Check Finished on the parent incident when all the work for this project is done."
        * If Stage = "Quality Control": "Check QC Passed when this incident is ready."
        * If Stage = "Ready to Invoice": "Check Billed on the parent incident when done."
    * Progress (visible if Type = Work Order and Stage = Assigned to Tech; drop list of "Job Progress" list items; when one is selected, also displays user + date + time by the field) 
    * Tags (standard button + field) 
    * Start (standard button; clicking this button starts tracking time for the current user on the current incident, with the following custom behaviors: 
      * If Service Location for the incident is "Shop": Starts time on the current incident (existing behavior)
      * If Service Location for the incident is not "Shop": Sets the prompts on the "Std Time Card Clock In" child screen as follows and starts time on the current incident (but does not display the child screen):
        * Time Card Category: current incident
        * Service Run: the most recently-selected Service Run on a Time Card row for the current day, or if none has been selected for the current day, defaults to "#1")
      * Error when a user tries to track time on an incident with the Billed checkbox checked (same error that is on the Time Card record). 
    * Stop (standard button)
    * Open Time Card (link; opens the current user's time card)
    * Switch (standard button, clicking this button opens the following child screen:
      * Std Time Card Clock In child screen:
        * Time Card Category (optional; drop list of all Doing and To Do incidents assigned to the current user + the current incident, if not assigned to the current user; this is standard behavior)
        * Service Run (custom for Good's Ag; visible if Service Location for the current incident is not "Shop"; drop list of Service Runs; defaults to the most recently-selected Service Run on a Time Card row for the current day, or if none has been selected for the current day, defaults to "#1") 
      * Error when a user tries to track time on an incident with the Billed checkbox checked (same error that is on the Time Card record). 
    * Archived Notes (standard button) 



  


  * Below the above columns:
    * Serial # (visible if Type = Work Order; editable for non-child incidents; read-only for child incidents, displaying the entry from the parent; plain text, long enough for 25 characters; warning on Save if blank and time has been tracked on the parent or one of the child incidents; warning message for the parent: "Serial # is blank."; warning message for a child: "Serial # is blank. Open the parent incident to set it.") 
    * Engine Serial # (visible if Type = Work Order; editable for non-child incidents; read-only for child incidents, displaying the entry from the parent; plain text, long enough for 25 characters; warning on save if blank and time has been tracked on the parent or one of the child incidents; warning message for the parent: "Engine Serial # is blank."; warning message for a child: "Engine Serial # is blank. Open the parent incident to set it.") 
    * Engine Hours (visible if Type = Work Order; editable for non-child incidents; read-only for child incidents, displaying the entry from the parent; plain text, long enough for 8 characters; warning on save if blank and time has been tracked on the parent or one of the child incidents; warning message for the parent: "Engine Hours is blank."; warning message for a child: "Engine Hours is blank. Open the parent incident to set it.") 
    * Separator Hours (visible if Type = Work Order; editable for non-child incidents; read-only for child incidents, displaying the entry from the parent; plain text, long enough for 8 characters; warning on save if blank and time has been tracked on the parent or one of the child incidents; warning message for the parent: "Separator Hours is blank."; warning message for a child: "Separator Hours is blank. Open the parent incident to set it.") 
    * Work Requested (label for existing incident body memo; warning on Save if blank and time has been tracked on the incident or one of the child incidents: "Work Requested is blank."; note that each parent and child will have their own field) 
    * Work Performed (visible if Type = Work Order; memo; warning on Save if blank and time has been tracked on the incident or one of the child incidents: "Work Performed is blank."; note that each parent and child will have their own field)



  


Development Specification

Ellis Miller 11/06/2023:

If you see a better way to arrange this, then we can consider that.

  


[ ] Service Location field

[ ] Progress Field 

Stage / Workflow handled in "Incident Stage Record"

Start / Switch buttons is handled in "Tracking Service Runs"

  


For Serial #, Engine Serial #, Engine Hours, Separator Hours#

[ ] Use a Stored____ field and a _____ macro to handle the child lookups. Put the validation on the macro

  


[ ] Add label above the normal memo

[ ] Add validation

  


[ ] Add new Work Performed memo

[ ] Add validation

  


BID: 1 Day
