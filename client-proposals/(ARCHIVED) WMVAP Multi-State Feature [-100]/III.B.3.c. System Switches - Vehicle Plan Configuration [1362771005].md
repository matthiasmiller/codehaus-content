3.2.3.3. System Switches - Vehicle Plan Configuration

  


Requirements

*Documented. Tim Reitz 08/19/2025

  


Related to the Vehicle Plan: Various details specific to each Vehicle Plan are configured in System Switches, to be displayed throughout the Solution and on printouts. All of these are read-only System Switches.

  


  * Label: Plan name 
    * Code: Config_VPlanName
    * Description: "This is used to set the official name of the Plan, to be displayed in various printouts, etc. 
    * Field Type: Plain text field." 
    * Default Value: N/A
    * Set to: As described in the "Dev Configuration - System Switches (Plan-Specific)" section of the proposal. 
    * Other Notes: 
      * N/A



  


  * Label: Optional plan name subtitle
    * Code: Config_VPlanNameSubtitle 
    * Field Type: Plain text field
    * Description: This is used to set a subtitle for the Plan name (if desired), to be displayed below the main Plan name in various printouts, etc." 
    * Default Value: N/A (may be left blank)
    * Set to: As described in the "Dev Configuration - System Switches (Plan-Specific)" section of the proposal. 
    * Other Notes: 
      * N/A



  


  * Label: Plan state abbreviation
    * Code: Config_VPlanStateAbbrev
    * Field Type: Plain text field
    * Description: "This is used to set the abbreviation of the state for the Plan, to be displayed in various printouts, etc." 
    * Default Value: N/A
    * Set to: As described in the "Dev Configuration - System Switches (Plan-Specific)" section of the proposal. 
    * Other Notes: 
      * N/A



  


  * Label: Plan state name
    * Code: Config_VPlanStateName
    * Field Type: Plain text field
    * Description: This is used to set the name of the state for the Plan, to be displayed in various printouts, etc."
    * Default Value: N/A
    * Set to: As described in the "Dev Configuration - System Switches (Plan-Specific)" section of the proposal. 
    * Other Notes: 
      * N/A



  


  * Label: Plan: Cargo: Uses entry fees
    * Code:  Config_VPlanUsesCargoEntryFee
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: "This is used to set whether or not the whole system uses Cargo Entry Fees." 
    * Default Value: N/A
    * Set to: As described in the "Dev Configuration - System Switches (Plan-Specific)" section of the proposal. 
    * Other Notes: 
      * N/A



  


  * Label: Plan: Cargo Premium: Uses % fees
    * Code: Config_VPlanCargoPremiumUses%
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: This is used to set whether or not the system includes Percentage options for Cargo Premium."
    * Default Value: N/A
    * Set to: As described in the "Dev Configuration - System Switches (Plan-Specific)" section of the proposal. 
    * Other Notes: 
      * Note that this can be set in addition to the "Uses flat fees" option for Cargo Premium.



  


  * Label: Plan: Cargo Premium: Uses flat fees
    * Code: Config_VPlanCargoPremiumUsesFlatFee 
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: "This is used to set whether or not the system includes Flat Fee options for Cargo Premium." 
    * Default Value: N/A
    * Set to: As described in the "Dev Configuration - System Switches (Plan-Specific)" section of the proposal. 
    * Other Notes: 
      * Note that this can be set in addition to the "Uses % fees" option for Cargo Premium.



  


  * Label: Plan: Collision: Uses entry fees
    * Code:  Config_VPlanUsesColEntryFee
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: "This is used to set whether or not the whole system uses Collision Entry Fees." 
    * Default Value: N/A
    * Set to: As described in the "Dev Configuration - System Switches (Plan-Specific)" section of the proposal. 
    * Other Notes: 
      * N/A



  


  * Label: Plan: Collision Premium: Uses % fees
    * Code: Config_VPlanColPremiumUses%
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: "This is used to set whether or not the system includes the Percentage options for Collision Premium." 
    * Default Value: N/A
    * Set to: As described in the "Dev Configuration - System Switches (Plan-Specific)" section of the proposal. 
    * Other Notes: 
      * Note that this can be set in addition to the "Uses flat fees" option for Collision Premium. 



  


  * Label: Plan: Collision Premium: Uses flat fees
    * Code: Config_VPlanColPremiumUsesFlatFee
    * Field Type: Drop list of "Yes" / "No" (boolean)
    * Description: "This is used to set whether or not the system includes Flat Fee options for Collision Premium." 
    * Default Value: N/A
    * Set to: As described in the "Dev Configuration - System Switches (Plan-Specific)" section of the proposal. 
    * Other Notes: 
      * Note that this can be set in addition to the "Uses % fees" option for Collision Premium.



  


Development Specification

Ellis Miller 04/24/2025: I think we should ONLY define these in derived catalogs so that we are ensured that they are correctly defined in all catalogs.

  


BID: 2 hour, should probably be 1 hour. Include the following item with this as well.

[ ] Make these Sometimes visible.

  


Murshid Rahman 05/08/2025: CLS Job ID [[PC0178320]].
