5.8. Wiki Page Record

*Done. 

  


Overview: The Solution includes the standard Silverloom Wiki feature for internal documentation. This includes the standard Wiki record pages and the standard Wiki report (see corresponding section of the proposal). Note that any customizations are noted as such in the spec. 

  


Accessed via: Wiki report

  


Sections and Fields: 

  * Wiki section: 
    * Title (plain text field; required; no validation against duplicate titles) 
    * Category (optional; drop list of Wiki Categories) 
    * Wiki Page ID (auto-set and read-only; unique identifier for the record) 
    * Archived Notes (button; opens a child screen with a memo where old notes can be pasted for historical documentation / future reference) 
    * Wiki Page Body (standard memo) 
    * Generate PDF (link; generates a PDF of the page, with the Title, Body, and a document version displaying the Last Modified date) 
    * Export to Word (link; gives the option to download a Word document version of the page, with the Title, Body, and a document version displaying the Last Modified date) 
    * Send Email (link; opens a new email draft with the ID and Title in the subject line and the page's URL in the email body; requires MailTo to be set up for the user's browser) 
    * Share (button; opens a child screen displaying the ID + Title, which can be copied and shared with other users of the Solution for clear & easy linking) 



  


Modification History: This contains the following standard features for modification tracking: 

  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access:

  * Visibility: Visible if the user is an Administrator or if the user's Restricted Data Policy Permission for the Wiki Category is not "Hidden" (standard) 
  * Editability: Editable if the user has the "Can Edit" or "Can Edit & Delete" Restricted Data Policy Permission for the Wiki Category (standard) 



  


Special Considerations: 

  * Copy Record: Allowed based on user's restricted data policy for Wiki Category; when copied, "Wiki Page ID" is cleared (standard) 
  * Delete Record: Allowed based on user's restricted data policy for Wiki Category (standard) 
  * Merge Record: Allowed without restrictions; the record from which the merge is initiated is completely replaced by the other (deleting all data for the first record) (standard) 



  


Other Notes:

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.


