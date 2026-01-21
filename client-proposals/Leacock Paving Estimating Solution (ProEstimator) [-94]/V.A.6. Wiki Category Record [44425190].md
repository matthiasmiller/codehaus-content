5.1.6. Wiki Category Record

  


Requirements

Overview: The Solution includes the standard Silverloom Wiki Categories feature for categorizing Wiki pages. This includes both the standard Wiki Category record pages and the standard Wiki Categories report (see corresponding section of the proposal). Note that any customizations are noted as such in the spec. 

  


Accessed via: Configure Wiki Categories Report

  


Sections and Fields: 

  * Category Name (required; plain text field; validation error message: "A Wiki Category name cannot be empty.") 
  * Parent (drop list of Wiki Categories, to allow the user to create hierarchies or "Wiki trees") 



  


  


Modification History: This contains the following standard features for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access (standard; can be controlled by Data Access Controls - see corresponding section of the proposal):

  * Visibility: Visible to all users
  * Editability: Editable for all users 



  


Special Considerations: 

  * Copy Record: Allowed, and all fields are copied (standard). 
  * Delete Record: Allowed for Administrator users and any users with the "User Can Delete Wiki Category" Permission (standard). 
  * Merge Record: Allowed without restrictions; the record from which the merge is initiated is completely replaced by the other (all data is deleted) (standard).



  


Other Notes:

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Mockup: N/A
