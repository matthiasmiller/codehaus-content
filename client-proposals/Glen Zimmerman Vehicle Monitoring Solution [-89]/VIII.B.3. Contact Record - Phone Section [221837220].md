7.2.3. Contact Record - Phone Section

*Done. 

  


  * Phone section (standard):



  


  * Phone (no label; embedded spreadsheet with the following; note that this can handle both US and Canadian phone numbers, as they use the same format: 
    * Columns:
      * Phone (auto-formats with dashes if 10 digits long)
      * Type (drop-list of the following list items: 
        * Fax
        * Home
        * Mobile
        * Work
      * Notes (plain text field) 
    * Automatically sorted by: N/A (none) 
    * Buttons to add/remove rows:
      * "✚": insert row
      * "🞭": delete selected row;
        * custom behavior: button is hidden for numbers that are selected as the "Mobile Phone" on the "Account Members" embedded spreadsheet on any Account records;
    * Other Notes:
      * The top row is considered to be the "Primary" phone number. 
      * Custom behavior: at least one "Mobile"-type phone number is required if "User ID" is not blank - error on Save: "At least one phone number is required because this Contact has login access."; 
      * Custom behavior: at least one "Mobile"-type phone number is required if the Contact is selected on the "Account Members" embedded spreadsheet for any Account records - error on Save: "At least one "Mobile"-type phone number is required because this Contact is included as an Account Member for one or more Accounts."; note that if the person does not have a phone, a number for a related contact (i.e. the Account Manager) can be entered to satisfy this requirement.)


