7.3.1.4. Account Overview - Request Reseller Transfer On-Screen Prompt

*Done. 

  


The following are visible with a gray background when the "Request Reseller Transfer" button is clicked (see corresponding spec): 

  


  * Cancel Transfer Request (button; visible in the location of the "Request Reseller Transfer" button if "Reseller Transfer Mode" checkbox is checked, 
    * when clicked, the following field(s) are affected: 
      * "Reseller Transfer Mode": sets to not checked, which the makes the "Request Reseller Transfer On-Screen Prompt" hidden, causing the data entry fields to be cleared)  
  * New Reseller (visible if "Reseller Transfer Mode" checkbox is checked; required; drop list of all active Account Resellers; defaults to blank) 
  * Reason / Comments (visible if "Reseller Transfer Mode" checkbox is checked; required; plain text field; defaults to blank) 
  * Submit Transfer Request (visible if "Reseller Transfer Mode" checkbox is checked; button; with the following details / behaviors: 
    * when clicked with required data entry fields filled, a row is added to the top of the "Account Reseller History" non-embedded spreadsheet with the following set: 
      * "Reason / Comments": sets to the contents of the "Reason / Comments" data entry field; 
      * "Prior Reseller Approval": if the user submitting the request is the "Prior Reseller" (individual) or a "Reseller Rep" for the "Prior Reseller" (organization): sets to checked;
      * "Prior Reseller Approval User": if the user submitting the request is the "Prior Reseller" (individual) or a "Reseller Rep" for the "Prior Reseller" (organization): sets via the "Set Prior Reseller Approval" Shared OnChange Action - see corresponding spec;
      * "Prior Reseller Approval Date": if the user submitting the request is the "Prior Reseller" (individual) or a "Reseller Rep" for the "Prior Reseller" (organization): sets via the "Set Prior Reseller Approval" Shared OnChange Action - see corresponding spec;
      * "New Reseller": sets to the contents of the "New Reseller" data entry field; 
    * on the first Save after this button is clicked and a new row is added, the "New Account Reseller Transfer Request" email is sent - see corresponding spec)


