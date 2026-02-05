7.3.1.2. Account Overview - Account Reseller Fields

*Done. 

  


  * Account Reseller (macro; with the following details / behaviors: 
    * if there are no rows on the "Account Reseller History" non-embedded spreadsheet (i.e. for brand new Account records):
      * required; 
      * drop list of all active Account Resellers (Contacts with the "Is Account Reseller" checkbox checked);
      * defaults to:  
        * if the creating user is an "Account Reseller" or a "Reseller Rep": defaults to the Contact for the "Account Reseller"; 
        * otherwise: defaults to blank; 
      * when set, the following field(s) are affected:
        * a row is added to the "Account Reseller History" non-embedded spreadsheet, with the following fields set:
          * "Account: set to the current Account;
          * "Requested By": set to the current user;
          * "Requested Date": set to the current date;
          * "Reason / Comments": set to "Initial Reseller for Account";
          * "New Reseller": set to the selection in this drop list;
          * "Transfer Complete Date": set to the current date; 
      * note that this immediately becomes read-only when set (see spec below), meaning that if it is set incorrectly, the user must either refresh the screen before saving or request a transfer to change it; 
    * if there is at least one row on the "Account Reseller History" non-embedded spreadsheet (i.e. the editable macro has been set, either manually or defaulted, at which point the Reseller Transfer feature must be used):
      * read-only;
      * displays the following:
        * if "Transfer Approved" checkbox is checked for the top row: displays the "New Reseller" from the top row of the "Account Reseller History" non-embedded spreadsheet - see corresponding spec, and see the spec for the "Request Reseller Transfer" feature); 
        * if "Transfer Approved" checkbox is not checked for the top row: displays the "New Reseller" for the second-from-the-top row;
      * displays as a link to open the selected record) 
  * Account Reseller Phone (label displays as just "Phone"; read-only macro; displays the primary Phone number for the selected "Account Reseller" Contact; link to dial the number directly, if the user has that capability on their device) 
  * Account Reseller Email (label displays as just "Email"; read-only macro; displays the primary Email address for the selected "Account Reseller" Contact; link to open an email draft with the "To:" defaulted in the user's default email client)
  * Account Reseller Address (label displays as just "Address"; read-only macro; displays the primary Address for the selected "Account Reseller", in the standard multi-line format without the addressee name)



  


  * Request Reseller Transfer (Upline) (label displays as "Request Reseller Transfer"; button; with the following details / behaviors:
    * visible in Edit Mode after the initial Save to "Upline Provider Roles" users (users who can edit the Account) if the top row in the "Account Reseller History" non-embedded spreadsheet has the "Transfer Complete" checkbox checked (i.e. if there is not a pending transfer in progress); 
    * when clicked, the following field(s) are affected:
      * "Reseller Transfer Mode": set to checked, which makes the "Request Reseller Transfer On-Screen Prompt" visible - see corresponding specs)
  * Reseller Transfer Mode (hidden; checkbox; with the following details / behaviors:
    * set to checked via the "Request Reseller Transfer" button (making the transfer fields visible) and unchecked via the "Cancel Transfer Request" or "Submit Transfer Request" buttons (hiding the transfer fields) - see corresponding specs; 
    * error on Save if this checkbox is checked: "Account cannot be saved while Reseller Transfer is in progress."; this prevents data from being saved in the transfer fields) 



  


  * "A Reseller Transfer has been requested for this account." (on-screen message in green font; visible if there is a row in the "Account Reseller History" non-embedded spreadsheet with the "Transfer Complete" checkbox not checked; displays in the location of the "Request Reseller Transfer" button) 



  


  * Request Reseller Transfer (Non-Upline) (label displays as "Request Reseller Transfer"; button; with the following details / behaviors:
    * visible out of Edit Mode to non-"Upline Provider Roles" users (users who cannot edit the Account) if the top row in the "Account Reseller History" non-embedded spreadsheet has the "Transfer Complete" checkbox checked (i.e. if there is not a pending transfer in progress); 
    * when clicked, opens the "Request Reseller Transfer (Non-Upline)" child screen -- see corresponding spec)
  * Approve Reseller Transfer (Non-Upline) (button; label displays as "Approve Reseller Transfer"; with the following details / behaviors:
    * visible out of Edit Mode to the "New Reseller" (if individual) or a "Reseller Rep" for the "New Reseller" Contact (if organization) if the top row in the "Account Reseller History" non-embedded spreadsheet has the "Transfer Complete" checkbox not checked (i.e. if there is a pending transfer in progress);
    * when clicked, runs the "Approve Reseller Transfer (Non-Upline)" user-initiated automatic process -- see corresponding spec)



  


  * Account Reseller History (button; visible to "Upline Provider Roles" users; opens the "Account Reseller History" child screen - see corresponding spec)


