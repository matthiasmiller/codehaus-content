5.3.3.5. Customer & Job Information Section - Lead Information Child Screen

  


Requirements

  * View Lead Information Child Screen (this child screen is opened via the "View Lead Information" button, and displays read-only versions of the fields in the "Lead Information" section on the main screen, as well as the "View / Edit Lead Information on Main Screen" checkbox)



  


  * View / Edit Lead Information on Main Screen (checkbox; with the following details / behaviors: 
    * defaults to checked for new records, both blank and copied; 
    * automatically becomes unchecked on Save (both the initial Save, and any subsequent Saves if checked); 
    * checkbox also can be manually checked or unchecked; 
    * when checked, the "Lead Information" section is visible on the main screen, for the user to be able to make changes if needed; 
    * when not checked, the corresponding fields are hidden on the main screen) 
  * Lead Information Display (no label; read-only display of all Lead Information details; note that this is the same as the contents of the Lead Information printout - see corresponding spec)



  


Development Specification

Mockup (included in the "Additional Items for Proposal Record" mockup tab): [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=2037082832#gid=2037082832](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=2037082832#gid=2037082832)

  


Ellis Miller 06/18/2025: 

[ ] View / Edit checkbox -- see design above.

[ ] Use a RichTextExpression with ProposalFormattedLeadInfo from the Lead Info Printout.
