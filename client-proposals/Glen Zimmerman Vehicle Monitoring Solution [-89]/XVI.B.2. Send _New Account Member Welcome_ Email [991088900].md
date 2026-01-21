16.2.2. Send "New Account Member Welcome" Email

TODO_VA: Tim Reitz 01/08/2026: Update based on the current Trigger snippet template

  


  * Name: Send "New Account Member Welcome" Email 
    * Overview: Runs from an Account record to send the "New Account Member Welcome" Email after a new Account Member is added to the Account. 
    * Initiated:
      * On the first Save after a new row is added to the "Account Members" embedded spreadsheet on the Account record. 
        * Note that if multiple new rows are added, a separate email should be sent for each one. 
    * Priority: 2
    * Action(s): 
      * Sends the "New Account Member Welcome" Email Merge - see corresponding spec
    * Database Trigger to be Enabled: 
      * __ (name TBD & documented in coding)


