16.3.1. Request Reseller Transfer (Non-Upline)

*Done. 

  


  * Name: "Request Reseller Transfer (Non-Upline)"  
    * Description: User-initiated automatic process, initiated by non-upline providers on an Account record, to request a Reseller transfer for the Account.  
    * Prompts: 
      * See the prompts specced on the "Request Reseller Transfer (Non-Upline)" Child Screen -- initially "New Reseller" and "Reason / Comments". 
    * Initiated:
      * When the "Submit Transfer Request" button is clicked on the "Request Reseller Transfer (Non-Upline) Child Screen on the Account record.
    * Action(s): 
      * adds a row to the top of the "Account Reseller History" non-embedded spreadsheet for the corresponding Account, with the following set: 
        * "Requested By": sets to the user who initiated the Transfer Request; 
        * "Requested Date": sets to the current date;
        * "Reason / Comments": sets to the contents of the "Reason / Comments" prompt; 
        * "Prior Reseller": sets to the current "Account Reseller" for the Account;
        * "New Reseller": sets to the contents of the "New Reseller" prompt; 
        * "New Reseller Approval": if the "Requested By" user is the "New Reseller" (individual) or a "Reseller Rep" for the "New Reseller" (organization): sets to checked;
        * "New Reseller Approval User":  if the "Requested By" user is the "New Reseller" (individual) or a "Reseller Rep" for the "New Reseller" (organization): sets to the "Requested By" user;
        * "New Reseller Approval Date": if the "Requested By" user is the "New Reseller" (individual) or a "Reseller Rep" for the "New Reseller" (organization): sets to the current date; 
      * sends the "New Account Reseller Transfer Request" email - see corresponding spec)
    * Other Notes:
      * This automatic process can be run by any user (not limited to the users who can edit a specific Account record).


