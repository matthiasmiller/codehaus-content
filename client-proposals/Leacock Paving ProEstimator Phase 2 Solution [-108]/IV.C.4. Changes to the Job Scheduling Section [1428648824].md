4.3.4. Changes to the Job Scheduling Section

  


Requirements

This includes the following new items:

  


  * PA 1 Call - This tracks the utility locate request process (when it was requested, when it was completed, and when it expires) so crews don't show up to dig without clearance.
    * Needs PA 1 Call (checkbox; this specifies whether the job requires PA 1 Call services)
    * PA 1 Call Requested (checkbox + date, which toggle)
    * PA 1 Call Completed (checkbox + date, which toggle; when set, also sets "PA 1 Call Expiration Date", based on the "PA 1 Call Completed" date and the "PA 1 Call Expiration Window" in Silverloom Settings)
    * PA 1 Call Expiration Date (label displays "Expiration Date"; date; editable if uploaded)



  


  * Job Scheduling - This shows all scheduled calendar events for the job in one place, so you can see at a glance which crews are assigned and when work is happening. ("virtual" embedded spreadsheet of linked Calendar Event records with the following:
    * Columns: 
      * Crew 
      * Start Date
      * Multiday
      * End Date
      * Downtime
      * View ("Link") 



  


  * Add Calendar Event (button; opens a lightbox screen with prompts to create a new Calendar Event record: 
    * Job # (hidden; defaults to the "Proposal #" for the current Proposal record)
    * Groups (at least one selection is required; multi-select drop list of "Awarded", non-Scheduled Groups for the Proposal; defaults to all selected)
    * Schedule Prep (checkbox; if checked, shows following fields)
      * Start Date (required; date) 
      * Multiday (checkbox) 
      * End Date (visible and required if "Multiday" is checked; date) 
      * Crew (required; drop list of active "Prep"-type Crews) 
    * Schedule Paving (checkbox; if checked, shows the following fields)
      * Start Date (required; date) 
      * Multiday (checkbox) 
      * End Date (visible and required if "Multiday" is checked; date) 
      * Crew (required; drop list of active "Paving"-type Crews) 
    * Create Calendar Event (button; clicking this button runs the "Create Calendar Event" automatic process to create and link the new Calendar Event record(s) - see corresponding spec) 



  


  * Job Completed (checkbox + date, which toggle; date defaults to the current date when the checkbox is checked)
    * This is the trigger point - when the foreman checks this box, the office knows the job is ready for final review and invoicing.



  


Development Specification

Mockup: 

  * Main screen: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=569310505#gid=569310505](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=569310505#gid=569310505)
  * Child screen: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=2037082832#gid=2037082832](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=2037082832#gid=2037082832)



  


  


  


TODO_IDD: Tim Reitz 12/03/2025: (for client) How do you refer to the PA 1 Call?: "PA 1 Call" / "PA 1Call" / "PA One Call"?

  


TODO_IDD: Tim Reitz 12/04/2025: For the Calendar Event creation / child screen, consider whether we should have a 3rd option for a second round of paving (maybe "Schedule Initial Paving" / "Schedule Secondary Paving"). 

  


  * Job Completed



_HLD: Tim Reitz 12/03/2025: I'm thinking this date belongs on the Calendar Event / "Job" record, since it's event/phase-specific. Then maybe a macro on the Proposal record to show the last date?

Matthias Miller 12/03/2025: If you do this, then you need a macro to make sure that you make sure all items are signed off on on all time cards for all approved groups before considering it closed.

TODO_IDD: Tim Reitz 12/04/2025: Work on this.
