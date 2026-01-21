11.14. Email Record

  


Requirements

TODO_AP: Tim Reitz 02/24/2025: Update to the current Record Snippet as needed. I think it might just be updating the "Modification History" details. 

  


Overview: The Email record tracks individual email communications that are created to be sent out from the Solution. This is not to be confused with the "FB Email Template" record. 

  


When a user clicks the "__", the Solution generates Email records for all Contacts who are due to have an email sent to them, based on a variety of criteria. These Email records are generated based directly on the FB Email Template records and the Solution's sending logic. Email records are visible via the "View/Send Emails Report" and are not send until manually triggered by a user (see corresponding section of the living spec). Email records are editable until they have been sent, at which point they become completely read-only. 

  


Accessed via: 

  * Faith Builders Scholarship Services | Communications | View/Send FBSS Emails
  * Faith Builders SPE | Communications | View/Send SPE Emails 



  


Sections and Fields: 

  * "Email" section header
  * Email Status (displays at the right-hand end of the section header; displays the following: 
    * "Draft - Needs Review" (if both the "Ready to Send" and "Sent" checkboxes are not checked) 
    * "Draft - Ready to Send" (if the "Ready to Send" checkbox is checked and the "Sent" checkbox is not checked) 
    * "Sent" (if the "Sent" checkbox is checked)



  


  * Email ID (__



TODO_NM: Tim Reitz 10/02/2024: What is the Email ID? (it hasn't been specced on the Email record before, and I don't see a visible field on the detail screen, but the View/Send Emails report mentions it in the sort. It looks like it's just a sequential numeric field? 

  


  * From (button; opens the following child screen:)
    * "From: Email" child screen: 
      * Name (From) (optional; plain text) 
      * Email (From) (required; email; must be in a valid email format)
  * (read-only; right text expression; displays the entered Name and Email)



  


  * To (button; opens the following child screen:) 
    * "To: Email" child screen: 
      * Embedded spreadsheet (RG) with the following: 
        * Columns: 
          * Name (To) (optional; plain text) 
          * Email (To) (optional; email; must be in a valid email format)
        * Automatically sorted by: N/A
        * Buttons to insert/remove rows: "+" / "-"
        * Show 4 rows without scrolling 
  * (read-only; right text expression; displays a comma-delimited list of Names and Emails from the child screen)



  


  * Cc (button; visible if in edit mode or there are rows in the child screen RG; opens the following child screen)
    * "Cc: Email" child screen: 
      * Embedded spreadsheet (RG) with the following: 
        * Columns: 
          * Name (Cc) (optional; plain text) 
          * Email (Cc) (optional; email; must be in a valid email format)
        * Automatically sorted by: N/A
        * Buttons to insert/remove rows: "+" / "-"
        * Show 4 rows without scrolling 
  * (read-only; right text expression; visible if in edit mode or there are rows in the RG; displays a comma delimited list of Names and Emails from the RG)



  


  * Bcc (button; opens the following child screen:)
    * "Bcc: Email" child screen: 
      * Embedded spreadsheet (RG) with the following: 
        * Columns: 
          * Name (Bcc) (optional; plain text) 
          * Email (Bcc) (optional; email; must be in a valid email format)
        * Automatically sorted by: N/A
        * Buttons to insert/remove rows: "+" / "-"
        * Show 4 rows without scrolling 
  * (read-only; right text expression; visible if in edit mode or there are rows in the RG; displays a comma delimited list of Names and Emails from the RG)



  


  * Attachments (button; visible if in edit mode or there are rows in the RG; opens the following child screen:)
    * "Attachments: Email" child screen: 
      * Embedded spreadsheet (RG) with the following: 
        * Columns: 
          * Attachment (optional; plain text; must be a valid full path to a PDF file in the Solution) 
        * Automatically sorted by: N/A
        * Buttons to insert/remove rows: "+" / "-"
        * Show 4 rows without scrolling 
  * (read-only; right text expression; visible if in edit mode or there are rows in the RG; displays a newline delimited list of Attachments from the RG)



  


  * Subject (optional; text field) 
  * Ready to Send (checkbox; visible if "Sent" checkbox is not checked; with the following special behaviors: 
    * sets to checked on Emails created for Contacts who do not have the "Review All Emails" checkbox checked; 
    * sets to not checked on Emails created for Contacts who have the "Review All Emails" checkbox checked; 
    * if not checked, the Email record will not send; 
    * once the "Sent" checkbox is checked, this checkbox is hidden; 
    * warning on Save (both on the detail screen and in imports) if this checkbox is not checked: "Email is not marked Ready to Send: Subject: "<Subject>"; To: <recipient(s)>.") 
  * Email Instructions (from Contact) (visible if "Ready to Send" is not checked; read-only text, displaying the contents of the "Email Instructions" field from the Contact record) 
  * Sent (read-only; checkbox; defaults to not checked; automatically checks when the email is sent, and displays the date/time to the right of the checkbox in the following format: "Sent on <MM/DD/YYYY>, <HH:MM:SS> <AM/PM>")
  * Body (optional; memo) 
  * Email Template (read-only; list of email templates; displays the corresponding FB Email Template from which the Email was created, as a link to the record)
  * Contact (visible if the corresponding FB Email Template "Level" = "Contact"; read-only; link to the Contact record for which the Email was generated)
  * Contact Group (visible if the corresponding FB Email Template "Level" = "Contact"; read-only; displays __ )



TODO_NM: Tim Reitz 10/02/2024: How does this work?

  * Distribution (__)



TODO_NM: Tim Reitz 10/02/2024: What's the spec for this?

  * Member Application (visible and required if the corresponding FB Email Template "Level" = "Member Application"; __) 



TODO_NM: Tim Reitz 10/02/2024: How does this work?

  * Family Application (__) 



TODO_NM: Tim Reitz 10/02/2024: What's the spec for this?

  * SPE Application (visible and required if the corresponding FB Email Template "Level" = "SPE Approval"; __)



TODO_NM: Tim Reitz 10/02/2024: How does this work?

  


Additional validations:

  * Error on save: if no recipient (at least "To" or "Cc" or "Bcc") is specified: "At least on recipient must be specified." 



Error on save: if any of the email addresses are not valid: "Please enter a valid '<type>' email address."

  * Error on save: if more than 5 attachments are supported: "__" 



TODO_NM: Tim Reitz 10/02/2024: What does "if more than 5 attachments are supported" mean? Also, what is the wording for this error?

  


Additional behaviors:

  * If there are no rows in the Bcc RG and Email (from) is modified, Bcc is set to Email (from).



  


Data Access: All users

  


Special Considerations: 

  * Copy Record: N/A (disallowed)
  * Delete Record: 
    * All users can delete if Email has not been sent.
    * Admins can delete after it has been sent.
  * Merge Record: N/A (disallowed)



  


Other Notes:

  * Editability: As mentioned above, the Email record cannot be edited after it has been sent.
  * Note that this record has a link to access Modification History (standard).



  


Development Specification

TODO_NM: Tim Reitz 10/02/2024: Should the user be able to enter multiple email addresses into the Email fields on the child screens? I noticed that if I enter multiple emails (comma-separated), the Name does not display on the expression field on the main detail screen. 

  


[ ] The Base email should be custom database level in an "AppHosting Email" catalog.

[ ] The custom fields should be added to the client catalog.
