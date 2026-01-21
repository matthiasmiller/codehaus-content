4.1. Dev Configuration - System Switches (Plan-specific)

  


Requirements

Custom System Switches with settings for the WI Group-specific Solution: 

  


Note that items marked "TBD" are to be discussed and determined, probably in deployment.

  


Related to the Vehicle Plan: Various details specific to each Vehicle Plan are configured in System Switches, to be displayed throughout the Solution and on printouts. 

  


  * Label: Plan name 
    * Code: Config_VPlanName
    * Description: "This is used to set the official name of the Plan, to be displayed in various printouts, etc. 
    * Field Type: Plain text field." 
    * Default Value: N/A
    * Set to: "Weaverland Vehicle Aid of Wisconsin, Inc."
    * Other Notes: 
      * N/A



  


  * Label: Optional Plan name subtitle
    * Code: Config_VPlanNameSubtitle 
    * Field Type: Plain text field
    * Description: "This is used to set a subtitle for the Plan name (if desired), to be displayed below the main Plan name in various printouts, etc." 
    * Default Value: N/A (may be left blank)
    * Set to: "of the churches of Weaverland Mennonite Conference Body"
    * Other Notes: 
      * N/A



  


  * Label: Plan state abbreviation
    * Code: Config_VPlanStateAbbrev
    * Field Type: Plain text field
    * Description: "This is used to set the abbreviation of the state for the Plan, to be displayed in various printouts, etc." 
    * Default Value: N/A
    * Set to: "WI"
    * Other Notes: 
      * N/A



  


  * Label: Plan state name
    * Code: Config_VPlanStateName
    * Field Type: Plain text field
    * Description: "This is used to set the name of the state for the Plan, to be displayed in various printouts, etc."
    * Default Value: N/A
    * Set to: "Wisconsin"
    * Other Notes: 
      * N/A



  


  * Label: Plan: Cargo: Uses entry fees
    * Code: Config_VPlanUsesCargoEntryFee
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: "This is used to set whether or not the whole system uses Cargo Entry Fees." 
    * Default Value: N/A
    * Set to: "No" 
    * Other Notes: 
      * N/A



  


  * Label: Plan: Cargo Premium: Uses % fees
    * Code: Config_VPlanCargoPremiumUses%
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: "This is used to set whether or not the system includes Percentage options for Cargo Premium."
    * Default Value: N/A
    * Set to: "Yes" 
    * Other Notes: 
      * Note that this can be set in addition to the "Uses flat fees" option for Cargo Premium.



  


  * Label: Plan: Cargo Premium: Uses flat fees
    * Code: Config_VPlanCargoPremiumUsesFlatFee 
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: "This is used to set whether or not the system includes Flat Fee options for Cargo Premium." 
    * Default Value: N/A
    * Set to: "No" 
    * Other Notes: 
      * Note that this can be set in addition to the "Uses % fees" option for Cargo Premium.



  


  * Label: Plan: Collision: Uses entry fees
    * Code: Config_VPlanUsesColEntryFee
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: "This is used to set whether or not the whole system uses Collision Entry Fees." 
    * Default Value: N/A
    * Set to: "No" 
    * Other Notes: 
      * N/A



  


  * Label: Plan: Collision Premium: Uses % fees
    * Code: Config_VPlanColPremiumUses%
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: "This is used to set whether or not the system includes the Percentage options for Collision Premium." 
    * Default Value: N/A
    * Set to: "Yes" 
    * Other Notes: 
      * Note that this can be set in addition to the "Uses flat fees" option for Collision Premium. 



  


  * Label: Plan: Collision Premium: Uses flat fees
    * Code: Config_VPlanColPremiumUsesFlatFee 
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: "This is used to set whether or not the system includes Flat Fee options for Collision Premium." 
    * Default Value: N/A
    * Set to: "No" 
    * Other Notes: 
      * Note that this can be set in addition to the "Uses % fees" option for Collision Premium.



  


  


Related to the Policy #: These System Switches can be set for a Plan's specific situation, with the intention of being set in one of the two following ways by the development team as part of the initial configuration:

  * Option 1: One policy number for the whole Plan. The number is provided to CCI and set in the System Switch to apply across the whole system. It may contain the prefix "SI" (for "Self-Insured").
    * For this approach, the full Policy # is hard-coded in the System Switch field.
  * Option 2: One policy number for each member/client. The details are configured in the System Switch by CCI, and an individual # is assigned to each client (normally based on the Contact ID). It also may contain the prefix "SI". 
    * For this approach, the logic is hard-coded in the System Switch field, to set the Policy # as needed.



  


  * Label: Contact Policy Number 
    * Code: Config_ContactDisplayPolicyNum 
    * Field Type: String expression 
    * Description: "This sets the Policy # (either per-Plan or per-Member), to be evaluated on the Contact record." 
    * Default Value: N/A
    * Set to display the WI-specific format for the Policy #, based on the following: 
      * Prefixed with "SI"
      * Contains 7 digits after the prefix
      * Based off of the Contact ID for the Plan member, with zeros added to the front of the ID number as needed to reach a total of 7 numeric digits.
      * The numeric portion increases sequentially with each new member and cannot be edited.
      * The full policy # is displayed throughout the Solution and on printouts in the following format "SI1000001"
      * Specifically: 



Assign Parameter vContactName = ValidatedListString( Contacts, "");

  


CustomContacts_MemberPolicyNumber( vContactName)

  * Other Notes: 
    * The set value for this System Switch is read-only in the Solution and hard-coded on a Plan-by-Plan basis (configured by CCI for deployment).
    * Technical details: This is a string expression evaluated on the Contact.



  


  


Related to the Claim General Release Printout: 

  * Label: General Release: Optional text below logo
    * Code: Config_PrintGenReleaseBelowLogo
    * Field Type: Plain text
    * Description: "This sets the Plan-specific wording for an optional text box below the logo of the Claim General Release printout." 
    * Default Value: N/A (may be left blank)
    * Set to: N/A (blank)
    * Other Notes: 
      * N/A



  


  


Related to the Insurance Card Printout: 

  * Label: Insurance Card: Displayed full Plan name
    * Code: Config_PrintInsCardPlanFullName 
    * Field Type: Plain text
    * Description: "This sets the full Plan name to display on the front of the Insurance Card printout. It can be simply the Plan name, or can also include additional text." 
    * Default Value: N/A
    * Set to: "Weaverland Vehicle Aid of Wisconsin, Inc."
    * Other Notes: 
      * N/A



  


  * Label: Insurance Card: Optional text to the right of the full Plan name
    * Code: Config_PrintInsCardRightOfPlanName 
    * Field Type: Plain text
    * Description: "This sets the Plan-specific text for an optional bold text field to the right of the full plan name on the front of the Insurance Card." 
    * Default Value: N/A (may be left blank)
    * Set to: N/A (blank)
    * Other Notes: 
      * N/A



  


  * Label: Insurance Card: Vehicle Code law reference
    * Code: Config_PrintInsCardVehicleCodeLaw 
    * Field Type: Plain text
    * Description: "This sets the reference to the specific vehicle code that requires the Insurance Card printout (on the back of the card)."  
    * Default Value: N/A
    * Set to: "the vehicle statuses"
    * Other Notes: 
      * N/A



  


  * Label: Insurance Card: Optional text below Plan name
    * Code: Config_PrintInsCardBelowPlanName
    * Field Type: Plain text
    * Description: "This sets the Plan-specific wording for an optional text box below the Plan name on back of the Insurance Card printout." 
    * Default Value: N/A (may be left blank)
    * Set to: N/A (blank)
    * Other Notes: 
      * N/A



  


  


Related to the Liability Declaration Page Printout: 

  * Label: Liability Declaration: Optional text below Vehicle details 
    * Code: Config_PrintLiabBelowVehicle
    * Field Type: Plain text
    * Description: "This sets the Plan-specific wording for an optional text box below the vehicle details on the Liability Declaration Page printout." 
    * Default Value: N/A (may be left blank)
    * Set to: N/A (blank)
    * Other Notes: 
      * N/A



  


  * Label: Liability Declaration: Includes "(Limited tort)" text
    * Code: Config_PrintLiabInclLimitedTort 
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: "This sets whether or not the "(Limited tort)" text appears below the "Liability Coverage" section label on the Liability Declaration Page printout." 
    * Default Value: N/A
    * Set to: "No" (as this is not needed by the WI Plan)
    * Other Notes: 
      * N/A



  


  * Label: Liability Declaration: Includes "First Party Benefits" section
    * Code: Config_PrintLiabInclFirstPartyBnfits
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: "This sets whether or not the "First Party Benefits" section and details appear on the Liability Declaration Page printout." 
    * Default Value: N/A
    * Set to: "No" (as this is not needed by the WI Plan)
    * Other Notes: 
      * N/A



TODO_VA: Tim Reitz 08/26/2025: We might actually need this turned on. 

  


Related to the Loss Payable Clause Printout:

  * Label: Loss Payable: Optional text above Vehicle details 
    * Code: Config_PrintLossPayableAboveVehicle
    * Field Type: String expression



TODO_VA: Tim Reitz 09/03/2025: Add blue to main living spec & ZWA-specific. 

  * Description: "This sets the Plan-specific wording for an optional text box above the vehicle details table on the Loss Payable Clause printout." 
  * Default Value: N/A (may be left blank)
  * Set to display the following: "Policy #: <Config_ContactDisplayPolicyNum>" (i.e. "Policy #: SI0000005"), specifically: 



Assign Parameter vContactName = ValidatedListString( Contacts, "");

  


"Policy #: " \+ CustomContacts_MemberPolicyNumber( vContactName)

  * Other Notes: 
    * N/A



  


  


Related to the Program Participation Agreement Printout:

  * Label: Program Participation Agreement Plan Name
    * Code: Config_PrintProgPartAgrPlanName
    * Field Type: Plain text
    * Description: "This sets the Plan name to display on the Program Participation Agreement printout. It can be simply the plan name, plan name plus additional text, the Plan-specific Policy #, or something else." 
    * Default Value: N/A
    * Set to: "Weaverland Vehicle Aid of Wisconsin, Inc."
    * Other Notes: 
      * N/A



  


Development Specification

Ellis Miller 09/05/2024: These items are overridden in derived catalogs.
