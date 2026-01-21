3.4. Silverloom Settings

The Silverloom Settings page, accessed from Advanced | Admin | Silverloom Settings, includes the following custom sections and fields for various configuration settings. It also may include standard sections & fields. 

  


  *   Contact Settings section (standard): 
    * Name Format (required; 
      * drop list of the following items: 
        * FirstName LastName
        * FirstName MiddleName LastName
        * LastName, FirstName
        * LastName, FirstName MiddleName; 
    * Apply Changes (button; clicking this after changing the selection in "Name Format" applies the change to existing Contacts in the Solution) 
    * "You must apply changes to update existing contacts. Overridden contact names will remain unchanged." (on-screen message in gray font) 



  


<Custom> section: 

  


Data Access: 

  * Visibility: Visible to all users (standard) 
  * Editability: Editable for "Administrator"-type Users only (standard) 



TODO_IDD: Can be customized, based on the "Custom_CanEditSilverloomSettings" macro, which defaults to "UserIsAdministrator". 

Tim Reitz 10/21/2024: This is per the plan as of today (planning to add this macro with the GW project). If this doesn't happen, we should update the TODO_IDD note here. 

  


Other Notes: 

  * Editability for the Silverloom Settings record can be controlled by a client-specific Permission. By default, editability is restricted to Users with the "Administrator" account type.


