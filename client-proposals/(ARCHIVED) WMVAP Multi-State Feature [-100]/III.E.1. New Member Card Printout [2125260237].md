3.5.1. New Member Card Printout

  


Requirements

*Documented. Tim Reitz 08/19/2025

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Purpose/Overview: The New Member Card is generated when a member joins or re-joins the Plan. This card is sent to the state of Pennsylvania as documentation of who has joined the Plan. 

  


This is a fully custom printout, displaying the text from the "New Member Card" field in Silverloom Settings.

  


Printed From:

  * Contact record: "Print Card" link (which is visible if the "New Member Card" field in Silverloom Settings is not blank)



  


File Format/Name: 

  * PDF
    * File Name: "<ClientLastName ClientFirstName> (exported on <current date in the yyyy-mm-dd format>)"



  


Fields to be Filled: 

  * Text from the "New Member Card" field in Silverloom Settings.



  


Handling Page Breaks: N/A (page breaks will fall wherever needed, but normally this would never reach a full page in length) 

  


Other Notes:

  * If a Plan does not need the New Member Card printout, the memo in Silverloom Settings is left blank (and the "Print" link on the Contact record is hidden as long as the memo is blank).
  * Includes the standard "Powered by Silverloom Business Suite" footer. 
  * N/A



  


Development Specification

Ellis Miller 09/05/2024: Was handled in Contact screen. Nothing to do. 

Tim Reitz 09/10/2024: But do add the "powered by Silverloom" footnote.
