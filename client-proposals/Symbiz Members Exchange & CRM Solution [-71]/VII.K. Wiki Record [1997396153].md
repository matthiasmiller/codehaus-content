7.11. Wiki Record

  


Requirements

Overview: The Solution includes the standard AppHosting Wiki feature for internal documentation. This includes the standard Wiki record pages and the standard Wiki report (see corresponding section of the proposal). 

  


Accessed via: Wiki report

  


Sections and Fields: 

  * Title (plain text field; required; no validation against duplicate titles; defaults to blank) 
  * Category (optional; drop list of Wiki Categories; defaults to blank) 
  * Wiki Page ID (auto-set and read-only; unique identifier for the record) 
  * Archived Notes (button; opens a child screen with a memo where old notes can be pasted for historical documentation / future reference) 
  * Wiki Page Body (standard memo) 
  * Generate PDF (link; generates a PDF of the page, with the Title, Body, and a document version displaying the Last Modified date) 
  * Export to Word (link; gives the option to download a Word document version of the page, with the Title, Body, and a document version displaying the Last Modified date) 
  * Send Email (link; opens a new email draft with the ID and Title in the subject line and the page's URL in the email body; requires MailTo to be set up for the user's browser) 
  * Share (button; opens a child screen displaying the ID + Title, which can be copied and shared with other users of the Solution for clear & easy linking) 



  


Data Access: See the Data Access Controls section and the Restricted Data Policies section of the proposal for details. Summary: Super Admins can view & edit all Wiki pages; other users' access is controlled by Restricted Data Policies. 

  


Special Considerations: 

  * Copy Record: Clears the ID.
  * Delete Record: Cannot be deleted if referenced by another record.
  * Merge Record: No restrictions.



  


Other Notes:

  * Whenever a new Wiki Category is set up, it defaults to being visible for Super Admins only. If Regional Reps should see it, it needs to be added to the "Regional Reps" Restricted Data Policy. If everyone should see it, it needs to be added to both "Default" and "Regional Reps" Restricted Data Policies. 
  * Note that this record includes a name, date, and time stamp for Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Change Requests: 

  * Tim Reitz 03/29/2024: [[[IN9469](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9471&)]] - ZSB - Add Wiki module
  * Tim Reitz 04/10/2024: [[[IN9697](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9699&)]] - ZSB - Changes to Wiki Module for Non-Admin Users


