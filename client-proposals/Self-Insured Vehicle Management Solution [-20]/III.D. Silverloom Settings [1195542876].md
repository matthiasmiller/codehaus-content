3.4. Silverloom Settings

  


Requirements

*Done. 

  


Overview: The Silverloom Settings page includes the following standard and custom sections and fields for various configuration settings. It also may include standard sections & fields. 

  


Accessed from: Advanced | Admin | Silverloom Settings

  


Sections and Fields: 

  * Invoicing Settings (standard) section:
    * Default Sales Tax Rate (number; 2 decimals)



  


  


  *   Contact Settings (standard) section: 
    * Name Format (required; 
      * drop list of the following items: 
        * FirstName LastName
        * FirstName MiddleName LastName
        * LastName, FirstName
        * LastName, FirstName MiddleName; 
      * custom: "LastName, FirstName MiddleName" is the option for deployment of this Solution) 
    * Apply Changes (button; clicking this after changing the selection in "Name Format" applies the change to existing Contacts in the Solution) 
    * "You must apply changes to update existing contacts. Overridden contact names will remain unchanged." (on-screen message in gray font) 



  


  


  * Current Period (custom) section:
    * Current Period Start Year (number; auto-calculated and read-only)
    * Period Start Date (date; auto-calculated and read-only)
    * Period End Date (date; auto-calculated and read-only)



  


  


  * Coverage Settings (custom) section:
    * Deductible $ (number; two decimals; defaults to blank; warning on Save if blank: "Deductible $ is blank."; this amount is used for deductible calculations) 
    * Bodily Injury Liability $ (Per Person) (number; no decimals; defaults to blank; warning on Save if blank: "Bodily Injury Liability $ (Per Person) is blank."; this amount is displayed on the Insurance Card and Liability Declaration Page printouts)
    * Bodily Injury Liability $ (Per Accident) (number; no decimals; defaults to blank; warning on Save if blank: "Bodily Injury Liability $ (Per Accident) is blank."; this amount is displayed on the Insurance Card and Liability Declaration Page printouts)
    * Property Damage Liability $ (Per Accident) (number; no decimals; defaults to blank; warning on Save if blank: "Property Damage Liability $ (Per Accident) is blank."; this amount is displayed on the Insurance Card and Liability Declaration Page printouts)
    * Medical Exp. Benefit $ (Per Person) (visible based on the "Liability Declaration: Includes "First Party Benefits" section" System Switch; number; no decimals; defaults to blank; warning on Save if blank: "Medical Exp. Benefit $ (Per Person) is blank."; this amount is displayed on the Liability Declaration Page printout)
    * Unins. Motorist Prop. Dmg. $ (Per Accident) (visible based on the "Liability Declaration: Includes "First Party Benefits" section" System Switch; number; no decimals; defaults to blank; warning on Save if blank: "Unins. Motorist Prop. Dmg. $ (Per Accident) is blank."; this amount is displayed on the Liability Declaration Page printout) 



  


  


  * Printouts Configuration (custom) section:
    * Configure New Member Card (button; opens a child screen with the following:) 
      * New Member Card Body (large memo that supports expressions, approximately the same width as the printout page, and about half the height; the contents of this field are displayed as the body of the New Member Card; may contain embedded expressions for specific data points, using "#expr#" syntax, to be evaluated on / printed from Contact records; initial configuration to be done at deployment by CCI, but can be edited by any Admin user)



  


  * Configure General Release Printout (button; opens a child screen with the following:)
    * Claim General Release Printout Body (large memo that supports expressions, approximately the same width as the printout page, and about half the height; the contents of this field are displayed as the body of the General Release Printout; may contain embedded expressions for specific data points, using "#expr#" syntax, to be evaluated on / printed from Claim records; initial configuration to be done at deployment by CCI, but can be edited by any Admin user) 



  


  * Configure Agent Change Notice (button; opens a child screen with the following:)
    * Agent Change Notice Printout Body (large memo that supports expressions, approximately the same width as the printout page, and about half the height; the contents of this field are displayed as the body of the Agent Change Notice Printout; may contain embedded expressions for specific data points, using "#expr#" syntax, to be evaluated on / printed from Contact records; initial configuration to be done at deployment by CCI, but can be edited by any Admin user)



  


  * Configure Authorized Signature (button; opens a child screen with the following:)
    * Authorized Signature (memo; the Plan Authorized Signature is uploaded here, to be included in various printouts)



  


  * Configure Plan Logo (button; opens a child screen with the following:)
    * Plan Logo (memo; the Plan Logo is uploaded here, to be included in various places)



  


  


  * Guidelines Compliance Questions (custom) section:
    * Guidelines Compliance Questions (no label; embedded spreadsheet with the following:  
      * Columns: 
        * Vehicle Type (Blank = All) (drop list of all active Vehicle Types)
        * Subtype (Blank = All) (drop list of Subtypes for the selected "Vehicle Type")
        * Question (required; plain text)
        * Print (required; drop-list of "If Yes", "If No", "Always"; note that this controls when the question, answer, and corresponding Statement are included on the Program Participation Agreement printout)
        * Statement if Yes (plain text; editable and required if "Print" is set to "If Yes" or "Always")
        * Statement if No (plain text; editable and required if "Print" is set to "If No" or "Always")
      * Automatically sorted by: 
        * First by: "Vehicle Type" (alphabetically) 
        * Second by: "Subtype" (alphabetically) 
      * Buttons to append and delete rows ("+"/"-") 
      * Additional Validations: 
        * Error on the fields and on Save if duplicate "Question" rows are entered for the same Vehicle Type: "Duplicate questions for same vehicle type are not allowed."; 
        * Error on the fields and on Save if duplicate "Question" rows are entered for the same Vehicle Type and Subtype: "Duplicate questions for same vehicle type and subtype are not allowed.") 



  


  


  * Plan-Specific Settings (custom) section:
    * Plan Name (auto-set and read-only; displays the contents of the "Plan name" System Switch) 
    * Plan Name Subtitle (auto-set and read-only; displays the contents of the "Plan name subtitle" System Switch) 
    * Plan Address:
      * Address (plain text; defaults to blank; warning on Save if blank: "Address is blank") 
      * Address Line 2 (no label; optional; plain text; defaults to blank) 
      * City (plain text; defaults to blank; warning on Save if blank: "Address City is blank")
      * State (auto-set and read-only; displays the contents of the "Plan state abbreviation" System Switch)
      * Zip (number field; defaults to blank; warning on Save if blank: "Address Zip is blank") 
    * Plan Phone (phone number field, auto-setting the numbers to the standard phone number format; defaults to blank; warning on Save if blank: "Plan Phone is blank") 
    * Plan Email (email field; validate that the entered text is in the standard email format - warning on the field if not: "Please enter a valid email address."; defaults to blank; warning on Save if blank: "Plan Email is blank")



  


  


Modification History: This contains the following standard feature for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users (standard) 
  * Editability: Editable for users included in the "Custom_CanEditSilverloomSettings" macro, which defaults to "Administrator"-type Users only (standard) 



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Change Requests: 

  * Tim Reitz 08/18/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident



  


  


TODO_: Tim Reitz 09/15/2025: It would be good to have these specced out more, to explain how they are calculated: 

  * Current Period Start Year (number; auto-calculated and read-only)
  * Period Start Date (date; auto-calculated and read-only)
  * Period End Date (date; auto-calculated and read-only)



Then we might also want to make sure that we are calculating these in the best / most efficient way (offhand, I feel like I remember that we're recalculating Start / End Dates on the Coverage sections of Vehicle records, rather than referencing these macros, etc.).
