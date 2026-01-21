5.2.3. Contact - Customer Details Section

  


Requirements

The Contact record also includes the following custom section and fields: 

  


  * Customer Details section (visible if "Contact Type" includes "Customer"):
    * Preferred Contact Method (optional; drop list of "Customer Contact Methods" list items; warning on Save if blank: "Customer Contact Method is blank.") 
    * Job Contacts (embedded spreadsheet with the following; used for tracking points of contact for the Customer, such as estimators or managers for a commercial customer:
      * Columns: 
        * Name (required; plain text)
        * Phone (phone number field, validating the entry is 10 digits long, and auto-formats to standard phone number format; warning on the initial Save after adding if blank: "Job Contact phone number  is missing: <JobContactNames>") 
        * Email (email field, validating that the entered text is in a valid email format; warning on the initial Save after adding if blank: "Job Contact email is missing: <JobContactNames>")  
        * Active (checkbox; defaults to checked; if unchecked, the text for the row changes to gray font and the row is moved below the active rows) 
        * Job Contact ID (hidden column/field; row ID field; with the following details / behaviors: 
          * for manually-added rows: auto-sets to a random number;
          * for rows added via the "Add New Job Contact from Proposal" automatic process (from the Proposal): sets to the value of the "Stored Job Contact ID" field there) 
      * Automatically sorted by:
        * First by: Active / Inactive
        * Second by: Name (alphabetically)
      * Buttons to append/remove rows: "✚" / "🞭" 
        * The "🞭" button is disabled when a row is selected for a Job Contact that is set as the "Job Contact" for one or more Proposal records (this is to prevent deleting data that is referenced on other records.) 
      * Show 6 rows without scrolling 
      * Other Notes: 
        * Rows can be added via the "Add New Job Contact from Proposal" automatic process (see corresponding spec), based on details entered on a Proposal record. 
    * Proposals for Customer (link; opens the "Proposals for Customer" report, filtered to the corresponding Contact - see corresponding spec)



  


Development Specification

Ellis Miller 06/10/2025:

[ ] Field

[ ] RG

[ ] To do warning on initial save, if you are missing phone/email, do a lookup on disk to see if if the name is in the RG and missing the phone there as well.

[ ] Add validation against deleting RG row if the contact ID is referenced. Will need a ProposalsByJobContactID.ndx.

5 Hours

  


_CCI: Tim Reitz 02/04/2025: Per Ellis, ask John Allan how to do the row ID if we want to sometimes set it from the Proposal record.
