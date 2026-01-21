3.4. Silverloom Settings

  


Requirements

The Silverloom Settings page, accessed from Advanced | Admin | Silverloom Settings, includes the following custom sections and fields for various configuration settings. It also may include standard sections & fields. See the following sub-sections in this spec. 

  


Modification History: This contains the following standard feature for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users (standard) 
  * Editability: Editable for users included in the "Custom_CanEditSilverloomSettings" macro, which defaults to "Administrator"-type Users only (standard) 



  


Other Notes: 

  * Editability for the Silverloom Settings record can be controlled by a client-specific Permission. By default, editability is restricted to Users with the "Administrator" account type, but this can be changed.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1957169876#gid=1957169876](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1957169876#gid=1957169876) 

  


  


Tim Reitz 01/21/2025: For detail screen editability, note that this is using the new "Custom_CanEditSilverloomSettings" macro (added with ZGW), defaulting to UserIsAdministrator.
