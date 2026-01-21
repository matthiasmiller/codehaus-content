5.3.8. Vehicle - Cards and Reports Section

  


Requirements

*Done. 

  


  * Cards & Reports section:
    * Print Program Participation Agreement (link; prompts the user to save the record before opening; generates the "Program Participation Agreement Printout" as a PDF in the browser, with fields filled for the Owner and the Vehicle - see corresponding printout spec)
    * Print Insurance Card (Front Only) (visible if the user has active Liability coverage; link; with the following details / behaviors: 
      * prompts the user to save the record before opening; 
      * opens a prompt screen with a "Select Coverage Range" filter, which is a drop list of Liability coverages; 
      * clicking "Continue" with an item selected generates the front page of the "Insurance Card (Front & Back) Printout" in the browser for the selected coverage for the Vehicle - see corresponding printout spec)
    * Print Insurance Card (Front & Back) (same as the spec for the "Print Insurance Card (Front Only)" link, except that it generates the full "Insurance Card (Front & Back)" printout) 
    * Print Liability Declaration Page (visible if the user has active Liability coverage; link; with the following details / behaviors: 
      * prompts the user to save the record before opening; 
      * opens a prompt screen with a "Select Liability Coverage" filter, which is a drop list of Liability coverages; 
      * clicking "Continue" with an item selected generates the "Liability Declaration Page Printout" in the browser for the selected coverage for the Vehicle - see corresponding printout spec) 
    * Print Loss Payable Clause (visible if "Payee Name" in the Loss Payable section of the Vehicle screen is not blank and the user has active "collision" coverage; link; with the following details / behaviors: 
      * prompts the user to save the record before opening; 
      * opens a prompt screen with a "Select <Alternate text for Collision - Short label> Coverage" prompt, which is a drop list of <Collision> coverages; 
      * clicking "Continue" with an item selected generates the "Loss Payable Clause Printout" for the selected coverage for the Vehicle - see corresponding printout spec)



  


Other Notes:

  * When printing the Insurance Card, if the current date is prior to the Current Period Start Date, the user is required to specify whether to print the card for the Previous Period (for the year preceding the current period) or Current Period (using the current period start/end dates).



  


Development Specification

TODO_CCI: Tim Reitz 08/15/2025: Could you provide details on what is included on the "Select Coverage Range" filter for the two "Print Insurance Card..." prompt screens? (both for Admin and non-Admin users) Thanks!

Sagar Sagar 12/15/2025: Mainly the period for "Effective from .... to ...." section in the printout.

  


TODO_CCI: Tim Reitz 08/15/2025: Similartly, could you provide details on what is included on the "Select Liability Coverage" filter for the "Print Liability Declaration Page" prompt screen? (both for Admin and non-Admin users) Thanks!

Sagar Sagar 12/15/2025: Mainly the period for "POLICY PERIOD" section in the right side of the printout.

  


TODO_CCI: Tim Reitz 08/15/2025: For the visibility conditions that say, "visible if the user has active Liability coverage;", what does "user" mean? Should it say, "visible to Admin users and the Owner's Agent if the Vehicle has active Liability coverage"? 

Sagar Sagar 12/15/2025: No they are actually not user restricted links that some will and see some will not. I believe we should rephrase this to something like "visible if the vehicle has active Liability coverage". Do you think the behavior is correct? Or should we restrict to other agents?

  


TODO_CCI: Tim Reitz 08/15/2025: Similarly, for the condition that says, "... and the user has active "collision" coverage", what does that mean? Thanks! 

Sagar Sagar 12/15/2025: Same as before. "... and the vehicle has active "collision" coverage"

  


TODO_CCI: Tim Reitz 08/15/2025: For the item in "Other Notes" (regarding printing the Insurance Card when the current date is prior to the Current Period Start Date), does this mean that an additional ask prompt is displayed in that case? Or does it have to do with the items in the drop list? Thanks!

Sagar Sagar 12/15/2025: Not an additional ask prompt. It has to do with the list items in the drop list.
