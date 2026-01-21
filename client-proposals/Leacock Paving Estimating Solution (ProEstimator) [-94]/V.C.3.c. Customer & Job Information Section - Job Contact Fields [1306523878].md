5.3.3.3. Customer & Job Information Section - Job Contact Fields

  


Requirements

  * Job Contact (drop list of options; with the following details / behaviors:
    * required if "Proposal Result" = "Awarded";
    * drop list includes the following items in the following sequence: 
      * all "Active" Job Contacts from the selected Customer's Contact record, in the following format: "<Name> \- <Phone> \- <Email>", and 
      * "(Use Customer as Contact)", and
      * "(New Job Contact)"; 
    * note that when the "Customer" field for the Proposal is set, this sets to blank, unless there is only one item in the "Job Contacts" table on the selected Customer's Contact record, in which case it defaults to that item; 
    * when a Job Contact item from the Customer's Contact record is selected, only the "Name" is displayed on the field (i.e., the " \- <Phone> \- <Email>" portion is displayed only when the drop list is opened); 
    * when "(Use Customer as Contact)" is selected, the "Short Display Name" is displayed on the field (i.e., "Use Customer as Contact" is displayed only when the drop list is opened); 
    * when changed, the following field(s) are affected: 
      * when set to a Job Contact item from the Customer's Contact record:
        * "Stored Job Contact ID": sets to the "Job Contact ID" for the selected Job Contact (from the Job Contacts embedded spreadsheet);
        * "Customer is Job Contact": becomes unchecked if previously checked; 
      * when set to "(Use Customer as Contact)":
        * "Stored Job Contact ID": clears if previously set;
        * "Customer is Job Contact": becomes checked; 
      * when set to "(New Job Contact)":
        * "Stored Job Contact ID": sets to a random number, resetting if previously set (used to facilitate the "Add New Job Contact from Proposal" automatic process);
        * "Customer is Job Contact": becomes unchecked if previously checked; 
    * when the "(New Job Contact)" option is selected, the below "Job Contact" fields become editable and required, then on the following Save, the "Add New Job Contact from Proposal" automatic process runs (see corresponding spec), after which the below fields become read-only again, displaying the details for the newly-selected Job Contact; 
    * editable in limited editing mode)



  


  * Stored Job Contact ID (hidden numeric field; with the following details / behaviors:
    * automatically sets/clears based on "Job Contact" \- see corresponding spec; 
    * used for linking & for reports/printouts) 
  * Customer is Job Contact (hidden field; checkbox; with the following details / behaviors:
    * automatically checks/unchecks based on "Job Contact" \- see corresponding spec;
    * used for linking & for reports/printouts) 
  * Stored New Job Contact Name (label displays as "New Job Contact Name"; visible and required if "Job Contact" = "(New Job Contact)"; plain text; used to facilitate the "Add New Job Contact from Proposal" automatic process)
    * editable in limited editing mode)



  


  * Job Contact Phone (macro; with the following behaviors:
    * if "Job Contact" ≠ "(New Job Contact)": read-only; dynamically displays the primary (top) phone number for the selected Job Contact; 
    * if "Job Contact" = "(New Job Contact)": displays & sets the "Stored New Job Contact Phone" hidden field (see corresponding spec); optional; validates that the entry is 10 digits long - error on change if not: "Phone must be 10 digits long."; auto-formats to standard phone number format)
    * editable in limited editing mode)
  * Job Contact Email (macro; with the following behaviors:
    * if "Job Contact" ≠ "(New Job Contact)": read-only; dynamically displays the top Primary email address for the selected Job Contact, as a link to open a new email with the email address defaulted;
    * if "Job Contact" = "(New Job Contact)": editable; displays & sets the "Stored New Job Contact Email" hidden field (see corresponding spec); validates that the entered text is in a valid email format - error on change if not: "Email must be in valid format.")
    * editable in limited editing mode)



  


  * Stored New Job Contact Phone (hidden stored field; phone number field; used to facilitate the "Add New Job Contact from Proposal" automatic process)
  * Stored New Job Contact Email (hidden stored field; email field; used to facilitate the "Add New Job Contact from Proposal" automatic process)



  


Development Specification

Job Contact - FOR NICCOLAS

We will use a trigger import to add the contact to the record.

  


[ ] Job Contact - use Complex helper list 

[ ] two non-contact options

[ ] Need to parse out name and find matching ID

  


[ ] Add a hidden ProposalJobContactID field that will have a value from the Customer's Job Contacts RG (or a new value for a new record).

  


[ ] Add an empty ProposalJobContactEntry macro and place it on the detail screen

  


[ ] We have a ProposalCustomerIsJobContact

  


[ ] Create a ProposalHasNewJobContact macro that checks whether we have a JobContactID that is not on the Contact record.

  


[ ] Use fields to store new contact info:

[ ] ProposalStoredNewJobContactName - This one is visible for entry if HasNewJobContact

[ ] ProposalStoredNewJobContactPhone - hidden, set by OnChange

[ ] ProposalStoredNewJobContactEmail - hidden, set by OnChange

  


[ ] We have JobContact macros that are conditionally editable (if IsNewJobContact). Add OnChange statements to set the underlying stored field.

[ ] ProposalJobContactPhone - Special: Phone

[ ] ProposalJobContactEmail - Special: Email

  


[ ] Add Field Change statements to clear out all of these values on the first save after the trigger import ran. Just use a Condition: NOT HasNewJobContact to clear all stored new fields.

[ ] ProposalStoredNewJobContactName 

[ ] ProposalStoredNewJobContactPhone

[ ] ProposalStoredNewJobContactEmail 

BID: 6 hours (without trigger)
