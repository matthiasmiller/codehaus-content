6.10.2. Incident - Schedule and Progress Section

New / updated spec for existing Schedule and Progress section (blue font represents changes to existing design / implementation):

  


  * Section is visible only if Type = Work Order



  


  * Left column: 
    * Scheduled (checkbox; defaults to unchecked; 
      * for non-child incidents: 
        * becomes read-only if checked and if time is tracked on the incident or a child incident; 
        * also becomes read-only if the Finished checkbox is checked; 
      * for child incidents, this field is always read-only and mirrors the parent incident's checkbox and date + time)
      * Note: moved from the existing Incidents section
    * Machine on Site (visible if Service Location is "Shop"; checkbox;
      * for non child-incidents:
        * editable for non-child incidents; 
        * defaults to unchecked;
        * warning on Save if blank and Stage is Pending, Work Schedule, and Assigned to Tech: "The machine is not marked as on site."
      * for child incidents:
        * read-only;
        * reflects the checkbox on the parent incident;
        * warning on Save if blank and Stage is Pending, Work Schedule, and Assigned to Tech: "The machine is not marked as on site. Check Machine on Site on the parent incident."  
    * QC Passed (checkbox plus username & date; used to track Quality Control approval and to advance a project to the Ready to Invoice stage; with the following behaviors:
      * for a non-child incident: 
        * visible if Scheduled checkbox is checked; 
        * editable if Stage = Quality Control or Ready to Invoice; 
        * when checked, the Incident advances to the "Ready to Invoice" Stage; 
        * if a parent, automatically becomes checked if all child incidents are manually checked;
        * if a parent, automatically becomes unchecked if any checked child incident is manually unchecked;
      * for a child incident: 
        * visible if Scheduled checkbox is checked;
        * editable if Stage = Quality Control or Ready to Invoice; 
        * automatically becomes checked if the parent is manually checked;
        * does not automatically become unchecked if the parent is manually unchecked;  
      * displays read-only username & date by the checkbox:
        * if the incident's checkbox was manually checked, displays in black text, showing the user who checked the box and the date;
        * if the incident's checkbox was automatically checked, displays in gray text, showing the user who checked the box of the incident that caused the current incident to auto-check and the corresponding date)
    * Finished (checkbox; with the following behaviors for non-child vs. child incidents:  
      * for non-child incidents: 
        * defaults to unchecked; 
        * when checked, displays read-only current date and time and clears the Projected Start Date and Calculated Finish Date; 
        * when checked, displays a pop-up message with the text from the "Work Order Finished Message" field in AppHosting.Zone Settings; 
        * becomes read-only when the Billed checkbox is checked or when the incident Status = Closed; 
      * for child incidents, this field is always read-only and mirrors the parent incident's checkbox and date + time)
    * Billed (checkbox; with the following behaviors for non-child vs. child incidents:
      * for non-child incidents: 
        * defaults to unchecked; 
        * when checked, displays read-only current date and time and sets the Incident Status to Closed;
        * is read-only when the incident Status = Closed;
      * for child incidents, this field is always read-only and mirrors the parent incident's checkbox)
    * Billed Hours (visible if the Billed checkbox is checked; auto-set and read-only;
      * for non-child incidents, displays the sum of the Incident Billed Hours fields on the Billed Hours RG;
      * for child incidents, displays the value of the corresponding row on the parent's Billed Hours RG)
    * Details (button; visible for non-child incidents if the Billed checkbox is checked; opens the Billed Hours Child Screen; see corresponding details) 



  


  * Billed Hours Child Screen: Used to store tracked work & travel time hours as of time that the Billed checkbox was checked; includes the following:  
    * Billed Hours (embedded spreadsheet with the following:  
      * Columns: 
        * Incident ID (displays the ID)
        * Incident Title (displays the Title)
        * View (displays as "Link"; link to open the corresponding incident)
        * Billed Work Hours (displays the value of the Actual Hours field for the incident at the time that the Billed checkbox was checked)
        * Billed Travel Time (displays the value of the Travel Time field for the incident at the time that the Billed checkbox was checked)
        * Incident Billed Hours (displays the sum of "Billed Work Hours" and "Billed Travel Time" for the row)
      * Automatically displays one row each for the parent incident and each child incident.
      * Automatically sorted by: Parent incident at the top, then all child incidents sorted by Incident ID
      * Show 10 rows without scrolling) 
    * Close (button to close the child screen) 



  


  * Center column: 
    * Estimated Hours (number field with the following behaviors:
      * for an independent incident:
        * visible if Scheduled checkbox is checked;
        * editable;
        * warning on Save if blank: "The Estimated Hours field is blank. Please enter an amount of Estimated Hours.");
      * for a parent incident:
        * visible if Scheduled checkbox is checked;
        * auto-set and read-only;
        * displays the sum of all Estimated Hours for Child Incidents;
        * must be empty to link a child incident - see details in the child incident spec below;
      * for a child incident:
        * visible if Scheduled checkbox is checked on the Parent Incident;
        * editable;
        * warning on Save if blank: "The Estimated Hours field is blank. Please enter an amount of Estimated Hours.") 
        * the new parent incident's Estimated Hours field must be empty. If there is a value in that field on the parent incident, show the following error message when saving the child incident: "The parent incident cannot have estimated hours when linked to a child incident. Open the parent incident and clear the Estimated Hours field to continue with linking.");
    * Actual Hours (visible if Scheduled checkbox is checked; auto-set and read-only;;
      * for independent incidents: dynamically displays the total hours tracked on the incident;
      * for parent incidents: dynamically displays the sum of all hours tracked on the incident and on all child incidents;
      * for child incidents: dynamically displays the total hours tracked on the incident) 
    * Service Runs (number field; visible only for non-child incidents; visible if Scheduled checkbox is checked and if Service Location is not Shop (or if there are Service Runs for the project); auto-set and read-only; dynamically displays the number of distinct Service Runs as tracked by Time Card rows; becomes frozen when the Billed checkbox is checked; this will count for the Parent Incident or any Child Incidents) 
      * Examples of distinct Service Runs:
        * Tech 1 tracked Service Run #1 on Monday and Service Run #1 on Tuesday. This would be 2 distinct Service Runs.
        * Tech 2 tracked Service Run #1 on Monday and two (e.g. Run #1 and Run #2) on Tuesday. This would be 3 distinct Service Runs.
        * Tech 1 and Tech 2 both tracked the same Service Run # on the same date for the same project. This would be treated as one Service Run. 
    * Incident Travel Time (number field to 2 decimal places; visible if Travel Time is assigned to the incident; becomes frozen when the Billed checkbox is checked; see calculation details in the "Tracking Service Runs" section; includes the following special behaviors:
      * if Override Travel Time is not checked: auto-set and read-only; dynamically displays the amount of Travel Time assigned to the incident
      * if Override Travel Time is checked: editable number field to 2 decimal places; defaults to the value that was in the read-only field; no validation against the total travel time for the day, etc.)
    * Override Travel Time (checkbox; visible if Travel Time is assigned to the incident; defaults to unchecked; when checked, the Travel Time field becomes editable; checkbox becomes read-only when the Billed checkbox is checked)
    * Project Travel Time (number field to 2 decimal places; auto-set and read-only; visible for non-child incidents if Travel Time is applied to the incident or a child of the incident; dynamically displays the sum of Incident Travel Times for the incident and all child incidents; becomes frozen when the Billed checkbox is checked)



  


  


  * Right column: 
    * Target Start Date (date field; manually set as an internal benchmark / commitment to the customer, and used for scheduling calculations; with the following behaviors:
      * for non-child incidents:
        * visible and required if the Scheduled checkbox is checked;  
        * defaults to blank;
        * error on Save if blank when the Scheduled checkbox is blank: "Target Start Date is blank";
        * the "Target Start Date" displays in red bold text if the entered date is in the past and no time has been tracked on the incident or a child incident) 
      * for child incidents: hidden)
    * Projected Start Date (date field with the following behaviors:
      * for non-child Incidents:
        * visible if Scheduled checkbox is checked;
        * auto-set and read-only;
        * displays the date that the project is expected to start, calculated based on the Calculated Finish Date for the last incident on the Assignee's schedule, the Weekly Shop Schedule and the Shop Schedule Override on the Assignee's Contact record, and the Estimated Hours for this project;
      * for child Incidents:
        * visible if the Scheduled checkbox on the Parent Incident is checked;
        * auto-set and read-only;
        * dynamically displays the Projected Start Date from the Parent Incident)
    * Actual Start Date (date field; auto-set and read-only; displays the first date that time was tracked on the Incident or a child Incident)
    * Calculated Project Finish Date (note: previously called Projected Finish Date) (auto-set and read-only; date field with the following behaviors: TODO_SG: Tim Reitz 04/11/2024: Do you want the calculations for project finish date vs. assignee finish date?
      * for non-child incidents:
        * visible if Scheduled checkbox is checked;
        * displays the date that the Project is expected to be completed, based on the Projected Start Date, the Weekly Shop Schedule and the Shop Schedule Override on the Assignee's Contact record, and Estimated Hours (for the entire project);
      * for child incidents:
        * visible if Scheduled checkbox is checked on the Parent Incident;
        * dynamically displays the Calculated Finish Date from the Parent Incident)
    * Calculated Assignee Finish Date (auto-set and read-only; date field with the following behaviors:
      * for non-child incidents:
        * visible if Scheduled checkbox is checked;
        * displays the date that the Assignee is projected to complete the portion of the entire project assigned to him, based on the Projected Start Date, the Weekly Shop Schedule and the Shop Schedule Override on the Assignee's Contact record, and total Estimated Hours for the incident(s) in the project that are assigned to the Assignee;
      * for child incidents:
        * visible if Scheduled checkbox is checked on the Parent Incident and if the Assignee on the child is different than the Assignee on the parent;
        * displays the date that the Assignee for the child is projected to complete the child incident assigned to him, based on the Projected Start Date, the Weekly Shop Schedule and the Shop Schedule Override on the Assignee's Contact record, and Estimated Hours for the child incident)
    * Project Finalization Date (date field; auto-set and read-only; with the following behaviors: 
      * for non-child incidents: 
        * visible if Scheduled checkbox is checked;
        * displays a calculated date based on the Calculated Finish Date for the project and the waiting hours (see details in the Scheduling Logic section of the proposal);  
      * for child incidents: 
        * visible if Scheduled checkbox is checked on the Parent Incident;
        * dynamically displays the Projected Finalization Date from the Parent Incident)



  


  * Other Notes:
    * Target Start Date vs. Due Date: The goal is to have the Target Start Date be the hard deadline for starting and the base for calculations; Due Date is more open ended and for reference purposes.


