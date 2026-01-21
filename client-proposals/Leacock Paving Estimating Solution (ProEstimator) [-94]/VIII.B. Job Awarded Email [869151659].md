8.2. Job Awarded Email

  


Requirements

Overview: This is an internal email that is sent after a Proposal is marked as "Awarded". It is sent via the "Send Job Awarded Email" Automatic Process (see corresponding spec) when a Proposal is marked as "Awarded". It includes following items (which cannot be edited on a per-sending basis, since this is automatically sent):

  


From: <the email address specified in the "From" email address for notifications" System Switch>

  


To: <email address specified in "Default Recipient for Job Awarded Email" in Silverloom Settings> 

  


CC: N/A 

  


BCC: N/A 

  


Reply To: N/A

  


Subject: "Job Awarded! (<"Job Name">)" 

  


Attachments: N/A

  


Body: <text specified in "Default Text for Job Awarded Email" in Silverloom Settings> 

  


Other Notes:

  * N/A



  


Development Specification

Ellis Miller 06/17/2025: 

[ ] ProposalEmailLink_JobAwarded macro that calls GenerateEmailLink

1 HOUR
