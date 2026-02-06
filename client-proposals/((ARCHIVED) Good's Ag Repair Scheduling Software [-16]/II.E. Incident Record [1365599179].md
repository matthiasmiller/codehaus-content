2.5. Incident Record

Overview: The Solution will use the standard AppHosting Incidents record, with some customizations.

  


Accessed via: 

  * Good's Ag Repair | Incidents | New Incident
  * All Incidents report



  


Custom Sections and Fields: 

  * Incident section:
    * Assignee (optional; drop list of employees)
    * Shadow Assignee (optional; drop list of all employees; see corresponding section)
    * Scheduled (checkbox; defaults to unchecked)
    * Type (optional; user-editable drop list)
    * Service Location (optional; user-editable drop list)
    * Workflow (optional; drop list varies according to Type)
    * Stage (auto-set and read-only; set according to Scheduled checkbox)
      * If Scheduled checkbox is unchecked, Stage displays as "Pending" with the following message below it: "Check Scheduled and fill in due date."
      * If Scheduled checkbox is checked, Stage displays as "Scheduled" with the following message below it: "Track time in time card for this work order."



  


  * Schedule and Progress section (when the Scheduled checkbox is unchecked, displays as "Progress Section". When the Scheduled Checkbox is checked, displays as "Schedule and Progress"):
    * Finished (checkbox; defaults to unchecked; when checked, it displays the current date and time in read-only format; when checked, displays a message: "Thanks for your work!")
    * Actual Start Date (auto-set and read-only; displays the first date that time was tracked on the Incident)
    * Estimated Hours (visible if Scheduled checkbox is checked; number field)
    * Actual Hours (visible if Scheduled checkbox is checked; auto-set and read-only; displays the number of hours that were tracked on the Incident)
    * Projected Start Date (visible if Scheduled checkbox is checked; auto-set and read-only; displays the date when the Scheduled checkbox was checked)
    * Projected Finish Date (visible if Scheduled checkbox is checked; auto-set and read-only; displays the date that the Project is expected to be completed, based on the Due Date, Estimated Hours, and the Weekly Shop Schedule on the Assignee's record)
    * Finished: (checkbox; defaults to unchecked; when checked, displays read-only current date and time and removes the Projected Start Date and Projected Finish Date; when checked, displays the following message: Thanks for your work!)



  


  * Related Incidents section:
    * Parent Incident (link to corresponding parent incident; display as "(none)" if no parent incident is selected)
    * ... (button; opens a child screen that allows searching for Incident ID, Assignee, or text; shows a list of matching Incidents with an options for "None")
    * Incident Hierarchy (memo; displays the full hierarchy of incidents, include the parent and all the child incidents; current incident is bold)
    * New Child (link; opens a new Child Incident with the parent defaulted)



  


Data Access: All Users

  


Special Considerations: 

  * Copy Record: 
  * Delete Record: 
  * Merge Record: 



  


Other Notes:

  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).


