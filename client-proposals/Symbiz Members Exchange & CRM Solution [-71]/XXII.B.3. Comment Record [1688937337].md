22.2.3. Comment Record

  


Requirements

Tim Reitz 04/06/2023: Per the client today, this can be a Phase 2 (or later) item. It can even wait until after the Investment Opportunity. 

  


Overview: The Comment screen is typically only viewed for creating comments in a conversation/in response to a Question. A Comment record is linked to an Investment Opportunity record or to a Question record.

  


Accessed via: TODO_IDD

  


Sections and Fields: 

  * Active (checkbox)
  * ID (auto-set and read-only; unique identifier)
  * Prior Discussion (read-only view of prior comments from the Discussion Thread; includes the Title/Investment Opportunity)
  * Author (list of Users; automatic and read-only; current user)
  * Date/Time (stored in GMT; displayed in local time)
  * Comment (memo)
  * New Discussion Thread (link)



  


Data Access:

  * Created by all users
  * Editable by the Author and Super Admins
  * Visible to all users



  


Special Considerations: 

  * Copy Record: 
  * Delete Record: 
  * Merge Record: 



  


Other Notes: 

  * Historical comments/conversations remain visible to all users, including ones who become members after the conversation.



  


Development Specification

Hidden Fields:

  * Comment Type
    * Investment Opportunity
    * Question
  * Investment Opportunity ID (required if Investment Opportunity)
  * Question ID (required if Question)



TODO_IDD: Tim Reitz 02/16/2023: Add to the requirements. 

  


TODO_IDD:

  * Have a macro that generates a conversation memo for a thread, with an optional "cutoff date/time"
  * Use this to show conversation in the Investment Opportunity record.



  


DONE_CCI: We discussed just using a standard memo like we do for incidents, but wasn't sure about edit collisions when questions / investment opps go out to 1000 users?

TODO_IDD: I think we need comment records with this many users.
