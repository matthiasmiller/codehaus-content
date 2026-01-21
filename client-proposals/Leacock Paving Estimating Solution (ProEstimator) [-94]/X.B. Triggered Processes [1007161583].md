10.2. Triggered Processes

  


Requirements

Triggered Processes: The Solution contains the following automatic processes that are initiated via a trigger in the Solution:

  


Development Specification

Ellis Miller 06/06/2025: 

  


Add New Job Contact from Proposal - ASSIGN TO NIC

[ ] I'm thinking we might be able to set Contact to a new list item (e.g. NewContactFromProposal123456). Then use a trigger on save so that this this contact is updated to the correct information from the Proposal record. That way we don't have to modify the Proposal record again.

Niccolas Miller 09/26/2025: Instead, set job contact name via field change on save to new contact stored value. Trigger runs based on ProposalHasNewJobContact and adds the contact to the customer record. On next record save, stored fields are cleared.

Tim Reitz 09/29/2025: Any updates needed to the living spec for this? 

4 Hours

  


Send Email Trigger

[ ] Add trigger. The work for the email is included elsewhere.

3 Hours

  


Set Proposal Results for Other Proposals in Family

[ ] x30 Trigger that finds the other items to change. 

[ ] Please assign Niccolas as a code reviewer.

6 Hours

  


[ ] Tim Reitz 01/29/2025: Please send me the details about the x30s once you have them done, so that I can document them more completely in the living spec. Thanks!

_NM

_VA: Tim Reitz 10/31/2025: 

  * Add New Job Contact from Proposal
  * Job Awarded
  * Set Proposal Results for Other Proposals in Family



[X] Update the specs based on the current Snippet. 

Tim Reitz 11/03/2025: Done today.
