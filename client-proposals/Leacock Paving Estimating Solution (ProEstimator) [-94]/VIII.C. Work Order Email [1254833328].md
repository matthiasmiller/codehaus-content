8.3. Work Order Email

  


Requirements

Overview: This is an internal email that can be sent after a Proposal is marked as "Awarded". It is sent via the mailto feature, opening a draft in the user's default email platform, with the following items defaulted:

  


To: N/A (blank, to be set by the user in the email draft)

  


CC: N/A (blank, to be set by the user in the email draft if needed) 

  


BCC: N/A (blank, to be set by the user in the email draft if needed) 

  


Subject: "Work Order for Proposal #<Proposal #>"  (user can edit in the email draft if desired) 

  


Attachments: N/A (the mailto feature does not support automatically including attachments; the user can manually download the file from ProEstimator and attach it to the email draft) 

  


Body: <text specified in "Default Text for Work Order Email" in Silverloom Settings>  (user can edit in the email draft if desired) 

  


Other Notes:

  * If the user wishes to include any attachments (i.e. Proposal printout PDF, Work Order printout PDF), they must attach them manually.



  


Development Specification

Ellis Miller 06/17/2025: 

[ ] ProposalEmailLink_JobAwarded macro that calls GenerateEmailLink

1 HOUR
