22.2.2. Discussion Thread Record

Tim Reitz 04/06/2023: Per the client today, this can be a Phase 2 (or later) item. It can even wait until after the Investment Opportunity. 

  


TODO_IDD: To be able to indent text via an expression, per John Allan:

It would be trivial. It would just be a matter of validating the indent amount, then calling a new function, CRichTextBuilder::IndentAll, which would simply call CRichTextDocument::IndentAll.

  


Overview: This screen provides a place for a member to start a conversation for other members to see and respond to.

  


Accessed via: TODO_IDD

  


Sections and Fields: 

  * Active (checkbox) 
  * ID (automatically assigned; unique identifier)
  * Topic (list of Question, Investment Opportunity) 
  * Title (visible and required if Topic = Question)
  * Investment Opportunity (visible and required if Topic = Investment Opportunity; drop list of items)
  * Author (list of Users; automatic and read-only; current user)
  * Date/Time (stored in GMT; displayed in local time)
  * Question (memo)
  * Discussion (read-only memo of Comments linked to this Discussion Thread, with New Comment link)



  


Data Access:

  * Created by all users
  * Editable by the Author and Super Admins
  * Visible to all users



  


Special Considerations: 

  * Copy Record: 
  * Delete Record: 
  * Merge Record: 



  


Other Notes: 

  * Historical conversations remain visible to all users, including ones who become members after the conversation.


