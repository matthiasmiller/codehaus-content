5.3.12. Proposal - Job Scheduling Section

  


Requirements

  * Job Scheduling section (visible if "Proposal Result" = "Awarded"; note editability in Limited Editing Mode for fields in this section - see specs below):



  


  * Job Scheduled Start Date (optional; date; with the following details / behaviors:
    * editable in Limited Editing Mode; 
    * editable for users with the "Edit job scheduling" Permission; 
    * when set, the following field(s) are affected: 
      * "Job Scheduled": is checked;
      * "Group Scheduled Start Date": sets to the same date (all rows on the Groups embedded spreadsheet with "Group Awarded" checked);
    * when cleared, the following field(s) are affected: 
      * "Job Scheduled": is unchecked;
      * "Group Scheduled Start Date": is cleared (all rows on the Groups embedded spreadsheet with Group Awarded" checked);
    * warning on the first Save after this field has been changed to a non-blank value: "All "Awarded" Groups have been scheduled to the Job Scheduled Start Date. Review & update as needed, if there are any Groups to be done at a different time."; 
    * warning on the field if cleared: ""Scheduled Start Date" for all Awarded Groups has been cleared. If you wish to undo, please refresh the page."; 
    * note that this is used as an approximate reference point scheduling and sales reporting, possibly to be replaced by an actual "Project Start Date" in the future if that is added to this software solution) 



  


  *  Job Scheduled (auto-set and read-only; checkbox; with the following details / behaviors: 
    * can be set in Limited Editing Mode; 
    * set / cleared by the "Job Scheduled Start Date" field (see corresponding spec); 
    * this is used for tracking whether the job / Proposal has been added to the schedule for doing the work; 
    * note that when this is checked, all fields in the Customer Acceptance section are read-only) 



  


  * "All "Awarded" Groups have been scheduled to the Job Scheduled Start Date. Review & update as needed, if there are any Groups to be done at a different time." (on-screen message in orange font; visible until the first Save after "Job Scheduled Start Date" has been edited)



  


Development Specification

Ellis Miller 06/18/2025: 

Fairly straightforward.

[ ] For on screen and on save warning, just compare the value to the value in saved record on disk.

4 HOURS

  


Murshid Rahman 10/09/2025: Coded in [[PC0181550]] - ZLP - Records: Proposal - Job Scheduling Section
