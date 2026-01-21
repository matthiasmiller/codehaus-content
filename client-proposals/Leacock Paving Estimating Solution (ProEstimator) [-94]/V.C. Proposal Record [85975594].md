5.3. Proposal Record

  


Requirements

Overview: The Proposal record tracks details of a sales lead and subsequent proposal and job details. This is the main record in the Solution, which brings together details from Contacts, Sales Items, Automated Proposal Groups, and other manually-entered details. 

  


Accessed via: 

  * Proposal report(s)
  * Main Menu | Proposals | New Proposal (opens a new blank Proposal record) 
  * Main Menu | Leads | New Lead (opens a new blank Proposal record; separate menu option from "New Proposal" due to different users with different roles / workflows) 
  * etc.



  


Sections and Fields: The sections and fields for this record are specced out in subsections below.

  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (User ID, date, and time stamp) 
  * Last Modified: (User ID, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users
  * Editability:
    * If "Ready to Send to Customer" checkbox is not checked: Editable for all users 
    * If "Ready to Send to Customer" checkbox is checked: Only the following items remain editable (all other fields become read-only), utilizing the "Limited Editing Mode" feature (note that other editability conditions still apply): 
      * "Sales Rep" - see corresponding spec;
      * "Job Name" - see corresponding spec;
      * "Job Contact" - see corresponding spec;
      * All editable fields in the "Documentation" section - see corresponding spec;
      * The following fields / columns on the "Groups" embedded spreadsheet:
        * "Group Awarded" - see corresponding spec; 
        * "Group Awarded Date" - see corresponding spec; 
        * "Group Target Start" - see corresponding spec; 
        * "Group Scheduled Start" - see corresponding spec;
      * "Show All Columns" checkbox - see corresponding spec;
      * All editable fields in the "Customer Acceptance" section - see corresponding spec; 
      * All editable fields in the "Job Scheduling" section - see corresponding spec; 



  


  


Special Considerations: 

  * Copy Record: Copying is allowed at any time (does not prompt to Save). Additional details: 
    * When a Proposal record is copied, the following field(s) are cleared by default:
      * "Dismiss Items Message" checkbox
    * Buttons are provided to determine which fields should be changed after the Proposal record is copied (they may be cleared or changed). One of the buttons must be selected in order to save the new Proposal record, ensuring that it is set up properly. See button specs & "Copy Actions Details" spec for additional details. 
  * Delete Record: Allow deletion if "Status" = "Canceled" and the Proposal is not set as the "Source" for any other Proposal 
    * Validation error message: "Proposals can only be deleted if they are canceled and have not had another proposal copied from them."
  * Merge Record: N/A (disallowed)



  


  


Other Notes:

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * Note that the defaults listed in the Proposal record spec are for blank new Proposals (as specified on at least some field specs). Defaults for Proposals created via the Copy feature are specified in the "Copy Feature" spec. 
  * Custom: Section heading bars are light purple (RGB: 210, 200, 240) if "Proposal Type" = "Change Order". This is to make it easy for the user to clearly distinguish Change Orders from main Proposals. All other Proposals have the standard Silverloom blue heading bars.
    * Note that this color can be finalized once it is seen in the Solution. 
    * Note that Proposals reports could also include this light purple background for Change Order rows, if desired. This would be an additional customization.
  * Proposals that have been imported into the Solution are noted with a hidden field, and can be treated differently from Proposals that were manually created in the Solution.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=569310505#gid=569310505](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=569310505#gid=569310505) 

  


Ellis Miller 06/17/2025: 

[ ] Limited Editing: I'd recommend using ForceLimitedEditing=ReadyToSendToClient

  


[ ] Section headings: Create a ProposalSectionHeadingColor that is a Proposal-level macro.

BASIC RECORD TYPE: 2 HOURS

  


  


TODO_CCI: Tim Reitz 06/25/2025: Please let me know if there are any other fields that end up being cleared on copy, so that I can document them in the spec. Thanks!
