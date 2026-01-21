8.1. Proposal to Customer Email

  


Requirements

Overview: This is an email that is sent to the Job Contact for a Proposal, as an official submission of the Proposal for consideration and acceptance. It is sent via the mailto feature, opening a draft in the user's default email platform, with the following items defaulted:

  


To: <"Job Contact Email" for the Proposal> (user can set other To: addresses in the email draft if desired) 

  


CC: N/A (blank, to be set by the user in the email draft if needed) 

  


BCC: N/A (blank, to be set by the user in the email draft if needed) 

  


Subject: "Proposal for "<"Job Name">" Project" (user can edit in the email draft if desired) 

  


Attachments: N/A (the mailto feature does not support automatically including attachments; the user can manually download the file from ProEstimator and attach it to the email draft) 

  


Body: <text specified in "Default Text for Proposal to Customer Email" in Silverloom Settings> (user can edit in the email draft if desired) 

  


  


Other Notes:

  * This normally should include the Proposal printout PDF, which the user must attach manually.



  


Development Specification

Ellis Miller 06/17/2025: 

[ ] ProposalEmailLink_ToCustomer macro that calls GenerateEmailLink

1 HOUR
