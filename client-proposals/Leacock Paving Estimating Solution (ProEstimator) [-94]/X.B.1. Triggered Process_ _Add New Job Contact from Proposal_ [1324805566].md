10.2.1. Triggered Process: "Add New Job Contact from Proposal"

  


Requirements

  * Name: "Add New Job Contact from Proposal": 
    * Overview: Runs from a Proposal record to add a new Job Contact to the Job Contacts table on the Customer's Contact record, and then to update the Job Contact on the Proposal. 
    * Initiated:
      * On the first Save after "Job Contact" is set to "(New Job Contact)" on the Proposal record
    * Priority: N/A
    * Action(s): 
      * Takes the manually-entered details for the new Job Contact from the Proposal:
        * Stored Job Contact ID
        * Stored New Job Contact Name 
        * Stored New Job Contact Phone 
        * Stored New Job Contact Email 
      * Adds a new row to the Job Contacts table on the Customer's Contact record, setting the corresponding fields. 
      * Sets the "Job Contact" on the Proposal to the newly-added item on the Customer's record, looking at the "Job Contact ID" & "Stored Job Contact ID".
    * Database Trigger to be Enabled: 
      * "Add New Job Contact from Proposal"



  


Development Specification

Ellis Miller 06/06/2025: 

  


Add New Job Contact from Proposal - ASSIGN TO NIC

[ ] I'm thinking we might be able to set Contact to a new list item (e.g. NewContactFromProposal123456). Then use a trigger on save so that this this contact is updated to the correct information from the Proposal record. That way we don't have to modify the Proposal record again.

Niccolas Miller 09/26/2025: Instead, set job contact name via field change on save to new contact stored value. Trigger runs based on ProposalHasNewJobContact and adds the contact to the customer record. On next record save, stored fields are cleared.

Tim Reitz 09/29/2025: Any updates needed to the living spec for this? 

4 Hours
