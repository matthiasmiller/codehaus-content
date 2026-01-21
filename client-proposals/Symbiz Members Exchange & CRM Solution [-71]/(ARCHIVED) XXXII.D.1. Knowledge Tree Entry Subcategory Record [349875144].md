32.4.1. Knowledge Tree Entry Subcategory Record

DONE_MM: Tim Reitz 04/06/2023: Client said that if it's easier, he's fine with not having Subcategories. Thoughts on how much complexity this would reduce? 

DONE_DH: Tim Reitz 04/11/2023: Yes, this would make things simpler. Still OK with it? 

Tim Reitz 04/18/2023: Yes, client is fine with this. Said he's all for keeping it simple and workable.

  


DONE_IDD:

[ ] deactivate this section

[X] deactivate the report section

[X] remove from Knowledge Tree Entry

[X] remove from KT record?

[X] Revisit Descriptions to make sure they're as simple as can be. 

  


  


Overview: This allows configuring the Knowledge Tree Entry Subcategories. These will always be unique to a user/member.

  


Accessed via: The Configure Knowledge Tree Entry Subcategories report

  


Sections and Fields: 

  * Subcategory ID (auto-set and read-only; unique identifier) 
  * Description (automatic and read-only; Subcategory Name + Category ID, i.e. "Bookkeeping #223"; unique identifier)
  * Member (automatic and read-only; current user)
  * Category (required; drop list of Knowledge Tree Entry Categories for the Member)
  * Subcategory Name (required; plain text)
  * Active (checkbox; filled by default)



  


Data Access: 

  * Visible to admins or to User



  


Other Notes:

  * Each member will start out with a blank list of Subcategories.


