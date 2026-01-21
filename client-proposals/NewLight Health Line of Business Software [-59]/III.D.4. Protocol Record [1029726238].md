3.4.4. Protocol Record

  


Requirements

The Protocol Record will include the following: 

  * Protocol Name
  * Active (checkbox)
  * Category (user-configurable list of categories)
  * About (formatted text)
  * Images (formatted text)
  * Signs and Symptoms (embedded spreadsheet with a user-configurable list of signs and symptoms) 
  * Testing Options (formatted text)
  * Home Remedies (formatted text)
  * Key Questions (formatted text)
  * Recommended Products (embedded spreadsheet of the following:)
    * SKU (drop-list of SKUs)
    * Description (read-only)
    * Dosage (editable; default to SKU's serving size)
  * Reference Articles (embedded spreadsheet of the following:)
    * Article/Recipe Title (list of articles/recipes; put the articles in the protocol's category at the top, separated by a line, with the additional protocols after it)
  * Cautions and Warnings (formatted text)



  


Amendments (visible if user has permission to view/edit amendments):

  * Embedded Spreadsheet of:
    * Date
    * Author
    * Notes
    * Reviewed (checkbox + date)
  * Notes (formatted text for selected row)



  


Editing:

  * A user who has permission to view/edit amendments can:
    * Create new, inactive protocols.
    * Add/edit amendments but NOT mark them reviewed
  * A user who has permission to edit protocol details can also:
    * Mark amendments as reviewed
    * Edit any part of the protocol, including marking them as active



  


Printing:

  * Print link (opens a prompt with a multi-select list of sections, then outputs the PDF)



  


Development Specification

They have 500 or so protocols. I'm thinking this is a lookup record.

  


TODO_IDD: Doesn't have to use a line delimiter -- as long as they can see which articles/recipes are for the current category, but still select something else if they want
