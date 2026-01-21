3.5.11. Postcard Printout

  


Requirements

*Documented. Tim Reitz 08/20/2025

  


Note that this is a feature that the WI Group might not use, but it does have the PA info hard-coded in the template as the return address, so that is being changed.

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Purpose/Overview: Postcards are used to send certain invitations and notifications by postal mail. They are generated from user-configured text on the Postcard records on a per-Contact Type basis (one, multiple, or all Contact Types can be selected).

  


Printed From: 

  * Postcard record: "Print Postcard" link



  


File Format/Name: 

  * Word RTF document: "Postcards"



  


Fields to be Filled: 

  * Front of postcard: 
    * Text from the "Text" memo field in the Postcard record



  


  * Back of postcard:
    * Return address:
      * "<Plan Name, from the "Plan name" System Switch>" Weaverland Mennonite Vehicle Aid Plan
      * "<Plan Address, from the Plan Address fields in Silverloom Settings, in the standard format, up to 3 lines>" 
      * 395 Cherry Hill Rd.
      * Richland PA 17087



  


  * "To" address for postcard recipient:
    * "<Contact LastName, FirstName>" 
    * "<Contact address, in standard format, up to 3 lines>" 



  


Handling Page Breaks:

  * Odd numbered pages display the "Front" with postcard memo text; 4 postcards per page
  * Even numbered pages display the "Back" with addresses; 4 postcards per page



  


Other Notes:

  * This printout does not include the standard "Powered by Silverloom Business Suite" footer. 
  * N/A



  


Development Specification

Tim Reitz 08/28/2024: Link to template & notes in Google Docs: [https://docs.google.com/document/d/1liOClM1cX3TDLaPqvAbHvenpNgt2eW-b/edit](https://docs.google.com/document/d/1liOClM1cX3TDLaPqvAbHvenpNgt2eW-b/edit)

  


Tim Reitz 07/18/2024: This is a feature that WI might not use, but it does have the PA info (hardcoded) as the return address, so we should change that.

  


Ellis Miller 09/05/2024: 

  


2 hours

  


Tim Reitz 09/10/2024: Exclude the "powered by Silverloom" footnote.

  


Sagar Sagar 05/20/2025: CLS job ID - [[PC0178344]]
