3.2.1. Silverloom Settings

  


Requirements

*Documented. Tim Reitz 08/18/2025

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Overview: The Silverloom settings page stores system-wide settings.

  


Accessed via: Advanced | Admin | Silverloom Settings

  


Data Access: Admin

  


Sections and Fields: 

Invoicing Settings section:

  * Default Sales Tax Rate (number; 2 decimals)



  


  


Contact Settings section:

  * Name Format (drop-list with four standard name format options)
  * Apply Changes (button; applies selected format to all contact names in the system)



  


  


Current Period (custom) section:

  * Current Period Start Year (number; auto-calculated and read-only)
  * Period Start Date (date; auto-calculated and read-only)
  * Period End Date (date; auto-calculated and read-only)



  


  


Coverage Settings (custom) section:

  * Deductible $ Amount ($) (number; two decimals; defaults to blank; warning on Save if blank: "Deductible $  is blank."required; this amount is used for deductible calculations) 
  * Bodily Injury Liability $ (Per Person) (number; no decimals; defaults to blank; warning on Save if blank: "Bodily Injury Liability $ (Per Person) is blank."; this amount is displayed on the Insurance Card and Liability Declaration Page printouts)
  * Bodily Injury Liability $ (Per Accident) (number; no decimals; defaults to blank; warning on Save if blank: "Bodily Injury Liability $ (Per Accident) is blank."; this amount is displayed on the Insurance Card and Liability Declaration Page printouts)
  * Property Damage Liability $ (Per Accident) (number; no decimals; defaults to blank; warning on Save if blank: "Property Damage Liability $ (Per Accident) is blank."; this amount is displayed on the Insurance Card and Liability Declaration Page printouts)
  * Medical Exp. Benefit $ (Per Person) (visible based on the "Liability Declaration: Includes "First Party Benefits" section" System Switch; number; no decimals; defaults to blank; warning on Save if blank: "Medical Exp. Benefit $ (Per Person) is blank."; this amount is displayed on the Liability Declaration Page printout)
  * Unins. Motorist Prop. Dmg. $ (Per Accident) (visible based on the "Liability Declaration: Includes "First Party Benefits" section" System Switch; number; no decimals; defaults to blank; warning on Save if blank: "Unins. Motorist Prop. Dmg. $ (Per Accident) is blank."; this amount is displayed on the Liability Declaration Page printout) 



  


  


Printouts Configuration (custom) section:

  * Configure New Member Card (button; opens a child screen with the following:) 
    * New Member Card Body (large memo that supports expressions, approximately the same width as the printout page, and about half the height; the contents of this field are displayed as the body of the New Member Card; may contain embedded expressions for specific data points, using "#expr#" syntax, to be evaluated on / printed from Contact records; initial configuration to be done at deployment by CCI, but can be edited by any Admin user)
    * Memo (unlabeled memo; the formatted card text is pasted into the memo)



  


  * Configure General Release Printout (button; opens a child screen with the following:)
    * Claim General Release Printout Body (large memo that supports expressions, approximately the same width as the printout page, and about half the height; the contents of this field are displayed as the body of the General Release Printout; may contain embedded expressions for specific data points, using "#expr#" syntax, to be evaluated on / printed from Claim records; initial configuration to be done at deployment by CCI, but can be edited by any Admin user) 



  


  * Configure Agent Change Notice (button; opens a child screen with the following:)
    * Agent Change Notice Printout Body (large memo that supports expressions, approximately the same width as the printout page, and about half the height; the contents of this field are displayed as the body of the Agent Change Notice Printout; may contain embedded expressions for specific data points, using "#expr#" syntax, to be evaluated on / printed from Contact records; initial configuration to be done at deployment by CCI, but can be edited by any Admin user)



  


  * Configure Authorized Signature (button; opens a child screen with the following:)
    * Authorized Signature (memo; the Plan Authorized Signature is uploaded here, to be included in various printouts)



  


  * Configure Plan Logo (button; opens a child screen with the following:)
    * Plan Logo (memo; the Plan Logo is uploaded here, to be included in various places)



  


  


Plan-Specific Settings (custom) section:

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



  


  


Guidelines Compliance Questions (custom) section:

(embedded spreadsheet with the following:) 

  * Columns: 
    * Vehicle Type (Blank = All) (drop-list of all active vehicle types)
    * Subtype (Blank = All) (drop-list of sub-types for the selected type)
    * Question (plain text)
    * Print (drop-list of If Yes, If No, Always)
    * Statement if Yes (plain text; editable and required if Print is set to "If Yes" or "Always")
    * Statement if No (plain text; editable and required if Print is set to "If No" or "Always")
  * Automatically sorted by: Vehicle Type + Subtype
  * Buttons to append and delete rows ("+"/"-") 



  


  


Referenced Wikis (custom) section:

  * Allowed Vehicles (drop-list of wiki pages)
  * Truck Weight Chart (drop-list of wiki pages)
  * Vehicle Guideline Sheet (drop-list of wiki pages)



  


Validation:

  * Error on save: if duplicate guidelines compliance questions are entered for the same vehicle type and subtype.



  


Development Specification

Change Requests: 

  * Tim Reitz 05/23/2025: [[[IN11468](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11470&)]] - ZWA - Multi-State Feature - Silverloom Settings - Misc Changes for Printout Templates
  * Tim Reitz 07/31/2025:  [[[IN11468](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11470&)]] - ZWA - Multi-State Feature - Silverloom Settings - Misc Changes for Printout Template
  * Tim Reitz 07/31/2025: [[[IN11611](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11613&)]] - ZWA - Silverloom Settings - Remove the newly-added "New Member Card Subtitle" field
  * 


  


  


Ellis Miller 09/04/2024: 

  


1 Day

[ ] Add these fields with your best guesses of layout. Email results to CR@ for feedback.

[ ] Note that we have two expression fields:

New Member Card Body

Claim General Release Printout

To reduce dev costs, let's not add report alerts for broken expressions. These aren't serious and are unlikely to break. Just reference NullReportAlert. See [[WS0003727]]

  


Sagar Sagar 06/02/2025: Corresponding CLS jobs 

  * [[PC0178122]] - ZWA - WMVAP - Changes to Silverloom Settings
  * [[PC0179426]] - ZWA - WMVAP - Silverloom Settings - Misc Changes for Printout Templates


