7.10.3. Registration: Registration Details (Internal) Section

  * Registration Details (Internal) Section (visible only to Regional Reps and Super Admins):
    * Notes (optional; plain text) 
    * Lead Follow-up Completed (editable checkbox \+ date, which toggle; used to track whether someone has followed up with the Lead after the Info Meeting; with the following behaviors:
      * visible if the following are true:
        * Event Status is not Canceled 
        * Event Type = Info Meeting,
        * Registrant Type = Lead,
        * Lead Status field on the Registrant's Contact record is not "Inactive Lead";
          * note that this last item is dynamic and the checkbox disappears if the Contact's Lead Status is changed to "Inactive Lead";
      * defaults to not checked;
      * checking this checkbox automatically checks the "Follow-up Completed" checkbox on the "Lead Details" section of the Contact record for the Registrant - see corresponding spec; 
      * if the Contact becomes a Member, the checkbox does not disappear because it depends on the Registrant Type for the Registration record, which is static; 
      * if it already is checked and Lead Status is changed to "Inactive Lead", it remains checked, even though it hidden, so that reporting works correctly) 



  


  * Current Lead Status (visible if Event Type = Info Meeting or Launch Meeting and if Registrant Type = Lead; auto-set and read-only; dynamically displays the current Lead Status from the Lead's Contact record)


