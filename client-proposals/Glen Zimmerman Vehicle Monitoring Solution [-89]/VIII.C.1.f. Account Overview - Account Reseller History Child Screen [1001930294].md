7.3.1.6. Account Overview - Account Reseller History Child Screen

  


Requirements

*Done. 

  


  * Account Reseller History Child Screen (includes the following: 
    * Account Reseller History (non-embedded spreadsheet with the following:
      * Columns: 
        * Requested By (list field of active User Profiles; auto-set and read-only; defaults to the user who initiated the Transfer Request when the row is added, either via the On-Screen Prompt or the Automatic Process)
        * Requested Date (date; auto-set and read-only; defaults to the current date when the row is added, either via the On-Screen Prompt or the Automatic Process)
        * Reason / Comments (required for rows other than the initial row; multi-line plan text; sets to the contents of the corresponding data entry field when the row is added, either via the On-Screen Prompt or the Automatic Process)
        * Prior Reseller (list field; auto-set and read-only; defaults to the current "Account Reseller" for the Account when the row is added, either via the On-Screen Prompt or the Automatic Process) 
        * Prior Reseller Approval (checkbox; with the following details / behaviors:
          * automatically checked when the row is added via the On-Screen Prompt by the "Prior Reseller" (individual) or a "Reseller Rep" for the "Prior Reseller" Contact;
          * editable until the first Save after it is checked; this allows the "Prior Reseller" to approve a transfer requested by another Reseller, and allows users with the "Full Access" Permission to approve instead of the Reseller;
          * when manually checked, the following field(s) are affected:
            * "Prior Reseller Approval User": sets via the "Set Prior Reseller Approval" Shared OnChange Action - see corresponding spec;
            * "Prior Reseller Approval Date": sets via the "Set Prior Reseller Approval" Shared OnChange Action - see corresponding spec;
            * "Transfer Complete Date": if "New Reseller Approval" is already checked, sets to the current date, otherwise, N/A)
        * Prior Reseller Approval User (hidden; list field of active User Profiles; set via the "Prior Reseller Approval" checkbox - see corresponding spec)
        * Prior Reseller Approval Date (hidden; date field; set via the "Prior Reseller Approval" checkbox - see corresponding spec)
        * Prior Reseller Approval Details (read-only macro; displays details about the approving user and date, in the following format: "<Short Display Name for the linked Contact of the User in "Prior Reseller Approval User" (<Prior Reseller Approval Date>)", i.e. "John Doe (12/01/2025)"))
        * New Reseller (required; auto-set and read-only; list field of all "Display Name" values for all active Account Resellers; set either via the On-Screen Prompt or the Automatic Process) 
        * New Reseller Approval (checkbox; with the following details / behaviors: 
          * automatically checked when one of the following happens:
            * when the row is added via the Automatic Process by the "New Reseller" (individual) or a "Reseller Rep" for the "New Reseller" Contact; 
            * when the transfer is approved via Automatic Process by the "New Reseller";
          * editable for users with the "Full Access" Permission; this allows these users to approve instead of the Reseller; 
          * when manually checked, the following field(s) are affected:
            * "New Reseller Approval User": sets to the "User ID" for the user who checked the "New Reseller Approval" checkbox; 
            * "New Reseller Approval Date": sets to the current date; 
            * "Transfer Complete Date": if "Prior Reseller Approval" is already checked, sets to the current date, otherwise, N/A)
        * New Reseller Approval User (hidden; list field of User Profiles; set via the "New Reseller Approval" checkbox or the Automatic Process - see corresponding specs)
        * New Reseller Approval Date (hidden; date field; set via the "New Reseller Approval" checkbox or the Automatic Process - see corresponding specs)
        * New Reseller Approval Details (read-only macro; displays details about the approving user and date, in the following format: "<Short Display Name for the linked Contact of the User in "Prior Reseller Approval User" (<New Reseller Approval Date>)", i.e. "John Doe (12/01/2025)")
        * Transfer Complete (read-only macro; checkbox; with the following details: 
          * displays as checked if "Transfer Complete Date" is not blank;
          * this also makes the whole row read-only, so that additional changes cannot be made; if a mistake was made, the Account can be transferred again;
          * on the first Save after this checkbox is checked, the "Account Reseller Transfer Complete" email notification is sent - see corresponding spec) 
        * Transfer Complete Date (date field; auto-set and read-only; sets to checked when both "Prior Reseller Approval" and "New Reseller Approval" are checked, either automatically or via the Automatic Process - see corresponding specs) 
      * Automatically sorted by: "Requested Date" (most recent at the top) 
      * Buttons to add/remove rows: 
        * No button to add rows here (since rows are always added via the "Account Reseller" editable macro or the "Request Reseller Transfer" feature) 
        * "Cancel Transfer" (visible if the currently-selected row does not have the "Transfer Complete" checkbox checked; deletes the selected row after prompting for confirmation) 
      * Shows 8 rows without scrolling 
      * Other Notes: 
        * Note that the initial row is used for setting the first Reseller, prior to any transfers occurring.
        * on the first Save after a new row is added (not including the initial row), the "Send "New Account Reseller Transfer Request" Email" triggered automatic process runs - see corresponding spec)



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=553864745#gid=553864745](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=553864745#gid=553864745)

  


Tim Reitz 12/09/2025: Non-embedded RG.
