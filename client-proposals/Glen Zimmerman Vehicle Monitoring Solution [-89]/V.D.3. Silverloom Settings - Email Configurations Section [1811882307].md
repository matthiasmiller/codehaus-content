5.4.3. Silverloom Settings - Email Configurations Section

  * Email Configurations (custom) section: 
    * From Name (__
    * From Email (__
    * Signature Name (__
    * Signature Title (__
    * BCC Email (__



TODO_VA: Tim Reitz 01/22/2026: Go with this generic approach (like we're doing for XFB) or include fielding for each email (like we do for ZET)?

Tim Reitz 01/27/2026: I'm thinking it will be a combination. 

  


TODO_NM (review): Tim Reitz 01/22/2026: FYI that I'm expecting there will be quite a few more emails coming here as we spec those out more. 

  


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
