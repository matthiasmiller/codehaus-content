5.3.9. Proposal - Proposal Finalization Section

  


Requirements

  * Proposal Finalization section: 



  


  * Ready to Send to Customer (checkbox \+ date, which toggle; with the following details / behaviors: 
    * editable if the "Sent to Customer" checkbox is not checked (i.e. becomes read-only when that checkbox is checked);
    * warning on save when checked: "Ensure that all photos / takeoffs / drawings are attached."; this is a reminder to the user about the standard procedure to have those things attached before sending;
    * when checked, the following field(s) are affected on change: 
      * "Stored Deposit Amount $": if "Deposit Required" is checked: sets based on the same calculation specced under the "Calculated Deposit Amount $" macro (see corresponding spec); 
      * "Proposal Date": sets to the current date; 
      * "Proposal Valid Through": sets based on Proposal Date (see corresponding spec); 
      * "Stored Proposal Oil Index": if "Override Oil Index" is not checked, sets to the current value of the "Current PA Oil Index" in Silverloom Settings;
    *   when unchecked, the following field(s) are affected on change: 
      * "Stored Deposit Amount $": clears; 
      * "Proposal Date": clears; 
      * "Proposal Valid Through": clears;
      * "Stored Proposal Oil Index": if "Override Oil Index" is not checked, clears;  
    * on the first Save after this is checked, the record enters Limited Editing Mode, making most fields on the Proposal read-only, so that no further changes are made to pricing, etc. - see the spec for Data Access; 
    * warning message on the field when checked: "Save this Proposal and refresh the page before making any additional changes, to finalize details." (this is to prevent additional changes from being made before the record enters Limited Editing Mode); 
    * warning message on the field when unchecked: "Save this Proposal and refresh the page before making any changes, to fully undo Ready to Send." (this is because the record must be saved after unchecking the checkbox, to fully exit Limited Editing Mode); 
    * note that if any changes need to be made prior to sending the Proposal to the Customer, the user can uncheck this checkbox, make necessary changes, then re-check it)



  


Development Specification

Change Requests: 

  * Tim Reitz 11/25/2025: [[[IN12304](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12306&)]] - ZLP - Phase 1 - Proposal Record - Improvements to "Deposit Required" / "Deposit Amount $"
  * 


  


  


Ellis Miller 06/18/2025: 

  


BID: 4 HOURS
