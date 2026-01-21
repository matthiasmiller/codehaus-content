5.4. Silverloom Settings

  


Requirements

*Done. 

  


Overview: The Silverloom Settings page includes the following custom sections and fields for various configuration settings. It also may include standard sections & fields. 

  


Accessed from: Advanced | Admin | Silverloom Settings

  


Sections and Fields: 

  * Invoicing Settings (standard) section:
    * Default Sales Tax Rate (number; 2 decimals)



  


  * Contact Settings (standard) section: 
    * Name Format (required; 
      * drop list of the following items: 
        * FirstName LastName
        * FirstName MiddleName LastName
        * LastName, FirstName
        * LastName, FirstName MiddleName;
      * custom: "FirstName MiddleName LastName" is the option for deployment of this Solution)  
    * Apply Changes (button; clicking this after changing the selection in "Name Format" applies the change to existing Contacts in the Solution) 
    * "You must apply changes to update existing contacts. Overridden contact names will remain unchanged." (on-screen message in gray font) 



  


  * End User Agreements (custom) section: 
    * End User Agreements (embedded spreadsheet with the following:) 
      * Columns: 
        * Upload / Effective Date (auto-set and read-only; date; with the following details / behaviors:
          * sets to the current date when a new row is added;
          * error on Save if there are duplicate dates: "There are multiple End User Agreements with the same "Upload / Effective Date".")
        * File (ellipsis button that opens a child screen with a memo; with the following details / behaviors:
          * the user can drag and drop the PDF file into this memo to save it in Silverloom);
          * validates against duplicate file names - error on Save if there are multiple files with the same file name: "There are multiple files with the same file name: "<file name>". Carefully delete the newly-added item(s) as needed."; 
          * memo defaults to the following text in red font: "Drag and drop a file into this memo, or use the paperclip icon to browse for files on your computer. Upload only one file per memo.")
      * Automatically sorted by: "Upload / Effective Date" (latest date at the top)
      * Buttons to add/remove rows: "Add" / "Delete" 
        * Warning on Save if a row has been deleted: "One or more End User Agreement files have been deleted. Refresh the page without saving to undo these changes."; 
      * Shows 6 rows without scrolling
      * Other Notes: 
        * Due to the Silverloom Settings page being visible only to users with the "Can Edit Silverloom Settings" Permission, other users cannot access previous versions of the EUA in Silverloom.)



  


  


  * Email Configurations (custom) section: 
    * New Device Request Email Body (multi-line plain text field that supports expressions; with the following details / behaviors: 
      * technical notes: 
        * expressions are evaluated on Account records; 
        * plain text is used here to facilitate sending the email via the mailto feature; 
      * this is used for setting & storing the default text for the email that can be used by Account Managers to request a new Device to be added to their Account - see corresponding spec; 
      * warning on Save if blank; 
      * to be initially set to the following at deployment of the Solution, but may be edited by Master Administrator users or by CodeCrafters: 



Hello, 

  


I am writing to request a new Device to be added to Account #<Account #, in bold font>>.

  


Primary Driver Information: 

Driver First Name: 

Driver Middle Name:

Driver Last Name:

Driver Date of Birth:

  


Primary Vehicle Information: 

Vehicle Year: 

Vehicle Make: 

Vehicle Model: 

Vehicle VIN (if accessible): 

  


Thank you, 

<"Short Display Name> of the requesting Contact> 

  


  * New User Request Email Body (multi-line plain text field that supports expressions; with the following details / behaviors: 
    * technical notes: 
      * expressions are evaluated on Account records; 
      * plain text is used here to facilitate sending the email via the mailto feature; 
    * this is used for setting & storing the default text for the email that can be used by Account Managers to request a new user to be added to their Account - see corresponding spec; 
    * warning on Save if blank; 
    * to be initially set to the following at deployment of the Solution, but may be edited by Master Administrator users or by CodeCrafters: 



Hello, 

  


I am writing to request a new user to be added to Account #<Account #, in bold font>>.

  


User Information: 

User Email Address: 

User First Name: 

User Middle Name:

User Last Name:

User Date of Birth:

  


Account Details: 

User Type (Account Manager / Driver): 

Primary Driver (Yes / No): 

If Primary Driver: Linked Device (Existing ID / New Device): 

  


Thank you, 

<"Short Display Name> of the requesting Contact> 

  


  


  


  


Modification History: This contains the following standard feature for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users (standard) 
  * Editability: Editable for users with the "Can Edit Silverloom Settings" Permission (standard) 



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Tim Reitz 07/23/2025: None included in the HLD.

  


Tim Reitz 10/15/2025: Permission to control editability is being added in [[[IN12251](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12253&)]] - CORE - Add New "Edit Silverloom Settings" Permission.
