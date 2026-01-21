11.13.2. FB Email Template - Email Template Section

TODO_VA: standard format for the RG

  


Email Template section:

  * Subject (plain text expression field) 
  * Body (memo)
  * Attachments (button; opens a child screen)



Embedded spreadsheet (RG):

Columns:

  * Attachment



Buttons:

  * "+" \- insert row
  * "-" \- delete selected row


  * (right text expression; displays a newline delimited list of attachments from the RG)



  


Validations:

  * Error on save: if the attachment is not a valid PDF file.
    * Error Message: "Only PDFs are supported as attachments. (Field: Attachment; Row: <FBEmailAttachmentPath>)"



  


Additional Notes:

  * Expressions (fields, macros) can be inserted into the Subject and Body using #expr# (e.g. #ContactName#) to be evaluated upon email creation.
    * These expressions either must not be level-tied or must match the specified Level. (e.g. #ContactName# will not evaluate if the Level is "Member Applications")
  * While an expression, text in Subject defaults to being plain text. Pound signs must be used designate text as an expression. Expressions are displayed in black text; plain text is displayed in gray text.
  * Attachments are displayed next to the Attachments button.


