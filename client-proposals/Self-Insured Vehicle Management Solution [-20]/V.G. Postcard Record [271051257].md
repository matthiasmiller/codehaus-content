5.7. Postcard Record

  


Requirements

*Done. 

  


Overview: This is a custom record that is used as a template for generating postcards.

  


Accessed via: Admin | Renewals and Printing | Postcards

  


Sections and Fields: 

  * Name/Description (plain text; with the following details / behaviors:
    * required -- error on the field and on Save: "A Postcard name cannot be empty.";
    * duplicate names are not allowed -- error on the field and on Save: "Duplicate Postcard names are not allowed: <name>")
  * Print Postcard (link; when clicked, prompts the user to save if not all changes are saved, then opens the prompt screen for the "Print Postcard Word Export" - see corresponding spec)
  * Text (required; memo; supports expressions)



  


Modification History: Note that this record does not contain the created / last modified / Modification History features.

  


Data Access: Admin

  


Special Considerations: 

  * Copy Record: Allowed, with "Name/Description" cleared on copy. 
  * Delete Record: Allowed
  * Merge Record: Allowed



  


Other Notes: 

  * N/A



  


Development Specification

Matthias Miller 07/20/2020: Technical details: 

  * Use ContactLookups or something similar to determine the number of recipients
  * Create a Repeat for List report using NumericPipeList to generate one row per page
  * Add a PostcardText macro
  * Add a PostcardAddress macro that takes the current page (1-n) and the current item on the page (1-4) and returns the appropriate address
  * You will need to accept the Postcard Name as an ask prompt.



  


Ellis Miller 08/18/2020: (3 days) Talk to me before implementation.
