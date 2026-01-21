16.3.2. Approve Reseller Transfer (Non-Upline)

*Done. 

  


  * Name: "Approve Reseller Transfer (Non-Upline)": 
    * Description: User-initiated automatic process, initiated by non-upline "New Reseller" providers on an Account record, to approve a Reseller transfer for the Account. 
    * Prompts: 
      * N/A
    * Initiated:
      * When the "Approve Transfer Request" button is clicked on the Account record.
    * Action(s): 
      * sets the following fields on the top row of the "Account Reseller History" non-embedded spreadsheet for the corresponding Account:
        * "New Reseller Approval": sets to checked;
        * "New Reseller Approval User": sets to the "User ID" for the user who clicked the button; 
        * "New Reseller Approval Date": sets to the current date; 
        * "Transfer Complete Date": if "Prior Reseller Approval" is already checked, sets to the current date (otherwise, N/A))
    * Other Notes:
      * This automatic process can be run by any user (not limited to the users who can edit a specific Account record).


