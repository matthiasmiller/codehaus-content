5.4.3. Silverloom Settings - Email Configurations Section

  


Requirements

  * Email Configurations (custom) section: 



  


  * New Device Request Email Body (button; opens a child screen with a multi-line plain text field that supports expressions; with the following details / behaviors: 
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

  


  


  * New User Request Email Body (button; opens a child screen with a multi-line plain text field that supports expressions; with the following details / behaviors: 
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

  


  


TODO_VA: Tim Reitz 02/05/2026: Spec out the rest: 

  


  * __ (button / child screen with the following:) 
    * "Email addresses must be separated by comma (,)" (note at the top of the child screen)
    * From (email field; initially set to "__@<service name>") 
    * To (email field; __) 
    * "__" (note in smaller font under the field)
    * CC (email field; __) 
    * BCC (email field; __) 
    * Reply To (email field; __) 
    * Body (memo; allows for expressions; __)



  


  


  * __ (button / child screen with the following:) 
    * "Email addresses must be separated by comma (,)" (note at the top of the child screen)
    * From (email field; initially set to "__@<service name>") 
    * To (email field; __) 
    * "__" (note in smaller font under the field)
    * CC (email field; __) 
    * BCC (email field; __) 
    * Reply To (email field; __) 
    * Body (memo; allows for expressions; __)



  


  


  * __ (button / child screen with the following:) 
    * "Email addresses must be separated by comma (,)" (note at the top of the child screen)
    * From (email field; initially set to "__@<service name>") 
    * To (email field; __) 
    * "__" (note in smaller font under the field)
    * CC (email field; __) 
    * BCC (email field; __) 
    * Reply To (email field; __) 
    * Body (memo; allows for expressions; __)



  


  


  * __ (button / child screen with the following:) 
    * "Email addresses must be separated by comma (,)" (note at the top of the child screen)
    * From (email field; initially set to "__@<service name>") 
    * To (email field; __) 
    * "__" (note in smaller font under the field)
    * CC (email field; __) 
    * BCC (email field; __) 
    * Reply To (email field; __) 
    * Body (memo; allows for expressions; __)



  


Development Specification

TODO_NM (review): Tim Reitz 01/22/2026: FYI that I'm expecting there will be quite a few more emails coming here as we spec those out more. 

  


Tim Reitz 02/05/2026: Template: 

  


  * __ (button / child screen with the following:) 
    * "Email addresses must be separated by comma (,)" (note at the top of the child screen)
    * From (email field; initially set to "__@<service name>") 
    * To (email field; __) 
    * "__" (note in smaller font under the field)
    * CC (email field; __) 
    * BCC (email field; __) 
    * Reply To (email field; __) 
    * Body (memo; allows for expressions; __)


