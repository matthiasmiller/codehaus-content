3.5.10. Claim General Release Printout

  


Requirements

*Documented. Tim Reitz 08/20/2025

  


Note: The existing text for this printout is different from what the WI Group uses. This is being changed to allow admin users to edit the text body as needed.

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Purpose/Overview: The General Release Agreement is used at the conclusion of a Claim to confirm the completion of the Claim. The body for the General Release is generated from the user-configured "Claim General Release Printout" text field in Silverloom Settings. 

  


Printed From: 

  * Claim record: "General Release PDF" link
  * Claim record: "General Release Word Document" link



  


File Format/Name: 

  * PDF: "General Release - <Claim ID> (exported on <current date in the yyyy-mm-dd format>)"
  * Word Document: "General Release - <Claim ID> (exported on <current date in the yyyy-mm-dd format>)"



  


Fields to be Filled (PDF & Word Document are the same):

  


  * Header: 
    * Logo (specific to the Plan) (hard-coded) (displays the "Plan Logo" from Silverloom Settings; dimensions: 500 x 108 points (max of 1.5" high, up to 6" wide)) 
    * "<displays the "General Release: Optional text below logo" System Switch> NAIC No. S0015
    * "<Plan Address Line 1 from Silverloom Settings> <Plan City from Silverloom Settings>, <Plan state abbreviation" System Switch> <Plan Zip from Silverloom Settings>" 395 Cherry Hill Rd. Richland PA 17087
    * "<Plan Phone from Silverloom Settings>" 717-933-4817



  


  * The printout body is drawn from the "Claim General Release Printout" text field in Silverloom Settings.
  * In the printout body:



Know all men by these presents, that I/we, <General Release Other Party, all uppercase> and/or heirs for sole consideration of the sum of <Total Release Amount, in words> to us to be paid by Weaverland Mennonite Vehicle Aid Plan on behalf of its insured <General Release Our Insured, all uppercase> release and discharge, and by these presents do for ourselves, our heirs, executors, administrators and assigns, release and forever discharge the said <General Release Our Insured, all uppercase> from any and all past, present, and future actions, causes of action, claims, demands, damages, costs, loss of services, expenses, compensation, third party actions, suits at law or in equity, including claims or suits for contribution and/or indemnity of whatever nature, and all consequential damage on account of, or in any way growing out of any and all known or unknown personal injuries to the aforesaid <General Release Other Party, all uppercase> which occurred on or about <Accident Date, in mm/dd/yyyy format> by reason of any and for all claims or demands whatsoever in law or in equity, which, our heirs, executors, administrators or assigns can, shall or may have reason of any matter, cause, or thing whatsoever prior to and on the date hereof.

It is understood and agreed that this is a full and final release of all claims of every nature and kind whatsoever against said <General Release Our Insured, all uppercase> and release claims that are known and unknown, suspected and unsuspected.

Nothing in this release shall be construed as compromising, releasing, or adversely affecting any first party medical, extra ordinary medical rights, benefits, recoveries or claims and or medical malpractice or similar rights, benefits, recoveries or claims, <General Release Other Party, all uppercase> has/have or may have out of the motor vehicle accident which occurred on or about <Accident Date, in mm/dd/yyyy format>.

I/we, <General Release Other Party, all uppercase> declare and represent that we rely wholly upon our own judgement, belief and knowledge of the nature, extent and duration of said damages and we have not been influenced to any extent whatsoever in making this general release by any representatives or statements regarding said damages, or regarding any other matters, made by the persons, firm, or corporations, who are hereby released, or by their insurers, attorneys, or their representatives.

I/we further state that we have carefully read the foregoing general release and know the contents thereof, and that we signed the same as our free act.

In witness thereof, I/we, <General Release Other Party, all uppercase>, intending to be legally bound hereby,

Have hereunto set our hands and seal the ______________ day of ___________, 20___

  


_______________________________________________ SEAL

(<General Release Other Party>)

  


IN THE PRESENCE OF:

  


_______________________________________________ SEAL

(Weaverland Mennonite Vehicle Aid Plan Representative)

  


________________________________________________

(Witness)

  


_______________

             (Date)

  


  


Handling Page Breaks: N/A (this printout always fits on a single page)

  


Other Notes:

  * This printout does not include the standard "Powered by Silverloom Business Suite" footer.
  * N/A



  


Development Specification

Tim Reitz 08/28/2024:  Link to template work in Docs: [https://docs.google.com/document/d/1t-6ZAvyDVE6lw9wO_NK5Z0g08bTYTheU/edit](https://docs.google.com/document/d/1t-6ZAvyDVE6lw9wO_NK5Z0g08bTYTheU/edit)

  


Ellis Miller 09/05/2024:

  


[ ] This will require a " \- Logo.r21" with cloning

[ ] No footer. 

  


1.5 Days
