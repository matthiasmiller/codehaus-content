3.4.2. Silverloom Settings - Leacock Paving Settings

  


Requirements

  * Leacock Paving Settings section (custom): 
    * Current PA Oil Index (read-only macro; with the following details / behaviors: 
      * displays details from the current row of the "PA Oil Index Details" embedded spreadsheet on the PA Oil Index Child Screen (see corresponding spec); 
      * displays bold text in the following format: "<PA Oil Index MMMM + YYYY, based on the "PA Oil Index Start Date"> Oil Index: $<PA Oil Index $>", i.e. "March 2025 Oil Index: $635.00") 
    * Edit PA Oil Index (button; opens the PA Oil Index Child Screen (see corresponding spec)) 



  


  * Proposal Deposit % (number; 2 decimals; defaults to "30.00" on Save if blank; this sets the percentage for the deposit required for some Proposals upon being awarded) 
  * Number of Days for Valid Proposal (number; no decimals; defaults to "30" on Save if blank; this sets the number of days for which the pricing for a Proposal is valid, and is used for the "Proposal Valid Through" date on the Proposal record) 



  


  * PA Oil Index Child Screen (custom):  
    * PA Oil Index Details (dated embedded spreadsheet with the following: 
      * Columns: 
        * PA Oil Index Start Date (required; date; with the following details / behaviors: 
          * defaults to the first date of the current month when a row is added; 
          * if a different date is set, auto-updates to the first of the month of the manually-entered date (so it always is the first of a month); 
          * validate against rows with duplicate dates - error on the field: "Duplicate Dates (<Date>) are not allowed." (standard validation for dated embedded spreadsheets); 
          * note that the month & year can be displayed with the "PA Oil Index $" value with an expression based on this date) 
        * PA Oil Index $ (required; number; 2 decimals) 
      * Automatically sorted by: Date (latest at the top) 
      * Buttons to append/remove rows: "✚" / "🞭" (no validations against deleting rows, since Proposals have the Oil Index stored on them and the top row is always displayed as the "Current" Oil Index) 
      * Show 10 rows without scrolling 
      * Other Notes: 
        * N/A 
      * Additional Validations: 
        * Warning on Save if there are no rows on this embedded spreadsheet: "No Oil Index set.")



  


Development Specification

Leacock Paving Settings section (custom): 

[ ] Add None-level OilIndexCurrentDisplay macro that does SilverloomSettingsField lookup for displayed text.

[ ] For the two fields that need value of 30, we have two options:

  * see if OnInit:30 is respected when we create a new system (developers with existing systems would have to set it manually). If that works, add a Required:TRue.
  * Otherwise just add a Modify Field Change expression to set the defaults on save if blank.



Email Ellis and Nic to let us know what you figured out.

2 Hours

  


PA Oil Index Child Screen (custom):  

[ ] Simple dated RG with AllowDuplicateDates:false. 

1 Hour
