10.2.2. Triggered Process: "Set Proposal Results for Other Proposals in Family"

  


Requirements

  * Name: "Set Proposal Results for Other Proposals in Family":
    * Overview: Runs from a Proposal record to set the "Proposal Result" for other "Original" / "Revised" Proposals in the same "family" after the Proposal is marked as "Awarded". 
    * Initiated:
      * On the first Save after "Proposal Result" = "Awarded" on the Proposal record.
    * Priority: 1
    * Action(s): 
      * Sets the "Proposal Result" for other Proposals with the same "Numeric ID" portion of the Proposal # that match the following criteria: 
        * "Proposal Type" = "Original" and "Proposal Result" is currently set to blank or "Pending" and "Proposal Date" is in a different year than the newly-Awarded Proposal: Sets to "Lost"; 
        * "Proposal Type" = "Original" and "Proposal Result" is currently set to blank or "Pending" and "Proposal Date" is in the same year as the newly-Awarded Proposal: Sets to "Archived"; 
        * "Proposal Type" = "Revised" and "Proposal Result" is currently set to blank or "Pending" (regardless of the year of the "Proposal Date"): Sets to "Archived"; 
      * Note: No changes are applied to Proposals with the same "Numeric ID" portion of the Proposal # that match the following criteria: 
        * "Proposal Type" = "Original" or "Revised" and "Proposal Result" = "Awarded" (the Proposal that was just set to "Awarded" gets an error on Save - see corresponding spec); 
        * "Proposal Type" = "Original" or "Revised" and "Proposal Result" = "Lost"; 
        * "Proposal Type" = "Original" or "Revised" and "Proposal Result" = "Archived"; 
        * "Proposal Type" = "Change Order" 
    * Database Trigger to be Enabled: 
      * "Set Proposal Results for Other Proposals in Family"



  


Development Specification

Ellis Miller 06/06/2025: 

Set Proposal Results for Other Proposals in Family

[ ] x30 Trigger that finds the other items to change. 

[ ] Please assign Niccolas as a code reviewer.

6 Hours
