7.6. Wiki Record

  


Requirements

Overview: The Solution includes the standard Silverloom Wiki feature for internal documentation. This includes the standard Wiki record pages and the standard Wiki report (see corresponding section of the proposal). Note that any customizations are noted as such in the spec.

  


Phase 1 does not include any customizations.

  


Accessed via: Wiki report

  


Sections and Fields: 

  * Wiki section: 
    * Title (plain text field; required; no validation against duplicate titles; defaults to blank) 
    * Category (optional; drop list of Wiki Categories; defaults to blank) 
    * Wiki Page ID (auto-set and read-only; unique identifier for the record) 
    * Archived Notes (button; opens a child screen with a memo where old notes can be pasted for historical documentation / future reference) 
    * Wiki Page Body (standard memo) 
    * Generate PDF (link; generates a PDF of the page, with the Title, Body, and a document version displaying the Last Modified date) 
    * Export to Word (link; gives the option to download a Word document version of the page, with the Title, Body, and a document version displaying the Last Modified date) 
    * Send Email (link; opens a new email draft with the ID and Title in the subject line and the page's URL in the email body; requires MailTo to be set up for the user's browser) 
    * Share (button; opens a child screen displaying the ID + Title, which can be copied and shared with other users of the Solution for clear & easy linking) 



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access (can be controlled by Data Access Controls - see corresponding section of the proposal):

  * Visibility: Visible to all users
  * Editability: Editable for all users



  


Special Considerations: 

  * Copy Record: Allowed; ID is cleared
  * Delete Record: Allowed 
  * Merge Record: Allowed



  


Other Notes:

  * N/A



  


Development Specification

Mockup: N/A
