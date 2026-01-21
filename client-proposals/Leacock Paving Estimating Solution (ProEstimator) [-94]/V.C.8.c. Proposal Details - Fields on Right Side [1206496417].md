5.3.8.3. Proposal Details - Fields on Right Side

  * Proposal Type (read-only list macro; with the following details / behaviors: 
    * displays the correct item from the Proposal Types List, based on the logic specified below:
      * "Original": if one of the following is true (i.e. if the Proposal record was created manually or it was created as a Duplicate, since Duplicate Proposals are treated like Original Proposals from the estimating standpoint): 
        * "Is Copied Record" is not checked or 
        * "Is Duplicate" is checked; 
      * "Revised": if "Is Revised" checkbox is checked and "Is Change Order" checkbox is not checked; 
      * "Change Order": if "Is Change Order" checkbox is checked (regardless of whether or not the "Is Revised" checkbox is also checked); 
      * blank: if "Is Copied Record" is checked and none of the following are checked: "Is Revised", "Is Change Order", "Is Duplicate") 



  


  * Source (visible if the hidden "Is Copied Record" checkbox is checked (in the "Copy Proposal" section at the top of the screen); special link field; with the following behaviors: 
    * label displays in standard font; 
    * the "field" is a link that displays the "Copied from Proposal #", in the following format: "Proposal # <Proposal #>", to open that Proposal; 
    * user note: this gives an easy visual reference to the fact that the current record was a created as a copy of another Proposal record) 
  * Replaced By (visible if one or more "Revised"-type copies of current Proposal record exist; special link field; with the following details / behaviors:
    * label displays in red font;
    * the "field" is a link that displays the most recent "Revised" Proposal that has the current Proposal as its "Copied from Proposal #", in the following format: "Proposal # <Proposal #>", to open to corresponding "Revised" Proposal record; 
    * user note: this gives an easy visual reference to the fact that the current record has had a "Revised" Proposal created from it, and normally is no longer relevant) 
  * View X Change Order(s) (link; with the following behaviors / details:
    * visible if "Proposal Type" ≠ "Change Order" and there is one or more "Change Order"-Type Proposals in the Solution that share the same "Numeric ID" \+ "Revision Suffix";



Austin Priest 11/25/2025: _VA This link is displaying on an original proposal that does not have any change orders when there are change orders for a revised proposal.

See this record. [https://testproestimator.silverloom.io/Detail/Edit/2?RecordType=Proposals&NumberID=-99&](https://testproestimator.silverloom.io/Detail/Edit/2?RecordType=Proposals&NumberID=-99&)

Tim Reitz 11/26/2025: Good catch! Chasing in [[[IN12347](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12349&)]]. 

  * opens the "Change Orders for Proposal" report (see corresponding spec);



Austin Priest 11/25/2025: _VA When you click on this link it is setting the Source Proposal # to the parent proposal number not the proposal number where the link was clicked.

Tim Reitz 11/26/2025: Good catch! Chasing in [[[IN12347](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12349&)]]. 

  * in place of "X", displays the number of corresponding "Change Order"-type Proposals)



Austin Priest 11/25/2025: _VA This is displaying the total number of change orders for the whole proposal family not just the number or change orders for the given proposal.

Tim Reitz 11/26/2025: Good catch! Chasing in [[[IN12347](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12349&)]].
