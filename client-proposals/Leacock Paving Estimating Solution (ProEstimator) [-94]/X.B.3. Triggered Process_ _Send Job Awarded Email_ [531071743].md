10.2.3. Triggered Process: "Send Job Awarded Email"

  


Requirements

  * Name: "Send Job Awarded Email": 
    * Overview: Runs from a Proposal record to send the "Job Awarded" Email after a Proposal is marked as "Awarded". 
    * Initiated:
      * On the first Save after "Proposal Result" = "Awarded" on the Proposal record. 
    * Priority: 2
    * Action(s): 
      * Sends the "Job Awarded Email" - see corresponding spec
    * Database Trigger to be Enabled: 
      * "Job Awarded"



  


Development Specification

Ellis Miller 06/06/2025: 

Send Email Trigger

[ ] Add trigger. The work for the email is included elsewhere.

3 Hours
