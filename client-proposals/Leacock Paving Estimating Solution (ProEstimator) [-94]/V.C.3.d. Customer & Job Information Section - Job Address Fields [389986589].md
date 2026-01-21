5.3.3.4. Customer & Job Information Section - Job Address Fields

  


Requirements

  * Use Customer Address for Job (checkbox; with the following details / behaviors:
    * when checked, the following fields are affected:
      * "Job Address": sets to the "Address" (line 1) of the Primary address on the Customer's Contact record at the time that the checkbox is checked;
      * "Address Line 2": sets to the "Address 2" of the Primary address on the Customer's Contact record at the time that the checkbox is checked; 
      * "City": sets to the "City" of the Primary address on the Customer's Contact record at the time that the checkbox is checked; 
      * "State": sets to the "State" of the Primary address on the Customer's Contact record at the time that the checkbox is checked; 
      * "Zip": sets to the "Zip" of the Primary address on the Customer's Contact record at the time that the checkbox is checked)
  * Job Address (this is "Line 1" of the address; plain text field; with the following details / behaviors: 
    * if "Use Customer Address for Job" is checked: read-only; see checkbox spec; 
    * if "Use Customer Address for Job" is not checked: editable and required; defaulting to blank for new blank Proposals)
  * Address Line 2 (no label; plain text field; with the following details / behaviors: 
    * if "Use Customer Address for Job" is checked: read-only; see checkbox spec;
    * if "Use Customer Address for Job" is not checked: editable and optional; defaulting to blank for new blank Proposals)
  * City (no label; plain text field; with the following details / behaviors: 
    * if "Use Customer Address for Job" is checked: read-only; see checkbox spec;
    * if "Use Customer Address for Job" is not checked: editable and required; defaulting to blank for new blank Proposals)
  * State (no label; drop list of US state & territory abbreviations; with the following details / behaviors: 
    * if "Use Customer Address for Job" is checked: read-only; see checkbox spec;
    * if "Use Customer Address for Job" is not checked: editable and required; defaulting to blank for new blank Proposals)
  * Zip (no label; plain text field; with the following details / behaviors: 
    * if "Use Customer Address for Job" is checked: read-only; see checkbox spec;
    * if "Use Customer Address for Job" is not checked: editable and required; defaulting to blank for new blank Proposals)



  


Development Specification

Ellis Miller 06/17/2025: 

[ ] ProposalUseCustomerAddress is a visible checkbox

  


[ ] Add hidden stored address fields:

[ ] ProposalStoredJobAddr1

[ ] ProposalStoredJobAddr2

[ ] ProposalStoredJobState

[ ] ProposalStoredJobCity

[ ] ProposalStoredJobZip

  


[ ] Add conditionally editable macros that either return contact information (if UseCustomerAddress) or return stored fields.

[ ] ProposalJobAddr1

[ ] ProposalJobAddr2

[ ] ProposalJobState

[ ] ProposalJobCity

[ ] ProposalJobZip

2 Hours
