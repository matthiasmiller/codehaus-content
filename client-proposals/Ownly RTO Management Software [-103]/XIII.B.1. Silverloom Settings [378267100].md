13.2.1. Silverloom Settings

  


Requirements

Overview: The Silverloom Settings page includes the following custom sections and fields for various configuration settings. It also may include standard sections & fields. 

  


Accessed from: Advanced | Admin | Silverloom Settings

  


Sections and Fields: 

  * Accounting Settings (custom):
    * Edit Accounting Company Settings (link; opens the Accounting Company record)
  * Invoicing Settings (standard) section:
    * Default Sales Tax Rate (number; 2 decimals)



  


  *   Contact Settings section (standard): 
    * Name Format (required; 
      * drop list of the following items: 
        * FirstName LastName
        * FirstName MiddleName LastName
        * LastName, FirstName
        * LastName, FirstName MiddleName; 
      * custom: FirstName LastName is the option for deployment of this Solution)  
    * Apply Changes (button; clicking this after changing the selection in "Name Format" applies the change to existing Contacts in the Solution) 
    * "You must apply changes to update existing contacts. Overridden contact names will remain unchanged." (on-screen message in gray font) 



  


  * Welcome Call Template section (custom):
    * Memo



  


Modification History: This contains the following standard feature for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users (standard) 
  * Editability: Editable for users included in the "Custom_CanEditSilverloomSettings" macro, which defaults to "Administrator"-type Users only (standard) 



TODO_: Can be customized, based on the "Custom_CanEditSilverloomSettings" macro. 

  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

TODO_: Can be customized, based on the "Custom_CanEditSilverloomSettings" macro, which defaults to "UserIsAdministrator". 

Tim Reitz 10/21/2024: This is per the plan as of today (planning to add this macro with the GW project). If this doesn't happen, we should update the TODO_ note here.
